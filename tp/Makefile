NAME = tp

$(NAME).pdf: $(NAME).markdown example/* img/*
	pandoc -s $< -o $@ --toc

distclean:
	@rm -rvf $(NAME).pdf

.PHONY: distclean
