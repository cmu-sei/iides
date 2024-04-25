'''Generates UML wsd file for full ERD'''
import json
import os


JSON_PATH = "json"
color_map = {
    'Person': '#b0d0ed',
    'Insider': '#043673',
    'Incident': '#009647',
    'Accomplice': '#b0d0ed',
    'Collusion': '#b0d0ed',
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
    'State Vocab': '#FFFFFF',
    'Insider Relationship Vocab': '#FFFFFF',
    'Country Vocab': '#FFFFFF',
    'Org Relationship': '#FFFFFF'
}


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

f = open("UML/source/iides.wsd", "w")
f.writelines(file_lines)

# Add relationships
relationships = '''

    Insider --o{ Accomplice
    Incident --|{ Insider : commits <
    Accomplice |o--o{ Job
    Job -- Organization : employs <
    Insider -- Job
    Organization }|--|{ Incident
    Organization -- OrgRelationship
    OrgRelationship -- Organization
    Insider }o--o| Sponsor
    Accomplice }o--o| Sponsor
    Insider |o--o| Organization : owns >
    Insider -- Collusion
    Collusion -- Insider
    Incident --o{ Impact
    Incident --|{ Target
    Incident --o{ Source
    Incident --o{ Note
    CourtCase ||--o{ Charge
    CourtCase ||--o{ Sentence
    Incident --o| Detection
    Incident --o| Response
    Response ||--o| LegalResponse
    LegalResponse ||--o{ CourtCase
    Organization --|{ Stressor
    Stressor }|-- Insider
    Incident --o{ TTP
'''
f.write(relationships)

f.write("}\n@enduml")
f.close()
