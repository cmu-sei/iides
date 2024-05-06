# TTP

Actions taken by the insider during the course of the incident.

## Properties

- **`id`** (required) *(string)* : A unique string that begins with "ttp--" and is appended with a UUIDv4.
	- Uses pattern: ^ttp--[UUIDv4]
- **`date`** *(datetime)* : The date and time the action happend. If over a range of time, the start time of the action.
- **`sequence_num`** *(integer)* : The sequence number of this action in the overall timeline of actions. Helpful if the sequence of events is known, but the dates are unknown.
- **`observed`** *(boolean)* : Whether the action was observed by the victim organization or investigative team at the time it happend.
- **`number_of_times`** *(integer)* : The number of times the insider took the particular action. E.g., subject issued "5" fraudulent checks over the course of three weeks.
- **`ttp_vocab`** *(string)* : A reference to the TTP framework being used by this TTP. Common options are IIDES, ATT&CK, CAPEC, etc.
	- Required if `tactic` exists.
- **`tactic`** *(string)* : The high level category or goal of the action.
	- A constant from [tactic-vocab](#tactic-vocab)
	- Required if `technique` exists.
- **`technique`** *(string)* : The general action taken. If technique exists, `tactic` should as well.
	- A constant from [technique-vocab](#technique-vocab)
- **`location`** *(string)* : Whether the insider conducted the action on-site or remotely.
- **`hours`** *(string)* : Whether the action was taken during work hours.
- **`device`** *(array)* : The device where this action either took place or a device that was affected by the action. A device where the action could be detected.
	- One or more constants from [device-vocab](#device-vocab)
- **`channel`** *(array)* : TODO
	- One or more constants from [channel-vocab](#channel-vocab)
- **`description`** *(date)* : Description of the action taken by the insider.

## Vocabularies

### tactic-vocab

Constants: `A`, `R`, `F`, `D`, `C`

| Const | Value | Description |
| --- | --- | --- |
| A | Access | Insider uses an account to take an action related to the incident.|
| R | Recruitment | Insider recruits, or is recruited by others.|
| F | Financial Transaction | Insider or colluding outsider makes a financial transaction related to the incident.|
| D | Data Exfiltration | TODO|
| C | Concealment | Insider or colluding outsider takes an action that conceals, or attempts to conceal, their activity.|

### technique-vocab

Constants: `A1`, `A2`, `A3`, `A4`, `A5`, `A6`, `A7`, `A8`, `A9`, `A10`, `A11`, `A12`, `A13`, `A14`, `R1`, `R2`, `R3`, `R4`, `F1`, `F2`, `F3`, `F4`, `F5`, `F6`, `F7`, `D`, `D`, `D`, `D`, `D`, `D`, `D`, `D`, `D`, `D`, `C1`, `C2`, `C3`, `C4`, `C5`, `C6`, `C7`, `C8`, `C9`, `C10`

| Const | Value | Description |
| --- | --- | --- |
| A1 | Own account | Insider uses their granted access in order to commit their attack.|
| A2 | Privileged Access Abuse | Insider uses their granted privileged access in order to commit their attack.|
| A3 | Insider Used Shared Account | Insider accesses an account they share with other employees.|
| A4 | Insider Used Dormant or Expired Account | Insider uses a company account that was either dormant or expired.|
| A5 | Insider Used Unattended Workstation (Unsecured) | Insider uses a workstation that was unassigned to an employee or uses a colleague's workstation when the colleague is not at their desk.|
| A6 | Insider Used Their Account After Termination/Resignation | Insider gains access to their company account after their termination date.|
| A7 | Insider Used Compromised Account | Insider uses the compromised account of another employee. E.g., Insider copied another employee's account and password prior to being terminated.|
| A8 | Used Unauthorized Access Path | Insider accesses systems using a previously unknown access path that they created. Ee.g., Insider used a backdoor account in order to gain access to the organization's systems.|
| A9 | Authorized Third-Party Account | Insider uses a third party account such as a vendor's account.|
| A10 | Coworker's Account | Insider uses a coworker's account.|
| A11 | Customer's Account | Insider uses a customer's account.|
| A12 | Database Administrator Account | Insider uses a database administrator's account.|
| A13 | Supervisor's Account | Insider uses their supervisor's account.|
| A14 | System Administrator Account | Insider uses a system administrator's account.|
| R1 | Outsider Recruits Insider | An outside entity that is not a competing organization encourages the insider to become an insider. E.g., Insider is contacted by known hacking specialist who asks insider to divulge company secrets to the hacker.|
| R2 | Insider Recruited Outside Aid | The insider recruites people outside of the organization to further their scheme. E.g., Insider recruits their unemployed friend into the scheme.|
| R3 | Insider Recruited Coworker(s) | Insider recruits fellow employees (other than the insider) to further their scheme.|
| R4 | Insider Recruited by Coworker(s) | Insider recruits fellow employees (other than the insider) to further their scheme.|
| F1 | Insider Sells Information | Insider sells, or attempts to sell, organizational information/data/property. E.g., Insider tried to sell company secrets on an online auction site.|
| F2 | Payoffs From Insider | Insider promises or gives other individuals or entities some amount of monetary compensation for aiding their scheme. E.g., Insider promises to give fellow employee $1,000 if they steal confidential information.|
| F3 | Payoffs to Insider | Insider benefits financially or is promised compensation from an outside entity. E.g., A competing organization promises insider $500 for every line of code stolen.|
| F4 | Insider Received/Transferred Fraudulent Funds | Insider receives or transfers funds that were fraudulently obtained. E.g., Insider took out cashier's checks on behalf of customers and used them for personal gain.|
| F5 | Insider Made Fraudulent Purchases | Insider uses fraudulently obtained funds to make purchases. E.g., Insider used general ledger funds from their organization to purchase cashier's checks in the amount of $10,000.|
| F6 | Insider Filed Fraudulent Tax Return | Insider files a fraudulent tax return. Often, this is using the identity of another person. E.g., Insider submitted multiple purported U.S. individual tax returns in the name of multiple people.|
| F7 | Insider Created/Used Fraudulent Asset | Insider creates an asset to use for future monetary gain. E.g., Insider defrauded the organization by providing false documentation claiming they wanted $250,000 to expand their business).|
| D | Paper | TODO|
| D | Removable Media | TODO|
| D | Email | TODO|
| D | Cloud Storage | TODO|
| D | Web-Based | TODO|
| D | Verbal | Insider exfiltrates data by stating it verbally to someone else.|
| D | Mobile Device | Insider exfiltrates data via mobile device.|
| D | Laptop | Insider exfiltrates data by taking it out of the organization on a laptop.|
| D | Other Technical/Digital | Insider exfiltrates data using other technical or digital means not listed in this vocabulary.|
| D | Other Non-Technical | Insider exfiltrates data using other non-technical means not listed in this vocabulary.|
| C1 | Insider Falsified Information | Insider manipulates information or identity falsely, to aid in their attack. E.g., Insider falsely signed a claim stating that they returned all organizational property upon resignation.|
| C2 | Insider Omitted Information | Insider manipulates information or identity, through omission to aid in their attack. E.g., Insider omits previous work for a competitor during a background check.|
| C3 | Insider Modified/Deleted Logs/Activity | Insider deletes or modifies log files or other information that would connect them to the incident. E.g., Insider tried to conceal their communications with their accomplice by deleting files from their personal email account.|
| C4 | Insider Physically Destroyed/Hid Evidence | Insider physically destroys or hides evidence that would connect them to the incident. E.g., Insider shredded papers containing employee PII that they had printed out to commit credit card fraud.|
| C5 | Insider Fled or Attempted to Flee | Insider flees, or attempts to flee, their home state in order to avoid detection of their scheme. E.g., Insider fled the country.|
| C6 | Insider Created/Used an Alias | Insider uses the identity of another person. E.g., Insider went under the alias "John Doe" when conducting business in their startup to cover their tracks.|
| C7 | Insider Framed another Individual | Insider takes steps to plant evidence, or otherwise falsely prove, that someone else committed the insider's actions.|
| C8 | Insider Made False Statements/Denied Involvement | Insider makes any sort of statement that is false, or denys their involvement in the incident. E.g., Insider lied to their supervisor, saying that they had not taken confidential information from them when they actually did.|
| C9 | Concealment of Current Illicit Activity - Other Technical | Any other technical method used by the insider in an attempt to hide malicious activities.|
| C10 | Concealment of Current Illicit Activity - Other Non-Technical | any other non-technical method used by the insider in an attempt to hide malicious activities.|

### attack-location-vocab

Constants: `1`, `2`, `3`, `4`

| Const | Value | Description |
| --- | --- | --- |
| 1 | On-site | Insider took the action while on-site at an organizational facility.|
| 2 | Remotely | Insider took the action while remote (i.e. not at an organizational facility).|
| 3 | Remotely from home | Insider took the action remotely while at their home.|
| 4 | Remotely while traveling | Insider took the action remotely while traveling.|

### attack-hours-vocab

Constants: `1`, `2`

| Const | Value | Description |
| --- | --- | --- |
| 1 | During Work Hours | Insider took the action during their normal working hours.|
| 2 | Outside of Work Hours | Insider took the action outside of their normal working hours.|

### device-vocab

Constants: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `99`

| Const | Value | Description |
| --- | --- | --- |
| 1 | Company Desktop | Organization owned desktop workstation.|
| 2 | Company Laptop | Organization owned laptop workstation.|
| 3 | Company Mobile Device | Organization owned mobile device.|
| 4 | Database Server | Database server.|
| 5 | Email Server | Email server.|
| 6 | File Server | File server.|
| 7 | Personal Computer | Personally owned computer.|
| 8 | Personal Mobile Device | Personally owned moble device.|
| 9 | Printer/Copier/Fax | Printer, copier, or fax machine.|
| 10 | Web Server | Web server.|
| 99 | Other | Other device not in this vocabulary.|

### channel-vocab

Constants: `1`, `2`, `3`, `4`, `5`, `6`, `9`

| Const | Value | Description |
| --- | --- | --- |
| 1 | Company Email | An email account the company controls.|
| 2 | Company Phone | A phone the company controls.|
| 3 | Instant Messaging | TODO|
| 4 | Online Forum | TODO|
| 5 | Personal Email | An email account the organization does not control or monitor.|
| 6 | Personal Phone | A phone the organization does not control or monitor.|
| 9 | Other | Other type of channel not listed in this vocabulary.|
