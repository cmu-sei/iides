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
- **`country`** *(string)* : The country that the person resided in at the time of the incident. Public implementations should use the standard codes provided by ISO 3166-1 alpha-2.
- **`postal_code`** *(integer)* : The postal code that the person resided in at the time of the incident.
- **`country_of_citizenship`** *(array)* : Citizenship(s) of the person. Public implementations should use the standard codes provided by ISO 3166-1 alpha-2.
  - One or more string values
- **`nationality`** *(array)* : The nationality or nationalities of the person.
  - One or more string values
- **`residency`** *(string)* : Residency status if the person was not a citizen of the country where they resided during the incident.
	- A constant from [residency-vocab](#residency-vocab)
- **`gender`** *(string)* : Sex or gender at the time of the incident.
	- A constant from [gender-vocab](#gender-vocab)
- **`age`** *(integer)* : Age at the time that the incident began.
- **`education`** *(string)* : Highest level of education at the time the incident began.
	- A constant from [education-vocab](#education-vocab)
- **`marital_status`** *(string)* : The marital status at the time of the incident.
	- A constant from [marital-status-vocab](#marital-status-vocab)
- **`number_of_children`** *(integer)* : The number of children that the person is responsible for, at the time of the incident.
- **`comment`** *(string)* : Comments or clarifications regarding any of the Person properties.

## Vocabularies

### suffix-vocab

Values: `Jr`, `Sr`, `III`, `IV`


### residency-vocab

Constants: `N`, `P`, `R`

| Const | Value | Description |
| --- | --- | --- |
| N | Naturalized | A formerly non-citizen that has undergone naturalization and become a citizen.|
| P | Permanent Resident | A foreign citizen who is a permitted to live in a country they are not a citizen of indefinitely.|
| R | Resident Alien | A foreign citizen who is a resident of a country they are not a citizen of.|

### gender-vocab

Constants: `F`, `M`, `N`, `O`

| Const | Value | Description |
| --- | --- | --- |
| F | Female | Female|
| M | Male | Male|
| N | Non-binary | Non-binary|
| O | Other | Other|

### education-vocab

Constants: `4`, `5`, `8`, `2`, `7`, `6`, `3`, `1`

| Const | Value | Description |
| --- | --- | --- |
| 4 | Associates Degree | Possessing an undergraduate degree at the associates level.|
| 5 | Bachelors Degree | Possessing an undegraduate degree at the bachelors level.|
| 8 | Doctorate | Possesing a graduate degree at the doctoral level.|
| 2 | High School Diploma or GED | Possessing a high school diploma or general education development (GED).|
| 7 | Masters Degree | Possessing a graduate degree at the masters level.|
| 6 | Professional Degree | Possessing a degree making one qualified for a particular profession.|
| 3 | Some College | Having completed some amount of collegiate coursework but not possessing a degree.|
| 1 | Some High School | Having completed some amount of high school coursework but not possessing a high school diploma.|

### marital-status-vocab

Constants: `1`, `2`, `3`, `4`, `5`

| Const | Value | Description |
| --- | --- | --- |
| 1 | Single | Not currently married.|
| 2 | Married | Currently belonging to a marriage or common law partnership with a spouse who is an intimate partner.|
| 3 | Divorced | Having legally exited a previous marriage.|
| 4 | Separated | Married but no longer in an intimate partnership with a spouse.|
| 5 | Widowed/Widower | Previously in a marriage that ended due to the death of their spouse.|
