# Sponsor

A sponsor is an individual or entity that recruited, instigated, motivated, or otherwise supported the insider's action. A sponsor MUST be associated with at least one insider or accomplice. The sponsor may be associated with multiple insiders or accomplices.

## Properties

- **`id`** (required) *(string)* : A unique string that begins with "sponsor--" and is appended with a UUIDv4
  - Uses pattern: ^sponsor--[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
- **`name`** *(string)* : The name of the individual or entity sponsoring the insider's actions
- **`sponsor_type`** *(string)* : The type of sponsor
	- A constant from [sponsor-type-vocab](#sponsor-type-vocab)

## Vocabularies

### sponsor-type-vocab

Constants: `OC`, `SS`, `FN`, `CE`, `OT`

| Const | Value | Description |
| --- | --- | --- |
| OC | Organized Crime | E.g., terrorist group, mafia, gang|
| SS | State Sponsor | Geopolitical, state, or national military with a speciific country of origin|
| FN | Foreign National | An individual whose objectives are aligned with either the political, commercial, or military interests of a country other than where the incident originated|
| CE | Criminal Enterprise | A group of individuals with an identified hierarchy or structure who engage in significant criminal activity|
| OT | Other | A sponsor type not listed in this vocabulary|

## License
This file is a part of the Insider Incident Data Exchange Standard (IIDES) - see https://github.com/cmu-sei/IIDES

Copyright 2024 Carnegie Mellon University.

[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution.  Please see Copyright notice for non-US Government use and distribution.

This work is provided "AS-IS" with "NO WARRANTIES OF ANY KIND - EXPRESS OR IMPLIED" and is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.

Requests for permission for non-licensed uses should be directed to the Software Engineering Institute at permission@sei.cmu.edu.

CERT® is registered in the U.S. Patent and Trademark Office by Carnegie Mellon University.

DM24-0776
