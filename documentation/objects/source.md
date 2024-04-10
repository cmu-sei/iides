# Source
TODO

## Properties
- **`id`** (required) *(string)* : TODO . Uses pattern 'source--[UUIDv4]'
	- pattern: ^source--[UUIDv4]
- **`title`** (required) *(date)* : TODO
- **`source_type`** *(string)* : TODO
	- A value from [source-type-vocab](#source-type-vocab)
- **`file_type`** *(string)* : TODO
	- A value from [source-file-type-vocab](#source-file-type-vocab)
- **`date`** *(date)* : TODO
- **`public`** *(boolean)* : TODO
- **`document`** *(string)* : TODO

## Vocabularies

### source-type-vocab

Values: `01`, `02`, `03`, `04`, `05`, `06`, `07`, `08`, `09`, `10`, `99`

| Const | Value | Description |
| --- | --- | --- |
| 01 | Court Document | TODO|
| 02 | DOJ Press Release | TODO|
| 03 | Investigator Notes | TODO|
| 04 | Letter | TODO|
| 05 | Lexis CourtLink | TODO|
| 06 | Logs | TODO|
| 07 | Media | TODO|
| 08 | Organization Interview | TODO|
| 09 | Personal Website | TODO|
| 10 | Insider Interview | TODO|
| 99 | Other | TODO|

### source-file-type-vocab

Values: `log`, `pdf`, `txt`, `docx`, `png`, `xlsx`

