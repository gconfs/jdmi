NAME = tp
LATEX_BYPRODUCTS = $(addprefix $(NAME).,aux log nav out snm toc vrb) _minted-$(NAME)
COMPILE = pdflatex -shell-escape

# This rule is the default and will do one pass of pdflatex regardless of
# dependencies freshness
quick:
	$(COMPILE) $(NAME).tex

$(NAME).pdf: $(NAME).tex tpacdc.sty example/* img/*
	$(COMPILE) $<
	$(COMPILE) $<
	$(COMPILE) $<

clean:
	@rm -rvf $(LATEX_BYPRODUCTS)
	
distclean: clean
	@rm -rvf $(NAME).pdf

.PHONY: quick clean distclean
