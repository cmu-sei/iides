# Court Case

Court Case contains information about legal proceedings related to the incident, whether it is charges against the insider or their accomplice(s), a civil suit, or a suit against another entity involved in the incident. A legal response can have one or more court cases, and a court case MUST be tied to only one legal response. Each court case can have one or more charges and one or more sentences.

## Properties

- **`id`** (required) _(string)_ : A unique string that begins with "court-case--" and is appended with a UUIDv4
  - Uses pattern: ^court-case--[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
- **`case_number`** _(string)_ : A case number assigned by the court system in which the case is being tried
- **`case_title`** _(string)_ : Title provided by the court system (e.g., 'USA v. LastName' or 'USA v. LastName, et al.')
- **`court_country`** _(string)_ : Country where the case was tried
  - A constant from [country-vocab](../common/country-vocab.md)
- **`court_state`** _(string)_ : State or region where the case was tried
  - A constant from [state-vocab](../common/state-vocab.md)
- **`court_district`** _(string)_ : District where the case was tried, if applicable (e.g., "CA Central District Court")
- **`court_type`** _(string)_ : Type or level of the court where the case is tried
  - A constant from [court-type-vocab](#court-type-vocab)
- **`case_type`** _(string)_ : Type of case
  - A constant from [case-type-vocab](#case-type-vocab)
- **`defendant`** _(array)_ : The names of all the defendants (or respondents or appellees) in the case
  - One or more string values
- **`plaintiff`** _(array)_ : The names of all the plaintiffs (or petitioners or appellants) in the case
  - One or more string values
- **`comment`** _(string)_ : Clarifying comments about any of the court case details, or its associated charges and sentences, such as concurrent sentences, the structure of a plea deal, or the status of the case

## Vocabularies

### court-type-vocab

Constants: `1`, `2`, `3`

| Const | Value         | Description                              |
| ----- | ------------- | ---------------------------------------- |
| 1     | Federal       | Top level government court               |
| 2     | International | Intergovernmental level court            |
| 3     | State         | State or regional level government court |

### case-type-vocab

Constants: `1`, `2`

| Const | Value    | Description                                                       |
| ----- | -------- | ----------------------------------------------------------------- |
| 1     | Civil    | A case dealing with a dispute between two people or organizations |
| 2     | Criminal | A case dealing with a violation of criminal law                   |

## License

This file is a part of the Insider Incident Data Exchange Standard (IIDES) - see https://github.com/cmu-sei/IIDES

Copyright 2024 Carnegie Mellon University.

[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution. Please see Copyright notice for non-US Government use and distribution.

This work is provided \"AS-IS\" with \"NO WARRANTIES OF ANY KIND - EXPRESS OR IMPLIED\" and is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.

Requests for permission for non-licensed uses should be directed to the Software Engineering Institute at permission@sei.cmu.edu.

CERT® is registered in the U.S. Patent and Trademark Office by Carnegie Mellon University.

DM24-0776
