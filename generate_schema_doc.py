"""
File: generate_large_schema.py

Summary:

This file will generate a file containing all the schema in one
large file. The schema file can them be used offline.

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
      obj_properties = {}  
      for obj in schema:
          if obj not in ['$id', '$schema']:
            obj_properties[obj] = schema[obj]
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