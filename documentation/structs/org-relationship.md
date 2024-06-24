# Org Relationship

Describes the relationship between two organizations involved in an incident.

## Properties

- **`id`** (required) *(string)* : A unique string that begins with "org-relationship--" and is appended with a UUIDv4.
  - Uses pattern: ^org-relationship--[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
- **`org1`** (required) *(string)* : The id of the first organization object.
  - Uses pattern: ^organization--[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
- **`org2`** (required) *(string)* : The id of the second organization object.
  - Uses pattern: ^organization--[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
- **`relationship`** (required) *(string)* : Defines the relationship between the two organizations. Reads as "Org1 is [relationship] to Org2." E.g., "Org1 is vendor to Org2."
	- A constant from [org-relationship-vocab](#org-relationship-vocab)

## Vocabularies

### org-relationship-vocab

Constants: `C`, `P`, `S`, `V`, `T`, `O`

| Const | Value | Description |
| --- | --- | --- |
| C | Competitor | Org1 and Org2 compete with each for the same customers.|
| P | Parent | Org1 is a parent company to Org2.|
| S | Subsidiary | Org1 is a subsidiary (child company) to Org2.|
| V | Vendor | Org1 provides goods, materials, or services to Org2 on a contractual basis.|
| T | Trusted Business Partner | A trusted business partner is an organization or individual that has an alliance (contractually, bonded, etc.) with the victim organization.|
| O | Other | Other type of relationship not described by this vocabulary.|

## License
This file is a part of the Insider Incident Data Exchange Standard (IIDES) - see https://github.com/cmu-sei/IIDES

Copyright 2024 Carnegie Mellon University.

[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution.  Please see Copyright notice for non-US Government use and distribution.

This work is provided “AS-IS” with “NO WARRANTIES OF ANY KIND - EXPRESS OR IMPLIED” and is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.

Requests for permission for non-licensed uses should be directed to the Software Engineering Institute at permission@sei.cmu.edu.

CERT® is registered in the U.S. Patent and Trademark Office by Carnegie Mellon University.

DM24-0776
