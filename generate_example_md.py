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
        if (schema.endswith(target_tag + '.json')):
            with open(schema) as f:
                return json.load(f)
    return None

def get_vocab(items, field, schema):
    """
    Returns the vocab definition of a given item for the given field, from the given schema
    """
    ret_val = ""
    print(items)
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


    # if isinstance(items, list):
    #     sub_schema_items = sub_schema['items']
    #     if '$ref' in sub_schema_items:
    #         mult_refs = False
    #         if 'prefixItems' in sub_schema_items:
    #             mult_refs = True
            
    #         ref_path = None

    #         if not mult_refs:
    #             ref_path = sub_schema_items['$ref']
    #             def_value = ref_path[ref_path.rfind('/')+1:]
    #             defs = schema['$defs']
    #             try:
    #                 vocab_array = defs[def_value]['oneOf']
    #             except:
    #                 try: vocab_array = defs[def_value]['anyOf']
    #                 except: vocab_array = []
    #             ret_val = "\n"
    #             for vocab_object in vocab_array:
    #                 if vocab_object['const'] in items:
    #                     ret_val = ret_val + (f"  - {vocab_object['title']} - {vocab_object['description']}\n")
    # elif isinstance(items, str):
    #     print(items)
    #     ref_path = schema['properties'][field]['$ref']
    #     defs = schema['$defs']

    #     try:
    #         vocab_array = defs[ref_path[ref_path.rfind('/')+1:]]['oneOf']
    #         for vocab_object in vocab_array:
    #             if vocab_object['const'] == items:
    #                 ret_val = f"{vocab_object['title']} - {vocab_object['description']})"
    #     except:
    #         vocab_array = []
    #         print(f"Error: could not get vocab: {items}\n")
    return ret_val


if __name__ == "__main__":

    # Get json files
    json_examples = get_json_files('example_jsons')
    json_schemas = get_json_files('json')

    print("Example paths: " + str(json_examples))
    for filename in json_examples:

        file_lines = []  # lines that will be written to the markdown file

        with open(filename, 'r') as f:
            example_data = json.load(f)
            print(example_data['id'])

        # Example Number
        file_lines.append(f"# {filename[filename.find('\\example')+1:filename.find('.json')].capitalize()}\n")

        if 'objects' in example_data:
            # Iterate through each IIDES object
            for object in example_data['objects']:
                tag = object['id'][0:object['id'].find("--")]
                file_lines.append(f"## {tag.capitalize()}\n")
                if 'comment' in object:
                    file_lines.append(f"{object['comment']}\n")
                
                # Find the correlating schema
                schema = find_schema(json_schemas, tag)
                #need to do something about references to other schema, accomplice and insider

                # Load the requested field
                for field in object:
                    # Append the file line with appropriate const, description, vocab
                    if field not in ['id','comment']:
                        items = object[field]
                        items_print = ''

                        try:
                            schema_field = schema['properties'][field]
                        except:
                            print("Not a default field: " + str(field))
                            continue

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
                                    print(item)
                        #item is a tuple
                        elif schema_field['type'] == "array" and items:
                            print("Not supported... yet ;)")
                        elif schema_field['type'] == 'number' or schema_field['type'] == 'integer':
                            items_print = f"{items:,}"
                        else:
                            items_print = f"{items}"
               
                        file_lines.append(f"- **`{field.capitalize().replace("_", " ")}`**:\n {items_print}")

        # Write output to markdown file
        f = open(f"{DOCUMENTATION_PATH}{filename[:filename.find('.json')]}.md", "w")
        f.writelines([line + '\n' for line in file_lines])
        f.close()
