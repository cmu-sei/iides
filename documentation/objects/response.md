# Response

Response describes the organization's response to the incident, including technical and behavioral controls, investigation, and legal response. An incident may have only one response entity. A response may have only one legal response entity.

## Properties

- **`id`** (required) *(string)* : A unique string that begins with "response--" and is appended with a UUIDv4
  - Uses pattern: ^response--[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
- **`technical_controls`** *(array)* : Controls put in place to limit or monitor the insider's access to devices, data, or the network or to limit or monitor network or device access for the user population more generally
  - One or more tuple values of the format ([technical-control-vocab](#technical-control-vocab), date)
- **`behavioral_controls`** *(array)* : Controls put in place to limit, monitor, or correct the insider's behavior within the organization
  - One or more tuple values of the format ([behavioral-control-vocab](#behavioral-control-vocab), date)
- **`investigated_by`** *(array)* : The organization(s) or entity(s) that investigated the incident
  - One or more constants from [investigator-vocab](#investigator-vocab)
- **`investigation_events`** *(array)* : Specific events that happened during the course of the investigation into the incident
  - One or more tuple values of the format ([investigation-vocab](#investigation-vocab), date)
- **`comment`** *(string)* : Clarifying comments or additional details about the organization's response

## Vocabularies

### technical-control-vocab

Constants: `1`, `2`

| Const | Value | Description |
| --- | --- | --- |
| 1 | Access to Technical System(s) Restricted | Insider's access to the organization's technical systems is restricted in any capacity (e.g., the organization declares that insider could only log onto system if another employee is present)|
| 2 | Access to Technical System(s) Terminated | Insider's access to the organization's technical systems is completely terminated (e.g., the insider's account is deleted upon termination from the company)|

### behavioral-control-vocab

Constants: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`

| Const | Value | Description |
| --- | --- | --- |
| 1 | Counseling | Insider is sent to counseling of any kind as a result of their actions|
| 2 | Demoted | Insider is demoted (.g., reduced their rank, title, or responsbilities)|
| 3 | Passed Over For Promotion | Organization chooses to promote someone other than the insider as a result of the insider's actions|
| 4 | Poor Performance Review | Insider receives a review of their work performance which is deemed below average|
| 5 | Put on Paid/Unpaid Leave | Insider is put on temporary leave from a job assignment, with or without pay and benefits|
| 6 | Referred to Employee Assistance Program | Insider is referred to the EAP as a result of their actions|
| 7 | Reported to HR | Insider is reported to Human Resources as a result of their actions|
| 8 | Suspended | Insider is suspended (definitely or indefinitely) and not allowed to conduct normal work for the organization|
| 9 | Terminated | Insider is terminated, or fired, from the organization|
| 10 | Transferred | Insider is transferred to another company location as a result of their actions|
| 11 | Verbal Reprimand | Insider receives a verbal reprimand from their supervisor as a result of their actions|
| 12 | Written Reprimand | Insider receives a written reprimand from their supervisor as a result of their actions|

### investigation-vocab

Constants: `1`, `2`, `3`, `4`, `5`, `6`

| Const | Value | Description |
| --- | --- | --- |
| 1 | Evidence Found | Evidence relevant to the incident is found (e.g., fellow employee found a USB drive left in the insider's computer that had sensitive company files downloaded on to it)|
| 2 | Insider Admits to Activity in Interview | Insider admits to involvement in insider incident while being interviewed by investigators about the incident (or related activity)|
| 3 | Insider's Residence/Workplace Searched | Investigators search the insider's home or workplace for evidence related to the incident|
| 4 | Case Opened Internally | The victim organization open a case to investigate the insider|
| 5 | Case Opened with Law Enforcement | Law enforcement opened a case to investigate the insider|
| 6 | Insider Interviewed | Insider is interviewed about the incident by investigators|

### investigator-vocab

Constants: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `99`

| Const | Value | Description |
| --- | --- | --- |
| 1 | Incident Response Team | Incident Response Team (IRT), whether internal to the organization or provided by an external contract|
| 2 | Internal Investigators | Other investigators internal to the victim organization|
| 3 | Law Enforcement - Federal | Federal law enforcement entity such as the FBI or USSS|
| 4 | Law Enforcement - Government Agency | Law enforcement belonging to a government agency such as DHS, USPS, or the IRS|
| 5 | Law Enforcement - Local/State | State or local law enforcement entity|
| 6 | Law Enforcement - Military/DoD | Law enforcement belonging to the military or Department of Defense such as military police or NCIS|
| 7 | Management | Management internal to the organization|
| 99 | Other | Other investigator not listed in this vocabulary|

## License
This file is a part of the Insider Incident Data Exchange Standard (IIDES) - see https://github.com/cmu-sei/IIDES

Copyright 2024 Carnegie Mellon University.

[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution.  Please see Copyright notice for non-US Government use and distribution.

This work is provided "AS-IS" with "NO WARRANTIES OF ANY KIND - EXPRESS OR IMPLIED" and is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.

Requests for permission for non-licensed uses should be directed to the Software Engineering Institute at permission@sei.cmu.edu.

CERT® is registered in the U.S. Patent and Trademark Office by Carnegie Mellon University.

DM24-0776
