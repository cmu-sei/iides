# Sponsor

An individual or entity that recruited, instigated, motivated, or otherwise supported the insider's action. A sponsor MUST be associated with at least one insider or accomplice. It may be associated with multiple insider and/or accomplices.

## Properties

- **`id`** (required) *(string)* : A unique string that begins with "sponsor--" and is appended with a UUIDv4.
	- Uses pattern: ^sponsor--[UUIDv4]
- **`name`** *(string)* : The name of the individual or entity sponsoring the insider's actions.
- **`sponsor_type`** *(string)* : The type of sponsor. If unknown, leave blank.
	- A constant from [sponsor-type-vocab](#sponsor-type-vocab)

## Vocabularies

### sponsor-type-vocab

Constants: `OC`, `SS`, `FN`, `CE`, `OT`

| Const | Value | Description |
| --- | --- | --- |
| OC | Organized Crime | E.g., terrorist group, mafia, gang.|
| SS | State Sponsor | Geopolitical, state, or national military with a speciific country of origin.|
| FN | Foreign National | An individual whose objectives are aligned with either the political, commercial, or military interests of a country other than where the incident originated.|
| CE | Criminal Enterprise | A group of individuals with an identified hierarchy or structure who engage in significant criminal activity.|
| OT | Other | A sponsor type not listed in this vocabulary.|
