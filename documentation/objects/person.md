# Person
TODO

## Properties
- **`first_name`** *(string)* : TODO
- **`middle_name`** *(string)* : TODO
- **`last_name`** *(string)* : TODO
- **`suffix`** *(string)* : TODO
	- A value from [suffix-vocab](#suffix-vocab)
- **`alias`** *(array)* : TODO
	- One or more string values
- **`city`** *(string)* : TODO
- **`state`** *(string)* : TODO
	- A value from [state-vocab](../common/state-vocab.md)
- **`country`** *(string)* : TODO
	- A value from [country-vocab](../common/country-vocab.md)
- **`postal_code`** *(integer)* : TODO
- **`country_of_citizenship`** *(array)* : TODO
	- One or more values from [country-vocab](../common/country-vocab.md)
- **`nationality`** *(array)* : TODO
	- One or more values from [country-vocab](../common/country-vocab.md)
- **`residency`** *(string)* : TODO
	- A value from [residency-vocab](#residency-vocab)
- **`gender`** *(string)* : TODO
	- A value from [gender-vocab](#gender-vocab)
- **`age`** *(integer)* : TODO
- **`education`** *(string)* : TODO
	- A value from [education-vocab](#education-vocab)
- **`marital_status`** *(string)* : TODO
	- A value from [marital-status-vocab](#marital-status-vocab)
- **`number_of_children`** *(integer)* : TODO
- **`comment`** *(string)* : TODO

## Vocabularies

### suffix-vocab

Values: `Jr`, `Sr`, `III`, `IV`


### residency-vocab

Values: `N`, `P`, `R`

| Const | Value | Description |
| --- | --- | --- |
| N | Naturalized | TODO|
| P | Permanent Resident | TODO|
| R | Resident Alien | TODO|

### gender-vocab

Values: `F`, `M`, `N`, `O`

| Const | Value | Description |
| --- | --- | --- |
| F | Female | TODO|
| M | Male | TODO|
| N | Non-binary | TODO|
| O | Other | TODO|

### education-vocab

Values: `4`, `5`, `8`, `2`, `7`, `6`, `3`, `1`

| Const | Value | Description |
| --- | --- | --- |
| 4 | Associates Degree | TODO|
| 5 | Bachelors Degree | TODO|
| 8 | Doctorate | TODO|
| 2 | High School Diploma or GED | TODO|
| 7 | Masters Degree | TODO|
| 6 | Professional Degree | TODO|
| 3 | Some College | TODO|
| 1 | Some High School | TODO|

### marital-status-vocab

Values: `1`, `2`, `3`, `4`, `5`

| Const | Value | Description |
| --- | --- | --- |
| 1 | Single | TODO|
| 2 | Married | TODO|
| 3 | Divorced | TODO|
| 4 | Separated | TODO|
| 5 | Widowed/Widower | TODO|
