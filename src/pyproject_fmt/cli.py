from __future__ import annotations

import os
from argparse import ArgumentParser, ArgumentTypeError, Namespace
from pathlib import Path
from typing import Sequence


class PyProjectFmtNamespace(Namespace):
    """Options for pyproject-fmt tool"""

    pyproject_toml: Path
    stdout: bool
    indent = 2


def pyproject_toml_path_creator(argument: str) -> Path:
    """Validate that pyproject.toml can be formatted.

    :param argument: the string argument passed in
    :return: the pyproject.toml path
    """
    path = Path(argument).absolute()
    if not path.exists():
        raise ArgumentTypeError("path does not exists")
    if not path.is_file():
        raise ArgumentTypeError("path is not a file")
    if not os.access(path, os.R_OK):
        raise ArgumentTypeError("cannot read path")  # pragma: no cover
    if not os.access(path, os.W_OK):
        raise ArgumentTypeError("cannot write path")  # pragma: no cover
    return path


def cli_parser() -> ArgumentParser:
    """Construct a parser that can be used to extract CLI arguments."""
    # Useful for sphinx-argparse-cli
    parser = ArgumentParser()
    parser.add_argument(
        "-s",
        "--stdout",
        action="store_true",
        help="print the formatted text to the stdout (instead of update in-place)",
    )
    parser.add_argument("pyproject_toml", type=pyproject_toml_path_creator, help="pyprojec.toml file to format")
    return parser


def cli_args(args: Sequence[str]) -> PyProjectFmtNamespace:
    """
    Load the tools options.

    :param args: CLI arguments
    :return: the parsed options
    """
    parser = cli_parser()
    return parser.parse_args(namespace=PyProjectFmtNamespace(), args=args)
