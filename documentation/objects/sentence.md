# Sentence

TODO

## Properties

- **`id`** (required) *(string)* : A unique string that begins with "sentence--" and is appended with a UUIDv4.
	- Uses pattern: ^sentence--[UUIDv4]
- **`sentence_type`** (required) *(string)* : TODO
	- A constant from [sentence-type-vocab](#sentence-type-vocab)
- **`quantity`** *(integer)* : The quantity of the sentence imposed. MUST be used with the metric property if used.
- **`metric`** *(string)* : The measurement type of the sentence imposed. MUST be used with the quantity property if used.
	- A constant from [sentence-metric-vocab](#sentence-metric-vocab)
- **`concurrency`** *(boolean)* : whether the sentence is to run concurrently (at the same time as) the sentence for other charges

## Vocabularies

### sentence-type-vocab

Constants: `01`, `02`, `03`, `04`, `05`, `06`, `07`, `08`, `09`, `10`, `11`, `12`, `13`, `14`, `15`, `16`, `17`, `18`

| Const | Value | Description |
| --- | --- | --- |
| 01 | Assessment | TODO|
| 02 | Community Service | TODO|
| 03 | Damages | TODO|
| 04 | Deportation | TODO|
| 05 | Drug Testing | TODO|
| 06 | Fine | TODO|
| 07 | Forfeiture | TODO|
| 08 | House Arrest | TODO|
| 09 | Incarceration | TODO|
| 10 | Injunction | TODO|
| 11 | Mental Health Treatment | TODO|
| 12 | No Internet Access | TODO|
| 13 | Probation | TODO|
| 14 | Restitution | TODO|
| 15 | Restraining Order | TODO|
| 16 | Special Assessment | TODO|
| 17 | Substance Abuse Treatment | TODO|
| 18 | Supervised Release | TODO|

### sentence-metric-vocab

Constants: `H`, `D`, `M`, `Y`, `D`

| Const | Value | Description |
| --- | --- | --- |
| H | Hour(s) | TODO|
| D | Day(s) | TODO|
| M | Month(s) | TODO|
| Y | Year(s) | TODO|
| D | Dollar(s) | TODO|
