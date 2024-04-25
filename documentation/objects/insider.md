# Insider

TODO

## Properties

- **`id`** (required) *(string)* : TODO
	- Uses pattern: ^insider--[UUIDv4]
- **`incident_role`** (required) *(string)* : TODO
	- A constant from [incident-role-vocab](#incident-role-vocab)
- **`motive`** *(array)* : TODO
	- One or more values from [motive-vocab](#motive-vocab)
- **`substance_abuse`** *(array)* : TODO
	- One or more values from [substance-abuse-vocab](#substance-abuse-vocab)
- **`substance_use_during_incident`** *(boolean)* : TODO
- **`psychological_issues`** *(array)* : TODO
	- One or more values from [psych-issues-vocab](#psych-issues-vocab)
- **`predispositions`** *(array)* : TODO
	- One or more tuple values of the format ([predisposition-type-vocab](#predisposition-type-vocab), [predisposition-subtype-vocab](#predisposition-subtype-vocab))
- **`concerning_behaviors`** *(array)* : TODO
	- One or more tuple values of the format ([cb-type-vocab](#cb-type-vocab), [cb-subtype-vocab](#cb-subtype-vocab))
- **`comment`** *(string)* : TODO
- **Inherits properties from [Person](person)**

## Vocabularies

### incident-role-vocab

Constants: `1`, `2`, `3`, `4`

| Const | Value | Description |
| --- | --- | --- |
| 1 | Primary | TODO|
| 2 | Co-Conspirator | TODO|
| 3 | Looked the other way | TODO|
| 4 | Approved primary insider's actions | TODO|

### motive-vocab

Constants: ``, ``, ``, ``, ``, ``, ``, ``, ``

| Const | Value | Description |
| --- | --- | --- |
|  | benefit_foreign_entity | TODO|
|  | benefit_new_employer | TODO|
|  | competitive_bus_adv | TODO|
|  | curiosity | TODO|
|  | financial_gain | TODO|
|  | freedom_of_info | TODO|
|  | recognition | TODO|
|  | revenge | TODO|
|  | other | TODO|

### substance-abuse-vocab

Constants: ``, ``, ``, ``, ``, ``, ``, ``, ``, ``

| Const | Value | Description |
| --- | --- | --- |
|  | alcohol | TODO|
|  | marijuana | TODO|
|  | legal_perscription_opiate | TODO|
|  | illegal_perscription_opiate | TODO|
|  | non_perscription_opiate | TODO|
|  | opiate_unknown | TODO|
|  | non_opiate_perscription | TODO|
|  | stimulant | TODO|
|  | Street Drugs | TODO|
|  | Other | TODO|

### psych-issues-vocab

Constants: ``, ``, ``, ``, ``, ``

| Const | Value | Description |
| --- | --- | --- |
|  | outpatient_treatment | TODO|
|  | inpatient_treatment | TODO|
|  | medication_noncompliance | TODO|
|  | experienced_acted_on_delusions | TODO|
|  | threatened_attempted_suicide | TODO|
|  | other | TODO|

### predisposition-type-vocab

Constants: `1.1`, `1.2`, `1.3`, `2.4`

| Const | Value | Description |
| --- | --- | --- |
| 1.1 | Social and Mental Health Issues | TODO|
| 1.2 | A History of Rule Violations | TODO|
| 1.3 | Suspicious Associations | TODO|
| 2.4 | Personal Stressful Events | TODO|

### predisposition-subtype-vocab

Constants: `1.1.1`, `1.1.2`, `1.1.3`, `1.1.4`, `1.1.5`, `1.1.6`, `1.1.7`, `1.2.1`, `1.2.2`, `1.2.3`, `1.2.4`, `1.2.5`, `1.2.6`, `1.3.1`, `1.3.2`, `2.4.1`, `2.4.2`, `2.4.3`, `2.4.4`

| Const | Value | Description |
| --- | --- | --- |
| 1.1.1 | Possible Psychological Issues | TODO|
| 1.1.2 | Diagnosed Psychological Issues | TODO|
| 1.1.3 | Gambling Problems | TODO|
| 1.1.4 | Substance Abuse | TODO|
| 1.1.5 | A History Of Financial Problems | TODO|
| 1.1.6 | Poor Hygiene | TODO|
| 1.1.7 | Risk Taker | TODO|
| 1.2.1 | Previous Arrest/Conviction For Related Crime | TODO|
| 1.2.2 | Previous Arrest/Conviction for Unrelated Crime | TODO|
| 1.2.3 | Previous Perpetrator of Domestic Violence | TODO|
| 1.2.4 | Hacking Related Activities | TODO|
| 1.2.5 | Previous Attempts to Disclose Through Illegitimate Means | TODO|
| 1.2.6 | Pending or Previous Defendant in Civil Action | TODO|
| 1.3.1 | Criminal Association | TODO|
| 1.3.2 | Internet Underground Association | TODO|
| 2.4.1 | Medical Problems | TODO|
| 2.4.2 | Relationship Problems | TODO|
| 2.4.3 | Emerging Financial Problems | TODO|
| 2.4.4 | Family Health Issues | TODO|

### cb-type-vocab

Constants: `3.1`, `3.2`, `3.3`, `3.4`, `3.5`, `3.6`, `3.7`

| Const | Value | Description |
| --- | --- | --- |
| 3.1 | Misuse of Company Resources | TODO|
| 3.2 | Technical Policy Abuse | TODO|
| 3.3 | Interpersonal Issues | TODO|
| 3.4 | Financial | TODO|
| 3.5 | Organizational Conflict | TODO|
| 3.6 | Suspicious Contact | TODO|
| 3.7 | Relocation | TODO|

### cb-subtype-vocab

Constants: `3.1.1`, `3.1.2`, `3.1.3`, `3.2.1`, `3.2.2`, `3.2.3`, `3.2.4`, `3.2.5`, `3.2.6`, `3.3.1`, `3.3.2`, `3.3.3`, `3.3.4`, `3.3.5`, `3.3.6`, `3.3.7`, `3.3.8`, `3.3.9`, `3.3.10`, `3.3.11`, `3.3.12`, `3.3.13`, `3.4.1`, `3.4.2`, `3.4.3`, `3.5.1`, `3.5.2`, `3.5.3`, `3.5.4`, `3.5.5`, `3.5.6`, `3.6.1`, `3.6.2`, `3.6.3`, `3.6.4`, `3.7.1`

| Const | Value | Description |
| --- | --- | --- |
| 3.1.1 | Theft Of Physical Company Property | TODO|
| 3.1.2 | Insider Expressed Ownership Of Work | TODO|
| 3.1.3 | Repeated Security Violations - Non-Technical | TODO|
| 3.2.1 | Other Unauthorized Software Acquisition | TODO|
| 3.2.2 | Repeated Security Violations - Technical | TODO|
| 3.2.3 | Unauthorized Download - Remotely | TODO|
| 3.2.4 | Unauthorized Download - On Site | TODO|
| 3.2.5 | IP Policy Violation | TODO|
| 3.2.6 | Violation of Need to Know | TODO|
| 3.3.1 | Employee Extortion, Threats, or Legal Demands | TODO|
| 3.3.2 | Conflict With Supervisor | TODO|
| 3.3.3 | Conflict With Coworker(s) | TODO|
| 3.3.4 | Work Attendance Problems | TODO|
| 3.3.5 | Human Resource Policy Violations or Complaints | TODO|
| 3.3.6 | Disgruntled Employee | TODO|
| 3.3.7 | Bragging | TODO|
| 3.3.8 | Concurrent Crimes | TODO|
| 3.3.9 | Formal Complaint | TODO|
| 3.3.10 | Informal Complaint | TODO|
| 3.3.11 | Insubordination | TODO|
| 3.3.12 | Physical Abuse/Harassment | TODO|
| 3.3.13 | Sexual Harassment | TODO|
| 3.4.1 | Unexplained Wealth | TODO|
| 3.4.2 | Employee Forms New Competing Business | TODO|
| 3.4.3 | Financial Conflict of Interest | TODO|
| 3.5.1 | Planning/Contact with Competing Organization | TODO|
| 3.5.2 | Employee Went To Work For A Competing Organization | TODO|
| 3.5.3 | Employee Sought Other Employment | TODO|
| 3.5.4 | Group Resignation | TODO|
| 3.5.5 | Insider Creates Legal Entity for Illegitimate Purpose | TODO|
| 3.5.6 | Falsified Background Information | TODO|
| 3.6.1 | Suspicious Foreign Contact | TODO|
| 3.6.2 | Suspicious Foreign Travel | TODO|
| 3.6.3 | Foreign Travel - Work Related | TODO|
| 3.6.4 | Planning/Contact with Conspirator | TODO|
| 3.7.1 | Geographic Relocation | TODO|
