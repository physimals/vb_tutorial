# -*- coding: utf-8 -*-
#
# VB tutorial documentation build configuration file
#
# This file is execfile()d with the current directory set to its
# containing dir.

# -- General configuration ------------------------------------------------

extensions = [
    'sphinx.ext.viewcode',
]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'vb_tutorial'
copyright = u'2020, University of Oxford'
author = u'Martin Craig'
build_dir = u"_build"

version = u'0.0.1'
release = u'0.0.1'
language = None
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_static_path = ['_static']

html_context = {
    'css_files': [
        '_static/theme_overrides.css',  # override wide tables in RTD theme
        ],
     }
     
# -- Options for LaTeX / PDF output ---------------------------------------------

latex_elements = {
  'extraclassoptions': 'openany,oneside'
}

latex_documents = [
    (master_doc, 'vb_tutorial.tex', u'Variational Bayes Tutorial',
     u'Martin Craig', 'manual'),
]

pdf_documents = [
    (master_doc, u'vb_tutoral', u'Variational Bayes Tutorial', u'Martin Craig'),
]
