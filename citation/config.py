"""Citation development configuration."""

import os

# Root of this application, useful if it
# doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# File path of bibtex file
BIBTEX_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'citation/static/citations.bib'
)