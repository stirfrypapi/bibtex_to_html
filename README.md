# Bibtex to HTML Formatting
## Author: Raymond Pang <pangr@umich.edu>

Install package dependencies with

pip install -e .

while in the citation folder.


To run on development server, run the citation_run shell script with

./bin/citation_run

and navigate to localhost:8000

Make sure to activate the script first with

chmod +x bin/citation_run


### TODO:

Formatting is currently in Flask/Jinja syntax. Final version should be in
Javascript/React components.

Citations are currently sitting in the file citations.bib. Final version should
pull bibtex citations from a database.
