# org-relationship
TODO

## Properties
- **`id`** (required) *(string)* : TODO . Uses pattern 'orgrelationship--[UUIDv4]'
	- Uses pattern: ^orgrelationship--[UUIDv4]
- **`org1`** (required) *(string)* : TODO . Uses pattern 'orgrelationship--[UUIDv4]'
	- Uses pattern: ^organization--[UUIDv4]
- **`org2`** (required) *(string)* : TODO . Uses pattern 'orgrelationship--[UUIDv4]'
	- Uses pattern: ^organization--[UUIDv4]
- **`relationship`** (required) *(string)* : TODO
	- A value from [org-relationship-vocab](#org-relationship-vocab)

## Vocabularies

### org-relationship-vocab

Values: `C`, `V`, `U`, `O`

| Const | Value | Description |
| --- | --- | --- |
| C | Competitor | TODO|
| V | Vendor | TODO|
| U | Unknown | TODO|
| O | Other | TODO|
