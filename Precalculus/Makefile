PYTHON = ../.venv/bin/python

PYFIGS := $(shell find figures -name "*.py")
PDFS := $(PYFIGS:.py=.pdf)

%.pdf: %.py
	$(PYTHON) $<

figures: $(PDFS)
	@echo "All figures generated"

clean-figures:
	$(RM) $(PDFS)

