# Example3


## Incident

The case was settled out of court, and no formal determination of guilt was made against Tech Solutions, but they agreed to a settlement to avoid the continuation of litigation.

- **`Id`**:
 incident--6e75f650-c1a5-4c71-8d2f-7e9d2bba0381
- **`Cia effect`**:
   - Confidentiality (*C*) &mdash; The protection of information from unauthorized access or disclosure
  - Integrity (*I*) &mdash; The protection of information from unauthorized modification or destruction
- **`Incident type`**:
   - Espionage (*E*) &mdash; The covert or illicit practice of spying on a foreign government, organization, entity, or person to obtain confidential information for military, political, strategic, or financial advantage
- **`Incident subtype`**:
   - Intellectual Property Theft (*E.1*) &mdash; Theft or robbery of an individual's or organization's ideas, inventions, or creative expressions, including trade secrets and proprietary products, even if the concepts or items being stolen originated from the insider
- **`Outcome`**:
   - Data Stolen (*DS*) &mdash; Any organizational information or assets that are stolen
  - Monetary Losses (*ML*) &mdash; Indirect loss of money through damage, detriment, or suffering related to the incident
- **`Status`**:
 Closed (*C*) &mdash; All investigations and legal proceedings are closed
- **`Summary`**:
 The case involved Alpha Innovations, a software development company, accusing Tech Solutions, through its acquisition of Zingerman's startup, of stealing trade secrets related to software algorithms. The lawsuit claimed that Mark Zingerman, a former engineer at Alpha Innovations, downloaded thousands of files related to Alpha Innovations' proprietary software before leaving to start his own company, which was soon acquired by Tech Solutions.
- **`Brief summary`**:
 Alpha Innovations sued Tech Solutions for intellectual property theft, claiming that ex-engineer Mark Zingerman stole software technology secrets before joining Tech Solutions. The case was settled with Tech Solutions agreeing to not use Alpha Innovations' technology and paying equity worth approximately $150 million.

## Insider

Mark Zingerman's actions of transferring confidential files from Alpha Innovations to his personal devices sparked the lawsuit. No public evidence of substance use or psychological issues affecting his actions has been documented.

- **`Id`**:
 insider--2fe80494-c7cf-4d75-85ef-736b55884664
- **`Incident role`**:
 Primary (*1*) &mdash; Insider is the primary perpetrator of the incident
- **`Motive`**:
   - Competitive Business Advantage (*3*) &mdash; Insider committed their attack in order to gain a business advantage for a competing company. Often, this is the insider starting their own company
  - Financial Gain (*5*) &mdash; Insider committed their attack to make a profit
- **`Substance use during incident`**:
 False
- **`first_name`**:
 Mark
- **`last_name`**:
 Zingerman
- **`alias`**:
 ['Matt Zinger', 'John Doe']
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
 8
- **`marital_status`**:
 2
- **`number_of_children`**:
 2
- **`Concerning behaviors`**:
   - Technical Policy Abuse (*['2', '2.4']*) &mdash; Violating policies regarding the use of the organization's IT systems
  - Technical Policy Abuse (*['2', '2.3']*) &mdash; Violating policies regarding the use of the organization's IT systems
  - Organizational Conflict (*['5', '5.1']*) &mdash; Competitive conflicts of interest with the organization
  - Organizational Conflict (*['5', '5.2']*) &mdash; Competitive conflicts of interest with the organization

## Organization

- **`Id`**:
 organization--8ed0c400-fa6a-4bd6-babe-4da40240442d
- **`Name`**:
 Alpha Innovations LLC
- **`City`**:
 New York
- **`State`**:
 New York
- **`Country`**:
 USA
- **`Postal code`**:
 10001
- **`Small business`**:
 False
- **`Industry sector`**:
 Transportation and Warehousing (*48*) &mdash; Services directly or indirectly involved in the movement of people.
- **`Industry subsector`**:
 Transit and Ground Passenger Transportation (*48.5*) &mdash; This subsector includes industries providing passenger transportation, such as buses and taxis.
- **`Business`**:
 Alpha Innovations operates as a software development company primarily involved in developing proprietary software systems.
- **`Parent company`**:
 Tech Giant Inc.
- **`Incident role`**:
 Primary Victim (*V*) &mdash; The organization was the primary victim organization of the insider's actions.

## Organization

- **`Id`**:
 organization--e7fda876-f31b-45a5-a540-7bb514ccecee
- **`Name`**:
 Tech Solutions Inc.
- **`City`**:
 San Francisco
- **`State`**:
 California
- **`Country`**:
 USA
- **`Postal code`**:
 94103
- **`Small business`**:
 False
- **`Industry sector`**:
 Transportation and Warehousing (*48*) &mdash; Services directly or indirectly involved in the movement of people.
- **`Industry subsector`**:
 Transit and Ground Passenger Transportation (*48.5*) &mdash; This subsector includes industries providing passenger transportation, such as buses and taxis.
- **`Business`**:
 Tech Solutions operates as a technology company offering various software and IT services globally, with a division focused on developing proprietary software technology.
- **`Incident role`**:
 Beneficiary (*B*) &mdash; The organization accepted trade secrets, customer lists, intellectual property, etc. that the insider obtained through the incident.

## Detection

- **`Id`**:
 detection--a181e814-aa3a-411e-ae79-79ceba48e36a
- **`First detected`**:
 2001-02-23
- **`Who detected`**:
   - Law Enforcement (*LE*) &mdash; Law enforcement discovered the insider's illegal activity (e.g., police noticed that the insider was gaining access to the company after hours)
  - Organization (*OR*) &mdash; The victim organization discovered the insider's activity (e.g., IT noticed that the insider had downloaded dozens of company trade secrets to their workstation)
- **`Detected method`**:
   - Technical Means (*2*) &mdash; The insider's activity was detected via analysis or anomalies in technical systems and software
  - Security Software (*4*) &mdash; The insider's activity was detected by security software (e.g., the insider tried to download a document with trade secrets and an automatic alert detected the download)
- **`Logs`**:
   - Access Logs (*AC*) &mdash; File or system access logs
  - Email Logs (*EM*) &mdash; Logs from email servers or services
  - Video Logs (*VD*) &mdash; Video, security cam, webcam, screen capture recordings

## Impact

Financial impact valued at approximately $150 million, which was the settlement amount Tech Solutions agreed to give Alpha Innovations in equity.

- **`Id`**:
 impact--d2eb25a4-1293-44ee-b8a6-a984714d8033
- **`High`**:
 150,000,000
- **`Low`**:
 150,000,000
- **`Metric`**:
 Dollars (*5*) &mdash; Specific financial impact of money stolen, restitution ordered, etc.
- **`Estimated`**:
 False

## Impact

Zingerman downloaded over 14,000 files before leaving the company to found his own startup, which was then bought by Tech Solutions.

- **`Id`**:
 impact--ea6f96c7-d4db-4021-b85b-057453ff2292
- **`High`**:
 14,000
- **`Metric`**:
 Files (*7*) &mdash; Number of physical or digital files stolen, read, or compromised
- **`Estimated`**:
 True

## Target

- **`Id`**:
 target--831dfcd9-11c5-407b-955e-287d531702b7
- **`Asset type`**:
 Information (*2*) &mdash; Data or business materials that contain important details belonging to a specific target owner
- **`Category`**:
 Product Information (*2.1*) &mdash; Information about products or services the organization sells
- **`Subcategory`**:
 Product Information (*2.1.1*) &mdash; Information about products or services offered by the organization
- **`Format`**:
 Electronic (*1*) &mdash; Technological digital format
- **`Owner`**:
 Organization (*O*) &mdash; The organization, rather than its employees or customers, owns the target
- **`Sensitivity`**:
   - Intellectual Property (IP) (*23*) &mdash; Information that has been created and is subject to protection of its creativity

## Target

- **`Id`**:
 target--a08d89e4-4b16-49e7-bdcc-0eea308a56e6
- **`Asset type`**:
 Technology (*5*) &mdash; Hardware, software, or firmware intended for the storage or transmission of data or the operation of equipment (as in computers running a manufacturing line)
- **`Category`**:
 Software (*5.2*) &mdash; Software or applications running on the organization's devices or systems
- **`Subcategory`**:
 Source code (*5.2.3*) &mdash; Underlying codebase for a product or system
- **`Format`**:
 Electronic (*1*) &mdash; Technological digital format
- **`Owner`**:
 Organization (*O*) &mdash; The organization, rather than its employees or customers, owns the target
- **`Sensitivity`**:
   - Intellectual Property (IP) (*23*) &mdash; Information that has been created and is subject to protection of its creativity

## Response

A third-party investigator was hired to look into the matter after an engineer at Alpha Innovations found Tech Solutions' software algorithms drastically similar to those developed by Alpha Innovations.

- **`Id`**:
 response--9923bad0-25bb-474a-bff7-4b23bfb3e240
- **`investigated_by`**:
 ['99', '7']
- **`investigation_events`**:
 [['1', '2001-11-00']]

## Court Case

- **`Id`**:
 court-case--3fcbf985-f10e-45b7-aacb-e16c89da1105
- **`Case number`**:
 01-cv-00939
- **`Case title`**:
 Alpha Innovations LLC v. Tech Solutions Inc.
- **`Court country`**:
 United States
- **`Court state`**:
 New York
- **`Court district`**:
 United States District Court for the Southern District of New York
- **`Court type`**:
 Federal (*1*) &mdash; Top level government court
- **`Case type`**:
 Civil (*1*) &mdash; A case dealing with a dispute between two people or organizations
- **`Defendant`**:
   - Tech Solutions Inc.
- **`Plaintiff`**:
   - Alpha Innovations LLC

## Charge

- **`Id`**:
 charge--3fcbf985-f10e-45b7-aacb-e16c89da1105
- **`Title`**:
 18 U.S.C
- **`Section`**:
 1836
- **`Nature of offense`**:
 Misappropriation of Trade Secrets
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
 sentence--c67354c2-5619-4ebc-85d0-21ca230c8a1d
- **`Sentence type`**:
 Restitution (*14*) &mdash; An attempt to measure in financial terms the extent of the gains or profits the defendant obtained through harming the victim
- **`Quantity`**:
 150,000,000
- **`Metric`**:
 Dollar(s) (*5*) &mdash; Imposed sentence is in terms of dollars (e.g. $10,000 in damages)
- **`Concurrency`**:
 False

## Legal Response

The legal response was primarily civil. The case did not involve law enforcement as it was not a criminal matter. The settlement resolved the dispute without a formal admission of wrongdoing.

- **`Id`**:
 legal-response--4dbe427c-8f98-4621-afa6-a20902afb8d2
- **`Insider settled`**:
 2003-02-09

## Job

Mark Zingerman was involved in the development of proprietary software technologies at Alpha Innovations before leaving to start his own company, which was later acquired by Tech Solutions.

- **`Id`**:
 job--afc08477-7f6f-4130-a966-f7b1e2188587
- **`Job function`**:
 Architecture and Engineering (*17*) &mdash; Architecture and Engineering
- **`Occupation`**:
 Engineers (*17.2*) &mdash; Aerospace Engineers, Bioengineers Engineers, Chemical Engineers, Civil Engineers, Electrical Engineers, Electronics Engineers, Environmental Engineers, Industrial Engineers, Marine Engineers, Naval Architects, Mechanical Engineers, Geological Engineers, etc.
- **`Title`**:
 Lead Engineer for Software Development
- **`Position technical`**:
 False
- **`Access authorization`**:
 Authorized Privileged User (*5*) &mdash; Authorized privileged access
- **`Employment type`**:
 Full-time (*FLT*) &mdash; Individual who is directly employed by the organization and works at least 35 hours per week or is classified by the organization as a full-time employee
- **`Hire date`**:
 1997-08-01
- **`Departure date`**:
 2006-01-27
- **`Tenure`**:
 P8Y5M26D

## Stressor

Insider left Alpha Innovations to start his own company.

- **`Id`**:
 stressor--3a9b7107-9d1c-4c9e-b5c2-e56b0bd408f0
- **`Date`**:
 2000-12-01
- **`Category`**:
 Employment Status (*1*) &mdash; The insider's employment status changed
- **`Subcategory`**:
 Insider Resigned (*1.9*) &mdash; The insider resigns from any organization, including the victim organization

## TTP

- **`Id`**:
 ttp--adfa4038-3dec-4d49-9dad-8cc35d41a261
- **`Date`**:
 2000-12-11
- **`Sequence num`**:
 1
- **`Observed`**:
 False
- **`Number of times`**:
 1
- **`TTP vocab`**:
 IIDES
- **`Tactic`**:
 Data Exfiltration (*7*) &mdash; Data (or copies of data) is removed from the organization without permission or explicitly against permission to use in an unauthorized way
- **`Technique`**:
 Laptop (*7.8*) &mdash; Data exfiltration by taking it out of the organization on a laptop
- **`Location`**:
   - Remotely (*2*) &mdash; Action taken while remote (i.e., not at an organizational facility)
- **`Hours`**:
   - During Work Hours (*1*) &mdash; Insider took the action during their normal working hours
- **`Device`**:
   - Company Laptop (*2*) &mdash; Organization owned laptop workstation
- **`Description`**:
 The insider locally downloaded files from the company cloud directories to their laptop.

## Accomplice

Chad Jones was accused of conspiring with Zingerman, motivating him financially to start a company using trade secrets from Alpha Innovations, which would then be bought by Tech Solutions.

- **`Id`**:
 accomplice--3426b922-135a-42f9-869d-f8b30e0d483b
- **`Relationship to insider`**:
 
- **`first_name`**:
 Chad
- **`last_name`**:
 Jones

## Note

This was a civil case. The insider was formally charged through a third-party civil court and later filed for bankruptcy.

- **`Id`**:
 note--afc08477-7f6f-4130-a966-f7b1e2188587
- **`Author`**:
 CMU Researcher
- **`Date`**:
 2004-05-28

## Org Relationship

- **`Id`**:
 org-relationship--83271b80-b5de-410e-b7ba-3c93ca5cba99
- **`Org2`**:
 organization--e7fda876-f31b-45a5-a540-7bb514ccecee
- **`Org1`**:
 organization--8ed0c400-fa6a-4bd6-babe-4da40240442d
- **`Relationship`**:
 C

## Source

- **`Id`**:
 source--267d8772-b2e0-4bea-92a6-224f157e6924
- **`Title`**:
 Settlement Agreement
- **`Source type`**:
 Court Document (*1*) &mdash; Legal document from a court case
- **`File type`**:
 PDF File (*pdf*) &mdash; A file in Portable Document Format
- **`Date`**:
 2002-09-13
- **`Public`**:
 True
- **`Document`**:
 https://fakeurl.com/cases/federal-appellate-courts/02-2235/02-2235-2002-09-13.html
