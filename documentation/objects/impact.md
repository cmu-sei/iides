# Impact

The quantified impact of the incident on the victim organization. An incident may have one or more impacts. An impact MUST be associated with only one incident.

## Properties

- **`id`** (required) *(string)* : A unique string that begins with "impact--" and is appended with a UUIDv4.
	- Uses pattern: ^impact--[UUIDv4]
- **`high`** (required) *(number)* : The quantity of the impact being measured. If a range, the high end of the range.
- **`low`** *(number)* : If a range, the low estimate of the range.
- **`metric`** (required) *(string)* : The type of impact being quantified.
	- A constant from [impact-metric-vocab](#impact-metric-vocab)
- **`estimated`** (required) *(boolean)* : True if the impact low and/or high is an estimated number or range.
- **`comment`** *(string)* : Clarifying comments.

## Vocabularies

### impact-metric-vocab

Constants: `01`, `02`, `03`, `04`, `05`, `06`, `07`, `08`, `09`, `10`, `11`, `12`, `13`, `14`, `15`, `16`

| Const | Value | Description |
| --- | --- | --- |
| 01 | Accounts | Computer, network, financial, user accounts.|
| 02 | Credit card numbers | Physical or digital credit or debit card numbers.|
| 03 | Customers | The number of customers effected (e.g., through stolen accounts, PII, etc.)|
| 04 | Documents | The number of physical or digital documents effected (stolen, deleted, modified, etc.).|
| 05 | Dollars | Specific financial impact of money stolen, restitution ordered, etc.|
| 06 | Employees | Number of employees effected.|
| 07 | Files | Number of physical or digital files stolen, read, or compromised.|
| 08 | Hours | Down time or time effected in hours.|
| 09 | Pages | Number of individual pages of a document(s) or file(s).|
| 10 | Person-hours | Person-hours or work time effected. Often occurs in sabotage incidents.|
| 11 | Identities | PII records, user information, etc.|
| 12 | Items | Generic items, such as merchandise.|
| 13 | Systems | Workstations, servers, virtual machines, etc.|
| 14 | Records | Records or rows. Often refers to database or accounting records.|
| 15 | Drugs | Number of pills, vials, syringes, etc. drugs or medicine taken or effected.|
| 16 | Trade Secrets | Number of trade secrets stolen or effected.|
