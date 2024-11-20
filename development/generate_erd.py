'''Generates UML wsd file for full ERD

## Licensing
This file is a part of the Insider Incident Data Exchange Standard (IIDES) - see [https://github.com/cmu-sei/IIDES](https://github.com/cmu-sei/IIDES)
Copyright 2024 Carnegie Mellon University.
[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution. Please see Copyright notice for non-US Government use and distribution.
This work is provided "AS-IS" with "NO WARRANTIES OF ANY KIND - EXPRESS OR IMPLIED" and is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.
Requests for permission for non-licensed uses should be directed to the Software Engineering Institute at permission@sei.cmu.edu.
CERT® is registered in the U.S. Patent and Trademark Office by Carnegie Mellon University.
DM24-0776'''
import json
import os
import sys


script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
iides_directory = os.path.dirname(script_directory)
JSON_PATH = os.path.join(iides_directory, 'json')

color_map = {
    'Person': '#b0d0ed',
    'Insider': '#043673;text:white',
    'Incident': '#009647',
    'Accomplice': '#b0d0ed',
    'Collusion': '#F5F5F5',
    'Organization': '#007BC0', 
    'Sponsor': '#b0d0ed',
    'Job': '#33c2C4',
    'Impact': '#D4EFDF',
    'Target': '#D4EFDF',
    'Source': '#D4EFDF',
    'Court Case': '#f9b8bd',
    'Charge': '#f9b8bd',
    'Sentence': '#f9b8bd',
    'Detection': '#FDB515',
    'Note': '#D4EFDF',
    'Response': '#EF3A47',
    'Legal Response': '#f9b8bd',
    'Stressor': '#b0d0ed',
    'TTP': '#A456ED',
    'Org Relationship': '#F5F5F5',
    'Org Owner': '#F5F5F5',
    'Relationship': '#F5F5F5',
    'Bundle': '#F5F5F5',
}


def get_json_files():
    '''Returns json files from which to generate markdown'''
    fnames = []
    for root, _, f_names in os.walk(JSON_PATH):
        for f in f_names:
            if "common" not in root:
                fnames.append(os.path.join(root, f))
    return fnames


def get_ref(ref):
    '''Parse json $ref string'''

    if ref.startswith('#'):
        # internal file reference
        ref_string = f"{ref[8:]}"
    else:
        # reference to other file
        ref_string = f"{ref[ref.rfind('/')+1:-5]}"
    return ref_string


file_lines = []
file_lines.append("@startuml IIDES\npackage \"IIDES\" #fff {\n\n")

# iterate through all json object files
json_files = get_json_files()
for filename in json_files:
    with open(filename) as f:
        data = json.load(f)
        print(data['title'])
        print(filename)
        if 'json/structs/' in filename:
            class_line = f"\nstruct {data['title'].replace(' ','')} "
        else:
            class_line = f"\nclass {data['title'].replace(' ','')} "
        if '$ref' in data.keys():
            # class inherits from another
            class_line += f"<<{data['$ref'][2:-5].capitalize()}>> "
        class_line += f"{color_map[data['title']]} {{\n"

        file_lines.append(class_line)
        for property in data['properties']:
            print(f"    {property}")
            if 'prefixItems' in data['properties'][property].keys():
                # property is an array of tuples
                type_string = ": ("
                refs = []
                for p_item in data['properties'][property]['prefixItems']:
                    if list(p_item.keys())[0] == '$ref':
                        refs.append(get_ref(p_item['$ref']))
                if len(refs) == 1:
                    type_string += f"{{field}} {refs[0]}, date)[1...*]"
                else:
                    type_string += f"{{field}} {', '.join(refs)})[1...*]"
            elif 'items' in data['properties'][property].keys():
                # property is an array
                type_string = ": "
                if '$ref' in data['properties'][property]['items'].keys():
                    type_string += get_ref(data['properties'][property]['items']['$ref'])
                else:
                    type_string += "string"
                if data['properties'][property]['type'] == 'array':
                    type_string += f"[{data['properties'][property]['minItems']}...*]"
            else:
                if '$ref' in data['properties'][property].keys():
                    type_string = f": {get_ref(data['properties'][property]['$ref'])}"
                else:
                    type_string = f": {data['properties'][property]['type']}"
            if property in data['required']:
                file_lines.append(f"\t* {property} {type_string} \n")
            else:
                file_lines.append(f"\t+ {property} {type_string} \n")

        file_lines.append("}")

new_file = os.path.join(iides_directory, 'UML/source/iides.wsd')
f = open(new_file, "w")
f.writelines(file_lines)

# Add relationships
relationships = '''

    Insider --o{ Accomplice
    Incident --|{ Insider : commits <
    Accomplice |o--o{ Job
    Job }o--o| Organization : employs <
    Insider |o--o{ Job
    Organization }o--o| Incident
    Organization }o-- OrgRelationship
    OrgRelationship --o{ Organization
    Insider }o--o| Sponsor
    Accomplice }o--o| Sponsor
    Insider }o..o{ Organization : OrgOwner >
    Accomplice }o..o{ Organization : OrgOwner >
    Insider -- Collusion
    Collusion -- Insider
    Incident --o{ Impact
    Incident --o{ Target
    Incident --o{ Source
    Incident --o{ Note
    CourtCase ||--o{ Charge
    CourtCase ||--o{ Sentence
    Incident --o| Detection
    Incident --o| Response
    Response ||--o| LegalResponse
    LegalResponse ||--o{ CourtCase
    Organization --o{ Stressor
    Stressor }o-- Insider
    Incident --o{ TTP
'''
f.write(relationships)

f.write('note as N1\n<size:10>This file is a part of the Insider Incident Data Exchange Standard (IIDES)\n<size:10>- see https://github.com/cmu-sei/IIDES\n<size:5> \n<size:10>Copyright 2024 Carnegie Mellon University.\n<size:5> \n<size:10>[DISTRIBUTION STATEMENT A] This material has been approved for public release\n<size:10>and unlimited distribution.  Please see Copyright notice for non-US\n<size:10>Government use and distribution.\n<size:5> \n<size:10>This work is provided \"AS-IS\" with \"NO WARRANTIES OF ANY KIND - EXPRESS OR IMPLIED\"\n<size:10>and is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.\n<size:5> \n<size:10>Requests for permission for non-licensed uses should be directed to the\n<size:10>Software Engineering Institute at permission@sei.cmu.edu.\n<size:5> \n<size:10>CERT® is registered in the U.S. Patent and Trademark Office by Carnegie Mellon University.\n<size:10>DM24-0776\nend note\n')

f.write("}\n@enduml")
f.close()
