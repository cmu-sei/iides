"""
File: generate_large_schema.py

Summary:

This file will generate a file containing all the schema in one
large file. The schema file can them be used offline.

*** COMMON REFERENCES ARE BROKEN ***
** MIGHT BE MISSING SOME REFERENCES...

"""
import os
import json


def get_json_files(jpath):
    '''Returns json files from which to generate markdown'''
    fnames = []
    for root, _, f_names in os.walk(jpath):
        for f in f_names:
            if f.endswith('.json'):
                fnames.append(os.path.join(root, f))
    return fnames

def iterate_replace_refs_list(my_list, schema_name):
    """ For the edge case of nested dictionaries in lists """
    for item in my_list:
        if isinstance(item, list):
            print("Iterating through nested list for key:", schema_name)
            iterate_replace_refs_list(item, schema_name)
        else:
            iterate_replace_refs(item, schema_name)
    else:
        print("Reached the end of the dictionary.")

def iterate_replace_refs(my_dict, schema_name):
    """ Recursively iterate through the schema finding $refs """
    for key, value in my_dict.items():
        if isinstance(value, dict):
            print("Iterating through nested dictionary for key:", key)
            iterate_replace_refs(value, schema_name)
        elif isinstance(value, list):
            print("Iterating through nested list for key:", key)
            iterate_replace_refs_list(value, schema_name)
        elif key == "$ref":
            if 'common' in value:
                newref = value
            else:
                newref = "#/properties/" + schema_name + "/" + value[2:]
            my_dict[key] = newref
            print(f"\n*****Found ref: {value}, {newref}\n")
            break
        else:
            print("Key:", key, "Value:", value)
    else:
        print("Reached the end of the dictionary.")

if __name__ == "__main__":
  # Define the directory containing JSON files (replace with your path)
  schema_doc = "schema_doc.json"

  json_schemas = get_json_files('json')
  properties = {}

  for filename in json_schemas:
      print(filename)
      with open(filename, 'r') as f:
            schema = json.load(f)
      name = filename[(filename.rfind("\\")+1):len(filename)-5]
      print(name)
      if name != "bundle":
        obj_properties = {}  
        for obj in schema:
            if obj not in ['$id', '$schema']:
              obj_properties[obj] = schema[obj]
            if obj == 'properties':
                iterate_replace_refs(obj_properties[obj], name)
        properties[name] = obj_properties

  f = open(f"{schema_doc}", "w")
  header = {
  f"$id": "iides/json/schema_doc.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Schema Doc",
  "description": "A combined schema including all schemas.",
  "type": "object",
  "properties": {}
  }

  header['properties'] = properties

  f.write(json.dumps(header, indent=4))
  # f.write(json.dumps(properties, indent=4))

  f.close()
  print("Successfuly made large doc.")