all: ballot.pdf

%.pdf: %.tex
	xelatex $<


.PHONY: clean view

clean:
	rm *.log *.aux *.pdf

view: ballot.pdf
	xdg-open ballot.pdf