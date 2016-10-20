from browser import document as doc
from browser import window as win
from browser import html
from browser.local_storage import storage
from browser import timer
from browser import alert
import json

# Setup the ace editor
ace = win.ace
editor = ace.edit("editor")
editor.setTheme("ace/theme/monokai")
editor.getSession().setMode("ace/mode/python")
editor.getSession().setTabSize(4)
editor.getSession().setUseSoftTabs(True)
doc["editor"].height = 500
editor.resize()

# Decorator to make a function visible in javascript
def exportjs(func):
    setattr(win, func.__name__, func)
    return func

@exportjs
def run_turtle():
    # Reset the canvas
    try:
      del doc["mycanvas"]
    except:
      pass
    import turtle
    t = turtle.Turtle()

    # Get the user code from ace
    code = editor.getValue()
    try:
        # Clear the previous error
        doc["error"].innerHTML = ""
        # Execute the code
        exec(code)
    except Exception as e:
        # If the code is wrong, display the error panel
        text = str(e)
        if isinstance(e, SyntaxError):
            a = e.args
            text = "At line {}, char {}: {}: \"{}\"".format(a[2], a[3], a[0], a[-1])
        html = """
            <div class="panel panel-danger">
                <div class="panel-heading">
                    <h3 class="panel-title">{}</h3>
                </div>
                <div class="panel-body">{}</div>
            </div>""".format(e.__name__, text)
        doc["error"].innerHTML = html
    # Finalize the drawing
    turtle.Screen().end()

    # Brython's turtle is impossible to reset...
    # Fuck this shit, delete the whole module.
    import sys
    del sys.modules["turtle"]

@exportjs
def change_binding(binding):
    doc["binding"].text = binding
    if binding == "default":
        binding = "keybinding"
    editor.setKeyboardHandler("ace/keyboard/" + binding)

def update_saves():
    saves = json.loads(storage["saves"])
    dropdown = doc["load-dropdown"]
    dropdown.innerHTML = ""
    for s in saves:
        link = html.A(s, href='#', onclick="load_buffer('{}')".format(s))
        dropdown <= html.LI(link)
    # <li><a href="#" onclick="load_buffer('{}')">{}</a></li>
        

@exportjs
def save_buffer():
    name = doc["save-name"].value
    if name == "":
        alert("Please type a name")
        return
    text = editor.getValue()
    saves = json.loads(storage["saves"])
    saves[name] = text
    storage["saves"] = json.dumps(saves)
    update_saves()

def autosave():
    text = editor.getValue()
    storage["autosave"] = text

@exportjs
def load_buffer(name=None):
    text = editor.getValue()
    if name is None:
        editor.setValue(storage["autosave"])
    else:
        saves = json.loads(storage["saves"])
        editor.setValue(saves[name])

# Load autosave if present
try:
    load_buffer()
except:
    print("No previous autosave.")
# Load saved buffers
if "saves" not in storage:
    storage["saves"] = json.dumps({})
update_saves()
# Autosave every second
timer.set_interval(autosave, 1000)
