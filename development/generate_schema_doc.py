"""
File: generate_large_schema.py

Summary:

This file will generate a file containing all the schema in one
large file. The schema file can then be used offline.

*** COMMON REFERENCES ARE BROKEN ***
** MIGHT BE MISSING SOME REFERENCES...

## Licensing
This file is a part of the Insider Incident Data Exchange Standard (IIDES) - see [https://github.com/cmu-sei/IIDES](https://github.com/cmu-sei/IIDES)
Copyright 2024 Carnegie Mellon University.
[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution. Please see Copyright notice for non-US Government use and distribution.
This work is provided "AS-IS" with "NO WARRANTIES OF ANY KIND - EXPRESS OR IMPLIED" and is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.
Requests for permission for non-licensed uses should be directed to the Software Engineering Institute at permission@sei.cmu.edu.
CERT® is registered in the U.S. Patent and Trademark Office by Carnegie Mellon University.
DM24-0776
"""
import os
import json
import sys

script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
iides_directory = os.path.dirname(script_directory)
JSON_PATH = os.path.join(iides_directory, 'json')


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
    schema_doc = os.path.join(iides_directory, "iides_full_schema.json")

    json_schemas = get_json_files(JSON_PATH)
    properties = {}

    for filename in json_schemas:
        print(filename)
        with open(filename, 'r') as f:
            schema = json.load(f)
        name = filename[len(iides_directory)+1:-5]
        print(name)
        if name != "bundle":
            obj_properties = {}
            for obj in schema:
                if obj not in ['$id', '$schema']:
                    obj_properties[obj] = schema[obj]
                if obj == 'properties':
                    iterate_replace_refs(obj_properties[obj], name)
            properties[name] = obj_properties

    f = open(schema_doc, "w")
    header = {
        "$id": "iides/json/iides_full_schema.json",
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": "IIDES Schema",
        "description": "A combined schema including all subschemas.",
        "type": "object",
        "properties": {}
    }

    header['properties'] = properties

    f.write(json.dumps(header, indent=4))
    f.close()

    print("Successfuly made large doc.")
