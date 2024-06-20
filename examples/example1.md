# Example1


## Incident

The leak severely impacted the confidentiality and integrity of CIA operations, exposing sensitive information and tools used for intelligence gathering.

- **`Id`**:
 incident--ef88113a-27a0-4a56-8f70-e8a5fd4541e6
- **`Cia effect`**:
   - Confidentiality (*C*) &mdash; The protection of information from unauthorized access or disclosure.
- **`Incident type`**:
   - Espionage (*E*) &mdash; The covert or illicit practice of spying on a foreign government, organization, entity, or person to obtain confidential information for military, political, strategic, or financial advantage.
- **`Incident subtype`**:
   - Government (*E.2*) &mdash; Covert intelligence-gathering activities to obtain government or military secrets for the benefit of another government to obtain political or military advantage.
- **`Outcome`**:
   - Data Deleted (*DD*) &mdash; Data was deleted from the victim organization's systems.
  - Monetary Losses (*ML*) &mdash; Indirect loss of money through damage, detriment, or suffering related to the incident.
  - Safety Impact (*SI*) &mdash; There was an impact, or potential for impact to safety, as a result of the incident.
  - Data Read (*DR*) &mdash; Organizational data was read by the insider.
  - Data Stolen (*DS*) &mdash; Any organizational information or assets that are stolen.
- **`Status`**:
 Closed (*C*) &mdash; All investigations and legal proceedings are closed.
- **`Summary`**:
 Joshua Adam Schulte, a former CIA software engineer, leaked classified CIA documents known as Vault 7 to WikiLeaks. These documents detailed the CIA's hacking tools and techniques, causing severe damage to U.S. national security, exposing CIA operations and personnel, and costing the agency hundreds of millions of dollars. Schulte was charged with espionage, unauthorized access to computer systems, and other related crimes. He was convicted and sentenced to 40 years in prison.
- **`Brief summary`**:
 Joshua Adam Schulte leaked classified CIA documents to WikiLeaks, detailing CIA hacking tools and techniques. This caused severe national security damage and financial costs. Schulte was convicted of espionage and sentenced to 40 years in prison.

## Insider

Joshua Adam Schulte had a history of social and mental health issues. He showed concerning behaviors such as repeated technical policy abuse and conflicts with his supervisor, as well as browsing dark web forums. The insider had multiple workplace incidents involving the harassment of colleagues, ultimately resulting in the insider being forced to move offices across the building. The insider believed he had been mistreated by staff, leading to a desire for revenge.

- **`Id`**:
 insider--5460491c-eacd-4074-aef9-f6f584893a59
- **`Incident role`**:
 Primary (*1*) &mdash; Insider is the primary perpetrator of the incident.
- **`Motive`**:
   - Revenge (*8*) &mdash; The insider wanted revenge for an actual or perceived wrong.
- **`Predispositions`**:
   - Social and Mental Health Issues (*['1', '1.1']*) &mdash; A history of behaviors related to the insider's mental health or unacceptable social behavior.
  - A History of Rule Violations (*['2', '2.4']*) &mdash; A history of violating the law or violating rules at other organizations.
  - Suspicious Associations (*['3', '3.2']*) &mdash; A history of associating with criminal or otherwise objectionable persons or entities.
- **`Concerning behaviors`**:
   - Technical Policy Abuse (*['3.2', '3.2.2']*) &mdash; Violating policies regarding the use of the organization's IT systems.
  - Interpersonal Issues (*['3.3', '3.3.2']*) &mdash; Conflicts with others in the organization or human resources (HR) issues.
- **`First name`**:
 Joshua
- **`Middle name`**:
 Adam
- **`Last name`**:
 Schulte
- **`Suffix`**:
 Jr
- **`Alias`**:
 ['JSchulte', 'Kinetic Panda', 'Nuclear Option', 'Voldemort']
- **`City`**:
 New York
- **`State`**:
 NY
- **`Country`**:
 US
- **`Postal code`**:
 10001
- **`Country of citizenship`**:
 ['US']
- **`Nationality`**:
 ['US']
- **`Gender`**:
 M
- **`Age`**:
 35
- **`Education`**:
 5
- **`Marital status`**:
 1
- **`Number of children`**:
 0

## Organization

- **`Id`**:
 organization--d1472454-0236-4b66-9013-65d0f916ee48
- **`Name`**:
 Central Intelligence Agency
- **`City`**:
 Langley
- **`State`**:
 VA
- **`Country`**:
 US
- **`Postal code`**:
 22,101
- **`Small business`**:
 False
- **`Industry sector`**:
 Public Administration (*92*) &mdash; Federal/State/Local administration and the oversight of public programs.
- **`Industry subsector`**:
 National Security (*92.811*) &mdash; This industry comprises government establishments of the Armed Forces, including the National Guard, primarily engaged in national security and related activities.
- **`Business`**:
 The Central Intelligence Agency (CIA) is a civilian foreign intelligence service of the federal government of the United States, tasked with gathering, processing, and analyzing national security information from around the world.
- **`Incident role`**:
 Primary Victim (*V*) &mdash; The organization was the primary victim organization of the insider's actions.
- **`Parent company`**:
 United States Government

## Organization

- **`Id`**:
 organization--19f19fa9-d96e-4407-901e-06ecaefd71b5
- **`Name`**:
 WikiLeaks
- **`Small business`**:
 False
- **`Industry sector`**:
 Information (*51*) &mdash; Hardware or software systems related to the processing, communications, and accessing of information.
- **`Industry subsector`**:
 Web Search Portals, Libraries, Archives, and Other Information Services (*51.9*) &mdash; Industries in the Web Search Portals, Libraries, Archives, and Other Information Services subsector group establishments supplying information, storing and providing access to information, searching and retrieving information, and operating Web sites that use search engines to allow for searching information on the Internet. The main components of the subsector are libraries, archives, and Web search portals.
- **`Business`**:
 WikiLeaks is a non-profit organization that publishes news leaks and classified media provided by anonymous sources.
- **`Incident role`**:
 Beneficiary (*B*) &mdash; The organization accepted trade secrets, customer lists, intellectual property, etc. that the insider obtained through the incident.

## Detection

Schulte's unauthorized activities were detected by the CIA's security team and subsequently investigated by law enforcement. Detection involved technical means such as monitoring access logs, audit logs, database logs, remote access logs, and system file logs.

- **`Id`**:
 detection--bd545866-663f-4d62-a39a-da3672842c9f
- **`First detected`**:
 2017-03-07T00:00:00Z
- **`Who detected`**:
   - Law Enforcement (*LE*) &mdash; Law enforcement discovered the insider's illegal activity (e.g., Police noticed that the insider was gaining access to the company after hours).
  - Security Team (*ST*) &mdash; Technical or personnnel security team discovered the insider's activity.
- **`Detected method`**:
   - Technical Means (*2*) &mdash; The insider's activity was detected via analysis or anomalies in technical systems and software.
  - Security Software (*4*) &mdash; The insider's activity was detected by security software (e.g., The insider tried to download a document with trade secrets and an automatic alert detected the download).
- **`Logs`**:
   - Access Logs (*AC*) &mdash; File or system access logs.
  - Audit Logs (*AU*) &mdash; Logs generated specifically for auditing purposes.
  - Database Logs (*DB*) &mdash; Logs from traditional or non-traditional database servers or services.
  - Remote Access Logs (*RA*) &mdash; Logs from remote access servers or clients.
  - System File Logs (*SF*) &mdash; File logs (create, delete, modify, etc.) from workstations, servers, and other systems.

## Impact

The Vault 7 leak included approximately 8,000 documents detailing CIA hacking tools and techniques.

- **`Id`**:
 impact--2d4ed800-002d-4ce5-bbb0-c89acc1f4254
- **`High`**:
 8,000
- **`Low`**:
 8,000
- **`Metric`**:
 Files (*7*) &mdash; Number of physical or digital files stolen, read, or compromised.
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
 Information (*2*) &mdash; Data/business materials which contain important details belonging to a specific target owner.
- **`Category`**:
 Government/Law Enforcement Information (*2.3*) &mdash; Classified or sensitive government or law enforcement information.
- **`Subcategory`**:
 Classified Information (*2.3.1*) &mdash; Information that is restricted by the government for reasons of national security.
- **`Format`**:
 Electronic (*1*) &mdash; Technological digital format.
- **`Owner`**:
 Organization (*O*) &mdash; The organization, rather than its employees or customers owns the target.
- **`Sensitivity`**:
   - Secret (*4*) &mdash; Public disclosure would cause serious damage to national security
  - SecretNoForn (*5*) &mdash; Secret / restricted to country of source
  - Top Secret (TS) (*6*) &mdash; Top secret, unauthorized disclosure would cause exceptionally grave damage to national security
  - TS/SCI (*7*) &mdash; Top secret / Sensitive compartmented information
- **`Description`**:
 Classified CIA information related to hacking tools and techniques disclosed to WikiLeaks as part of the Vault 7 leaks.

## Response

Schulte left the CIA in November of 2016, before departing from the agency planted a service to still allow remote access to government files and databases, which he used to access classified information post departure.

- **`Id`**:
 response--f42fc7ae-48a1-48f9-bf84-0d4b13f7a64c
- **`Technical controls`**:
   - Access to Technical System(s) Restricted (*['1', '2016-11-01']*) &mdash; Insider's access to the organization's technical systems is restricted in any capacity E.g., Organization declares that insider could only log onto system if another employee is present.
  - Access to Technical System(s) Terminated (*['2', '2016-11-01']*) &mdash; Insider's access to the organization's technical systems is completely terminated E.g., Insider's account is deleted upon termination from the company.
- **`Behavioral controls`**:
   - Terminated (*['4', '2016-11-01']*) &mdash; Insider is terminated, or fired, from the organization.
- **`Investigated by`**:
   - Law Enforcement - Federal (*4*) &mdash; Federal law enforcement entity such as the FBI or USSS.
  - Internal Investigators (*7*) &mdash; Other investigators internal to the victim organization.
- **`Investigation events`**:
   - Insider's Residence/Workplace Searched (*['1', '2017-03-07']*) &mdash; Investigators search the insider's home or workplace for evidence related to the incident.
  - Evidence Found (*['2', '2017-03-07']*) &mdash; Evidence relevant to the incident is found. E.g., Fellow employee found a USB drive left in the insider's computer that had sensitive company files downloaded on to it.
  - Insider Admits to Activity in Interview (*['3', '2018-06-18']*) &mdash; Insider admits to involvement in insider incident while being interviewed by investigators about the incident (or related activity).

## Court-case

This case involved multiple charges against Joshua Adam Schulte, including espionage and unauthorized disclosure of classified information to WikiLeaks (known as the Vault 7 leak), computer hacking, unauthorized access to CIA computer systems, causing transmission of harmful computer commands, and receipt, possession, and transportation of child pornography.

- **`Id`**:
 court-case--0e430311-72ee-4776-be74-3c1969d141c0
- **`Case number`**:
 17 Cr. 548 (PAC)
- **`Case title`**:
 USA vs. Schulte
- **`Court country`**:
 United States
- **`Court state`**:
 New York
- **`Court district`**:
 Southern District of New York
- **`Court type`**:
 Federal (*1*) &mdash; Top level government court.
- **`Case type`**:
 Criminal (*2*) &mdash; A case dealing with a violation of criminal law.
- **`Defendant`**:
   - Joshua Adam Schulte
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
 Not Guilty (*3*) &mdash; The defendant pleaed not guilty to a charge.
- **`Plea bargain`**:
 False
- **`Disposition`**:
 Convicted (*2*) &mdash; Plead or been found guilty by a court.

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
 Not Guilty (*3*) &mdash; The defendant pleaed not guilty to a charge.
- **`Plea bargain`**:
 False
- **`Disposition`**:
 Convicted (*2*) &mdash; Plead or been found guilty by a court.

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
 Not Guilty (*3*) &mdash; The defendant pleaed not guilty to a charge.
- **`Plea bargain`**:
 False
- **`Disposition`**:
 Convicted (*2*) &mdash; Plead or been found guilty by a court.

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
 Not Guilty (*3*) &mdash; The defendant pleaed not guilty to a charge.
- **`Plea bargain`**:
 False
- **`Disposition`**:
 Convicted (*2*) &mdash; Plead or been found guilty by a court.

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
 Not Guilty (*3*) &mdash; The defendant pleaed not guilty to a charge.
- **`Plea bargain`**:
 False
- **`Disposition`**:
 Convicted (*2*) &mdash; Plead or been found guilty by a court.

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
 Not Guilty (*3*) &mdash; The defendant pleaed not guilty to a charge.
- **`Plea bargain`**:
 False
- **`Disposition`**:
 Convicted (*2*) &mdash; Plead or been found guilty by a court.

## Charge

- **`Id`**:
 charge--10b415ea-7ea6-4068-b394-db1d18349b92
- **`Title`**:
 18 U.S.C.
- **`Section`**:
 2252A(a)(2)(A)
- **`Nature of offense`**:
 Receipt of child pornography.
- **`Count`**:
 1
- **`Plea`**:
 Not Guilty (*3*) &mdash; The defendant pleaed not guilty to a charge.
- **`Plea bargain`**:
 False
- **`Disposition`**:
 Convicted (*2*) &mdash; Plead or been found guilty by a court.

## Charge

- **`Id`**:
 charge--4ded5348-219f-4d74-851e-f7803b49e35e
- **`Title`**:
 18 U.S.C.
- **`Section`**:
 2252A(a)(5)(B)
- **`Nature of offense`**:
 Possession of child pornography.
- **`Count`**:
 1
- **`Plea`**:
 Not Guilty (*3*) &mdash; The defendant pleaed not guilty to a charge.
- **`Plea bargain`**:
 False
- **`Disposition`**:
 Convicted (*2*) &mdash; Plead or been found guilty by a court.

## Charge

- **`Id`**:
 charge--a919f8e3-0674-4269-bc8a-d71a539018e1
- **`Title`**:
 18 U.S.C.
- **`Section`**:
 2252A(a)(1)
- **`Nature of offense`**:
 Transportation of child pornography.
- **`Count`**:
 1
- **`Plea`**:
 Not Guilty (*3*) &mdash; The defendant pleaed not guilty to a charge.
- **`Plea bargain`**:
 False
- **`Disposition`**:
 Convicted (*2*) &mdash; Plead or been found guilty by a court.

## Sentence

- **`Id`**:
 sentence--21e74a96-ba47-46fe-8338-736ab19552ba
- **`Sentence type`**:
 Incarceration (*9*) &mdash; Imprisonment.
- **`Quantity`**:
 40
- **`Metric`**:
 Year(s) (*4*) &mdash; Imposed sentence is in terms of years. E.g. 5 years no Internet access.
- **`Concurrency`**:
 False

## Sentence

Lifetime supervised release, to run concurrently.

- **`Id`**:
 sentence--1141c372-543a-42f5-a640-c88b8ab16ae2
- **`Sentence type`**:
 Supervised Release (*16*) &mdash; Defendant is released into the community, subject to special conditions and restrictions, after the completion of a prison sentence.
- **`Quantity`**:
 60
- **`Metric`**:
 Year(s) (*4*) &mdash; Imposed sentence is in terms of years. E.g. 5 years no Internet access.
- **`Concurrency`**:
 True

## Legal-response

Joshua Adam Schulte was investigated and charged for multiple offenses, including espionage, unauthorized disclosure of classified information (Vault 7 leaks), computer hacking, and possession of child pornography. The judgment date is in relation to the charges specifically related to the dissemination of the Stolen CIA Files.

- **`Id`**:
 legal-response--b318c37b-2f76-421f-bf12-0833e836b00c
- **`Law enforcement contacted`**:
 2017-03-07
- **`Insider arrested`**:
 2017-08-24
- **`Insider charged`**:
 2018-06
- **`Insider pleads`**:
 2018-06
- **`Insider judgment`**:
 2022-07-13
- **`Insider sentenced`**:
 2024-02-01

## Job

Schulte was employed as a software engineer in the Center for Cyber Intelligence (CCI) at the CIA, where he had access to sensitive and classified information.

- **`Id`**:
 job--e76248a2-82df-4c7d-b7a0-bf86eb85c570
- **`Job function`**:
 Computer and Mathematical (*15*) &mdash; Computer and Mathematical
- **`Occupation`**:
 Computer Occupations (*15.1*) &mdash; Computer Systems Analysts, Information Security Analysts, Network Support Specialists, User Support Specialists, Network Architects, Systems Administrators, Software Developers, Web Developers, Interface Designers, Etc.
- **`Title`**:
 Software Engineer
- **`Position technical`**:
 True
- **`Access authorization`**:
 Administrator/Root (*2*) &mdash; Authorized full administrative access.
- **`Employment type`**:
 Full-time (*FLT*) &mdash; Individual who is directly employed by the organization and works at least 35 hours per week (or is classified by the organization as a full-time employee).
- **`Hire date`**:
 2010-01-01
- **`Departure date`**:
 2016-11-11
- **`Tenure`**:
 P6Y10M10D

## Stressor

Joshua Adam Schulte internal disputes and a hostile work environment at the CIA (self-imposed) contributed to his decision to steal and leak classified information as revenge for mistreatment.

- **`Id`**:
 stressor--28ecfbf3-5eb1-429f-8a55-c2e16f08ebcd
- **`Date`**:
 2016
- **`Category`**:
 Organizational Issues (*2*) &mdash; The insider's employer had problems or changes that directly or indirectly affected the insider.
- **`Subcategory`**:
 Hostile Work Environment (*2.12*) &mdash; A work environment that is difficult or uncomfortable for another person to work in due to discrimination of any kind.

## Ttp

- **`Id`**:
 ttp--a181e814-aa3a-411e-ae79-79ceba48e36a
- **`Date`**:
 2016-04-20T14:00:00Z
- **`Sequence num`**:
 1
- **`Observed`**:
 True
- **`Number of times`**:
 2
- **`Ttp vocab`**:
 IIDES
- **`Tactic`**:
 Data Exfiltration (*7*) &mdash; Data (or copies of data) is removed from the organization without permission or explicitly against permission to use in an unauthorized way.
- **`Technique`**:
 Email (*7.3*) &mdash; Insider exfiltrates data through electronic mail (e.g., Insider e-mailed confidential information to competitor).
- **`Location`**:
   - On-site (*1*) &mdash; Action taken while on-site at an organizational facility.
- **`Hours`**:
   - During Work Hours (*1*) &mdash; Insider took the action during their normal working hours.
- **`Device`**:
   - Company Desktop (*1*) &mdash; Organization owned desktop workstation.
- **`Channel`**:
   - Company Email (*1*) &mdash; An email account the company controls.
  - Online Forum (*4*) &mdash; Private or public forum accessed via the Internet.
  - Personal Email (*5*) &mdash; An email account the organization does not control or monitor.
- **`Description`**:
 Schulte used a personal email account to exfiltrate classified CIA information from the organization's database server to his personal computer.

## Ttp

- **`Id`**:
 ttp--a154e814-aa3a-411e-ae79-79ceba48e79b
- **`Date`**:
 2016-04-20T14:00:00Z
- **`Sequence num`**:
 2
- **`Observed`**:
 True
- **`Number of times`**:
 1
- **`Ttp vocab`**:
 IIDES
- **`Tactic`**:
 Data Exfiltration (*7*) &mdash; Data (or copies of data) is removed from the organization without permission or explicitly against permission to use in an unauthorized way.
- **`Technique`**:
 Removable Media (*7.2*) &mdash; Insider exfiltrates data through digital equipment or media (e.g., Insider had trade secrets owned by the victim organization on a flash drive and sent the flash drive to the competitor to be copied).
- **`Location`**:
   - Remotely (*2*) &mdash; Action taken while remote (i.e. not at an organizational facility).
- **`Hours`**:
   - Outside of Work Hours (*2*) &mdash; Insider took the action outside of their normal working hours.
- **`Device`**:
   - Personal Computer (*7*) &mdash; Personally owned computer.
- **`Channel`**:
   - Other (*9*) &mdash; Other type of channel not listed in this vocabulary.
- **`Description`**:
 Schulte then loaded the data on a removable media disk

## Ttp

- **`Id`**:
 ttp--a154e814-aa3a-411e-ae79-79ceba48e77b
- **`Date`**:
 2016-04-20T14:00:00Z
- **`Sequence num`**:
 2
- **`Observed`**:
 True
- **`Number of times`**:
 2
- **`Ttp vocab`**:
 IIDES
- **`Tactic`**:
 Malware (*4*) &mdash; Malicious software is used.
- **`Technique`**:
 Backdoor (*4.1*) &mdash; A malicious program that allows an attacker to perform actions on a remote system, such as transferring files, acquiring passwords, or executing arbitrary commands.
- **`Location`**:
   - On-site (*1*) &mdash; Action taken while on-site at an organizational facility.
- **`Hours`**:
   - During Work Hours (*1*) &mdash; Insider took the action during their normal working hours.
- **`Device`**:
   - Company Desktop (*1*) &mdash; Organization owned desktop workstation.
- **`Channel`**:
   - Other (*9*) &mdash; Other type of channel not listed in this vocabulary.
- **`Description`**:
 Before leaving the CIA, Schulte planted a backdoor into the CIA network

## Ttp

- **`Id`**:
 ttp--a154e814-aa3a-411e-ae79-79ceba48e76b
- **`Date`**:
 2016-04-20T14:00:00Z
- **`Sequence num`**:
 3
- **`Observed`**:
 True
- **`Number of times`**:
 1
- **`Ttp vocab`**:
 IIDES
- **`Tactic`**:
 Data Exfiltration (*7*) &mdash; Data (or copies of data) is removed from the organization without permission or explicitly against permission to use in an unauthorized way.
- **`Technique`**:
 Other Technical/Digital (*7.9*) &mdash; Insider exfiltrates data using other technical or digital means not listed in this vocabulary.
- **`Location`**:
   - Remotely (*2*) &mdash; Action taken while remote (i.e. not at an organizational facility).
- **`Hours`**:
   - Outside of Work Hours (*2*) &mdash; Insider took the action outside of their normal working hours.
- **`Device`**:
   - Database Server (*4*) &mdash; Database server.
- **`Channel`**:
   - Company Email (*1*) &mdash; An email account the company controls.
  - Personal Email (*5*) &mdash; An email account the organization does not control or monitor.
  - Other (*9*) &mdash; Other type of channel not listed in this vocabulary.
- **`Description`**:
 After leaving the CIA, Schulte hosted a server on the CIA's network to continue accessing and exfiltrating classified data.

## Note

The child pornography charges were included in the JSON because they are relevant to the overall investigation of Joshua Adam Schulte. Although they do not directly pertain to the insider threat, they were pivotal in leading to his initial arrest and subsequent comprehensive charges.

- **`Id`**:
 note--b372b9ad-cb92-4db6-be28-1e3f62605858
- **`Author`**:
 CMU Researcher
- **`Date`**:
 2024-05-17T00:00:00Z

## Source

- **`Id`**:
 source--5565e706-d762-4b35-b54a-6f22a80badb2
- **`Title`**:
 Joshua Adam Schulte Charged with Unauthorized Disclosure of Classified Information and Other Offenses
- **`Source type`**:
 DOJ Press Release (*2*) &mdash; Press release from the Department of Justice or US Attorneys' Office.
- **`File type`**:
 HTML File (*html*) &mdash; A file in HTML format.
- **`Date`**:
 2018-06-18T00:00:00Z
- **`Public`**:
 True
- **`Document`**:
 https://www.justice.gov/opa/pr/joshua-adam-schulte-charged-unauthorized-disclosure-classified-information-and-other-offenses

## Source

- **`Id`**:
 source--d6a29cb3-519f-4d62-a1f6-a86439bef53d
- **`Title`**:
 Former CIA Officer Joshua Adam Schulte Sentenced to 40 Years in Prison for Espionage and Child Pornography Offenses
- **`Source type`**:
 DOJ Press Release (*2*) &mdash; Press release from the Department of Justice or US Attorneys' Office.
- **`File type`**:
 HTML File (*html*) &mdash; A file in HTML format.
- **`Date`**:
 2023-01-18T00:00:00Z
- **`Public`**:
 True
- **`Document`**:
 https://www.justice.gov/usao-sdny/pr/former-cia-officer-joshua-adam-schulte-sentenced-40-years-prison-espionage-and-child

## Source

- **`Id`**:
 source--7e3ef93e-31b0-4e17-a32a-98540326fd05
- **`Title`**:
 CIA Engineer Convicted of Largest Theft of Classified Data in Agency’s History
- **`Source type`**:
 Media (*5*) &mdash; News, blog, or similar publication.
- **`File type`**:
 HTML File (*html*) &mdash; A file in HTML format.
- **`Date`**:
 2022-07-13T00:00:00Z
- **`Public`**:
 True
- **`Document`**:
 https://www.nytimes.com/2022/07/13/nyregion/cia-engineer-joshua-schulte-theft-convicted.html

## Source

- **`Id`**:
 source--d36603a3-2510-4617-87eb-10eea6ab672e
- **`Title`**:
 USA v. Schulte Docket Information
- **`Source type`**:
 Court Document (*1*) &mdash; Legal document from a court case.
- **`File type`**:
 HTML File (*html*) &mdash; A file in HTML format.
- **`Date`**:
 2022-07-13T00:00:00Z
- **`Public`**:
 True
- **`Document`**:
 https://www.courtlistener.com/docket/6359557/united-states-v-schulte/
