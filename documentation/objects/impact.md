# Impact

This is the quantified impact of the incident on the victim organization. An incident may have one or more impacts. An impact MUST be associated with only one incident.

## Properties

- **`id`** (required) _(string)_ : A unique string that begins with "impact--" and is appended with a UUIDv4
  - Uses pattern: ^impact--[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
- **`high`** (required) _(number)_ : The quantity of the impact being measured. If a range, the high end of the range
- **`low`** _(number)_ : If a range, the low estimate of the range
- **`metric`** (required) _(string)_ : The type of impact being quantified
  - A constant from [impact-metric-vocab](#impact-metric-vocab)
- **`estimated`** (required) _(boolean)_ : True if the impact `high` or `low` property is an estimated number
- **`comment`** _(string)_ : Clarifying comments

## Vocabularies

### impact-metric-vocab

Constants: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`, `16`

| Const | Value               | Description                                                                            |
| ----- | ------------------- | -------------------------------------------------------------------------------------- |
| 1     | Accounts            | Computer, network, financial, user accounts                                            |
| 2     | Credit card numbers | Physical or digital credit or debit card numbers                                       |
| 3     | Customers           | The number of customers effected (e.g., through stolen accounts, PII, etc.)            |
| 4     | Documents           | The number of physical or digital documents effected (stolen, deleted, modified, etc.) |
| 5     | Dollars             | Specific financial impact of money stolen, restitution ordered, etc.                   |
| 6     | Employees           | Number of employees effected                                                           |
| 7     | Files               | Number of physical or digital files stolen, read, or compromised                       |
| 8     | Hours               | Down time or time effected in hours                                                    |
| 9     | Pages               | Number of individual pages of a document(s) or file(s)                                 |
| 10    | Person-hours        | Person-hours or work time effected. Often occurs in sabotage incidents                 |
| 11    | Identities          | PII records, user information, etc.                                                    |
| 12    | Items               | Generic items such as merchandise                                                      |
| 13    | Systems             | Workstations, servers, virtual machines, etc.                                          |
| 14    | Records             | Records or rows such as database or accounting records                                 |
| 15    | Drugs               | Number of pills, vials, syringes, etc. for drugs or medicine taken or effected         |
| 16    | Trade Secrets       | Number of trade secrets stolen or effected                                             |

## License

This file is a part of the Insider Incident Data Exchange Standard (IIDES) - see https://github.com/cmu-sei/IIDES

Copyright 2024 Carnegie Mellon University.

[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution. Please see Copyright notice for non-US Government use and distribution.

This work is provided \"AS-IS\" with \"NO WARRANTIES OF ANY KIND - EXPRESS OR IMPLIED\" and is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.

Requests for permission for non-licensed uses should be directed to the Software Engineering Institute at permission@sei.cmu.edu.

CERT® is registered in the U.S. Patent and Trademark Office by Carnegie Mellon University.

DM24-0776
