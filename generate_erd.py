'''Generates UML wsd file for full ERD'''
import json
from os import listdir

color_map = {
    'person': '#b0d0ed',
    'insider': '#043673',
    'incident': '#009647',
    'Accomplice': '#b0d0ed',
    'collusion': '#b0d0ed',
    'organization': '#007BC0', 
    'sponsor': '#b0d0ed',
    'job': '#33c2C4',
    'impact': '#D4EFDF',
    'target': '#D4EFDF',
    'source': '#D4EFDF',
    'courtCase': '#f9b8bd',
    'charge': '#f9b8bd',
    'sentence': '#f9b8bd',
    'detection': '#FDB515',
    'note': '#D4EFDF',
    'response': '#EF3A47',
    'legalResponse': '#f9b8bd',
    'stressor': '#b0d0ed',
    'attackTTP': '#A456ED'
}

file_lines = []
file_lines.append("@startuml IIDES_TEST\npackage \"IIDES TEST\" #fff {\n\n")

# iterate through all json object files
for object in listdir("json/objects"):
    with open('json/objects/'+object) as f:
        data = json.load(f)
        print(data['title'])
        file_lines.append(
            f"\nclass {data['title'].capitalize()} {color_map[data['title']]} {{\n")
        for property in data['properties']:
            print(f"    {property}")
            if 'items' in data['properties'][property].keys():
                enum = data['properties'][property]['items']['$ref'][8:]
                if data['properties'][property]['type'] == 'array':
                    type_string = f": {enum}[{data['properties'][property]['minItems']}...*]"
                else:
                    type_string = f": {enum}"
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
