'''Generates markdown files from json schema

## Licensing
This file is a part of the Insider Incident Data Exchange Standard (IIDES) - see [https://github.com/cmu-sei/IIDES](https://github.com/cmu-sei/IIDES)
Copyright 2024 Carnegie Mellon University.
[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution. Please see Copyright notice for non-US Government use and distribution.
This work is provided "AS-IS" with "NO WARRANTIES OF ANY KIND - EXPRESS OR IMPLIED" and is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.
Requests for permission for non-licensed uses should be directed to the Software Engineering Institute at permission@sei.cmu.edu.
CERT® is registered in the U.S. Patent and Trademark Office by Carnegie Mellon University.
DM24-0776
'''
import json
import os
import sys


script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
iides_directory = os.path.dirname(script_directory)
DOCUMENTATION_PATH = os.path.join(iides_directory, 'examples')
EXAMPLE_JSON_PATH = os.path.join(iides_directory, 'examples', 'json')
JSON_SCHEMA_PATH = os.path.join(iides_directory, 'json')


def get_json_files(jpath):
    """
    Returns a list of JSON files from the given directory path.

    Args:
        jpath (str): Path to the directory containing JSON files.

    Returns:
        list: List of paths to JSON files.
    """
    fnames = []
    for root, _, f_names in os.walk(jpath):
        for f in f_names:
            if f.endswith('.json'):
                fnames.append(os.path.join(root, f))
    return fnames


def find_schema(schema_paths, target_tag):
    """
    Returns the JSON schema file corresponding to the target tag.

    Args:
        schema_paths (list): List of paths to schema files.
        target_tag (str): Target schema tag to find.

    Returns:
        dict: The JSON schema corresponding to the target tag, or None if not found.
    """
    for path in schema_paths:
        if f'{target_tag}.json' in path:
            with open(path, "r", encoding='utf-8') as schema_file:
                return json.load(schema_file)
    return None


def get_vocab(items, field, schema):
    """
    Returns the vocab definition of a given item for the given field from the given schema.

    Args:
        items (any): The value of the field in the JSON object.
        field (str): The name of the field.
        schema (dict): The JSON schema for the object.

    Returns:
        str: The vocab definition as a string.
    """
    ret_val = ""

    # Function to fetch vocab array from schema definitions
    def get_vocab_array(ref_path, defs, key='oneOf'):
        try:
            return defs[ref_path[ref_path.rfind('/') + 1:]][key]
        except KeyError:
            return []

    # Tuple case
    if isinstance(items, list):
        refs = []
        for elems in schema['properties'][field]['items']['prefixItems']:
            if '$ref' in elems:
                refs.append(elems['$ref'])
        
        for ref in refs:
            vocab_array = get_vocab_array(ref, schema['$defs'])
            for vocab_object in vocab_array:
                if vocab_object.get('const') == items[0]:
                    ret_val += f"{vocab_object['title']} (*{items}*) &mdash; {vocab_object['description']}"
        if not ret_val:
            print(f"Error: could not get vocab: {items}, {refs}\n")
        return ret_val

    try:
        ref_path = schema['properties'][field]['$ref']
        vocab_array = get_vocab_array(ref_path, schema['$defs'])
        for vocab_object in vocab_array:
            if vocab_object.get('const') == items:
                ret_val = f"{vocab_object['title']} (*{items}*) &mdash; {vocab_object['description']}"
                break
        if not ret_val:
            ret_val = items
            print(f"Error: could not get vocab: {items}, {ref_path}\n")
    except KeyError:
        try:
            ref_path = schema['properties'][field]['items']['$ref']
            vocab_array = get_vocab_array(ref_path, schema['$defs'], 'anyOf')
            if not vocab_array:
                vocab_array = get_vocab_array(ref_path, schema['$defs'])
            for vocab_object in vocab_array:
                if vocab_object.get('const') == items:
                    ret_val = f"{vocab_object['title']} (*{items}*) &mdash; {vocab_object['description']}"
                    break
            if not ret_val:
                print(f"Error: could not get vocab: {items}, {ref_path}\n")
        except KeyError:
            print(f"Error: could not get vocab: {items}, {field}\n")

    return ret_val


def process_field(items, field, schema, schema_field):
    """
    Processes a field in the JSON object according to its schema definition.

    Args:
        items (any): The value of the field in the JSON object.
        field (str): The name of the field.
        schema (dict): The JSON schema for the object.
        schema_field (dict): The schema definition for the specific field.

    Returns:
        str: The processed field value as a string.
    """
    if schema_field['type'] == "string":
        return get_vocab(items, field, schema) if '$ref' in schema_field else str(items)
    elif schema_field['type'] == "array":
        return process_array_field(items, field, schema, schema_field)
    elif schema_field['type'] in ['number', 'integer']:
        if field == 'postal_code':
            return items
        return f"{items:,}"
    else:
        return str(items)


def process_array_field(items, field, schema, schema_field):
    """
    Processes an array field in the JSON object according to its schema definition.

    Args:
        items (list): The value of the array field in the JSON object.
        field (str): The name of the field.
        schema (dict): The JSON schema for the object.
        schema_field (dict): The schema definition for the specific field.

    Returns:
        str: The processed array field value as a string.
    """
    items_print = ""
    if 'type' not in schema_field['items'] or schema_field['items']['type'] != "array":
        if '$ref' in schema['properties'][field]['items']:
            items_print = "\n".join(f"  - {get_vocab(item, field, schema)}" for item in items)
        else:
            items_print = "\n".join(f"  - {item}" for item in items)
    elif schema_field['items']['type'] == "array":
        items_print = "\n".join(f"  - {get_vocab(item, field, schema)}" for item in items)
    return items_print


desired_order = [
    "incident",
    "insider",
    "organization",
    "detection",
    "impact",
    "target",
    "response",
    "court-case",
    "charge",
    "sentence",
    "legal-response",
    "job",
    "stressor",
    "ttp"
]


def get_sort_index(target_schema):
    """
    Gets the sort index based on the desired order.

    Args:
        target_schema (str): The target schema name.

    Returns:
        int: The index of the target schema in the desired order, or the length of the desired order if not found.
    """
    if target_schema in desired_order:
        return desired_order.index(target_schema)
    else:
        return len(desired_order)


if __name__ == "__main__":

    # Get json files
    json_examples = get_json_files(EXAMPLE_JSON_PATH)
    json_schemas = get_json_files(JSON_SCHEMA_PATH)

    for filename in json_examples:
        file_lines = []

        with open(filename, 'r', encoding='utf-8') as f:
            example_data = json.load(f)

        # Example Number
        title = os.path.splitext(os.path.basename(filename))[0].capitalize()
        file_lines.append(f"# {title}\n")

        if 'objects' in example_data:
            # Iterate through each IIDES object
            objects = example_data['objects']
            sorted_objects = sorted(objects, key=lambda obj: get_sort_index(obj['id'][0:obj['id'].find("--")].lower()))

            for obj in sorted_objects:
                tag = obj['id'].split("--")[0]
                formatted_tag = tag.replace('-', ' ').title()
                if formatted_tag == 'Ttp':
                    formatted_tag = 'TTP'
                file_lines.append(f"\n## {formatted_tag}\n")

                if 'comment' in obj:
                    file_lines.append(f"{obj['comment']}\n")

                # Find the correlating schema
                schema = find_schema(json_schemas, tag)
                # TODO: Implement cross file references for
                # Person/Country/State vocabs

                for field, items in obj.items():
                    if field == 'comment':
                        continue

                    schema_field = schema['properties'].get(field)
                    if not schema_field:
                        print(f"Not a default field: {field}")
                        file_lines.append(f"- **`{field}`**:\n {items}")
                        continue

                    items_print = process_field(items, field, schema, schema_field)
                    formatted_field = field.capitalize().replace('_', ' ')
                    if formatted_field == 'Ttp vocab':
                        formatted_field = 'TTP vocab'
                    file_lines.append(f"- **`{formatted_field}`**:\n {items_print}")

        # Write output to markdown file
        new_path = os.path.split(filename)[-1][:-5]
        f = open(f"{DOCUMENTATION_PATH}/{new_path}.md", "w", encoding="utf-8")
        f.writelines([line + '\n' for line in file_lines])
        f.close()
        print("Successfuly made markdown: " + str(filename[:-5]))
