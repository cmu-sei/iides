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


def get_ref(ref):
    if ref.startswith('#'):
        # internal file reference
        ref_string = f"[{ref[8:]}](#{ref[8:]})"
    else:
        # reference to other file
        ref_string = f"[{ref[ref.rfind('/')+1:-5]}]({ref[:-5]}.md)"
    return ref_string


def is_dependent(property):
    dependent = None
    if "dependentRequired" in data:
        for present_property in data['dependentRequired'].items():
            if property in present_property[1]:
                dependent = present_property[0]
    return dependent


def get_properties(properties, required):
    '''Return formatted strings for object properties'''

    lines = []

    for p in properties:
        print(f"\t{p}")
        property_string = f"- **`{p}`** "
        if p in required:
            property_string += "(required) "
        if "format" in properties[p]:
            property_string += f"*({properties[p]['format']})* "
        else:
            property_string += f"*({properties[p]['type']})* "
        property_string += f": {properties[p]['description']}"
        lines.append(property_string)

        if '$ref' in properties[p].keys():
            # A string that can be one of a list of values
            vocab_ref = "\t- A constant from "
            vocab_ref += get_ref(properties[p]['$ref'])
            lines.append(vocab_ref)

        if properties[p]['type'] == 'array':
            vocab_ref = "\t- One or more "
            if 'prefixItems' in properties[p].keys():
                # An array of tuples
                vocab_ref += "tuple values of the format ("
                refs = []
                for p_item in properties[p]['prefixItems']:
                    if list(p_item.keys())[0] == '$ref':
                        refs.append(get_ref(p_item['$ref']))
                if len(refs) == 1:
                    vocab_ref += f"{refs[0]}, date)"
                else:
                    vocab_ref += f"{', '.join(refs)})"
            else:
                # An array of strings
                print("HERE")
                if '$ref' in properties[p]['items'].keys():
                    vocab_ref += "constants from "
                    vocab_ref += get_ref(properties[p]['items']['$ref'])
                else:
                    vocab_ref += f"{properties[p]['items']['type']} values"
            lines.append(vocab_ref)

        if 'pattern' in properties[p].keys():
            lines.append(f"\t- Uses pattern: {properties[p]['pattern']}")
        
        if is_dependent(p):
            lines.append(f"\t- Required if `{is_dependent(p)}` exists.")

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
            lines.append(f"\nConstants: {', '.join(values)}\n")

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
        file_lines.append(f"# {data['title']}\n")
        file_lines.append(f"{data['description']}\n")

        if 'properties' in data:
            file_lines.append("## Properties\n")
            file_lines.extend(
                get_properties(data['properties'], data['required']))

        if '$ref' in data:
            # class inherits properties from another
            file_lines.append(
                f"- **Inherits properties from "
                f"[{data['$ref'][2:-5].capitalize()}]({data['$ref'][2:-5]})**"
            )

        if '$defs' in data:
            file_lines.append("\n## Vocabularies")
            file_lines.extend(get_vocab(data['$defs']))

        # Write output to markdown file
        f = open(f"{DOCUMENTATION_PATH}{filename[5:-5]}.md", "w")
        f.writelines([line + '\n' for line in file_lines])
        f.close()
