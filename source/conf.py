# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import sphinx_rtd_theme

# -- Project information -----------------------------------------------------

project = 'NaughtyAttributes'
copyright = '2017, Denis Rizov'
author = 'Denis Rizov'

# The full version, including alpha/beta/rc tags
release = '2.1.4'

# -- General configuration ---------------------------------------------------

# Extensions
extensions = [
    "sphinx_rtd_theme"
]

# Code block
highlight_language = "csharp"

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# Theme
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    'collapse_navigation': False,  # Collapse navigation (False makes it tree-like)
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']
