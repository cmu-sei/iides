# Incident
TODO description of incident

## Properties
- **`id`** (required) *(string)* : TODO . Uses pattern 'incident--[UUIDv4]'
	- pattern: ^incident--[UUIDv4]
- **`cia_effect`** *(array)* : TODO
	- One or more values from [cia-vocab](#cia-vocab)
- **`incident_type`** *(array)* : TODO
	- One or more values from [incident-type-vocab](#incident-type-vocab)
- **`outcome`** *(array)* : TODO
	- One or more values from [outcome-type-vocab](#outcome-type-vocab)
- **`status`** *(string)* : TODO
	- A value from [incident-status-vocab](#incident-status-vocab)
- **`summary`** *(string)* : TODO
- **`brief_summary`** *(string)* : TODO
- **`comment`** *(string)* : TODO

## Vocabularies

### incident-status-vocab

Values: `P`, `I`, `L`, `C`

| Const | Value | Description |
| --- | --- | --- |
| P | In Progress | TODO|
| I | Under Investigation | TODO|
| L | In Legal Proceedings | TODO|
| C | Complete | TODO|

### cia-vocab

Values: `C`, `I`, `A`

| Const | Value | Description |
| --- | --- | --- |
| C | Confidentiality | TODO|
| I | Integrity | TODO|
| A | Availability | TODO|

### outcome-type-vocab

Values: `BR`, `DC`, `DD`, `DR`, `DS`, `MD`, `ML`, `MS`, `NN`, `OT`, `RO`, `SI`, `UK`, `IT`

| Const | Value | Description |
| --- | --- | --- |
| BR | Bankruptcy | TODO|
| DC | Data Created | TODO|
| DD | Data Deleted | TODO|
| DR | Data Read | TODO|
| DS | Data Stolen | TODO|
| MD | Monetary Damages | TODO|
| ML | Monetary Losses | TODO|
| MS | Money Stolen | TODO|
| NN | No net negative | TODO|
| OT | Other | TODO|
| RO | Restituion Ordered | TODO|
| SI | Safety Impact | TODO|
| UK | Unknown | TODO|
| IT | Used in Identity Theft | TODO|

### incident-type-vocab

Values: `F`, `S`, `T`, `M`

| Const | Value | Description |
| --- | --- | --- |
| F | Fraud | TODO|
| S | Sabotage | TODO|
| T | Theft of IP | TODO|
| M | Misuse | TODO|
