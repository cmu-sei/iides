# Person

Abstract class for inheritance by the Insider and Accomplice objects. Describes the properties of an individual that MAY be inherited by those classes.

## Properties

- **`first_name`** *(string)* : The first, or given, name of the individual.
- **`middle_name`** *(string)* : The middle name of the individual.
- **`last_name`** *(string)* : The last, or family, name of the individual.
- **`suffix`** *(string)* : The name suffix of the individual.
	- A constant from [suffix-vocab](#suffix-vocab)
- **`alias`** *(array)* : A list of aliases (other names) the individual has used, and/or the anonymized of the individual in court records.
	- One or more string values
- **`city`** *(string)* : The city (or county/district) that the person resided in at the time of the incident.
- **`state`** *(string)* : The state (or region) that the person resided in at the time of the incident.
	- A constant from [state-vocab](../common/state-vocab.md)
- **`country`** *(string)* : The country that the person resided in at the time of the incident.
	- A constant from [country-vocab](../common/country-vocab.md)
- **`postal_code`** *(integer)* : The postal code that the person resided in at the time of the incident.
- **`country_of_citizenship`** *(array)* : TODO
	- One or more values from [country-vocab](../common/country-vocab.md)
- **`nationality`** *(array)* : TODO
	- One or more values from [country-vocab](../common/country-vocab.md)
- **`residency`** *(string)* : TODO
	- A constant from [residency-vocab](#residency-vocab)
- **`gender`** *(string)* : TODO
	- A constant from [gender-vocab](#gender-vocab)
- **`age`** *(integer)* : TODO
- **`education`** *(string)* : TODO
	- A constant from [education-vocab](#education-vocab)
- **`marital_status`** *(string)* : TODO
	- A constant from [marital-status-vocab](#marital-status-vocab)
- **`number_of_children`** *(integer)* : TODO
- **`comment`** *(string)* : TODO

## Vocabularies

### suffix-vocab

Values: `Jr`, `Sr`, `III`, `IV`


### residency-vocab

Constants: `N`, `P`, `R`

| Const | Value | Description |
| --- | --- | --- |
| N | Naturalized | TODO|
| P | Permanent Resident | TODO|
| R | Resident Alien | TODO|

### gender-vocab

Constants: `F`, `M`, `N`, `O`

| Const | Value | Description |
| --- | --- | --- |
| F | Female | TODO|
| M | Male | TODO|
| N | Non-binary | TODO|
| O | Other | TODO|

### education-vocab

Constants: `4`, `5`, `8`, `2`, `7`, `6`, `3`, `1`

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

Constants: `1`, `2`, `3`, `4`, `5`

| Const | Value | Description |
| --- | --- | --- |
| 1 | Single | TODO|
| 2 | Married | TODO|
| 3 | Divorced | TODO|
| 4 | Separated | TODO|
| 5 | Widowed/Widower | TODO|
