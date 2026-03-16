PYTHON = PYTHONPATH=$(shell pwd) ../.venv/bin/python

PYFIGS := $(shell find figures -name "*.py" ! -path "figures/common/*")
PDFS := $(PYFIGS:.py=.pdf)

figures/%.pdf: figures/%.py
	$(PYTHON) $<

figures: $(PDFS)
	@echo "All figures generated"

clean-figures:
	$(RM) $(PDFS)

