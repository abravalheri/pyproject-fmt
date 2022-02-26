from pyproject_fmt import __version__ as version

project = "pyproject-fmt"
author = "Bernát Gábor"
copyright = "2022, Bernát Gábor"
release = version

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "myst_parser",
    "sphinx_argparse_cli",
    "sphinx_copybutton",
]

myst_enable_extensions = ["html_image", "linkify", "replacements", "smartquotes"]

source_suffix = [".rst", ".md"]

html_theme = "furo"
pygments_style = "sphinx"
pygments_dark_style = "monokai"

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}
