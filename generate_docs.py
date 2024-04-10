'''Generates markdown files from json schema'''
import json
import os
import getopt
import sys

DOCUMENTATION_PATH = "documentation/"
JSON_PATH = "json"

fnames = []  # json files from which to generate markdown

argv = sys.argv[1:]
opts, args = getopt.getopt(argv, "f:")
for opt, arg in opts:
    if opt in ('-f', '--filename'):
        fnames.append(arg)


# if no file is specified, iterate through all json files
if len(fnames) == 0:
    for root, d_names, f_names in os.walk(JSON_PATH):
        for f in f_names:
            fnames.append(os.path.join(root, f))

for filename in fnames:
    file_lines = []
    with open(filename) as f:
        data = json.load(f)
        print(data['title'])

        # Title and description
        file_lines.append(f"# {data['title'].capitalize()}")
        file_lines.append(f"{data['description']}\n")
        file_lines.append("## Properties")

        # Properties
        # - property_name (type): description of property
        for property in data['properties']:
            property_string = f"- **`{property}`** "
            if property in data['required']:
                property_string += "(required) "
            property_string += (
                f"*({data['properties'][property]['type']})* "
                f": {data['properties'][property]['description']}"
            )
            file_lines.append(property_string)
            if 'items' in data['properties'][property].keys():
                if data['properties'][property]['type'] == 'array':
                    vocab_ref = "\t- One or more values "
                else:
                    vocab_ref = "\t- A value "
                vocab_ref += (
                    f"from ["
                    f"{data['properties'][property]['items']['$ref'][8:]}]"
                    f"(#{data['properties'][property]['items']['$ref'][8:]})"
                )
                file_lines.append(vocab_ref)
            if 'pattern' in data['properties'][property].keys():
                pattern = data['properties'][property]['pattern']
                file_lines.append(f"\t- pattern: {pattern}")

        # Vocabularies
        if '$defs' in data:
            file_lines.append("\n## Vocabularies")
            for definition in data['$defs']:
                file_lines.append(f"\n### {definition}")
                if 'enum' in data['$defs'][definition].keys():
                    # Vocab is specificified as an enumeration
                    values = [f"`{v}`" for v in data['$defs'][definition]['enum']]
                    file_lines.append(f"\nValues: {', '.join(values)}\n")
                else:
                    # Vocab is specified as anyOf
                    values = [f"`{v['const']}`" for v in data['$defs'][definition]['anyOf']]
                    file_lines.append(f"\nValues: {', '.join(values)}\n")
                    file_lines.append("| Const | Value | Description |")
                    file_lines.append("| --- | --- | --- |")
                    for vocab in data['$defs'][definition]['anyOf']:
                        row = f"| {vocab['const']} | {vocab['title']} |"
                        if 'description' in vocab.keys():
                            file_lines.append(f"{row} {vocab['description']}|")
                        else:
                            file_lines.append(f"{row} |")

    # Write output to markdown file
    f = open(f"{DOCUMENTATION_PATH}{filename[5:-5]}.md", "w")
    f.writelines([line + '\n' for line in file_lines])
    f.close()
