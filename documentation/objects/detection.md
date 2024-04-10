# Detection
TODO

## Properties
- **`id`** (required) *(string)* : TODO . Uses pattern 'detection--[UUIDv4]'
	- pattern: ^detection--[UUIDv4]
- **`first_detected`** *(date)* : TODO
- **`who_detected`** *(array)* : TODO
	- One or more values from [detection-team-vocab](#detection-team-vocab)
- **`what_detected`** *(array)* : TODO
	- One or more values from [detection-method-vocab](#detection-method-vocab)
- **`logs`** *(array)* : TODO
	- One or more values from [detection-log-vocab](#detection-log-vocab)
- **`comment`** *(string)* : TODO

## Vocabularies

### detection-team-vocab

Values: `LE`, `OR`, `CU`, `CO`, `AU`, `SR`, `IR`, `ST`, `MG`, `II`, `RR`

| Const | Value | Description |
| --- | --- | --- |
| LE | Law Enforcement | TODO|
| OR | Organization | TODO|
| CU | Customer | TODO|
| CO | Competitor | TODO|
| AU | Auditor | TODO|
| SR | Self-Reported | TODO|
| IR | Incident Response Team | TODO|
| ST | Security Team | TODO|
| MG | Management | TODO|
| II | Internal Investigators | TODO|
| RR | Researcher | TODO|

### detection-method-vocab

Values: `1`, `2`, `3`, `4`, `5`

| Const | Value | Description |
| --- | --- | --- |
| 1 | Audit | TODO|
| 2 | Information System | TODO|
| 3 | Non-Technical Means | TODO|
| 4 | Software | TODO|
| 5 | System Failure | TODO|

### detection-log-vocab

Values: `AC`, `AU`, `BR`, `DB`, `EM`, `FS`, `IS`, `RA`, `SF`, `VD`, `WB`

| Const | Value | Description |
| --- | --- | --- |
| AC | Access Logs | TODO|
| AU | Audit Logs | TODO|
| BR | Bank Records | TODO|
| DB | Database Logs | TODO|
| EM | Email Logs | TODO|
| FS | Financial Statements | TODO|
| IS | ISP Logs | TODO|
| RA | Remote Access Logs | TODO|
| SF | System File Logs | TODO|
| VD | Video Logs | TODO|
| WB | Web Logs | TODO|
