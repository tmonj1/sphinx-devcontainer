# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import sphinx_rtd_theme
import sphinx_fontawesome

# -- Project information -----------------------------------------------------

project = 'Sphinxによるドキュメント作成'
copyright = '2021, tmj'
author = 'tmj'

# The short X.Y version
version = '0.1'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
  "sphinx.ext.todo",
  "sphinx_rtd_theme",
  "sphinxcontrib.trimblank",
  "sphinx_fontawesome",
  "sphinxcontrib.blockdiag",
  "sphinxcontrib.seqdiag",
  "sphinxcontrib.actdiag",
  "sphinxcontrib.nwdiag",
  "sphinx_tsegsearch"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'ja'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Enable Todo list.
todo_include_todos = True

# i18n settings:
# * set the language after translation to ja
# * set translation folders to locale
language = 'ja'
locale_dirs = ['locale']
gettext_compact = False

# Keep blanks to adjacent to ascii characters in html documents
trimblank_keep_alnum_blank = ['html', 'singlehtml']

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# enable auto-numbering for figures, tables and code blocks.
numfig = True

# blockdiag
blockdiag_html_image_format = "SVG"
blockdiag_latex_image_format = "SVG"

# common definition file
rst_prolog= u"""
.. include:: definitions.txt
"""
