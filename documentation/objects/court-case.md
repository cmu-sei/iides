# Court Case

Information about legal procedings related to the incident, whether charges against the insider or their accomplice(s), a civil suit, or a suit against another entity involved in the incident. A legal response can have one or more court cases, and a court case MUST be tied to only one legal response. Each court case can have one or more charges and one or more sentences.

## Properties

- **`id`** (required) *(string)* : A unique string that begins with "court-case--" and is appended with a UUIDv4.
  - Uses pattern: ^court-case--[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
- **`case_number`** *(string)* : A case number assigned by the court system in which the case is being tried.
- **`case_title`** *(string)* : Title provided by the court system (e.g., 'USA v. LastName' or 'USA v. LastName, et al.').
- **`court_country`** *(string)* : Country where the case was tried.
	- A constant from [country-vocab](../common/country-vocab.md)
- **`court_state`** *(string)* : State or region where the case was tried.
	- A constant from [state-vocab](../common/state-vocab.md)
- **`court_district`** *(string)* : District where the case was tried, if applicable (e.g., "CA Central District Court").
- **`court_type`** *(string)* : Type or level of the court where the case is tried.
	- A constant from [court-type-vocab](#court-type-vocab)
- **`case_type`** *(string)* : Type of case.
	- A constant from [case-type-vocab](#case-type-vocab)
- **`defendant`** *(array)* : The names of all the defendants (or respondants, or appellees) in the case.
  - One or more string values
- **`plaintiff`** *(array)* : The names of all the plaintiffs (or petitioners, or appellants) in the case.
  - One or more string values
- **`comment`** *(string)* : Clarifying comments about any of the court case details, or its associated charges and sentences, such as which sentences run concurrently, the structure of a plea deal, or the status of the case.

## Vocabularies

### court-type-vocab

Constants: `1`, `2`, `3`

| Const | Value | Description |
| --- | --- | --- |
| 1 | Federal | Top level government court.|
| 2 | International | Intergovernmental level court.|
| 3 | State | State or regional level government court.|

### case-type-vocab

Constants: `1`, `2`

| Const | Value | Description |
| --- | --- | --- |
| 1 | Civil | A case dealing with a dispute between two people or organizations.|
| 2 | Criminal | A case dealing with a violation of criminal law.|
