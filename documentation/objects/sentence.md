# Sentence
TODO

## Properties
- **`id`** (required) *(string)* : TODO . Uses pattern 'sentence--[UUIDv4]'
	- pattern: ^sentence--[UUIDv4]
- **`sentence_type`** (required) *(string)* : TODO
	- A value from [sentence-type-vocab](#sentence-type-vocab)
- **`quantity`** *(integer)* : TODO
- **`metric`** *(string)* : TODO
	- A value from [sentence-metric-vocab](#sentence-metric-vocab)
- **`concurrency`** *(boolean)* : TODO

## Vocabularies

### sentence-type-vocab

Values: `01`, `02`, `03`, `04`, `05`, `06`, `07`, `08`, `09`, `10`, `11`, `12`, `13`, `14`, `15`, `16`, `17`, `18`

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

Values: `H`, `D`, `M`, `Y`, `D`

| Const | Value | Description |
| --- | --- | --- |
| H | Hour(s) | TODO|
| D | Day(s) | TODO|
| M | Month(s) | TODO|
| Y | Year(s) | TODO|
| D | Dollar(s) | TODO|
