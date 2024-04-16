# Response
TODO

## Properties
- **`id`** (required) *(string)* : TODO
	- Uses pattern: ^reponse--[UUIDv4]
- **`technical_controls`** *(array)* : TODO
	- One or more values of the format ([technical-control-vocab](#technical-control-vocab), date)
- **`behavioral_controls`** *(array)* : TODO
	- One or more values of the format ([behavioral-control-vocab](#behavioral-control-vocab), date)
- **`investigated_by`** *(array)* : TODO
	- One or more values from [investigator-vocab](#investigator-vocab)
- **`investigation_events`** *(array)* : TODO
	- One or more values of the format ([investigation-vocab](#investigation-vocab), date)
- **`comment`** *(string)* : TODO

## Vocabularies

### technical-control-vocab

Values: `01`, `02`

| Const | Value | Description |
| --- | --- | --- |
| 01 | Access to Technical System(s) Restricted | TODO|
| 02 | Access to Technical System(s) Terminated | TODO|

### beahvioral-control-vocab

Values: `01`, `02`, `03`, `04`, `05`, `06`, `07`, `08`, `09`, `10`, `11`, `12`

| Const | Value | Description |
| --- | --- | --- |
| 01 | Demoted | TODO|
| 02 | Suspended | TODO|
| 03 | Put on Paid/Unpaid Leave | TODO|
| 04 | Terminated | TODO|
| 05 | Poor Performance Review | TODO|
| 06 | Passed Over For Promotion | TODO|
| 07 | Counseling | TODO|
| 08 | Referred to Employee Assistance Program | TODO|
| 09 | Reported to HR | TODO|
| 10 | Transferred | TODO|
| 11 | Verbal Reprimand | TODO|
| 12 | Written Reprimand | TODO|

### investigation-vocab

Values: `01`, `02`, `03`

| Const | Value | Description |
| --- | --- | --- |
| 01 | Insider's Residence/Workplace Searched | TODO|
| 02 | Evidence Found | TODO|
| 03 | Insider Admits to Activity in Interview | TODO|

### investigator-vocab

Values: `IR`, `MM`, `LE`, `II`

| Const | Value | Description |
| --- | --- | --- |
| IR | Incident Response Team | TODO|
| MM | Management | TODO|
| LE | Law Enforcement | TODO|
| II | Internal Investigators | TODO|
