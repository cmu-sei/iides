# Collusion
TODO

## Properties
- **`id`** (required) *(string)* : TODO
	- Uses pattern: ^collusion--[UUIDv4]
- **`insider1`** (required) *(string)* : TODO
	- Uses pattern: ^insider--[UUIDv4]
- **`insider2`** (required) *(string)* : TODO
	- Uses pattern: ^insider--[UUIDv4]
- **`relationship`** (required) *(string)* : TODO
	- A value from [insider-relationship-vocab](../common/insider-relationship-vocab.md)
- **`recruitment`** *(string)* : TODO
	- A value from [recruitment-vocab](#recruitment-vocab)

## Vocabularies

### recruitment-vocab

Values: `1`, `2`, `3`, `4`, `5`, `9`

| Const | Value | Description |
| --- | --- | --- |
| 1 | Avoid Detection | TODO|
| 2 | Greater Payoff | TODO|
| 3 | Insider Resigned | TODO|
| 4 | Separation of Duties | TODO|
| 5 | Share the Wealth | TODO|
| 9 | Other | TODO|
