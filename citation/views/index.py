import flask
import citation
import bibtexparser
import os
import pprint


def get_all_fields(bib_database):
    """Get all fields."""
    fields = set()
    for entry in bib_database.entries:

        for field in entry.keys():
            fields.add(field)

    print(fields)
    return fields


def sanitize_bib_database(citations, fields):
    """Sanitize citations so that empty fields are not missing."""
    context = {"citations": []}

    for citation in citations:

        for field in fields:
            if field not in citation.keys():
                citation[field] = ""  # add empty field

        context["citations"].append(citation)

    return context

@citation.app.route("/", methods=["GET"])
def index():
    """Render view for index."""
    print(os.getcwd())
    print(citation.app.config["BIBTEX_PATH"])
    # reads the bibtex file into a list of dictionaries
    with open(citation.app.config["BIBTEX_PATH"]) as bibtex_file:
        bib_parse = bibtexparser.bparser.BibTexParser(common_strings=True)

        bib_database = bib_parse.parse_file(bibtex_file)

    all_fields = get_all_fields(bib_database)

    # pprint.pprint(bib_database.entries)

    context = sanitize_bib_database(bib_database.entries, all_fields)
    return flask.render_template("index.html", **context)
