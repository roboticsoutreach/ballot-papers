#! /usr/bin/env python3

import io
import os

import click

from datetime import date

from jinja2 import Environment, FileSystemLoader, Template
from ruamel.yaml import YAML

from typing import List

latex_jinja_env = Environment(
    block_start_string="\BLOCK{",
    block_end_string="}",
    variable_start_string="\VAR{",
    variable_end_string="}",
    comment_start_string="\#{",
    comment_end_string="}",
    line_statement_prefix="%%",
    line_comment_prefix="%#",
    trim_blocks=True,
    autoescape=False,
    loader=FileSystemLoader(os.path.abspath(".")),
)


@click.group()
def cli():
    pass


@cli.command(help="Get the names of the ballot papers")
@click.argument("config_file", type=click.File("rb"))
@click.argument("ext", type=click.STRING)
def list(config_file: io.BufferedReader, ext: str):
    yaml = YAML()
    config = yaml.load(config_file)

    for name, _ in config["papers"].items():
        print(f"ballot-{name}.{ext}")


@cli.command(help="Generate the TeX source for the ballot papers.")
@click.argument("config_file", type=click.File("rb"))
def tex(config_file: io.BufferedReader):
    yaml = YAML()
    config = yaml.load(config_file)
    click.echo(f"Loaded {config_file.name}")

    for name, paper in config["papers"].items():
        candidates: List[str] = paper["candidates"]
        sorted(candidates)
        if config["config"]["ron"]:
            candidates.append("Re-open Nominations")
        generate_ballot_tex(
            name, config["config"]["org"], paper["title"], paper["date"], candidates
        )


@cli.command(help="Generate the TeX source for a merged document")
@click.argument("config_file", type=click.File("rb"))
def texpack(config_file: io.BufferedReader):
    yaml = YAML()
    config = yaml.load(config_file)
    click.echo(f"Loaded {config_file.name}")

    template = latex_jinja_env.get_template("template-pack.tex")

    click.echo(f"Generating Merged Ballot")

    render = template.render(ballot_list=config["papers"].items())

    with open(f"ballot-pack.tex", "w") as fh:
        fh.write(render)


def generate_ballot_tex(
    name: str, org: str, title: str, date: date, candidates: List[str]
):
    """Generate the tex source for a ballot paper."""

    template = latex_jinja_env.get_template("template-ballot.tex")

    click.echo(f"Generating Ballot for {title}")

    render = template.render(
        name=name,
        org=org,
        title=title,
        date=date.isoformat(),
        candidate_list=candidates,
    )

    with open(f"ballot-{name}.tex", "w") as fh:
        fh.write(render)


if __name__ == "__main__":
    cli()
