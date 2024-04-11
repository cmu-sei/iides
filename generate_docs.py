'''Generates markdown files from json schema'''
import json
import os

DOCUMENTATION_PATH = "documentation/"
JSON_PATH = "json"


def get_json_files():
    '''Returns json files from which to generate markdown'''
    fnames = []
    for root, _, f_names in os.walk(JSON_PATH):
        for f in f_names:
            fnames.append(os.path.join(root, f))
    return fnames


def get_properties(properties, required):
    '''Return formatted strings for object properties'''

    lines = []

    for p in properties:
        property_string = f"- **`{p}`** "
        if p in required:
            property_string += "(required) "
        property_string += (
            f"*({properties[p]['type']})* "
            f": {properties[p]['description']}"
        )
        lines.append(property_string)

        if 'items' in properties[p].keys():
            if properties[p]['type'] == 'array':
                vocab_ref = "\t- One or more values "
            else:
                vocab_ref = "\t- A value "
            if '$ref' in properties[p]['items'].keys():
                vocab_ref += "from ["
                ref = properties[p]['items']['$ref']
                if ref.startswith('#'):
                    # internal file reference
                    vocab_ref += f"{ref[8:]}](#{ref[8:]})"
                else:
                    # reference to other file
                    vocab_ref += f"{ref[ref.rfind('/')+1:-5]}]({ref[:-5]}.md)"
            lines.append(vocab_ref)

        if 'pattern' in properties[p].keys():
            lines.append(f"\t- Uses pattern: {properties[p]['pattern']}")

    return lines


def get_vocab(definitions):
    lines = []

    for d in definitions:
        lines.append(f"\n### {d}")
        if 'enum' in definitions[d].keys():
            # Vocab is specificified as an enumeration
            values = [f"`{v}`" for v in definitions[d]['enum']]
            lines.append(f"\nValues: {', '.join(values)}\n")
        else:
            # Vocab is specified as anyOf or oneOf
            try:
                values = [f"`{v['const']}`" for v in definitions[d]['anyOf']]
                table_data = definitions[d]['anyOf']
            except KeyError:
                values = [f"`{v['const']}`" for v in definitions[d]['oneOf']]
                table_data = definitions[d]['oneOf']
            lines.append(f"\nValues: {', '.join(values)}\n")

            has_descriptions = False
            for row in table_data:
                if 'description' in row.keys():
                    has_descriptions = True
                    break
            if has_descriptions:
                lines.append("| Const | Value | Description |")
                lines.append("| --- | --- | --- |")
            else:
                lines.append("| Const | Value |")
                lines.append("| --- | --- |")

            for vocab in table_data:
                row = f"| {vocab['const']} | {vocab['title']} |"
                if 'description' in vocab.keys():
                    lines.append(f"{row} {vocab['description']}|")
                else:
                    lines.append(f"{row} |")
    return lines


if __name__ == "__main__":

    # Get json files
    json_files = get_json_files()

    for filename in json_files:
        file_lines = []  # lines that will be written to the markdown file

        with open(filename) as f:
            data = json.load(f)
            print(data['title'])

        # Title and description of object
        file_lines.append(f"# {data['title']}")
        file_lines.append(f"{data['description']}\n")

        if 'properties' in data:
            file_lines.append("## Properties")
            file_lines.extend(
                get_properties(data['properties'], data['required']))

        if '$defs' in data:
            file_lines.append("\n## Vocabularies")
            file_lines.extend(get_vocab(data['$defs']))

        # Write output to markdown file
        f = open(f"{DOCUMENTATION_PATH}{filename[5:-5]}.md", "w")
        f.writelines([line + '\n' for line in file_lines])
        f.close()
