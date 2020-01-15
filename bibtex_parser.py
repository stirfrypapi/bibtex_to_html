import bibtexparser
import pprint
import os

print(os.getcwd())

# reads the bibtex file into a list of dictionaries
with open('/Users/Raymond/Desktop/eecs499/citation/citation/static/citations.bib') as bibtex_file:
    bib_parse = bibtexparser.bparser.BibTexParser(common_strings=True)

    bib_database = bib_parse.parse_file(bibtex_file)

pprint.pprint(bib_database.entries)











# from pybtex.database import parse_file
#
# bib_data = parse_file('/Users/Raymond/Desktop/eecs499/citation/citation/static/citations.bib', bib_format="bibtex")
#
# print(bib_data.to_string(bib_format="bibtex"))



