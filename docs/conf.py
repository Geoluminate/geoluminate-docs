# -*- coding: utf-8 -*-
# All configuration values have a default; values that are commented out
# serve to show the default.

import importlib
import os
import sys
from datetime import datetime
from pathlib import Path

import django
import toml

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath("../"))
parent = os.path.dirname(os.getcwd())
sys.path.append(parent)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.local.settings")

django.setup()


# Project information --------------------------------------
package_meta = toml.load("../pyproject.toml")["tool"]["poetry"]
project = package_meta["name"].title()
version = package_meta["version"]  # The short X.Y version.
release = version
authors = ["Sam Jennings"]
copyright = f"{datetime.now().year}, {authors[0]}"
language = "en"

# General configuration -------------------------------------

current_file_path = Path(__file__).parent.absolute()

geoluminate_docs_static = current_file_path / "_static"

geoluminate_project_brand = Path("../project/static/img/brand/")

# https://sphinx-book-theme.readthedocs.io/en/stable/
html_theme = "sphinx_book_theme"
html_static_path = [
    "_static",
    # str(geoluminate_project_brand),
    # str(geoluminate_docs_static),
]
# html_title = None
html_short_title = ""


html_show_copyright = True
html_last_updated_fmt = "%b %d, %Y"

# BRANDING / LOGO

project_logo = geoluminate_project_brand / "logo.svg"

if project_logo.exists():
    html_logo = str(project_logo)
else:
    html_logo = str(geoluminate_docs_static / "logo.svg")

icon = geoluminate_project_brand / "icon.svg"

if icon.exists():
    html_favicon = str(icon)
else:
    html_favicon = str(geoluminate_docs_static / "icon.svg")


# https://sphinx-book-theme.readthedocs.io/en/stable/reference.html
# https://pydata-sphinx-theme.readthedocs.io/en/latest/user_guide/index.html
html_theme_options = {
    "repository_url": package_meta["homepage"],
    "use_repository_button": True,
    # "logo_only": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "home_page_in_toc": True,
    "extra_footer": (
        '<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License"'
        ' style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This documentation'
        ' is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons'
        " Attribution 4.0 International License</a>."
    ),
}

# https://utteranc.es
# https://sphinx-comments.readthedocs.io/en/latest/utterances.html
comments_config = {
    "utterances": {
        "repo": "/".join(package_meta["homepage"].split("/")[-2:]),
        "issue-term": "pathname",
        "theme": "preferred-color-scheme",
        "label": "documentation",
        "crossorigin": "anonymous",
    }
}


autodoc2_packages = [f"../{package['include']}" for package in package_meta["packages"]]

autodoc2_render_plugin = "myst"

autodoc2_skip_module_regexes = [
    r"geoluminate.conf",
    r".*migrations.*",
    r".*tests.*",
]

# autodoc2_parse_docstrings = True

# autodoc2_docstring_parser_regexes = [("myst", r".*choices*")]

# Any additional Sphinx extension modules go here
extensions = [
    "sphinx.ext.viewcode",
    "sphinx.ext.duration",
    # 'sphinx.ext.doctest',
    "sphinx.ext.todo",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosectionlabel",
    "sphinx_copybutton",
    "sphinxext.opengraph",
    # "autodoc2",
    "sphinx_comments",
    "myst_parser",
    "sphinx_tippy",
]


# The master toctree document.
master_doc = "index"

# Path to additional templates relative to this directory
templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = ".rst"


# The language for content autogenerated by Sphinx. Refer to documentation for a list of supported languages.

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [
    # match any directory not beginning with docs
    "^(?!docs).*",
    "_build",
]

# The reST default role (used for this markup: `text`) to use for all documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = False

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False


autodoc_default_options = {
    "exclude-members": "__weakref__",
}

myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    # "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

autosectionlabel_prefix_document = True


# -- Options for HTML output ---------------------------------------------------

html_css_files = ["tippy.css"]
# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = False


# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''


# Output file base name for HTML help builder.
htmlhelp_basename = f"{package_meta['name']}doc"


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    (
        "index",
        f"{package_meta['name']}.tex",
        f"{project} Documentation",
        authors[0],
        "manual",
    ),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (
        "index",
        package_meta["name"],
        f"{project} Documentation",
        authors[0],
        1,
    )
]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        "index",
        package_meta["name"],
        f"{project} Documentation",
        authors[0],
        package_meta["name"],
        "One line description of project.",
        "Miscellaneous",
    ),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
# texinfo_no_detailmenu = False
