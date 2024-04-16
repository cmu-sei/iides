# Court Case
TODO

## Properties
- **`id`** (required) *(string)* : TODO
	- Uses pattern: ^court-case--[UUIDv4]
- **`case_number`** *(string)* : TODO
- **`court_country`** *(string)* : TODO
	- A value from [country-vocab](../common/country-vocab.md)
- **`court_state`** *(string)* : TODO
	- A value from [state-vocab](../common/state-vocab.md)
- **`court_district`** *(string)* : TODO
- **`court_type`** *(string)* : TODO
	- A value from [court-type-vocab](#court-type-vocab)
- **`case_type`** *(string)* : TODO
	- A value from [case-type-vocab](#case-type-vocab)
- **`defendant`** *(array)* : TODO
	- One or more string values
- **`plaintiff`** *(array)* : TODO
	- One or more string values
- **`comment`** *(string)* : TODO

## Vocabularies

### court-type-vocab

Values: `1`, `2`, `3`

| Const | Value | Description |
| --- | --- | --- |
| 1 | Federal | TODO|
| 2 | Foreign | TODO|
| 3 | State | TODO|

### case-type-vocab

Values: `1`, `2`

| Const | Value | Description |
| --- | --- | --- |
| 1 | Civil | TODO|
| 2 | Criminal | TODO|
