# Impact
TODO

## Properties
- **`id`** (required) *(string)* : TODO . Uses pattern 'impact--[UUIDv4]'
	- pattern: ^impact--[UUIDv4]
- **`high`** (required) *(integer)* : TODO
- **`low`** *(integer)* : TODO
- **`metric`** (required) *(string)* : TODO
	- A value from [impact-metric-vocab](#impact-metric-vocab)
- **`estimated`** (required) *(boolean)* : TODO
- **`comment`** *(string)* : TODO

## Vocabularies

### impact-metric-vocab

Values: `01`, `02`, `03`, `04`, `05`, `06`, `07`, `08`, `09`, `10`, `11`, `12`, `13`, `14`, `15`, `16`

| Const | Value | Description |
| --- | --- | --- |
| 01 | Accounts | TODO|
| 02 | Credit card numbers | TODO|
| 03 | Customers | TODO|
| 04 | Documents | TODO|
| 05 | Dollars | TODO|
| 06 | Employees | TODO|
| 07 | Files | TODO|
| 08 | Hours | TODO|
| 09 | Pages | TODO|
| 10 | Person-hours | TODO|
| 11 | Identities | TODO|
| 12 | Items | TODO|
| 13 | Systems | TODO|
| 14 | Records | TODO|
| 15 | Drugs | TODO|
| 16 | Trade Secrets | TODO|
