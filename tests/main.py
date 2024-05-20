"Test schema files for formatting and validation"
import json
import os
import pathlib
from jsonschema import validate, exceptions


cur = pathlib.Path(__file__).parent.resolve()

for subdir, dirs, files in os.walk(cur):
    for file in files:
        if os.path.isfile(os.path.join(subdir, file)) and file.endswith('.json'):
            # load the test file
            with open(os.path.join(subdir, file), encoding='utf-8') as json_file:
                test_file = json.load(json_file)
            print(f"\n{test_file['description']}")
            # load the schema file that the test file references
            with open(os.path.join(cur, test_file['$schema']), encoding='utf-8') as json_file:
                # json formatting will be tested on load
                schema = json.load(json_file)

            # load each test_case
            case_num = 0
            for test_case in test_file['tests']:
                # validate the schema file
                out = f"\tTest case {case_num}: "
                try:
                    validate(instance=test_case['data'], schema=schema)
                except exceptions.ValidationError:
                    if test_case['valid']:
                        # If validation error but the data is correct
                        print(out, "Failed, but shouldn't have", f"\t({test_case['description']})")
                    else:
                        # If validation error and data was incorrect
                        print(out, "Good")
                else:
                    if test_case['valid']:
                        # If no validation error and the data is correct
                        print(out, "Good")
                    else:
                        # If no validation error and the data is incorrect
                        print(out, "Passed, but shouldn't have", f"\t({test_case['description']})")

                case_num += 1
