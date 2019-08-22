PYEXE=pipenv run ballot
CONFIG=candidates.yml
PAPERS_TEX=$(shell $(PYEXE) list $(CONFIG) tex)
PAPERS_PDF=$(shell $(PYEXE) list $(CONFIG) pdf)

all: $(PAPERS_PDF) ballot-pack.pdf ballot-print.pdf

ballot-print.pdf: template-print.tex ballot-pack.pdf
	xelatex template-print.tex
	mv template-print.pdf ballot-print.pdf

%.pdf: %.tex
	xelatex $<

$(PAPERS_TEX): $(CONFIG)
	$(PYEXE) tex $(CONFIG)

ballot-pack.tex:
	$(PYEXE) texpack $(CONFIG)

.PHONY: clean view

clean:
	rm -f *.log *.aux *.pdf ballot-*.tex

view: ballot.pdf
	xdg-open ballot.pdf
