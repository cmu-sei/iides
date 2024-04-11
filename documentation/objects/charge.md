# Charge
TODO

## Properties
- **`id`** (required) *(string)* : TODO
	- Uses pattern: ^charge--[UUIDv4]
- **`title`** (required) *(string)* : TODO
- **`section`** *(string)* : TODO
- **`nature_of_offense`** *(string)* : TODO
- **`count`** *(integer)* : TODO
- **`plea`** *(string)* : TODO
	- A value from [charge-plea-vocab](#charge-plea-vocab)
- **`plea_bargain`** *(boolean)* : TODO
- **`category`** *(string)* : TODO
	- A value from [charge-disposition-vocab](#charge-disposition-vocab)

## Vocabularies

### charge-plea-vocab

Values: `1`, `2`, `3`, `4`

| Const | Value | Description |
| --- | --- | --- |
| 1 | Guilty | TODO|
| 2 | No Contest | TODO|
| 3 | Not Guilty | TODO|
| 4 | Refused to Enter a Plea | TODO|

### charge-disposition-vocab

Values: `01`, `02`, `03`, `04`, `05`, `06`, `07`, `08`, `09`, `10`, `11`

| Const | Value | Description |
| --- | --- | --- |
| 01 | Acquitted | TODO|
| 02 | Convicted | TODO|
| 03 | Dismissed | TODO|
| 04 | Diversion/Deferred Prosecution | TODO|
| 05 | Expunged | TODO|
| 06 | No charges filed/Charges dropped | TODO|
| 07 | Pending | TODO|
| 08 | Pled down | TODO|
| 09 | Sealed | TODO|
| 10 | Suspended sentence | TODO|
| 11 | Vacated | TODO|
