'''Generates markdown files from json schema'''
import json
import os
import sys


script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
iides_directory = os.path.dirname(script_directory)
DOCUMENTATION_PATH = os.path.join(iides_directory, 'examples')
EXAMPLE_JSON_PATH = os.path.join(iides_directory, 'examples', 'json')
JSON_SCHEMA_PATH = os.path.join(iides_directory, 'json')


def get_json_files(jpath):
    '''Returns json files from which to generate markdown'''
    fnames = []
    for root, _, f_names in os.walk(jpath):
        for f in f_names:
            if f.endswith('.json'):
                fnames.append(os.path.join(root, f))
    return fnames


def find_schema(schema_paths, target_tag):
    """
    Returns the desired json schema file
    param: a list of schemas
    param: target schema path
    """
    for path in schema_paths:
        name = path[path.rfind("\\")+1:]
        if name == target_tag + '.json':
            with open(path, "r", encoding='utf-8') as schema_file:
                return json.load(schema_file)
    return None


def get_vocab(items, field, schema):
    """
    Returns the vocab definition of a given item for the given field, from the given schema
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
            print(f"Error: could not get vocab: {items}\n")
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
            print(f"Error: could not get vocab: {items}\n")
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
                print(f"Error: could not get vocab: {items}\n")
        except KeyError:
            print(f"Error: could not get vocab: {items}\n")

    return ret_val

    try: #string case
        ref_path = schema['properties'][field]['$ref']
        defs = schema['$defs']

        try:
            vocab_array = defs[ref_path[ref_path.rfind('/')+1:]]['oneOf']
            for vocab_object in vocab_array:
                if vocab_object['const'] == items:
                    ret_val = f"{vocab_object['title']} (*{items}*) &mdash; {vocab_object['description']}"
        except:
            ret_val = items
            vocab_array = []
            print(f"Error: could not get vocab: {items}\n")
    except: #list case
        try:
            ref_path = schema['properties'][field]['items']['$ref']
            defs = schema['$defs']

            try:
                vocab_array = defs[ref_path[ref_path.rfind('/')+1:]]['anyOf']
                for vocab_object in vocab_array:
                    if vocab_object['const'] == items:
                        ret_val = f"{vocab_object['title']} (*{items}*) &mdash; {vocab_object['description']}"
            except:
                try:
                    vocab_array = defs[ref_path[ref_path.rfind('/')+1:]]['oneOf']
                    for vocab_object in vocab_array:
                        if vocab_object['const'] == items:
                            ret_val = f"{vocab_object['title']} (*{items}*) &mdash; {vocab_object['description']}"
                except:
                    print(f"Error: could not get vocab: {items}\n")
                #just a list case first:

        except:
            print(f"Error: could not get vocab: {items}\n")
    return ret_val

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


def get_sort_index(tag):
    """
    Function to get the sort index based on the desired order
    """
    if tag in desired_order:
        return desired_order.index(tag)
    else:
        return len(desired_order)


if __name__ == "__main__":

    # Get json files
    json_examples = get_json_files(EXAMPLE_JSON_PATH)
    json_schemas = get_json_files(JSON_SCHEMA_PATH)

    for filename in json_examples:

        file_lines = []  # lines that will be written to the markdown file

        with open(filename, 'r', encoding='utf-8') as f:
            example_data = json.load(f)

        # Example Number
        title = os.path.split(filename)[-1].capitalize().replace('.json', '')
        file_lines.append(f"# {title}\n")

        if 'objects' in example_data:
            # Iterate through each IIDES object
            objects = example_data['objects']
            sorted_objects = sorted(objects, key=lambda obj: get_sort_index(obj['id'][0:obj['id'].find("--")].lower()))

            for object in sorted_objects:
                tag = object['id'][0:object['id'].find("--")]
                file_lines.append(f"\n## {tag.capitalize()}\n")
                if 'comment' in object:
                    file_lines.append(f"{object['comment']}\n")

                # Find the correlating schema
                schema = find_schema(json_schemas, tag)
                #need to do something about references to other schema, accomplice and insider

                # Load the requested field
                for field in object:
                    # Append the file line with appropriate const, description, vocab
                    if field != 'comment':
                        items = object[field]
                        items_print = ''

                        try:
                            schema_field = schema['properties'][field]
                        except Exception as e:
                            print("Not a default field: " + str(field))
                            file_lines.append(f"- **`{field.capitalize().replace('_', ' ')}`**:\n {items}")
                            continue
                        #items is a string
                        if schema_field['type'] == "string":
                            if '$ref' in schema_field:
                                #There is vocab for this item
                                items_print = get_vocab(items, field, schema)
                            else:
                                items_print = f"{items}"
                        # item is a list
                        elif schema_field['type'] == "array" and ('type' not in schema_field['items'] or schema_field['items']['type'] != "array"): 
                            if '$ref' in schema['properties'][field]['items']:
                                #There is vocab to parse for this field entry
                                for item in items:
                                    items_print= items_print + (f"\n  - {get_vocab(item, field, schema)}")
                            else:
                                for item in items:
                                    items_print = items_print + (f"\n  - {item}")
                        # item is a tuple
                        elif schema_field['type'] == "array" and ('type' in schema_field['items'] and schema_field['items']['type'] == "array"):
                            for item in items:
                                items_print= items_print + (f"\n  - {get_vocab(item, field, schema)}")
                        elif schema_field['type'] == 'number' or schema_field['type'] == 'integer':
                            items_print = f"{items:,}"
                        else:
                            items_print = f"{items}"
               
                        file_lines.append(f"- **`{field.capitalize().replace('_', ' ')}`**: {items_print}")

        # Write output to markdown file
        new_path = os.path.split(filename)[-1][:-5]
        f = open(f"{DOCUMENTATION_PATH}/{new_path}.md", "w")
        f.writelines([line + '\n' for line in file_lines])
        f.close()
        print("Successfuly made markdown: " + str(filename[:-5]))
