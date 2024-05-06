# Response

Describes the organization's response to the incident, including technical and behavioral controls, investigation, and legal response. An incident may have only one response entity. A response may have only one legal response entity.

## Properties

- **`id`** (required) *(string)* : A unique string that begins with "response--" and is appended with a UUIDv4.
	- Uses pattern: ^reponse--[UUIDv4]
- **`technical_controls`** *(array)* : Controls put in place to limit or monitor the insider's access to devices, data, or the network, or to limit/monitor network/device access for the user population more generally.
	- One or more tuple values of the format ([technical-control-vocab](#technical-control-vocab), date)
- **`behavioral_controls`** *(array)* : Controls put in place to limit, monitor, or correct the insider's behavior within the organization.
	- One or more tuple values of the format ([behavioral-control-vocab](#behavioral-control-vocab), date)
- **`investigated_by`** *(array)* : The organization(s) or entity(s) that investigated the incident.
	- One or more constants from [investigator-vocab](#investigator-vocab)
- **`investigation_events`** *(array)* : Specific events that happend during the course of the investigation into the incident.
	- One or more tuple values of the format ([investigation-vocab](#investigation-vocab), date)
- **`comment`** *(string)* : Clarifying comments or additional details about the organization's response.

## Vocabularies

### technical-control-vocab

Constants: `01`, `02`

| Const | Value | Description |
| --- | --- | --- |
| 01 | Access to Technical System(s) Restricted | Insider's access to the organization's technical systems is restricted in any capacity E.g., Organization declares that insider could only log onto system if another employee is present.|
| 02 | Access to Technical System(s) Terminated | Insider's access to the organization's technical systems is completely terminated E.g., Insider's account is deleted upon termination from the company.|

### beahvioral-control-vocab

Constants: `01`, `02`, `03`, `04`, `05`, `06`, `07`, `08`, `09`, `10`, `11`, `12`

| Const | Value | Description |
| --- | --- | --- |
| 01 | Demoted | Insider is demoted. E.g., lowered their rank, title, or responsbilities.|
| 02 | Suspended | Insider is suspended (definitely or indefinitely) and not allowed to conduct normal work for the organization.|
| 03 | Put on Paid/Unpaid Leave | Insider is put on temporary leave from a job assignment, with or without pay and benefits.|
| 04 | Terminated | Insider is terminated, or fired, from the organization.|
| 05 | Poor Performance Review | Insider receives a review of their work performance which is deemed below average|
| 06 | Passed Over For Promotion | Organization chooses to promote someone other than the insider as a result of the insider's actions.|
| 07 | Counseling | Insider is sent to counseling of any kind as a result of their actions.|
| 08 | Referred to Employee Assistance Program | Insider is referred to the EAP as a result of their actions.|
| 09 | Reported to HR | Insider is reported to Human Resources as a result of their actions.|
| 10 | Transferred | Insider is transferred to another company location as a result of their actions.|
| 11 | Verbal Reprimand | Insider receives a verbal reprimand from their supervisor as a result of their actions.|
| 12 | Written Reprimand | Insider receives a written reprimand from their supervisor as a result of their actions.|

### investigation-vocab

Constants: `01`, `02`, `03`

| Const | Value | Description |
| --- | --- | --- |
| 01 | Insider's Residence/Workplace Searched | Investigators search the insider's home or workplace for evidence related to the incident.|
| 02 | Evidence Found | Evidence relevant to the incident is found. E.g., Fellow employee found a USB drive left in the insider's computer that had sensitive company files downloaded on to it.|
| 03 | Insider Admits to Activity in Interview | Insider admits to involvement in insider incident while being interviewed by investigators about the incident (or related activity).|

### investigator-vocab

Constants: `01`, `02`, `03`, `04`, `05`, `06`, `07`, `99`

| Const | Value | Description |
| --- | --- | --- |
| 01 | Incident Response Team | Incident Response Team (IRT), whether internal to the organization or provided by an external contract.|
| 02 | Management | Management internal to the organization.|
| 03 | Law Enforcement - Local/State | State or local law enforcement entity.|
| 04 | Law Enforcement - Federal | Federal law enforcement entity such as the FBI or USSS.|
| 05 | Law Enforcement - Military/DoD | Law enforcement belonging to the military or Department of Defense, such as military police or NCIS. |
| 06 | Law Enforcement - Government Agency | Law enforcement belonging to a government agency such as DHS, USPS, IRS, etc.|
| 07 | Internal Investigators | Other investigators internal to the victim organization.|
| 99 | Other | Other investigator not lised in this vocabulary.|
