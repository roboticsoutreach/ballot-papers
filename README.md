# Ballot Paper

A LaTeX Ballot Paper generation script.

First used for the SRO AGM 2019.

## Usage

Requirements:

- GNU Make
- Python 3
- xelatex
- pipenv (See Pipfile)
  - Ruamel.YAML
  - Jinja2
  - Click

Generation: `make`

This will create a pdf for every ballot paper, a merged version and a version with each ballot paper at A6 size on an A4 page ready for printing.

## Configuration

In order to configure what data to put on the ballot papers, you should use a YAML file called `candidates.yml`. There is an example of the format in `candidates.example.yml`.


## Notes

This probably isn't the most efficient way to generate these. We like to be a bit overkill sometimes at SRO.

Licenced under the MIT Licence.
