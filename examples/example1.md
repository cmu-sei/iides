# Example1


## Incident

The leak severely impacted the confidentiality and integrity of agency operations, exposing sensitive information.

- **`Id`**:
 incident--ef88113a-27a0-4a56-8f70-e8a5fd4541e6
- **`Cia effect`**:
   - Confidentiality (*C*) &mdash; The protection of information from unauthorized access or disclosure
- **`Incident type`**:
   - Espionage (*E*) &mdash; The covert or illicit practice of spying on a foreign government, organization, entity, or person to obtain confidential information for military, political, strategic, or financial advantage
- **`Incident subtype`**:
   - Government (*E.2*) &mdash; Covert intelligence-gathering activities to obtain government or military secrets for the benefit of another government to obtain political or military advantage
- **`Outcome`**:
   - Data Deleted (*DD*) &mdash; Data was deleted from the victim organization's systems
  - Monetary Losses (*ML*) &mdash; Indirect loss of money through damage, detriment, or suffering related to the incident
  - Safety Impact (*SI*) &mdash; There was an impact or potential for impact to safety as a result of the incident
  - Data Read (*DR*) &mdash; Organizational data was read by the insider
  - Data Stolen (*DS*) &mdash; Any organizational information or assets that are stolen
- **`Status`**:
 Closed (*C*) &mdash; All investigations and legal proceedings are closed
- **`Summary`**:
 Oliver Griffin, a former software engineer at a government agency, leaked sensitive documents to an unauthorized entity. These documents detailed the agency's secret tools and techniques, causing severe damage to national security, exposing operations and personnel, and costing the agency substantial financial resources. Griffin was charged with unauthorized access to computer systems, dissemination of classified information, and other related crimes. He was convicted and sentenced to 35 years in prison.
- **`Brief summary`**:
 Oliver Griffin leaked sensitive documents to an unauthorized entity, detailing cybersecurity tools and techniques. This caused severe national security damage and financial costs. Griffin was convicted of multiple charges and sentenced to 35 years in prison.

## Insider

Oliver James Griffin had a history of social and mental health issues. He showed concerning behaviors, such as repeated technical policy abuse and conflicts with his supervisor as well as browsing dark web forums. The insider had multiple workplace incidents.

- **`Id`**:
 insider--5460491c-eacd-4074-aef9-f6f584893a59
- **`Incident role`**:
 Primary (*1*) &mdash; Insider is the primary perpetrator of the incident
- **`Motive`**:
   - Revenge (*8*) &mdash; The insider wanted revenge for an actual or perceived wrong
- **`Predispositions`**:
   - Social and Mental Health Issues (*['1', '1.1']*) &mdash; A history of behaviors related to the insider's mental health or unacceptable social behavior
  - A History of Rule Violations (*['2', '2.4']*) &mdash; A history of violating the law or violating rules at other organizations
  - Suspicious Associations (*['3', '3.2']*) &mdash; A history of associating with criminal or otherwise objectionable persons or entities
- **`Concerning behaviors`**:
   - Technical Policy Abuse (*['2', '2.2']*) &mdash; Violating policies regarding the use of the organization's IT systems
  - Interpersonal Issues (*['3', '3.2']*) &mdash; Conflicts with others in the organization or human resources (HR) issues
- **`first_name`**:
 Oliver
- **`middle_name`**:
 James
- **`last_name`**:
 Griffin
- **`suffix`**:
 Jr
- **`alias`**:
 ['OGriffin', 'Silent Hawk', 'Shadow Walker', 'Dark Avenger']
- **`city`**:
 New York
- **`state`**:
 NY
- **`country`**:
 US
- **`postal_code`**:
 10001
- **`country_of_citizenship`**:
 ['US']
- **`nationality`**:
 ['US']
- **`gender`**:
 M
- **`age`**:
 35
- **`education`**:
 5
- **`marital_status`**:
 1
- **`number_of_children`**:
 0

## Organization

- **`Id`**:
 organization--d1472454-0236-4b66-9013-65d0f916ee48
- **`Name`**:
 Government Agency
- **`City`**:
 Washington
- **`State`**:
 DC
- **`Country`**:
 US
- **`Postal code`**:
 20500
- **`Small business`**:
 False
- **`Industry sector`**:
 Public Administration (*92*) &mdash; Federal/State/Local administration and the oversight of public programs.
- **`Industry subsector`**:
 National Security (*92.811*) &mdash; This industry comprises government establishments of the Armed Forces, including the National Guard, primarily engaged in national security and related activities.
- **`Business`**:
 A government agency responsible for various administrative and regulatory functions within the federal government of the United States.
- **`Incident role`**:
 Primary Victim (*V*) &mdash; The organization was the primary victim organization of the insider's actions.
- **`Parent company`**:
 United States Government

## Organization

- **`Id`**:
 organization--19f19fa9-d96e-4407-901e-06ecaefd71b5
- **`Name`**:
 Global News Network
- **`Small business`**:
 False
- **`Industry sector`**:
 Information (*51*) &mdash; Hardware or software systems related to the processing, communications, and accessing of information.
- **`Industry subsector`**:
 Web Search Portals, Libraries, Archives, and Other Information Services (*51.9*) &mdash; Industries in the Web Search Portals, Libraries, Archives, and Other Information Services subsector group establishments supplying information, storing and providing access to information, searching and retrieving information, and operating websites that use search engines to allow for searching information on the Internet. The main components of the subsector are libraries, archives, and web search portals.
- **`Business`**:
 Global News Network is a nonprofit organization that publishes news and media content from various sources.
- **`Incident role`**:
 Beneficiary (*B*) &mdash; The organization accepted trade secrets, customer lists, intellectual property, etc. that the insider obtained through the incident.

## Detection

Griffin's unauthorized activities were detected by the government's security team and subsequently investigated by law enforcement. Detection involved technical means such as monitoring access logs, audit logs, database logs, remote access logs, and system file logs.

- **`Id`**:
 detection--bd545866-663f-4d62-a39a-da3672842c9f
- **`First detected`**:
 2001-03-07T00:00:00Z
- **`Who detected`**:
   - Law Enforcement (*LE*) &mdash; Law enforcement discovered the insider's illegal activity (e.g., police noticed that the insider was gaining access to the company after hours)
  - Security Team (*ST*) &mdash; Technical or personnel security team discovered the insider's activity
- **`Detected method`**:
   - Technical Means (*2*) &mdash; The insider's activity was detected via analysis or anomalies in technical systems and software
  - Security Software (*4*) &mdash; The insider's activity was detected by security software (e.g., the insider tried to download a document with trade secrets and an automatic alert detected the download)
- **`Logs`**:
   - Access Logs (*AC*) &mdash; File or system access logs
  - Audit Logs (*AU*) &mdash; Logs generated specifically for auditing purposes
  - Database Logs (*DB*) &mdash; Logs from traditional or non-traditional database servers or services
  - Remote Access Logs (*RA*) &mdash; Logs from remote access servers or clients
  - System File Logs (*SF*) &mdash; File logs (create, delete, modify, etc.) from workstations, servers, and other systems

## Impact

The leak included approximately 5 highly sensitive documents.

- **`Id`**:
 impact--2d4ed800-002d-4ce5-bbb0-c89acc1f4254
- **`High`**:
 5
- **`Low`**:
 5
- **`Metric`**:
 Files (*7*) &mdash; Number of physical or digital files stolen, read, or compromised
- **`Estimated`**:
 True

## Impact

The financial impact of the breach was substantial, with estimates ranging from hundreds of millions to a billion dollars for damage control and security improvements.

- **`Id`**:
 impact--5f3ee38d-2d4c-4ea9-9857-41f9537477ea
- **`High`**:
 1,000,000,000
- **`Low`**:
 100,000,000
- **`Metric`**:
 Dollars (*5*) &mdash; Specific financial impact of money stolen, restitution ordered, etc.
- **`Estimated`**:
 True

## Target

- **`Id`**:
 target--2a6f542f-a3e6-43e9-b628-cc9c97765276
- **`Asset type`**:
 Information (*2*) &mdash; Data or business materials that contain important details belonging to a specific target owner
- **`Category`**:
 Government/Law Enforcement Information (*2.3*) &mdash; Classified or sensitive government or law enforcement information
- **`Subcategory`**:
 Classified Information (*2.3.1*) &mdash; Information that is restricted by the government for reasons of national security
- **`Format`**:
 Electronic (*1*) &mdash; Technological digital format
- **`Owner`**:
 Organization (*O*) &mdash; The organization, rather than its employees or customers, owns the target
- **`Sensitivity`**:
   - Secret (*4*) &mdash; Public disclosure would cause serious damage to national security
  - SecretNoForn (*5*) &mdash; Secret / restricted to country of source
  - Top Secret (TS) (*6*) &mdash; Top secret - unauthorized disclosure would cause exceptionally grave damage to national security
  - TS/SCI (*7*) &mdash; Top secret / Sensitive compartmented information
- **`Description`**:
 Classified agency information related to hacking tools and techniques disclosed to an unauthorized entity.

## Response

Griffin left the agency in November of 2001. Before departing from the agency, he planted a service to still allow remote access to government files and databases, which he used to access classified information post departure.

- **`Id`**:
 response--f42fc7ae-48a1-48f9-bf84-0d4b13f7a64c
- **`technical_controls`**:
 [['1', '2001-11-01'], ['2', '2001-11-01']]
- **`behavioral_controls`**:
 [['9', '2001-11-01']]
- **`investigated_by`**:
 ['2', '3']
- **`investigation_events`**:
 [['3', '2002-03-07'], ['1', '2002-03-07'], ['2', '2003-06-18']]

## Court Case

This case involved multiple charges against Oliver Griffin, including unauthorized access to classified information, computer hacking, unauthorized access to government computer systems, and causing transmission of harmful computer commands.

- **`Id`**:
 court-case--0e430311-72ee-4776-be74-3c1969d141c0
- **`Case number`**:
 1:22-cr-00123-JMF
- **`Case title`**:
 USA vs. Griffin
- **`Court country`**:
 United States
- **`Court state`**:
 New York
- **`Court district`**:
 Southern District of New York
- **`Court type`**:
 Federal (*1*) &mdash; Top level government court
- **`Case type`**:
 Criminal (*2*) &mdash; A case dealing with a violation of criminal law
- **`Defendant`**:
   - Oliver Griffin
- **`Plaintiff`**:
   - United States of America

## Charge

- **`Id`**:
 charge--2bc9e36b-53c3-44fa-8997-ccb5d8ac9418
- **`Title`**:
 18 U.S.C.
- **`Section`**:
 793(e)
- **`Nature of offense`**:
 Illegal gathering and transmission of national defense information.
- **`Count`**:
 3
- **`Plea`**:
 Not Guilty (*3*) &mdash; The defendant pleaded not guilty to the charge
- **`Plea bargain`**:
 False
- **`Disposition`**:
 Convicted (*2*) &mdash; Pleaded or found guilty by a court

## Charge

- **`Id`**:
 charge--0572191b-beef-484c-841f-149a9f17fd8f
- **`Title`**:
 18 U.S.C.
- **`Section`**:
 641
- **`Nature of offense`**:
 Theft of government property.
- **`Count`**:
 1
- **`Plea`**:
 Not Guilty (*3*) &mdash; The defendant pleaded not guilty to the charge
- **`Plea bargain`**:
 False
- **`Disposition`**:
 Convicted (*2*) &mdash; Pleaded or found guilty by a court

## Charge

- **`Id`**:
 charge--868f7fd1-b492-40a4-b21f-f5a31cd5e219
- **`Title`**:
 18 U.S.C.
- **`Section`**:
 1030(a)(1)
- **`Nature of offense`**:
 Unauthorized access to a computer to obtain classified information.
- **`Count`**:
 1
- **`Plea`**:
 Not Guilty (*3*) &mdash; The defendant pleaded not guilty to the charge
- **`Plea bargain`**:
 False
- **`Disposition`**:
 Convicted (*2*) &mdash; Pleaded or found guilty by a court

## Charge

- **`Id`**:
 charge--d59dd57a-96b5-472f-a788-dcdb30ec5cb6
- **`Title`**:
 18 U.S.C.
- **`Section`**:
 1030(a)(2)
- **`Nature of offense`**:
 Unauthorized access to a computer to obtain information from a department or agency of the U.S.
- **`Count`**:
 1
- **`Plea`**:
 Not Guilty (*3*) &mdash; The defendant pleaded not guilty to the charge
- **`Plea bargain`**:
 False
- **`Disposition`**:
 Convicted (*2*) &mdash; Pleaded or found guilty by a court

## Charge

- **`Id`**:
 charge--cc6be1c8-5c76-4286-84a0-2b456a288c13
- **`Title`**:
 18 U.S.C.
- **`Section`**:
 1030(a)(5)(A)
- **`Nature of offense`**:
 Causing transmission of harmful computer commands.
- **`Count`**:
 1
- **`Plea`**:
 Not Guilty (*3*) &mdash; The defendant pleaded not guilty to the charge
- **`Plea bargain`**:
 False
- **`Disposition`**:
 Convicted (*2*) &mdash; Pleaded or found guilty by a court

## Charge

- **`Id`**:
 charge--9259e182-5643-4a4d-b078-4bb251fe2595
- **`Title`**:
 18 U.S.C.
- **`Section`**:
 1519
- **`Nature of offense`**:
 Obstruction of justice.
- **`Count`**:
 1
- **`Plea`**:
 Not Guilty (*3*) &mdash; The defendant pleaded not guilty to the charge
- **`Plea bargain`**:
 False
- **`Disposition`**:
 Convicted (*2*) &mdash; Pleaded or found guilty by a court

## Sentence

- **`Id`**:
 sentence--21e74a96-ba47-46fe-8338-736ab19552ba
- **`Sentence type`**:
 Incarceration (*9*) &mdash; Imprisonment
- **`Quantity`**:
 35
- **`Metric`**:
 Year(s) (*4*) &mdash; Imposed sentence is in terms of years (e.g. five years no Internet access)
- **`Concurrency`**:
 False

## Sentence

Lifetime supervised release, to run concurrently.

- **`Id`**:
 sentence--1141c372-543a-42f5-a640-c88b8ab16ae2
- **`Sentence type`**:
 Supervised Release (*16*) &mdash; Defendant is released into the community, subject to special conditions and restrictions, after the completion of a prison sentence
- **`Quantity`**:
 60
- **`Metric`**:
 Year(s) (*4*) &mdash; Imposed sentence is in terms of years (e.g. five years no Internet access)
- **`Concurrency`**:
 True

## Legal Response

The insider was investigated and charged for multiple offenses, including unauthorized disclosure of classified information, computer hacking, and possession of illicit digital content. The judgment date is in relation to the charges specifically related to the dissemination of stolen classified files.

- **`Id`**:
 legal-response--b318c37b-2f76-421f-bf12-0833e836b00c
- **`Law enforcement contacted`**:
 2002-03-07
- **`Insider arrested`**:
 2002-08-24
- **`Insider charged`**:
 2003-06
- **`Insider pleads`**:
 2003-06
- **`Insider judgment`**:
 2004-07-13
- **`Insider sentenced`**:
 2005-02-01

## Job

The insider was employed as a software engineer in a high-security governmental agency, where they had access to sensitive and classified information.

- **`Id`**:
 job--e76248a2-82df-4c7d-b7a0-bf86eb85c570
- **`Job function`**:
 Computer and Mathematical (*15*) &mdash; Computer and Mathematical
- **`Occupation`**:
 Computer Occupations (*15.1*) &mdash; Computer Systems Analysts, Information Security Analysts, Network Support Specialists, User Support Specialists, Network Architects, Systems Administrators, Software Developers, Web Developers, Interface Designers, etc.
- **`Title`**:
 Software Engineer
- **`Position technical`**:
 True
- **`Access authorization`**:
 Administrator/Root (*2*) &mdash; Authorized full administrative access
- **`Employment type`**:
 Full-time (*FLT*) &mdash; Individual who is directly employed by the organization and works at least 35 hours per week or is classified by the organization as a full-time employee
- **`Hire date`**:
 2001-01-01
- **`Departure date`**:
 2006-11-11
- **`Tenure`**:
 P5Y10M10D

## Stressor

Oliver Griffin's internal disputes and a hostile work environment at the agency (self-imposed) contributed to his decision to steal and leak classified information as revenge for mistreatment.

- **`Id`**:
 stressor--28ecfbf3-5eb1-429f-8a55-c2e16f08ebcd
- **`Date`**:
 2002
- **`Category`**:
 Organizational Issues (*2*) &mdash; The insider's employer had problems or changes that directly or indirectly affected the insider
- **`Subcategory`**:
 Hostile Work Environment (*2.12*) &mdash; A work environment that is difficult or uncomfortable for another person to work in due to discrimination of any kind

## TTP

- **`Id`**:
 ttp--a181e814-aa3a-411e-ae79-79ceba48e36a
- **`Date`**:
 2002-04-20T14:00:00Z
- **`Sequence num`**:
 1
- **`Observed`**:
 True
- **`Number of times`**:
 2
- **`TTP vocab`**:
 IIDES
- **`Tactic`**:
 Data Exfiltration (*7*) &mdash; Data (or copies of data) is removed from the organization without permission or explicitly against permission to use in an unauthorized way
- **`Technique`**:
 Email (*7.3*) &mdash; Data exfiltration through electronic mail (e.g., the insider e-mailed confidential information to competitor)
- **`Location`**:
   - On-site (*1*) &mdash; Action taken while on site at an organizational facility
- **`Hours`**:
   - During Work Hours (*1*) &mdash; Insider took the action during their normal working hours
- **`Device`**:
   - Company Desktop (*1*) &mdash; Organization owned desktop workstation
- **`Channel`**:
   - Company Email (*1*) &mdash; An email account the company controls
  - Online Forum (*4*) &mdash; Private or public forum accessed via the Internet
  - Personal Email (*5*) &mdash; An email account the organization does not control or monitor
- **`Description`**:
 Griffin used a personal email account to exfiltrate classified agency information from the organization's database server to his personal computer.

## TTP

- **`Id`**:
 ttp--a154e814-aa3a-411e-ae79-79ceba48e79b
- **`Date`**:
 2002-04-20T14:00:00Z
- **`Sequence num`**:
 2
- **`Observed`**:
 True
- **`Number of times`**:
 1
- **`TTP vocab`**:
 IIDES
- **`Tactic`**:
 Data Exfiltration (*7*) &mdash; Data (or copies of data) is removed from the organization without permission or explicitly against permission to use in an unauthorized way
- **`Technique`**:
 Removable Media (*7.2*) &mdash; Data exfiltration through digital equipment or media (e.g., the insider had trade secrets owned by the victim organization on a flash drive and sent the flash drive to the competitor to be copied)
- **`Location`**:
   - Remotely (*2*) &mdash; Action taken while remote (i.e., not at an organizational facility)
- **`Hours`**:
   - Outside of Work Hours (*2*) &mdash; Insider took the action outside of their normal working hours
- **`Device`**:
   - Personal Computer (*7*) &mdash; Personally owned computer
- **`Channel`**:
   - Other (*9*) &mdash; Other type of channel not listed in this vocabulary
- **`Description`**:
 Griffin then loaded the data on a removable media disk.

## TTP

- **`Id`**:
 ttp--a154e814-aa3a-411e-ae79-79ceba48e77b
- **`Date`**:
 2002-04-20T14:00:00Z
- **`Sequence num`**:
 2
- **`Observed`**:
 True
- **`Number of times`**:
 2
- **`TTP vocab`**:
 IIDES
- **`Tactic`**:
 Malware (*4*) &mdash; Malicious software is used
- **`Technique`**:
 Backdoor (*4.1*) &mdash; A malicious program that allows an attacker to perform actions on a remote system, such as transferring files, acquiring passwords, or executing arbitrary commands
- **`Location`**:
   - On-site (*1*) &mdash; Action taken while on site at an organizational facility
- **`Hours`**:
   - During Work Hours (*1*) &mdash; Insider took the action during their normal working hours
- **`Device`**:
   - Company Desktop (*1*) &mdash; Organization owned desktop workstation
- **`Channel`**:
   - Other (*9*) &mdash; Other type of channel not listed in this vocabulary
- **`Description`**:
 Before leaving the agency, Griffin planted a backdoor into the agency network.

## TTP

- **`Id`**:
 ttp--a154e814-aa3a-411e-ae79-79ceba48e76b
- **`Date`**:
 2002-04-20T14:00:00Z
- **`Sequence num`**:
 3
- **`Observed`**:
 True
- **`Number of times`**:
 1
- **`TTP vocab`**:
 IIDES
- **`Tactic`**:
 Data Exfiltration (*7*) &mdash; Data (or copies of data) is removed from the organization without permission or explicitly against permission to use in an unauthorized way
- **`Technique`**:
 Other Technical/Digital (*7.9*) &mdash; Data exfiltration using other technical or digital means not listed in this vocabulary
- **`Location`**:
   - Remotely (*2*) &mdash; Action taken while remote (i.e., not at an organizational facility)
- **`Hours`**:
   - Outside of Work Hours (*2*) &mdash; Insider took the action outside of their normal working hours
- **`Device`**:
   - Database Server (*4*) &mdash; Database server
- **`Channel`**:
   - Company Email (*1*) &mdash; An email account the company controls
  - Personal Email (*5*) &mdash; An email account the organization does not control or monitor
  - Other (*9*) &mdash; Other type of channel not listed in this vocabulary
- **`Description`**:
 After leaving the agency, Griffin hosted a server on the agency's network to continue accessing and exfiltrating classified data.

## Note

The charges related to illicit digital content were included in the JSON because they are relevant to the overall investigation of Oliver Griffin. Although they do not directly pertain to the insider threat, they were pivotal in leading to his initial arrest and subsequent comprehensive charges.

- **`Id`**:
 note--b372b9ad-cb92-4db6-be28-1e3f62605858
- **`Author`**:
 CMU Researcher
- **`Date`**:
 2024-05-17T00:00:00Z

## Source

- **`Id`**:
 source--53455e706-d762-4b35-b54a-7e33b91cbec3
- **`Title`**:
 Mock Case Description
- **`Source type`**:
 DOJ Press Release (*2*) &mdash; Press release from the Department of Justice or U.S. Attorneys' Office
- **`File type`**:
 HTML File (*html*) &mdash; A file in HTML format
- **`Date`**:
 2024-07-18T00:00:00Z
- **`Public`**:
 True
- **`Document`**:
 ./source/example1desc.md

## Source

- **`Id`**:
 source--5565e706-d762-4b35-b54a-6f22a80badb2
- **`Title`**:
 Oliver Griffin Charged with Unauthorized Disclosure of Classified Information and Other Offenses
- **`Source type`**:
 DOJ Press Release (*2*) &mdash; Press release from the Department of Justice or U.S. Attorneys' Office
- **`File type`**:
 HTML File (*html*) &mdash; A file in HTML format
- **`Date`**:
 2003-06-18T00:00:00Z
- **`Public`**:
 True
- **`Document`**:
 https://www.fakeurl.com/oliver-griffin-charged

## Source

- **`Id`**:
 source--d6a29cb3-519f-4d62-a1f6-a86439bef53d
- **`Title`**:
 Former Intelligence Officer Oliver Griffin Sentenced to 35 Years in Prison for Espionage
- **`Source type`**:
 DOJ Press Release (*2*) &mdash; Press release from the Department of Justice or U.S. Attorneys' Office
- **`File type`**:
 HTML File (*html*) &mdash; A file in HTML format
- **`Date`**:
 2004-01-18T00:00:00Z
- **`Public`**:
 True
- **`Document`**:
 https://www.fakeurl.com/oliver-griffin-sentenced

## Source

- **`Id`**:
 source--7e3ef93e-31b0-4e17-a32a-98540326fd05
- **`Title`**:
 Intelligence Engineer Convicted of Largest Theft of Classified Data in Agency's History
- **`Source type`**:
 Media (*5*) &mdash; News, blog, or similar publication
- **`File type`**:
 HTML File (*html*) &mdash; A file in HTML format
- **`Date`**:
 2002-07-13T00:00:00Z
- **`Public`**:
 True
- **`Document`**:
 https://www.fakeurl.com/intelligence-engineer-convicted

## Source

- **`Id`**:
 source--d36603a3-2510-4617-87eb-10eea6ab672e
- **`Title`**:
 USA v. Griffin Docket Information
- **`Source type`**:
 Court Document (*1*) &mdash; Legal document from a court case
- **`File type`**:
 HTML File (*html*) &mdash; A file in HTML format
- **`Date`**:
 2002-07-13T00:00:00Z
- **`Public`**:
 True
- **`Document`**:
 https://www.fakeurl.com/usa-v-griffin-docket
