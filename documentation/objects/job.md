# Job

Details of the employment relationship between an individual and an organization.

## Properties

- **`id`** (required) *(string)* : A unique string that begins with "job--" and is appended with a UUIDv4.
	- Uses pattern: ^job--[UUIDv4]
- **`job_function`** *(string)* : Functional category of the individual's job.
	- A constant from [job-function-vocab](#job-function-vocab)
	- Required if `occupation` exists.
- **`occupation`** *(string)* : The subcategory of the individual's job. When present, job_function should also be present.
	- A constant from [occupation-vocab](#occupation-vocab)
	- Required if `title` exists.
- **`title`** *(string)* : The individual's job title. If title is specified, occupation should be as well.
- **`position_technical`** *(boolean)* : The individual had access to technical areas of the organization during the incident (e.g. IT admin, network engineer, help desk associate, etc.)
- **`access_authorization`** *(string)* : The level of access control given by this job.
	- A constant from [access-auth-vocab](#access-auth-vocab)
- **`employment_type`** *(string)* : The individual's employment arangement at the time of the incident.
	- A constant from [employment-type-vocab](#employment-type-vocab)
- **`hire_date`** *(date)* : Date the individual is hired into this position.
- **`departure_date`** *(date)* : Date the individual departed from this position.
- **`tenure`** *(timedelta)* : The amount of time the individual spent in this particular job role.
- **`comment`** *(string)* : Clarifying comments or details about the job or the individual's employment with the organization.

## Vocabularies

### job-function-vocab

Constants: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`, `16`, `18`, `19`, `20`, `21`, `22`, `23`, `25`

| Const | Value | Description |
| --- | --- | --- |
| 1 | Accounting Service | TODO|
| 2 | Architecture and Engineering | TODO|
| 3 | Arts, Design, Entertainment, Sports, and Media | TODO|
| 4 | Building and Grounds Cleaning and Maintenance | TODO|
| 5 | Business and Financial Operations | TODO|
| 6 | Community and Social Service | TODO|
| 7 | Computer | TODO|
| 8 | Educational Instruction | TODO|
| 9 | Food Preparation and Serving Related | TODO|
| 10 | Healthcare Practitioner | TODO|
| 11 | Healthcare Support | TODO|
| 12 | Installation, Maintenance, and Repair | TODO|
| 13 | Legal | TODO|
| 14 | Life, Physical, and Social Science | TODO|
| 15 | Management | TODO|
| 16 | Military Specific | TODO|
| 18 | Office and Administrative Support | TODO|
| 19 | Production | TODO|
| 20 | Protective Service | TODO|
| 21 | Sales and Related | TODO|
| 22 | Student | TODO|
| 23 | Transportation and Material Moving | TODO|
| 25 | Other | TODO|

### occupation-vocab

Constants: `1.1`, `1.2`, `1.3`, `1.4`, `2.1`, `2.2`, `2.3`, `2.4`, `2.5`, `2.6`, `3.1`, `3.2`, `3.3`, `3.4`, `3.5`, `4.1`, `4.2`, `5.1`, `5.2`, `5.3`, `5.4`, `5.5`, `5.6`, `5.7`, `5.8`, `5.9`, `5.10`, `5.11`, `5.12`, `5.13`, `5.14`, `5.15`, `5.16`, `5.17`, `5.18`, `6.1`, `6.2`, `6.3`, `6.4`, `6.5`, `7.1`, `7.2`, `7.3`, `7.4`, `7.5`, `7.6`, `7.7`, `7.8`, `7.9`, `7.10`, `7.11`, `7.12`, `7.13`, `8.1`, `8.2`, `9.1`, `9.2`, `9.3`, `10.1`, `10.2`, `10.3`, `10.4`, `10.5`, `10.6`, `10.7`, `10.8`, `10.9`, `10.10`, `10.11`, `10.12`, `11.1`, `12.1`, `12.2`, `13.1`, `13.2`, `14.1`, `14.2`, `14.3`, `14.4`, `14.5`, `14.6`, `14.7`, `15.1`, `15.2`, `15.3`, `15.4`, `15.5`, `15.6`, `15.7`, `15.8`, `15.9`, `15.10`, `15.11`, `15.12`, `15.13`, `15.14`, `15.15`, `15.16`, `15.17`, `15.18`, `15.19`, `15.20`, `15.21`, `16.1`, `16.2`, `18.1`, `18.2`, `18.3`, `18.4`, `18.5`, `18.6`, `18.7`, `18.8`, `18.9`, `18.10`, `18.11`, `18.12`, `18.13`, `18.14`, `18.15`, `18.16`, `18.17`, `18.18`, `18.19`, `18.20`, `18.21`, `19.1`, `19.2`, `20.1`, `20.2`, `20.3`, `20.4`, `20.5`, `20.6`, `20.7`, `21.1`, `21.2`, `21.3`, `21.4`, `21.1`, `22.1`, `23.1`, `23.2`, `25.1`

| Const | Value | Description |
| --- | --- | --- |
| 1.1 | Accountants | TODO|
| 1.2 | Accounting Clerks | TODO|
| 1.3 | Accounts Payable Clerks | TODO|
| 1.4 | Bookkeepers | TODO|
| 2.1 | Chemical Engineering | TODO|
| 2.2 | Electrical and Electronic Engineering | TODO|
| 2.3 | Electrical Engineers | TODO|
| 2.4 | Engineers | TODO|
| 2.5 | Hardware Engineers | TODO|
| 2.6 | Mechanical Engineers | TODO|
| 3.1 | Communications | TODO|
| 3.2 | Editors | TODO|
| 3.3 | Graphic Designers | TODO|
| 3.4 | Lighting Technicians | TODO|
| 3.5 | News Analysts, Reporters, and Journalists | TODO|
| 4.1 | Building Cleaning Workers | TODO|
| 4.2 | Grounds Maintenance Workers | TODO|
| 5.1 | Auditors | TODO|
| 5.2 | Budget Analysts | TODO|
| 5.3 | Claims Adjuster, Examiners, and Investigators | TODO|
| 5.4 | Compliance Officers | TODO|
| 5.5 | Consumer Lending | TODO|
| 5.6 | Credit Analysts | TODO|
| 5.7 | Financial Advisors | TODO|
| 5.8 | Financial and Investment Analysts | TODO|
| 5.9 | Financial  Specialists | TODO|
| 5.10 | Human Resources Specialists | TODO|
| 5.11 | Loan Officers | TODO|
| 5.12 | Management Analysts | TODO|
| 5.13 | Marketing Specialists | TODO|
| 5.14 | Payroll and Timekeeping Clerks | TODO|
| 5.15 | Personal Financial Advisors | TODO|
| 5.16 | Project Management Specialists | TODO|
| 5.17 | Revenue Agents | TODO|
| 5.18 | Tax Preparers | TODO|
| 6.1 | Child, Family, and Social Workers | TODO|
| 6.2 | Clergy | TODO|
| 6.3 | Counselors | TODO|
| 6.4 | Educational Advisors | TODO|
| 6.5 | Probation Officers | TODO|
| 7.1 | Computer Network Architects | TODO|
| 7.2 | Computer Network Support Specialists | TODO|
| 7.3 | Computer Programmers | TODO|
| 7.4 | Computer Systems Analyst | TODO|
| 7.5 | Computer User Support Specialists | TODO|
| 7.6 | Data Scientists | TODO|
| 7.7 | Database Administrators | TODO|
| 7.8 | Database Specialists | TODO|
| 7.9 | Information Technology | TODO|
| 7.10 | Network and Computer Systems Administrators | TODO|
| 7.11 | Network Engineer | TODO|
| 7.12 | Software Developers | TODO|
| 7.13 | Website and Digital Interface Designers | TODO|
| 8.1 | Computer Science Professors | TODO|
| 8.2 | Educational Teachers | TODO|
| 9.1 | Food Preparation | TODO|
| 9.2 | Food Servers | TODO|
| 9.3 | Servers | TODO|
| 10.1 | Diagnostic Medical Sonographers | TODO|
| 10.2 | Gynecologists | TODO|
| 10.3 | Medical Records Specialists | TODO|
| 10.4 | Medical Technicians | TODO|
| 10.5 | Nursing | TODO|
| 10.6 | Occupational Therapists | TODO|
| 10.7 | Optometrists | TODO|
| 10.8 | Pharmacists | TODO|
| 10.9 | Physicians | TODO|
| 10.10 | Radiologists | TODO|
| 10.11 | Respiratory Therapists | TODO|
| 10.12 | Speech Language Pathologists | TODO|
| 11.1 | Healthcare Support Workers | TODO|
| 12.1 | First-Line Supervisors of Mechanics, Installers, and Repairers | TODO|
| 12.2 | Installations, Maintenance, and Repair Helpers | TODO|
| 13.1 | Administrative Law Judges | TODO|
| 13.2 | Lawyers | TODO|
| 14.1 | Biological Scientists | TODO|
| 14.2 | Chemists | TODO|
| 14.3 | Hydrologists | TODO|
| 14.4 | Political Scientists | TODO|
| 14.5 | Psychologists | TODO|
| 14.6 | Scientists | TODO|
| 14.7 | Social Scientists | TODO|
| 15.1 | Administrative Services Manager | TODO|
| 15.2 | Architectural and Engineering Managers | TODO|
| 15.3 | Chief Executives | TODO|
| 15.4 | Computer and Information Systems Managers | TODO|
| 15.5 | Construction Managers | TODO|
| 15.6 | Financial Managers | TODO|
| 15.7 | Food Service Managers | TODO|
| 15.8 | General and Operations Managers | TODO|
| 15.9 | Human Resources Managers | TODO|
| 15.10 | Industrial Production Managers | TODO|
| 15.11 | Legislators | TODO|
| 15.12 | Management | TODO|
| 15.13 | Marketing Managers | TODO|
| 15.14 | Medical and Health Services Manager | TODO|
| 15.15 | Office Managers | TODO|
| 15.16 | Property, Real Estate, and Community Association Managers | TODO|
| 15.17 | Public Relations Managers | TODO|
| 15.18 | Purchasing Managers | TODO|
| 15.19 | Sales Managers | TODO|
| 15.20 | Training and Development Managers | TODO|
| 15.21 | Transportation Managers | TODO|
| 16.1 | Intelligence | TODO|
| 16.2 | Special Forces | TODO|
| 18.1 | Administrative Workers | TODO|
| 18.2 | Bank Tellers | TODO|
| 18.3 | Court, Municipal, and License Clerks | TODO|
| 18.4 | Customer Service Representatives | TODO|
| 18.5 | Data Entry Workers | TODO|
| 18.6 | Dispatchers | TODO|
| 18.7 | Eligibility Interviewers, Government Programs | TODO|
| 18.8 | File Clerks | TODO|
| 18.9 | Financial Clerks | TODO|
| 18.10 | First-Line Supervisors of Office and Administrative Support Workers | TODO|
| 18.11 | Insurance Claims and Policy Processing Clerks | TODO|
| 18.12 | Loan Interviewers and Clerks | TODO|
| 18.13 | Meter Readers, Utilities | TODO|
| 18.14 | Office Administrative Services | TODO|
| 18.15 | Office Clerks | TODO|
| 18.16 | Payroll and Timekeeping Clerks | TODO|
| 18.17 | Payroll Supervisors | TODO|
| 18.18 | Postal Service Clerks | TODO|
| 18.19 | Receptionists | TODO|
| 18.20 | Secretaries and Administrative Assistants | TODO|
| 18.21 | Shipping, Receiving and Inventory Clerks | TODO|
| 19.1 | Computer Numerically Controlled Tool Programmers | TODO|
| 19.2 | Inspectors, Testers, Sorters, Samplers, and Weighers | TODO|
| 20.1 | Correctional Officers | TODO|
| 20.2 | Detectives and Criminal Investigators | TODO|
| 20.3 | Firefighters | TODO|
| 20.4 | Police and Sheriffs Patrol Officers | TODO|
| 20.5 | Police Officers | TODO|
| 20.6 | Security Guards | TODO|
| 20.7 | Special Agents | TODO|
| 21.1 | Cashiers | TODO|
| 21.2 | Financial Service Sales Agents | TODO|
| 21.3 | Insurance Sales Agents | TODO|
| 21.4 | Real Estate Agents | TODO|
| 21.1 | Sales | TODO|
| 22.1 | Student | TODO|
| 23.1 | Transportation Inspectors | TODO|
| 23.2 | Courier | TODO|
| 25.1 | Other | TODO|

### access-auth-vocab

Constants: `REV`, `ADM`, `AAD`, `AAC`, `APU`, `AUU`, `FMR`, `NGA`, `UNA`

| Const | Value | Description |
| --- | --- | --- |
| REV | Access Revoked | TODO|
| ADM | Administrator/Root | TODO|
| AAD | Authorized Account & Data | TODO|
| AAC | Authorized Account Only | TODO|
| APU | Authorized Privileged User | TODO|
| AUU | Authorized Unprivileged User | TODO|
| FMR | Former Employee, Access not Deactivated | TODO|
| NGA | Never Given Access | TODO|
| UNA | Unauthorized | TODO|

### employment-type-vocab

Constants: `CCT`, `CFT`, `CPT`, `INT`, `FCT`, `FFT`, `FPT`, `TMP`, `VOL`, `OTH`

| Const | Value | Description |
| --- | --- | --- |
| CCT | Current Contractor | TODO|
| CFT | Current Full-time | TODO|
| CPT | Current Part-time | TODO|
| INT | Intern/Trainee/Aprentice | TODO|
| FCT | Former Contractor | TODO|
| FFT | Former Full Time | Individual who used to work for the organization on a full time basis, but is no longer employed by the organization.|
| FPT | Former Part Time | Individual who used to work for the organizaion on a part time basis, but is no longer employed by the organizaion.|
| TMP | Temporary Employee | Individual hired for a brief period of time or until a certain project is completed.|
| VOL | Volunteer | Individual not employed by the organization, but who donates their time to working on projects without receiving pay or benefits.|
| OTH | Other | Other employment type not listed in this vocabulary.|
