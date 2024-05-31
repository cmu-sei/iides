'''Generates markdown files from json schema'''
import json
import os

DOCUMENTATION_PATH = "documentation/"
JSON_PATH = "example_jsons"


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
    for schema in schema_paths:
        if (schema[schema.rindex('\\')+1:] == (target_tag + '.json')):
            with open(schema) as f:
                return json.load(f)
    return None

def get_vocab(items, field, schema):
    """
    Returns the vocab definition of a given item for the given field, from the given schema
    """
    ret_val = ""

    #Tuple case
    if isinstance(items, list):
        refs = []
        for elems in schema['properties'][field]['items']['prefixItems']:
            if '$ref' in elems:
                refs.append(elems['$ref'])
        try:
            for ref in refs:
                defs = schema['$defs']
                ref_path = ref
                vocab_array = defs[ref_path[ref_path.rfind('/')+1:]]['oneOf']
                count = 0
                for vocab_object in vocab_array:
                    if vocab_object['const'] == items[0]:
                        ret_val = ret_val + f"{vocab_object['title']} - {vocab_object['description']}"
                        count +=1
        except:
            vocab_array = []
            print(f"Error: could not get vocab: {items}\n")
        return ret_val
    

    try: #string case
        ref_path = schema['properties'][field]['$ref']
        defs = schema['$defs']

        try:
            vocab_array = defs[ref_path[ref_path.rfind('/')+1:]]['oneOf']
            for vocab_object in vocab_array:
                if vocab_object['const'] == items:
                    ret_val = f"{vocab_object['title']} - {vocab_object['description']}"
        except:
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
                        ret_val = f"{vocab_object['title']} - {vocab_object['description']}"
            except:
                try:
                    vocab_array = defs[ref_path[ref_path.rfind('/')+1:]]['oneOf']
                    for vocab_object in vocab_array:
                        if vocab_object['const'] == items:
                            ret_val = f"{vocab_object['title']} - {vocab_object['description']}"
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

# Function to get the sort index based on the desired order
def get_sort_index(tag):
    if tag in desired_order:
        return desired_order.index(tag)
    else:
        return len(desired_order)

if __name__ == "__main__":

    # Get json files
    json_examples = get_json_files('example_jsons')
    json_schemas = get_json_files('json')

    print("Example paths: " + str(json_examples))
    for filename in json_examples:

        file_lines = []  # lines that will be written to the markdown file

        with open(filename, 'r') as f:
            example_data = json.load(f)

        # Example Number
        file_lines.append(f"# {filename[filename.find('\\example')+1:filename.find('.json')].capitalize()}\n")

        if 'objects' in example_data:
            # Iterate through each IIDES object
            objects = example_data['objects']
            sorted_objects = sorted(objects, key=lambda obj: get_sort_index(obj['id'][0:obj['id'].find("--")].lower()))

            for object in sorted_objects:
                tag = object['id'][0:object['id'].find("--")]
                file_lines.append(f"## {tag.capitalize()}\n")
                if 'comment' in object:
                    file_lines.append(f"{object['comment']}\n")
                
                # Find the correlating schema
                print(tag)
                schema = find_schema(json_schemas, tag)
                #need to do something about references to other schema, accomplice and insider

                # Load the requested field
                for field in object:
                    # Append the file line with appropriate const, description, vocab
                    if field not in ['comment']:
                        items = object[field]
                        items_print = ''

                        try:
                            schema_field = schema['properties'][field]
                        except:
                            print("Not a default field: " + str(field))
                            file_lines.append(f"- **`{field.capitalize().replace("_", " ")}`**:\n {items}")
                            continue
                        if field == 'location':
                            print("Trying to get location vocab")
                        #items is a string
                        if schema_field['type'] == "string":
                            if '$ref' in schema_field: 
                                #There is vocab for this item
                                items_print = f"  - *{items}*: {get_vocab(items, field, schema)}"
                            else:
                                items_print = f"  - {items}" 
                        #item is a list
                        elif schema_field['type'] == "array" and ('type' not in schema_field['items'] or schema_field['items']['type'] != "array"): 
                            if '$ref' in schema['properties'][field]['items']:
                                #There is vocab to parse for this field entry
                                for item in items:
                                    items_print= items_print + (f"  - *{item}*: {get_vocab(item, field, schema)}\n")
                            else:
                                for item in items:
                                    items_print = items_print + (f"  - {item}\n")
                        #item is a tuple
                        elif schema_field['type'] == "array" and ('type' in schema_field['items'] and schema_field['items']['type'] == "array"):
                            for item in items:
                                items_print= items_print + (f"  - *{item}*: {get_vocab(item, field, schema)}\n")
                        elif schema_field['type'] == 'number' or schema_field['type'] == 'integer':
                            items_print = f"{items:,}"
                        else:
                            items_print = f"{items}"
               
                        file_lines.append(f"- **`{field.capitalize().replace("_", " ")}`**:\n {items_print}")

        # Write output to markdown file
        f = open(f"{DOCUMENTATION_PATH}{filename[:filename.find('.json')]}.md", "w")
        f.writelines([line + '\n' for line in file_lines])
        f.close()
        print("Successfuly made markdown: " + str(filename[:filename.find('.json')]))
