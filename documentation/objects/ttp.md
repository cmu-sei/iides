# TTP

Action taken by the insider or colluding outsider(s) during the course of the incident, categorized into a tactic, technique, and procedure (TTP). An incident may have multiple TTPs. A TTP must be connected to an incident.

## Properties

- **`id`** (required) *(string)* : A unique string that begins with "ttp--" and is appended with a UUIDv4.
  - Uses pattern: ^ttp--[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
- **`date`** *(datetime)* : The date and time the action happend. If over a range of time, the start time of the action.
- **`sequence_num`** *(integer)* : The sequence number of this action in the overall timeline of actions. Helpful if the sequence of events is known, but the dates are unknown.
- **`observed`** *(boolean)* : Whether the action was observed by the victim organization or investigative team at the time it happend.
- **`number_of_times`** *(integer)* : The number of times this particular action took place. E.g., subject issued "5" fraudulent checks over the course of three weeks.
- **`ttp_vocab`** *(string)* : A reference to the TTP framework being used by this TTP. Common options are IIDES, ATT&CK, CAPEC, etc.
  - Default: "IIDES"
  - Required if `tactic` exists.
- **`tactic`** *(string)* : The high level category or goal of the action.
	- A constant from [tactic-vocab](#tactic-vocab)
  - Required if `technique` exists.
- **`technique`** *(string)* : The general action taken. If technique exists, `tactic` should as well.
	- A constant from [technique-vocab](#technique-vocab)
- **`location`** *(string)* : Whether the action was taken on-site or remotely.
- **`hours`** *(string)* : Whether the action was taken during work hours.
- **`device`** *(array)* : The device where this action either took place or a device that was affected by the action. A device where the action could be detected.
  - One or more constants from [device-vocab](#device-vocab)
- **`channel`** *(array)* : Methods used to transmit information outside, or into, the victim organization.
  - One or more constants from [channel-vocab](#channel-vocab)
- **`description`** *(string)* : Description of the action/procedure.

## Vocabularies

### tactic-vocab

Constants: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`

| Const | Value | Description |
| --- | --- | --- |
| 1 | Access | Insider uses an organizational account or access path to take an action related to the incident.|
| 2 | Recruitment | Insider recruits, or is recruited by others.|
| 3 | Financial Transaction | Insider or colluding outsider makes a financial transaction related to the incident.|
| 4 | Malware | Malicious software is used.|
| 5 | Malicous Action | An intentionally malicious action not included in the other tactics.|
| 6 | Concealment | Insider or colluding outsider takes an action that conceals, or attempts to conceal, their activity.|
| 7 | Data Exfiltration | Data (or copies of data) is removed from the organization without permission or explicitly against permission to use in an unauthorized way.|
| 8 | Data Impact | Harmful action involving the organization's data which compromises the organization in some way.|
| 9 | Safety Impact | Harmful action involving the organization's personnel that compromises the safety of one or more individuals in the organization.|

### technique-vocab

Constants: `1.1`, `1.2`, `1.3`, `1.4`, `1.5`, `1.6`, `1.7`, `1.8`, `1.9`, `1.10`, `1.11`, `1.12`, `1.13`, `1.14`, `2.1`, `2.2`, `2.3`, `2.4`, `3.1`, `3.2`, `3.3`, `3.4`, `3.5`, `3.6`, `3.7`, `4.1`, `4.2`, `4.3`, `4.4`, `4.5`, `4.6`, `4.7`, `4.8`, `4.9`, `4.10`, `4.11`, `4.12`, `4.13`, `5.1`, `5.2`, `5.3`, `5.4`, `6.1`, `6.2`, `6.3`, `6.4`, `6.5`, `6.6`, `6.7`, `6.8`, `6.9`, `6.10`, `7.1`, `7.2`, `7.3`, `7.4`, `7.5`, `7.6`, `7.7`, `7.8`, `7.9`, `7.10`, `8.1`, `8.2`, `8.3`, `8.4`, `8.5`, `8.6`, `9.1`, `9.2`, `9.3`, `9.4`, `9.5`

| Const | Value | Description |
| --- | --- | --- |
| 1.1 | Own account | Insider uses their granted access in order to commit their attack.|
| 1.2 | Privileged Access Abuse | Insider uses their granted privileged access in order to commit their attack.|
| 1.3 | Shared Account | Insider accesses an account they share with other employees.|
| 1.4 | Dormant or Expired Account | Insider uses a company account that was either dormant or expired.|
| 1.5 | Unattended Workstation (Unsecured) | Insider uses a workstation that was unassigned to an employee or uses a colleague's workstation when the colleague is not at their desk.|
| 1.6 | Own Account After Termination/Resignation | Insider gains access to their company account after their termination date.|
| 1.7 | Compromised Account | Insider uses the compromised account of another employee. E.g., Insider copied another employee's account and password prior to being terminated.|
| 1.8 | Unauthorized Access Path | Insider accesses systems using a previously unknown access path that they created. E.g., Insider used a backdoor account in order to gain access to the organization's systems.|
| 1.9 | Authorized Third-Party Account | Insider uses a third party account such as a vendor's account.|
| 1.10 | Coworker's Account | Insider uses a coworker's account.|
| 1.11 | Customer's Account | Insider uses a customer's account.|
| 1.12 | Database Administrator Account | Insider uses a database administrator's account.|
| 1.13 | Supervisor's Account | Insider uses their supervisor's account.|
| 1.14 | System Administrator Account | Insider uses a system administrator's account.|
| 2.1 | Outsider Recruits Insider | An outside entity that is not a competing organization encourages the insider to become an insider. E.g., Insider is contacted by known hacking specialist who asks insider to divulge company secrets to the hacker.|
| 2.2 | Insider Recruited Outside Aid | The insider recruites people outside of the organization to further their scheme. E.g., Insider recruits their unemployed friend into the scheme.|
| 2.3 | Insider Recruited Coworker(s) | Insider recruits fellow employees to further their scheme.|
| 2.4 | Insider Recruited by Coworker(s) | Insider is recruited by fellow employees to further their scheme.|
| 3.1 | Sells Information | Insider or accomplice sells, or attempts to sell, organizational information/data/property. E.g., Insider tried to sell company secrets on an online auction site.|
| 3.2 | Payoffs From Insider | Insider promises or gives other individuals or entities some amount of monetary compensation for aiding their scheme. E.g., Insider promises to give fellow employee $1,000 if they steal confidential information.|
| 3.3 | Payoffs to Insider | Insider benefits financially or is promised compensation from an outside entity. E.g., A competing organization promises insider $500 for every line of code stolen.|
| 3.4 | Received/Transferred Fraudulent Funds | Insider or accomplice receives or transfers funds that were fraudulently obtained. E.g., Insider took out cashier's checks on behalf of customers and used them for personal gain.|
| 3.5 | Fraudulent Purchases | Insider or accomplice uses fraudulently obtained funds to make purchases. E.g., Insider used general ledger funds from their organization to purchase cashier's checks in the amount of $10,000.|
| 3.6 | Filed Fraudulent Tax Return | Insider or accomplice files a fraudulent tax return. Often, this is using the identity of another person. E.g., Insider submitted multiple purported U.S. individual tax returns in the name of multiple people.|
| 3.7 | Insider Created/Used Fraudulent Asset | Insider creates an asset to use for future monetary gain. E.g., Insider defrauded the organization by providing false documentation claiming they wanted $250,000 to expand their business).|
| 4.1 | Backdoor | A malicious program that allows an attacker to perform actions on a remote system, such as transferring files, acquiring passwords, or executing arbitrary commands.|
| 4.2 | Bootkit | A malicious program which targets the Master Boot Record of the target computer.|
| 4.3 | Keylogger | The insider utilized either a hardware, or software, keylogger as part of their scheme.|
| 4.4 | Exploit Kit | A software toolkit to target common vulnerabilities.|
| 4.5 | Ransomware | A type of malware that encrypts files on a victim's system, demanding payment of ransom in return for the access codes required to unlock files.|
| 4.6 | Remote Access Trojan | A remote access trojan program (or RAT), is a trojan horse capable of controlling a machine through commands issued by a remote attacker.|
| 4.7 | Resource Exploitation Software | A type of malware that steals a system's resources (e.g., CPU cycles), such as a malicious bitcoin miner.|
| 4.8 | Rogue Security Software | A fake security product that demands money to clean phony infections.|
| 4.9 | Rootkit | A type of malware that hides its files or processes from normal methods of monitoring in order to conceal its presence and activities.|
| 4.10 | Screen Capture Software | A type of malware used to capture images or video from the target systems screen, used for exfiltration and command and control.|
| 4.11 | Spyware | Software that gathers information on a user's system without their knowledge and sends it to another party. Spyware is generally used to track activities for the purpose of delivering advertising.|
| 4.12 | Logic Bomb | a piece of code intentionally inserted into a software system that will set off a malicious function when specified conditions are met (e.g., a programmer may hide a piece of code that starts deleting files should they ever be terminated from the company).|
| 4.13 | Wiper | A piece of malware whose primary aim is to delete files or entire disks on a machine.|
| 5.1 | Bypassed Physical Security of Organizational Facilities | Gains unauthorized physical access to organizational facilities (e.g., Insider gained access to the company building late on a Sunday night).|
| 5.2 | Exploited Known Security Vulnerabilities | Uses a security vulnerability known to the organization to further their scheme (e.g., Organization knew the insider didn't have a firewall on their computer but did nothing about it, and the insider was able to use this security vulnerability to compromise the system).|
| 5.3 | Social Engineering of Employees | Uses a social engineering technique as part of the attack (e.g., Insider sent a phishing e-mail to co-workers).|
| 5.4 | Used/Executed Unauthorized Software | Uses or executes any sort of unauthorized software on an organizational system (e.g., Insider used a credit card skimmer in order to obtain customer PII). This grouping includes installing or running unauthorized software.|
| 6.1 | Falsified Information | Insider or accomplice manipulates information or identity falsely, to aid in their attack. E.g., Insider falsely signed a claim stating that they returned all organizational property upon resignation.|
| 6.2 | Omitted Information | Insider or accomplice manipulates information or identity, through omission to aid in their attack. E.g., Insider omits previous work for a competitor during a background check.|
| 6.3 | Modified/Deleted Logs/Activity | Insider or accomplice deletes or modifies log files or other information that would connect them to the incident. E.g., Insider tried to conceal their communications with their accomplice by deleting files from their personal email account.|
| 6.4 | Physically Destroyed/Hid Evidence | Insider or accomplice physically destroys or hides evidence that would connect them to the incident. E.g., Insider shredded papers containing employee PII that they had printed out to commit credit card fraud.|
| 6.5 | Fled or Attempted to Flee | Insider or accomplice flees, or attempts to flee, their home state in order to avoid detection of their scheme. E.g., Insider fled the country.|
| 6.6 | Created/Used an Alias | Insider or accomplice uses the identity of another person. E.g., Insider went under the alias "John Doe" when conducting business in their startup to cover their tracks.|
| 6.7 | Framed another Individual | Insider or accomplice takes steps to plant evidence, or otherwise falsely prove, that someone else committed the insider's actions.|
| 6.8 | False Statements/Denied Involvement | Insider or accomplice makes any sort of statement that is false, or denys their involvement in the incident. E.g., Insider lied to their supervisor, saying that they had not taken confidential information from them when they actually did.|
| 6.9 | Concealment of Current Illicit Activity - Other Technical | Any other technical method used by the insider or accomplice in an attempt to hide malicious activities.|
| 6.10 | Concealment of Current Illicit Activity - Other Non-Technical | Any other non-technical method used by the insider or accomplice in an attempt to hide malicious activities.|
| 7.1 | Paper | Insider exfiltrates data through printed or hand-written materials (e.g., Insider takes screenshots of important data, prints the screenshots, and walks out of work with them).|
| 7.2 | Removable Media | Insider exfiltrates data through digital equipment or media (e.g., Insider had trade secrets owned by the victim organization on a flash drive and sent the flash drive to the competitor to be copied).|
| 7.3 | Email | Insider exfiltrates data through electronic mail (e.g., Insider e-mailed confidential information to competitor).|
| 7.4 | Cloud Storage | Insider exfiltrates data to external cloud storage (e.g., Insider downloaded company PII and uploaded it to their personal Box account).|
| 7.5 | Web-Based | Insider exfiltrates data to any based with the World Wide Web (e.g., Insider posted the stolen employee PII to the Internet). The category includes data exfiltrated over various web protocols that are not covered more specifically by another grouping, such as exfiltration using the File Transfer Protocol (FTP) or exfiltration over a Virtual Private Network (VPN).|
| 7.6 | Verbal | Insider exfiltrates data by stating it verbally to someone else.|
| 7.7 | Mobile Device | Insider exfiltrates data via mobile device.|
| 7.8 | Laptop | Insider exfiltrates data by taking it out of the organization on a laptop.|
| 7.9 | Other Technical/Digital | Insider exfiltrates data using other technical or digital means not listed in this vocabulary.|
| 7.10 | Other Non-Technical | Insider exfiltrates data using other non-technical means not listed in this vocabulary.|
| 8.1 | Physical Attack to Organizational Equipment | Insider or accomplice physically harms any of the organization's physical equipment (e.g., Insider pours glue into USB ports in all desktops).|
| 8.2 | Modified Critical Data | Insider or accomplice modifies data that is critical to the victim organization (e.g., The insider was able to remotely access the victim organization's systems, to modify employee information and change passwords).|
| 8.3 | Deleted Critical Data | Insider or accomplice deletes data that is critical to the victim organization (e.g., The insider was able to remotely access the victim organization's systems to delete files).|
| 8.4 | Used Data in Identity Theft | Insider or accomplice uses data to pretend to be someone else (e.g., to submit false tax returns, open bank accounts, etc.)|
| 8.5 | Posted Data Publicly | Posted internal, sensitive, or confidential data in a public forum.|
| 8.6 | Sold or Gave Away Critical Data | Sold or gave away internal data to an external individual or company.|
| 9.1 | Doxxed Individuals | Publicly posted information about individuals (customers or employees) online for purpose of instigating outside harassment.|
| 9.2 | Threatened Violence | Threatened violence or physical harm against other individuals in the organization.|
| 9.3 | Threatened Suicide | Threated physical harm to theirself.|
| 9.4 | Attempted Violence | Attempted violence or physical harm against other individuals in the organization (successful or unsuccesful).|
| 9.5 | Attempted Suicide | Attempted physical harm to theirself (successful or unsuccessful).|

### attack-location-vocab

Constants: `1`, `2`, `3`, `4`

| Const | Value | Description |
| --- | --- | --- |
| 1 | On-site | Action taken while on-site at an organizational facility.|
| 2 | Remotely | Action taken while remote (i.e. not at an organizational facility).|
| 3 | Remotely from home | Action taken remotely while at the insider's or accomplice's home.|
| 4 | Remotely while traveling | Action remotely while traveling.|

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
| 3 | Instant Messaging | Direct, synchronous or asynchronous communication via app, software, or web.|
| 4 | Online Forum | Private or public forum accessed via the Internet.|
| 5 | Personal Email | An email account the organization does not control or monitor.|
| 6 | Personal Phone | A phone the organization does not control or monitor.|
| 9 | Other | Other type of channel not listed in this vocabulary.|
