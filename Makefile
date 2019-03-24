PYEXE=pipenv run ballot
CONFIG=example.yml
PAPERS_TEX=$(shell $(PYEXE) list $(CONFIG) tex)
PAPERS_PDF=$(shell $(PYEXE) list $(CONFIG) pdf)

all: $(PAPERS_PDF)

%.pdf: %.tex
	xelatex $<

$(PAPERS_TEX): $(CONFIG)
	$(PYEXE) tex $(CONFIG)

.PHONY: clean view

clean:
	rm -f *.log *.aux *.pdf ballot-*.tex

view: ballot.pdf
	xdg-open ballot.pdf
