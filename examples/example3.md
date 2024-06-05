# Examples/json/example3

## Incident

The case was settled out of court, and no formal determination of guilt was made against Uber, but they agreed to a settlement to avoid the continuation of litigation.

- **`Id`**:
   - incident--6e75f650-c1a5-4c71-8d2f-7e9d2bba0381
- **`Cia effect`**:
   - *C*: Confidentiality - The protection of information from unauthorized access or disclosure.
  - *I*: Integrity - The protection of information from unauthorized modification or destruction.

- **`Incident type`**:
   - *E*: Espionage - The covert or illicit practice of spying on a foreign government, organization, entity, or person to obtain confidential information for military, political, strategic, or financial advantage.

- **`Incident subtype`**:
   - *E1*: Intellectual Property Theft - Theft or robbery of an individual's or organization's ideas, inventions, or creative expressions, including trade secrets and proprietary products, even if the concepts or items being stolen originated from the thief.

- **`Outcome`**:
   - *DS*: Data Stolen - Any organizational information or assets that are stolen.
  - *ML*: Monetary Losses - Indirect loss of money through damage, detriment, or suffering related to the incident.

- **`Status`**:
   - *C*: Closed - All investigations and legal proceedings are closed.
- **`Summary`**:
   - The case involved Waymo, a self-driving car company spun off from Google, accusing Uber, through its acquisition of Otto, of stealing trade secrets related to LiDAR technology. The lawsuit claimed that Anthony Levandowski, a former Google engineer, downloaded thousands of files related to Waymo’s self-driving technology before leaving to start Otto, which was soon acquired by Uber.
- **`Brief summary`**:
   - Waymo sued Uber for intellectual property theft, claiming that ex-Google engineer Anthony Levandowski stole LiDAR technology secrets before joining Uber. The case was settled with Uber agreeing to not use Waymo’s technology and paying equity worth approximately $245 million.
## Insider

Anthony Levandowski's actions of transferring confidential files from Waymo to his personal devices sparked the lawsuit. No public evidence of substance use or psychological issues affecting his actions has been documented.

- **`Id`**:
   - insider--2fe80494-c7cf-4d75-85ef-736b55884664
- **`Incident role`**:
   - *1*: Primary - Insider is the primary perpetrator of the incident.
- **`Motive`**:
   - *3*: Competitive Business Advantage - Insider committed their attack in order to gain a business advantage for a competing company. Often, this is the insider starting their own company.
  - *5*: Financial Gain - Insider committed their attack to make a profit.

- **`Substance use during incident`**:
 False
- **`First name`**:
 Anthony
- **`Last name`**:
 Levandowski
- **`Alias`**:
 ['Anton Levy', 'John Doe']
- **`City`**:
 San Francisco
- **`State`**:
 CA
- **`Country`**:
 US
- **`Postal code`**:
 94107
- **`Country of citizenship`**:
 ['US']
- **`Nationality`**:
 ['US']
- **`Gender`**:
 M
- **`Age`**:
 40
- **`Education`**:
 8
- **`Marital status`**:
 2
- **`Number of children`**:
 2
- **`Concerning behaviors`**:
   - *['3.2', '3.2.4']*: Technical Policy Abuse - Violating policies regarding the use of the organization's IT systems.
  - *['3.2', '3.2.3']*: Technical Policy Abuse - Violating policies regarding the use of the organization's IT systems.
  - *['3.5', '3.5.1']*: Organizational Conflict - Competitive conflicts of interest with the organization.
  - *['3.5', '3.5.2']*: Organizational Conflict - Competitive conflicts of interest with the organization.

## Organization

- **`Id`**:
   - organization--8ed0c400-fa6a-4bd6-babe-4da40240442d
- **`Name`**:
   - Waymo LLC
- **`City`**:
   - Mountain View
- **`State`**:
   - California
- **`Country`**:
   - USA
- **`Postal code`**:
 94,043
- **`Small business`**:
 False
- **`Industry sector`**:
   - *48*: Transportation and Warehousing - Services directly or indirectly involved in the movement of people.
- **`Industry subsector`**:
   - *48.5*: Transit and Ground Passenger Transportation - This subsector includes industries providing passenger transportation, such as buses and taxis.
- **`Business`**:
   - Waymo operates as a self-driving technology company primarily involved in developing autonomous driving systems.
- **`Parent company`**:
   - Alphabet Inc.
- **`Incident role`**:
   - *V*: Primary Victim - The organization was the primary victim organization of the insider's actions.
## Organization

- **`Id`**:
   - organization--e7fda876-f31b-45a5-a540-7bb514ccecee
- **`Name`**:
   - Uber Technologies Inc.
- **`City`**:
   - San Francisco
- **`State`**:
   - California
- **`Country`**:
   - USA
- **`Postal code`**:
 94,103
- **`Small business`**:
 False
- **`Industry sector`**:
   - *48*: Transportation and Warehousing - Services directly or indirectly involved in the movement of people.
- **`Industry subsector`**:
   - *48.5*: Transit and Ground Passenger Transportation - This subsector includes industries providing passenger transportation, such as buses and taxis.
- **`Business`**:
   - Uber operates as a technology company offering ridesharing, food delivery, and transportation services globally, with a division focused on developing autonomous vehicle technology.
- **`Incident role`**:
   - *B*: Beneficiary - The organization accepted trade secrets, customer lists, intellectual property, etc. that the insider obtained through the incident.
## Detection

- **`Id`**:
   - detection--a181e814-aa3a-411e-ae79-79ceba48e36a
- **`First detected`**:
   - 2017-02-23
- **`Who detected`**:
   - *LE*: Law Enforcement - Law enforcement discovered the insider's illegal activity (e.g., Police noticed that the insider was gaining access to the company after hours).
  - *OR*: Organization - The victim organization discovered the insider's activity (e.g., IT noticed that the insider had downloaded dozens of company trade secrets to their workstation).

- **`Detected method`**:
   - *2*: Technical Means - The insider's activity was detected via analysis or anomalies in technical systems and software.
  - *4*: Security Software - The insider's activity was detected by security software (e.g., The insider tried to download a document with trade secrets and an automatic alert detected the download).

- **`Logs`**:
   - *AC*: Access Logs - File or system access logs.
  - *EM*: Email Logs - Logs from email servers or services.
  - *VD*: Video Logs - Video, security cam, webcam, screen capture recordings.

## Impact

Financial impact valued at approximately $245 million, which was the settlement amount Uber agreed to give Waymo in equity.

- **`Id`**:
   - impact--d2eb25a4-1293-44ee-b8a6-a984714d8033
- **`High`**:
 245,000,000
- **`Low`**:
 245,000,000
- **`Metric`**:
   - *5*: Dollars - Specific financial impact of money stolen, restitution ordered, etc.
- **`Estimated`**:
 False
## Impact

Levandowski downloaded over 14,000 files before leaving the company to found his own startup, that was then bought by Uber

- **`Id`**:
   - impact--ea6f96c7-d4db-4021-b85b-057453ff2292
- **`High`**:
 14,000
- **`Metric`**:
   - *7*: Files - Number of physical or digital files stolen, read, or compromised.
- **`Estimated`**:
 True
## Target

- **`Id`**:
   - target--831dfcd9-11c5-407b-955e-287d531702b7
- **`Asset type`**:
   - *2*: Information - Data/business materials which contain important details belonging to a specific target owner.
- **`Category`**:
   - *2.1*: Product Information - Information about products or services the organization sells
- **`Subcategory`**:
   - *2.1.1*: Product Information - Information about products or services offered by the organization.
- **`Format`**:
   - *1*: Electronic - Technological digital format.
- **`Owner`**:
   - *O*: Organization - The organization, rather than its employees or customers owns the target.
- **`Sensitivity`**:
   - *23*: Intellectual Property (IP) - Information that has been created and is subject to protection of its creativity.

## Target

- **`Id`**:
   - target--a08d89e4-4b16-49e7-bdcc-0eea308a56e6
- **`Asset type`**:
   - *5*: Technology - Hardware, software, or firmware intended for the storage or transmission of data or the operation of equipment (as in computers running a manufacturing line).
- **`Category`**:
   - *5.2*: Software - Software or applications running on the organization's devices or systems.
- **`Subcategory`**:
   - *5.2.3*: Source code - Underlying codebase for a product or system.
- **`Format`**:
   - *1*: Electronic - Technological digital format.
- **`Owner`**:
   - *O*: Organization - The organization, rather than its employees or customers owns the target.
- **`Sensitivity`**:
   - *23*: Intellectual Property (IP) - Information that has been created and is subject to protection of its creativity.

## Response

A third party investigator was hired to look into the matter after an engineer at Waymo found Uber's autonomous vehicle sensors drastically similar to those developed by Waymo.

- **`Id`**:
   - response--9923bad0-25bb-474a-bff7-4b23bfb3e240
- **`Investigated by`**:
 ['99', '2']
- **`Investigation events`**:
 [['2', '2016-11-00']]
## Court-case

- **`Id`**:
   - court-case--3fcbf985-f10e-45b7-aacb-e16c89da1105
- **`Case number`**:
   - 17-cv-00939
- **`Case title`**:
   - Waymo LLC v. Uber Technologies, Inc.
- **`Court country`**:
   - *United States*: 
- **`Court state`**:
   - *California*: 
- **`Court district`**:
   - United States District Court for the Northern District of California
- **`Court type`**:
   - *1*: Federal - Top level government court.
- **`Case type`**:
   - *1*: Civil - A case dealing with a dispute between two people or organizations.
- **`Defendant`**:
   - Uber Technologies, Inc

- **`Plaintiff`**:
   - Waymo LLC

## Charge

- **`Id`**:
   - charge--3fcbf985-f10e-45b7-aacb-e16c89da1105
- **`Title`**:
   - 18 U.S.C
- **`Section`**:
   - 1836
- **`Nature of offense`**:
   - Misappropriation of Trade Secrets
- **`Count`**:
 1
- **`Plea`**:
   - *3*: Not Guilty - The defendant pleaed not guilty to a charge.
- **`Plea bargain`**:
 False
- **`Disposition`**:
   - *2*: Convicted - Plead or been found guilty by a court.
## Sentence

- **`Id`**:
   - sentence--c67354c2-5619-4ebc-85d0-21ca230c8a1d
- **`Sentence type`**:
   - *14*: Restitution - An attempt to measure in financial terms the extent of the gains or profits the defendant obtained through harming the victim.
- **`Quantity`**:
 245,000,000
- **`Metric`**:
   - *5*: Dollar(s) - Imposed sentence is in terms of dollars. E.g. $10,000 in damages.
- **`Concurrency`**:
 False
## Legal-response

The legal response was primarily civil. The case did not involve law enforcement as it was not a criminal matter. The settlement resolved the dispute without a formal admission of wrongdoing.

- **`Id`**:
   - legal-response--4dbe427c-8f98-4621-afa6-a20902afb8d2
- **`Insider settled`**:
   - 2018-02-09
## Job

Anthony Levandowski was involved in the development of autonomous vehicle technologies at Waymo, a division of Google, before leaving to start Otto, which was later acquired by Uber.

- **`Id`**:
   - job--afc08477-7f6f-4130-a966-f7b1e2188587
- **`Job function`**:
   - *17*: Architecture and Engineering - Architecture and Engineering
- **`Occupation`**:
   - *17.2*: Engineers - Aerospace Engineers, Bioengineers Engineers, Chemical Engineers, Civil Engineers, Electrical Engineers, Electronics Engineers, Environmental Engineers, Industrial Engineers, Marine Engineers, Naval Architects, Mechanical Engineers, Geological Engineers, Etc.
- **`Title`**:
   - Lead Engineer for Autonomous Vehicle Technology
- **`Position technical`**:
 False
- **`Access authorization`**:
   - *5*: Authorized Privileged User - Authorized privileged access.
- **`Employment type`**:
   - *FLT*: Full-time - Individual who is directly employed by the organization and works at least 35 hours per week (or is classified by the organization as a full-time employee).
- **`Hire date`**:
   - 2007-08-01
- **`Departure date`**:
   - 2016-01-27
- **`Tenure`**:
   - P8Y5M26D
## Stressor

Insider left Waymo to start his own company.

- **`Id`**:
   - stressor--3a9b7107-9d1c-4c9e-b5c2-e56b0bd408f0
- **`Date`**:
   - 2015-12-01
- **`Category`**:
   - *1*: Employment Status - The insider's employment status changed.
- **`Subcategory`**:
   - *1.9*: Insider Resigned - The insider resigns from any organization, including the victim organization.
## Ttp

- **`Id`**:
   - ttp--adfa4038-3dec-4d49-9dad-8cc35d41a261
- **`Date`**:
   - 2015-12-11
- **`Sequence num`**:
 1
- **`Observed`**:
 False
- **`Number of times`**:
 1
- **`Ttp vocab`**:
   - IIDES
- **`Tactic`**:
   - *7*: Data Exfiltration - Data (or copies of data) is removed from the organization without permission or explicitly against permission to use in an unauthorized way.
- **`Technique`**:
   - *7.8*: Laptop - Insider exfiltrates data by taking it out of the organization on a laptop.
- **`Location`**:
   - *2*: Remotely - Action taken while remote (i.e. not at an organizational facility).

- **`Hours`**:
   - *1*: During Work Hours - Insider took the action during their normal working hours.

- **`Device`**:
   - *2*: Company Laptop - Organization owned laptop workstation.

- **`Description`**:
   - The insider locally downloaded files from the company cloud directories to their laptop.
## Accomplice

Co-founder and former chief executive officer of Uber was accused of having conspired with Levandowski, motivating him financially to starting a company using trade secrets from Waymo, that would then be bought by Uber.

- **`Id`**:
   - accomplice--3426b922-135a-42f9-869d-f8b30e0d483b
- **`Relationship to insider`**:
   - *2*: 
- **`First name`**:
 Travis
- **`Last name`**:
 Kalanick
## Note

This was a civil case, the insider was formally charged through a third party civil court and later filed for bankruptcy

- **`Id`**:
   - note--afc08477-7f6f-4130-a966-f7b1e2188587
- **`Author`**:
   - CMU Researcher
- **`Date`**:
   - 2024-05-28
## Org-relationship

- **`Id`**:
   - org-relationship--83271b80-b5de-410e-b7ba-3c93ca5cba99
- **`Org2`**:
   - organization--e7fda876-f31b-45a5-a540-7bb514ccecee
- **`Org1`**:
   - organization--8ed0c400-fa6a-4bd6-babe-4da40240442d
- **`Relationship`**:
   - *C*: 
## Source

- **`Id`**:
   - source--267d8772-b2e0-4bea-92a6-224f157e6924
- **`Title`**:
   - Settlement Agreement
- **`Source type`**:
   - *1*: Court Document - Legal document from a court case.
- **`File type`**:
   - *pdf*: 
- **`Date`**:
   - 2017-09-13
- **`Public`**:
 True
- **`Document`**:
   - https://law.justia.com/cases/federal/appellate-courts/cafc/17-2235/17-2235-2017-09-13.html
