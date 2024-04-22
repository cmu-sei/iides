# TTP

TODO

## Properties

- **`id`** (required) *(string)* : TODO
	- Uses pattern: ^ttp--[UUIDv4]
- **`date`** *(string)* : TODO
- **`sequence_num`** *(integer)* : TODO
- **`observed`** *(boolean)* : TODO
- **`number_of_times`** *(integer)* : TODO
- **`ttp_vocab`** *(string)* : att&ck, capec, etc.
- **`tactic`** *(string)* : TODO
	- A constant from [tactic-vocab](#tactic-vocab)
- **`technique`** *(string)* : TODO
	- A constant from [technique-vocab](#technique-vocab)
- **`location`** *(string)* : TODO
- **`hours`** *(string)* : TODO
- **`device`** *(string)* : TODO. Affected device
- **`description`** *(string)* : TODO

## Vocabularies

### tactic-vocab

Constants: `4.1`, `4.4`, `4.7`, `4.8`

| Const | Value | Description |
| --- | --- | --- |
| 4.1 | Access | TODO|
| 4.4 | Recruitment | TODO|
| 4.7 | Financial Transaction | TODO|
| 4.8 | Concealment | TODO|

### technique-vocab

Constants: `4.1.1`, `4.1.2`, `4.1.3`, `4.1.4`, `4.1.5`, `4.1.6`, `4.1.7`, `4.1.8`, `4.1.9`, `4.1.10`, `4.1.11`, `4.1.12`, `4.1.13`, `4.1.14`, `4.4.`, `4.4.`, `4.4.`, `4.4.`, `4.7.1`, `4.7.2`, `4.7.3`, `4.7.4`, `4.7.5`, `4.7.6`, `4.7.7`, `4.8.1`, `4.8.2`, `4.8.3`, `4.8.4`, `4.8.5`, `4.8.6`, `4.8.7`, `4.8.8`, `4.8.9`, `4.8.10`

| Const | Value | Description |
| --- | --- | --- |
| 4.1.1 | Own account | TODO|
| 4.1.2 | Privileged Access Abuse | TODO|
| 4.1.3 | Insider Used Shared Account | TODO|
| 4.1.4 | Insider Used Dormant or Expired Account | TODO|
| 4.1.5 | Insider Used Unattended Workstation (Unsecured) | TODO|
| 4.1.6 | Insider Used Their Account After Termination/Resignation | TODO|
| 4.1.7 | Insider Used Compromised Account | TODO|
| 4.1.8 | Used Unauthorized Access Path | TODO|
| 4.1.9 | Authorized Third-Party Account | TODO|
| 4.1.10 | Coworker's Account | TODO|
| 4.1.11 | Customer's Account | TODO|
| 4.1.12 | Database Administrator Account | TODO|
| 4.1.13 | Supervisor's Account | TODO|
| 4.1.14 | System Administrator Account | TODO|
| 4.4. | Outsider Recruits Insider | TODO|
| 4.4. | Insider Recruited Outside Aid | TODO|
| 4.4. | Insider Recruited Coworker(s) | TODO|
| 4.4. | Insider Recruited by Coworker(s) | TODO|
| 4.7.1 | Attempt to Sell Organization Information/Data/IP | TODO|
| 4.7.2 | Payoffs From Insider | TODO|
| 4.7.3 | Payoffs to Insider | TODO|
| 4.7.4 | Insider Received/Transferred Fraudulent Funds | TODO|
| 4.7.5 | Insider Made Fraudulent Purchases | TODO|
| 4.7.6 | Insider Filed Fraudulent Tax Return | TODO|
| 4.7.7 | Insider Created/Used Fraudulent Asset | TODO|
| 4.8.1 | Insider Falsified Information | TODO|
| 4.8.2 | Insider Omitted Information | TODO|
| 4.8.3 | Insider Modified/Deleted Logs/Activity | TODO|
| 4.8.4 | Insider Physically Destroyed/Hid Evidence | TODO|
| 4.8.5 | Insider Fled or Attempted to Flee | TODO|
| 4.8.6 | Insider Created/Used an Alias | TODO|
| 4.8.7 | Insider Framed another Individual | TODO|
| 4.8.8 | Insider Made False Statements/Denied Involvement | TODO|
| 4.8.9 | Concealment of Current Illicit Activity - Other Technical | TODO|
| 4.8.10 | Concealment of Current Illicit Activity - Other Non-Technical | TODO|

### attack-location-vocab

Constants: `1`, `2`, `3`, `4`

| Const | Value | Description |
| --- | --- | --- |
| 1 | On-site | TODO|
| 2 | Remotely | TODO|
| 3 | Remotely from home | TODO|
| 4 | Remotely while traveling | TODO|

### attack-hours-vocab

Constants: `1`, `2`

| Const | Value | Description |
| --- | --- | --- |
| 1 | During Work Hours | TODO|
| 2 | Outside of Work Hours | TODO|

### device-vocab

Constants: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`

| Const | Value | Description |
| --- | --- | --- |
| 1 | Company Desktop | TODO|
| 2 | Company Laptop | TODO|
| 3 | Company Mobile Device | TODO|
| 4 | Database Server | TODO|
| 5 | Email Server | TODO|
| 6 | File Server | TODO|
| 7 | Personal Computer | TODO|
| 8 | Personal Mobile Device | TODO|
| 9 | Printer/Copier/Fax | TODO|
| 10 | Web Server | TODO|
