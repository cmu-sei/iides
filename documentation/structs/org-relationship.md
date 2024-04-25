# Org Relationship

Describes the relationship between two organizations involved in an incident.

## Properties

- **`id`** (required) *(string)* : TODO
	- Uses pattern: ^org-relationship--[UUIDv4]
- **`org1`** (required) *(string)* : The id of the first organization object.
	- Uses pattern: ^organization--[UUIDv4]
- **`org2`** (required) *(string)* : The id of the second organization object.
	- Uses pattern: ^organization--[UUIDv4]
- **`relationship`** (required) *(string)* : TODO. Reads as "Org1 is [relationship] to Org2." E.g., "Org1 is vendor to Org2."
	- A constant from [org-relationship-vocab](#org-relationship-vocab)

## Vocabularies

### org-relationship-vocab

Constants: `C`, `P`, `S`, `V`, `T`, `O`

| Const | Value | Description |
| --- | --- | --- |
| C | Competitor | TODO|
| P | Parent | TODO|
| S | Subsidiary | TODO|
| V | Vendor | TODO|
| T | Trusted Business Partner | A trusted business partner is an organization or individual that has an alliance (contractually, bonded, etc.) with the victim organization.|
| O | Other | Other type of relationship not described by this vocabulary.|
