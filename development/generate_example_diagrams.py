'''Generates diagrams (UML wsd) from example jsons'''

import json
import os
import sys

script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
iides_directory = os.path.dirname(script_directory)
JSON_PATH = os.path.join(iides_directory, 'examples', 'json')


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

# All UML Relationships
relationships = {
    ("Insider", "Accomplice"): ["Insider --o{ Accomplice\n"],
    ("Incident", "Insider"): ["Incident --|{ Insider : commits <\n"],
    ("Accomplice", "Job"): ["Accomplice |o--o{ Job\n"], 
    ("Job", "Organization"): ["Job }o--o| Organization : employs <\n"],
    ("Insider", "Job"): ["Insider |o--o{ Job\n"],
    ("Organization", "Incident"): ["Organization }o--o| Incident\n"],
    ("Organization", "OrgRelationship"): ["Organization }o-- OrgRelationship\n", "OrgRelationship --o{ Organization\n"],
    ("Insider", "Sponsor"): ["Insider }o--o| Sponsor\n"],
    ("Accomplice", "Sponsor"): ["Accomplice }o--o| Sponsor\n"],
    ("Insider", "Organization"): ["Insider }o..o{ Organization\n"],
    ("Accomplice", "Organization"): ["Accomplice }o..o{ Organization\n"],
    ("Insider", "Collusion"): ["Insider -- Collusion\n", "Collusion -- Insider"],
    ("Incident", "Impact"): ["Incident --o{ Impact\n"],
    ("Incident", "Target"): ["Incident --o{ Target\n"],
    ("Incident", "Source"): ["Incident --o{ Source\n"],
    ("Incident", "Note"): ["Incident --o{ Note\n"],
    ("CourtCase", "Charge"): ["CourtCase ||--o{ Charge\n"],
    ("CourtCase", "Sentence"): ["CourtCase ||--o{ Sentence\n"],
    ("Incident", "Detection"): ["Incident --o| Detection\n"],
    ("Incident", "Response"): ["Incident --o| Response\n"],
    ("Response", "LegalResponse"): ["Response ||--o| LegalResponse\n"],
    ("LegalResponse", "CourtCase"): ["LegalResponse ||--o{ CourtCase\n"],
    ("Organization", "Stressor"): ["Organization --o{ Stressor\n"],
    ("Stressor", "Insider"): ["Stressor }o-- Insider\n"],
    ("Incident", "TTP"): ["Incident --o{ TTP\n"]
}

count = 1

# loop through our "example_jsons" directory 
for file_name in os.listdir(JSON_PATH):
    file_lines = []
    seen_classes = set()

    file_lines.append(f"@startuml {file_name[:-5].capitalize()}\n\n")
    if (file_name == 'README.md'): continue

    with open(JSON_PATH + '/' + file_name) as f:
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

            seen_classes.add(name)

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
    for r in relationships:
        if (r[0] in seen_classes and r[1] in seen_classes):
            file_lines.extend(relationships[r])
    file_lines.append("@enduml")

    new_path = os.path.join(iides_directory, 'UML', 'source', f'{file_name[:-5]}.wsd')
    new_f = open(new_path, "w")
    new_f.writelines(file_lines)
    count += 1
