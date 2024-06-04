'''Generates diagrams (UML wsd) from example jsons'''

import json
import os

example_jsons_path = 'example_jsons'

# The color maps
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
    'CourtCase': '#f9b8bd',
    'Charge': '#f9b8bd',
    'Sentence': '#f9b8bd',
    'Detection': '#FDB515',
    'Note': '#D4EFDF',
    'Response': '#EF3A47',
    'LegalResponse': '#f9b8bd',
    'Stressor': '#b0d0ed',
    'TTP': '#A456ED',
    'OrgRelationship': '#F5F5F5',
    'OrgOwner': '#F5F5F5',
    'Relationship': '#F5F5F5'
}

# All UML relationships
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

count = 1

# loop through our "example_jsons" directory 
for file_name in os.listdir(example_jsons_path):
    file_lines = []
    file_lines.append("@startuml IIDES\n\n")
    if (file_name == 'README.md'): continue

    with open(example_jsons_path + '/' + file_name) as f:
        data = json.load(f)
        for obj in data.get("objects"):
            class_lines = []

            # grab name and write the UML class header
            id = obj.get("id")
            name = id[0:id.find("--")]
            if ("-" in name):
                parts = name.split("-")
                parts[0] = parts[0].capitalize()
                parts[1] = parts[1].capitalize()
                name = ''.join(parts)
            elif (name == 'ttp'):
                name = 'TTP'
            else:
                name = name.capitalize()

            line_1 = f"Class {name} {color_map[name]}" + " {\n"
            class_lines.append(line_1)

            # now write the rest of the class based on the 
            # inner attributes of the object
            for key in obj:
                curr_line = ''
                if key == "id" or key == "title":
                    curr_line += "* "
                else:
                    curr_line += "+ "    

                # add newlines to long strings (like the summary)
                if isinstance(obj[key], str):
                    words = obj[key].split()
                    text = ""
                    word_count = 0
                    for word in words:
                        text += word + " "
                        word_count += 1
                        # adding a new line every 15 words
                        if word_count == 15: 
                            text += "\n"
                            word_count = 0
                    curr_line += f"{key} : {text}\n"
                else:
                    curr_line += f"{key} : {obj[key]}\n"
                
                # add this to our "class_lines"
                class_lines.append(curr_line)
            
            # finish the class by placing a line and end curly bracket,
            # then we add it to the full file in 'file_lines'
            class_lines.append("---\n}\n")
            file_lines.extend(class_lines)

    # add relationships and the enduml before finishing
    file_lines.append(relationships)
    file_lines.append("@enduml")

    new_f = open(f"example_diagrams/example{count}.wsd", "w")
    new_f.writelines(file_lines)
    count += 1