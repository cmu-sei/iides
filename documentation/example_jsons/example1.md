# Example1

## Incident

The leak severely impacted the confidentiality and integrity of CIA operations, exposing sensitive information and tools used for intelligence gathering.

- **`Cia effect`**:
   - *C*: Confidentiality - The protection of information from unauthorized access or disclosure.

- **`Incident type`**:
   - *E*: Espionage - The covert or illicit practice of spying on a foreign government, organization, entity, or person to obtain confidential information for military, political, strategic, or financial advantage.

- **`Incident subtype`**:
   - *E2*: Government - Covert intelligence-gathering activities to obtain government or military secrets for the benefit of another government to obtain political or military advantage.

- **`Outcome`**:
   - *DD*: Data Deleted - Data was deleted from the victim organization's systems.
  - *ML*: Monetary Losses - Indirect loss of money through damage, detriment, or suffering related to the incident.
  - *SI*: Safety Impact - There was an impact, or potential for impact to safety, as a result of the incident.
  - *DR*: Data Read - Organizational data was read by the insider.
  - *DS*: Data Stolen - Any organizational information or assets that are stolen.

- **`Status`**:
   - *C*: Closed - All investigations and legal proceedings are closed.
- **`Summary`**:
   - Joshua Adam Schulte, a former CIA software engineer, leaked classified CIA documents known as Vault 7 to WikiLeaks. These documents detailed the CIA's hacking tools and techniques, causing severe damage to U.S. national security, exposing CIA operations and personnel, and costing the agency hundreds of millions of dollars. Schulte was charged with espionage, unauthorized access to computer systems, and other related crimes. He was convicted and sentenced to 40 years in prison.
- **`Brief summary`**:
   - Joshua Adam Schulte leaked classified CIA documents to WikiLeaks, detailing CIA hacking tools and techniques. This caused severe national security damage and financial costs. Schulte was convicted of espionage and sentenced to 40 years in prison.
## Insider

Joshua Adam Schulte had a history of social and mental health issues. He showed concerning behaviors such as repeated technical policy abuse and conflicts with his supervisor, as well as browsing dark web forums. The insider had multiple workplace incidents involving the harassment of colleagues, ultimately resulting in the insider being forced to move offices across the building. The insider believed he had been mistreated by staff, leading to a desire for revenge.

- **`Incident role`**:
   - *1*: Primary - Insider is the primary perpetrator of the incident.
- **`Motive`**:
   - *8*: Revenge - The insider wanted revenge for an actual or perceived wrong.

- **`Predispositions`**:
   - *['1', '1.1']*: Social and Mental Health Issues - A history of behaviors related to the insider's mental health or unacceptable social behavior.
  - *['2', '2.4']*: A History of Rule Violations - A history of violating the law or violating rules at other organizations.
  - *['3', '3.2']*: Suspicious Associations - A history of associating with criminal or otherwise objectionable persons or entities.

- **`Concerning behaviors`**:
   - *['3.2', '3.2.2']*: Technical Policy Abuse - Violating policies regarding the use of the organization's IT systems.
  - *['3.3', '3.3.2']*: Interpersonal Issues - Conflicts with others in the organization or human resources (HR) issues.

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

- **`Name`**:
   - Central Intelligence Agency
- **`City`**:
   - Langley
- **`State`**:
   - Virginia
- **`Country`**:
   - US
- **`Postal code`**:
 22,101
- **`Small business`**:
 False
- **`Industry sector`**:
   - *92*: Public Administration - Federal/State/Local administration and the oversight of public programs.
- **`Industry subsector`**:
   - *92.811*: National Security - This industry comprises government establishments of the Armed Forces, including the National Guard, primarily engaged in national security and related activities.
- **`Business`**:
   - The Central Intelligence Agency (CIA) is a civilian foreign intelligence service of the federal government of the United States, tasked with gathering, processing, and analyzing national security information from around the world.
- **`Incident role`**:
   - *V*: Primary Victim - The organization was the primary victim organization of the insider's actions.
- **`Parent company`**:
   - United States Government
## Organization

- **`Name`**:
   - WikiLeaks
- **`Small business`**:
 False
- **`Industry sector`**:
   - *51*: Information - Hardware or software systems related to the processing, communications, and accessing of information.
- **`Industry subsector`**:
   - *51.9*: Web Search Portals, Libraries, Archives, and Other Information Services - Industries in the Web Search Portals, Libraries, Archives, and Other Information Services subsector group establishments supplying information, storing and providing access to information, searching and retrieving information, and operating Web sites that use search engines to allow for searching information on the Internet. The main components of the subsector are libraries, archives, and Web search portals.
- **`Business`**:
   - WikiLeaks is a non-profit organization that publishes news leaks and classified media provided by anonymous sources.
- **`Incident role`**:
   - *B*: Beneficiary - The organization accepted trade secrets, customer lists, intellectual property, etc. that the insider obtained through the incident.
## Detection

Schulte's unauthorized activities were detected by the CIA's security team and subsequently investigated by law enforcement. Detection involved technical means such as monitoring access logs, audit logs, database logs, remote access logs, and system file logs.

- **`First detected`**:
   - 2017-03-07T00:00:00Z
- **`Who detected`**:
   - *LE*: Law Enforcement - Law enforcement discovered the insider's illegal activity (e.g., Police noticed that the insider was gaining access to the company after hours).
  - *ST*: Security Team - Technical or personnnel security team discovered the insider's activity.

- **`Detected method`**:
   - *2*: Technical Means - The insider's activity was detected via analysis or anomalies in technical systems and software.
  - *4*: Security Software - The insider's activity was detected by security software (e.g., The insider tried to download a document with trade secrets and an automatic alert detected the download).

- **`Logs`**:
   - *AC*: Access Logs - File or system access logs.
  - *AU*: Audit Logs - Logs generated specifically for auditing purposes.
  - *DB*: Database Logs - Logs from traditional or non-traditional database servers or services.
  - *RA*: Remote Access Logs - Logs from remote access servers or clients.
  - *SF*: System File Logs - File logs (create, delete, modify, etc.) from workstations, servers, and other systems.

## Impact

The Vault 7 leak included approximately 8,000 documents detailing CIA hacking tools and techniques.

- **`High`**:
 8,000
- **`Low`**:
 8,000
- **`Metric`**:
   - *7*: Files - Number of physical or digital files stolen, read, or compromised.
- **`Estimated`**:
 True
## Impact

The financial impact of the breach was substantial, with estimates ranging from hundreds of millions to a billion dollars for damage control and security improvements.

- **`High`**:
 1,000,000,000
- **`Low`**:
 100,000,000
- **`Metric`**:
   - *5*: Dollars - Specific financial impact of money stolen, restitution ordered, etc.
- **`Estimated`**:
 True
## Target

- **`Asset type`**:
   - *2*: Information - Data/business materials which contain important details belonging to a specific target owner.
- **`Category`**:
   - *2.3*: Government/Law Enforcement Information - Classified or sensitive government or law enforcement information.
- **`Subcategory`**:
   - *2.3.1*: Classified Information - Information that is restricted by the government for reasons of national security.
- **`Format`**:
   - *1*: Electronic - Technological digital format.
- **`Owner`**:
   - *O*: Organization - The organization, rather than its employees or customers owns the target.
- **`Sensitivity`**:
   - *4*: Secret - Public disclosure would cause serious damage to national security
  - *5*: SecretNoForn - Secret / restricted to country of source
  - *6*: Top Secret (TS) - Top secret, unauthorized disclosure would cause exceptionally grave damage to national security
  - *7*: TS/SCI - Top secret / Sensitive compartmented information

- **`Description`**:
   - Classified CIA information related to hacking tools and techniques disclosed to WikiLeaks as part of the Vault 7 leaks.
## Response

Schulte left the CIA in November of 2016, before departing from the agency planted a service to still allow remote access to government files and databases, which he used to access classified information post departure.

- **`Technical controls`**:
   - *['1', '2016-11-01']*: Access to Technical System(s) Restricted - Insider's access to the organization's technical systems is restricted in any capacity E.g., Organization declares that insider could only log onto system if another employee is present.
  - *['2', '2016-11-01']*: Access to Technical System(s) Terminated - Insider's access to the organization's technical systems is completely terminated E.g., Insider's account is deleted upon termination from the company.

- **`Behavioral controls`**:
   - *['4', '2016-11-01']*: Terminated - Insider is terminated, or fired, from the organization.

- **`Investigated by`**:
   - *4*: Law Enforcement - Federal - Federal law enforcement entity such as the FBI or USSS.
  - *7*: Internal Investigators - Other investigators internal to the victim organization.

- **`Investigation events`**:
   - *['1', '2017-03-07']*: Insider's Residence/Workplace Searched - Investigators search the insider's home or workplace for evidence related to the incident.
  - *['2', '2017-03-07']*: Evidence Found - Evidence relevant to the incident is found. E.g., Fellow employee found a USB drive left in the insider's computer that had sensitive company files downloaded on to it.
  - *['3', '2018-06-18']*: Insider Admits to Activity in Interview - Insider admits to involvement in insider incident while being interviewed by investigators about the incident (or related activity).

## Court-case

This case involved multiple charges against Joshua Adam Schulte, including espionage and unauthorized disclosure of classified information to WikiLeaks (known as the Vault 7 leak), computer hacking, unauthorized access to CIA computer systems, causing transmission of harmful computer commands, and receipt, possession, and transportation of child pornography.

- **`Case number`**:
   - 17 Cr. 548 (PAC)
- **`Case title`**:
   - USA vs. Schulte
- **`Court country`**:
   - *United States*: 
- **`Court state`**:
   - *New York*: 
- **`Court district`**:
   - Southern District of New York
- **`Court type`**:
   - *1*: Federal - Top level government court.
- **`Case type`**:
   - *2*: Criminal - A case dealing with a violation of criminal law.
- **`Defendant`**:
   - Joshua Adam Schulte

- **`Plaintiff`**:
   - United States of America

## Charge

- **`Title`**:
   - 18 U.S.C.
- **`Section`**:
   - 793(e)
- **`Nature of offense`**:
   - Illegal gathering and transmission of national defense information.
- **`Count`**:
 3
- **`Plea`**:
   - *3*: Not Guilty - The defendant pleaed not guilty to a charge.
- **`Plea bargain`**:
 False
- **`Disposition`**:
   - *2*: Convicted - Plead or been found guilty by a court.
## Charge

- **`Title`**:
   - 18 U.S.C.
- **`Section`**:
   - 641
- **`Nature of offense`**:
   - Theft of government property.
- **`Count`**:
 1
- **`Plea`**:
   - *3*: Not Guilty - The defendant pleaed not guilty to a charge.
- **`Plea bargain`**:
 False
- **`Disposition`**:
   - *2*: Convicted - Plead or been found guilty by a court.
## Charge

- **`Title`**:
   - 18 U.S.C.
- **`Section`**:
   - 1030(a)(1)
- **`Nature of offense`**:
   - Unauthorized access to a computer to obtain classified information.
- **`Count`**:
 1
- **`Plea`**:
   - *3*: Not Guilty - The defendant pleaed not guilty to a charge.
- **`Plea bargain`**:
 False
- **`Disposition`**:
   - *2*: Convicted - Plead or been found guilty by a court.
## Charge

- **`Title`**:
   - 18 U.S.C.
- **`Section`**:
   - 1030(a)(2)
- **`Nature of offense`**:
   - Unauthorized access to a computer to obtain information from a department or agency of the U.S.
- **`Count`**:
 1
- **`Plea`**:
   - *3*: Not Guilty - The defendant pleaed not guilty to a charge.
- **`Plea bargain`**:
 False
- **`Disposition`**:
   - *2*: Convicted - Plead or been found guilty by a court.
## Charge

- **`Title`**:
   - 18 U.S.C.
- **`Section`**:
   - 1030(a)(5)(A)
- **`Nature of offense`**:
   - Causing transmission of harmful computer commands.
- **`Count`**:
 1
- **`Plea`**:
   - *3*: Not Guilty - The defendant pleaed not guilty to a charge.
- **`Plea bargain`**:
 False
- **`Disposition`**:
   - *2*: Convicted - Plead or been found guilty by a court.
## Charge

- **`Title`**:
   - 18 U.S.C.
- **`Section`**:
   - 1519
- **`Nature of offense`**:
   - Obstruction of justice.
- **`Count`**:
 1
- **`Plea`**:
   - *3*: Not Guilty - The defendant pleaed not guilty to a charge.
- **`Plea bargain`**:
 False
- **`Disposition`**:
   - *2*: Convicted - Plead or been found guilty by a court.
## Charge

- **`Title`**:
   - 18 U.S.C.
- **`Section`**:
   - 2252A(a)(2)(A)
- **`Nature of offense`**:
   - Receipt of child pornography.
- **`Count`**:
 1
- **`Plea`**:
   - *3*: Not Guilty - The defendant pleaed not guilty to a charge.
- **`Plea bargain`**:
 False
- **`Disposition`**:
   - *2*: Convicted - Plead or been found guilty by a court.
## Charge

- **`Title`**:
   - 18 U.S.C.
- **`Section`**:
   - 2252A(a)(5)(B)
- **`Nature of offense`**:
   - Possession of child pornography.
- **`Count`**:
 1
- **`Plea`**:
   - *3*: Not Guilty - The defendant pleaed not guilty to a charge.
- **`Plea bargain`**:
 False
- **`Disposition`**:
   - *2*: Convicted - Plead or been found guilty by a court.
## Charge

- **`Title`**:
   - 18 U.S.C.
- **`Section`**:
   - 2252A(a)(1)
- **`Nature of offense`**:
   - Transportation of child pornography.
- **`Count`**:
 1
- **`Plea`**:
   - *3*: Not Guilty - The defendant pleaed not guilty to a charge.
- **`Plea bargain`**:
 False
- **`Disposition`**:
   - *2*: Convicted - Plead or been found guilty by a court.
## Sentence

- **`Sentence type`**:
   - *9*: Incarceration - Imprisonment.
- **`Quantity`**:
 40
- **`Metric`**:
   - *4*: Year(s) - Imposed sentence is in terms of years. E.g. 5 years no Internet access.
- **`Concurrency`**:
 False
## Sentence

Lifetime supervised release, to run concurrently.

- **`Sentence type`**:
   - *16*: Supervised Release - Defendant is released into the community, subject to special conditions and restrictions, after the completion of a prison sentence.
- **`Quantity`**:
 60
- **`Metric`**:
   - *4*: Year(s) - Imposed sentence is in terms of years. E.g. 5 years no Internet access.
- **`Concurrency`**:
 True
## Legal-response

Joshua Adam Schulte was investigated and charged for multiple offenses, including espionage, unauthorized disclosure of classified information (Vault 7 leaks), computer hacking, and possession of child pornography. The judgement date is in relation to the charges specifically related to the dissemination of the Stolen CIA Files.

- **`Law enforcement contacted`**:
   - 2017-03-07
- **`Insider arrested`**:
   - 2017-08-24
- **`Insider charged`**:
   - 2018-06
- **`Insider pleads`**:
   - 2018-06
- **`Insider judgment`**:
 2022-07-13
- **`Insider sentenced`**:
   - 2024-02-01
## Job

Schulte was employed as a software engineer in the Center for Cyber Intelligence (CCI) at the CIA, where he had access to sensitive and classified information.

- **`Job function`**:
   - *15*: Computer and Mathematical - Computer and Mathematical
- **`Occupation`**:
   - *15.1*: Computer Occupations - Computer Systems Analysts, Information Security Analysts, Network Support Specialists, User Support Specialists, Network Architects, Systems Administrators, Software Developers, Web Developers, Interface Designers, Etc.
- **`Title`**:
   - Software Engineer
- **`Position technical`**:
 True
- **`Access authorization`**:
   - *2*: Administrator/Root - Authorized full administrative access.
- **`Employment type`**:
   - *FLT*: Full-time - Individual who is directly employed by the organization and works at least 35 hours per week (or is classified by the organization as a full-time employee).
- **`Hire date`**:
   - 2010-01-01
- **`Departure date`**:
   - 2016-11-11
- **`Tenure`**:
   - P6Y10M10D
## Stressor

Joshua Adam Schulte internal disputes and a hostile work environment at the CIA (self-imposed) contributed to his decision to steal and leak classified information as revenge for mistreatment.

- **`Date`**:
   - 2016
- **`Category`**:
   - *2*: Organizational Issues - The insider's employer had problems or changes that directly or indirectly affected the insider.
- **`Subcategory`**:
   - *2.12*: Hostile Work Environment - A work environment that is difficult or uncomfortable for another person to work in due to discrimination of any kind.
## Ttp

- **`Date`**:
   - 2016-04-20T14:00:00Z
- **`Sequence num`**:
 1
- **`Observed`**:
 True
- **`Number of times`**:
 2
- **`Ttp vocab`**:
   - IIDES
- **`Tactic`**:
   - *7*: Data Exfiltration - Data (or copies of data) is removed from the organization without permission or explicitly against permission to use in an unauthorized way.
- **`Technique`**:
   - *7.3*: Email - Insider exfiltrates data through electronic mail (e.g., Insider e-mailed confidential information to competitor).
- **`Location`**:
   - *1*: On-site - Action taken while on-site at an organizational facility.

- **`Hours`**:
   - *1*: During Work Hours - Insider took the action during their normal working hours.

- **`Device`**:
   - *1*: Company Desktop - Organization owned desktop workstation.

- **`Channel`**:
   - *1*: Company Email - An email account the company controls.
  - *4*: Online Forum - Private or public forum accessed via the Internet.
  - *5*: Personal Email - An email account the organization does not control or monitor.

- **`Description`**:
   - Schulte used a personal email account to exfiltrate classified CIA information from the organization's database server to his personal computer.
## Ttp

- **`Date`**:
   - 2016-04-20T14:00:00Z
- **`Sequence num`**:
 2
- **`Observed`**:
 True
- **`Number of times`**:
 1
- **`Ttp vocab`**:
   - IIDES
- **`Tactic`**:
   - *7*: Data Exfiltration - Data (or copies of data) is removed from the organization without permission or explicitly against permission to use in an unauthorized way.
- **`Technique`**:
   - *7.2*: Removable Media - Insider exfiltrates data through digital equipment or media (e.g., Insider had trade secrets owned by the victim organization on a flash drive and sent the flash drive to the competitor to be copied).
- **`Location`**:
   - *2*: Remotely - Action taken while remote (i.e. not at an organizational facility).

- **`Hours`**:
   - *2*: Outside of Work Hours - Insider took the action outside of their normal working hours.

- **`Device`**:
   - *7*: Personal Computer - Personally owned computer.

- **`Channel`**:
   - *9*: Other - Other type of channel not listed in this vocabulary.

- **`Description`**:
   - Schulte then loaded the data on a removable media disk
## Ttp

- **`Date`**:
   - 2016-04-20T14:00:00Z
- **`Sequence num`**:
 2
- **`Observed`**:
 True
- **`Number of times`**:
 2
- **`Ttp vocab`**:
   - IIDES
- **`Tactic`**:
   - *4*: Malware - Malicious software is used.
- **`Technique`**:
   - *4.1*: Backdoor - A malicious program that allows an attacker to perform actions on a remote system, such as transferring files, acquiring passwords, or executing arbitrary commands.
- **`Location`**:
   - *1*: On-site - Action taken while on-site at an organizational facility.

- **`Hours`**:
   - *1*: During Work Hours - Insider took the action during their normal working hours.

- **`Device`**:
   - *1*: Company Desktop - Organization owned desktop workstation.

- **`Channel`**:
   - *9*: Other - Other type of channel not listed in this vocabulary.

- **`Description`**:
   - Before leaving the CIA, Schulte planted a backdoor into the CIA network
## Ttp

- **`Date`**:
   - 2016-04-20T14:00:00Z
- **`Sequence num`**:
 3
- **`Observed`**:
 True
- **`Number of times`**:
 1
- **`Ttp vocab`**:
   - IIDES
- **`Tactic`**:
   - *7*: Data Exfiltration - Data (or copies of data) is removed from the organization without permission or explicitly against permission to use in an unauthorized way.
- **`Technique`**:
   - *7.9*: Other Technical/Digital - Insider exfiltrates data using other technical or digital means not listed in this vocabulary.
- **`Location`**:
   - *2*: Remotely - Action taken while remote (i.e. not at an organizational facility).

- **`Hours`**:
   - *2*: Outside of Work Hours - Insider took the action outside of their normal working hours.

- **`Device`**:
   - *4*: Database Server - Database server.

- **`Channel`**:
   - *1*: Company Email - An email account the company controls.
  - *5*: Personal Email - An email account the organization does not control or monitor.
  - *9*: Other - Other type of channel not listed in this vocabulary.

- **`Description`**:
   - After leaving the CIA, Schulte hosted a server on the CIA's network to continue accessing and exfiltrating classified data.
## Note

The child pornography charges were included in the JSON because they are relevant to the overall investigation of Joshua Adam Schulte. Although they do not directly pertain to the insider threat, they were pivotal in leading to his initial arrest and subsequent comprehensive charges.

- **`Author`**:
   - CMU Researcher
- **`Date`**:
   - 2024-05-17T00:00:00Z
## Source

- **`Title`**:
   - Joshua Adam Schulte Charged with Unauthorized Disclosure of Classified Information and Other Offenses
- **`Source type`**:
   - *2*: DOJ Press Release - Press release from the Department of Justice or US Attorneys' Office.
- **`File type`**:
   - *html*: 
- **`Date`**:
   - 2018-06-18T00:00:00Z
- **`Public`**:
 True
- **`Document`**:
   - https://www.justice.gov/opa/pr/joshua-adam-schulte-charged-unauthorized-disclosure-classified-information-and-other-offenses
## Source

- **`Title`**:
   - Former CIA Officer Joshua Adam Schulte Sentenced to 40 Years in Prison for Espionage and Child Pornography Offenses
- **`Source type`**:
   - *2*: DOJ Press Release - Press release from the Department of Justice or US Attorneys' Office.
- **`File type`**:
   - *html*: 
- **`Date`**:
   - 2023-01-18T00:00:00Z
- **`Public`**:
 True
- **`Document`**:
   - https://www.justice.gov/usao-sdny/pr/former-cia-officer-joshua-adam-schulte-sentenced-40-years-prison-espionage-and-child
## Source

- **`Title`**:
   - CIA Engineer Convicted of Largest Theft of Classified Data in Agency’s History
- **`Source type`**:
   - *5*: Media - News, blog, or similar publication.
- **`File type`**:
   - *html*: 
- **`Date`**:
   - 2022-07-13T00:00:00Z
- **`Public`**:
 True
- **`Document`**:
   - https://www.nytimes.com/2022/07/13/nyregion/cia-engineer-joshua-schulte-theft-convicted.html
## Source

- **`Title`**:
   - USA v. Schulte Docket Information
- **`Source type`**:
   - *1*: Court Document - Legal document from a court case.
- **`File type`**:
   - *html*: 
- **`Date`**:
   - 2022-07-13T00:00:00Z
- **`Public`**:
 True
- **`Document`**:
   - https://www.courtlistener.com/docket/6359557/united-states-v-schulte/
