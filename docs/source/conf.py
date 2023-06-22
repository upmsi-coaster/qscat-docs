# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'QSCAT'
copyright = '2023'
author = 'Louis Facun'

release = '1.1.3-beta'
version = '1.1.3-beta'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.bibtex',
]
# -- Bibtex configuration
bibtex_bibfiles = ['refs.bib']
bibtex_reference_style = 'author_year'

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output
html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# Enable numeric figure references
numfig = True
numfig_secnum_depth = 2