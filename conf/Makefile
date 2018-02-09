NAME = conf
LATEX_BYPRODUCTS = $(addprefix $(NAME).,aux log nav out snm toc vrb)

# This rule is the default and will do one pass of pdflatex regardless of
# dependencies freshness
quick:
	pdflatex $(NAME).tex

$(NAME).pdf: $(NAME).tex img/*
	pdflatex $<
	pdflatex $<
	pdflatex $<

clean:
	@rm -rvf $(LATEX_BYPRODUCTS)
distclean: clean
	@rm -rvf $(NAME).pdf

.PHONY: quick clean distclean
