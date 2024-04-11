'''Generates UML wsd file for full ERD'''
import json
from os import listdir

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
    'Attack TTP': '#A456ED'
}

file_lines = []
file_lines.append("@startuml IIDES\npackage \"IIDES\" #fff {\n\n")

# iterate through all json object files
for object in listdir("json/objects"):
    with open('json/objects/'+object) as f:
        data = json.load(f)
        print(data['title'])
        file_lines.append(
            f"\nclass {data['title'].replace(' ','')} {color_map[data['title']]} {{\n")
        for property in data['properties']:
            print(f"    {property}")
            if 'items' in data['properties'][property].keys():
                # property is an array and/or vocab
                type_string = ": "
                if '$ref' in data['properties'][property]['items'].keys():
                    enum = data['properties'][property]['items']['$ref']
                    if enum.endswith('.json'):
                        enum = enum[:-5]
                    type_string += enum[enum.rfind('/')+1:]
                if data['properties'][property]['type'] == 'array':
                    type_string += f"[{data['properties'][property]['minItems']}...*]"
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

    Insider --o{ Accomplice : Relationship
    Incident --|{ Insider : commits <
    Accomplice -- Job
    Job -- Organization : employs <
    Insider -- Job
    Organization }|--|{ Incident
    Organization }o--o{ Organization : OrgRelationship
    Insider }o--o| Sponsor
    Accomplice }o--o| Sponsor
    Insider |o--o| Organization : owns >
    Insider -- Collusion
    Collusion -- Insider
    Incident --|{ Impact
    Incident --|{ Target
    Incident --o{ Source
    Incident --o{ Note
    CourtCase --|{ Charge
    CourtCase |o--|{ Sentence
    Incident -- Detection
    Incident -- Response
    Response -- LegalResponse
    LegalResponse --|{ CourtCase
    Organization --|{ Stressor
    Stressor }|-- Insider
    Incident --o{ AttackTTP
'''
f.write(relationships)

f.write("}\n@enduml")
f.close()
