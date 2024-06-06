# Example2


## Incident

- **`Id`**:
 incident--0e339a3d-37fa-455c-b818-7aae0e34a2a8
- **`Cia effect`**:
   - Confidentiality (*C*) &mdash; The protection of information from unauthorized access or disclosure.
- **`Incident type`**:
   - Espionage (*E*) &mdash; The covert or illicit practice of spying on a foreign government, organization, entity, or person to obtain confidential information for military, political, strategic, or financial advantage.
- **`Incident subtype`**:
   - Government (*E.2*) &mdash; Covert intelligence-gathering activities to obtain government or military secrets for the benefit of another government to obtain political or military advantage.
- **`Outcome`**:
   - Data Read (*DR*) &mdash; Organizational data was read by the insider.
  - Data Stolen (*DS*) &mdash; Any organizational information or assets that are stolen.
- **`Status`**:
 Closed (*C*) &mdash; All investigations and legal proceedings are closed.
- **`Summary`**:
 The insider, an ex-Air Force member, worked as a translater for the National Security Agency in May 2017. During this time, she printed a report from her work computer that detailed hacking attempts by a Russian intelligence service against local election officers and voter registration databases. She then shared this Top Secret information with an online news outlet. This report revealed the sources and methods used to acquire the information contained on the report, which, if disclosed, could be harmful to the United States. The FBI investigated and later arrested the insider in June 2017. The insider pleaded guilty in June 2018 to one felony count of unauthorized transmission of national defense information and was convicted.
- **`Brief summary`**:
 The insider leaked Top Secret information to an online news outlet. The insider pleaded guilty to one felony count of unauthorized transmission of national defense information in June 2018, and was convicted.

## Insider

The insider previously had a very clean record, and was an unlikely suspect. The insider was a 'good kid' who had no apparent history of leaking or any disciplinary proceedings during their military service in the Air Force.

- **`Id`**:
 insider--04548271-8e9f-4e40-8bad-9cf77c858070
- **`Incident role`**:
 Primary (*1*) &mdash; Insider is the primary perpetrator of the incident.
- **`Motive`**:
   - Freedom of Information (*6*) &mdash; The insider held the belief that it is in the best interest of the public to share the victim organization's confidential information with the public. E.g., sharing unfavorable test results of a product or unfavorable information about an organization's internal practices.
- **`Substance use during incident`**:
 False
- **`First name`**:
 Reality
- **`Middle name`**:
 Leigh
- **`Last name`**:
 Winner
- **`Alias`**:
 ['Sara Winners', 'Jane Doe']
- **`City`**:
 Augusta
- **`State`**:
 GA
- **`Country`**:
 US
- **`Postal code`**:
 30907
- **`Country of citizenship`**:
 ['US']
- **`Nationality`**:
 ['US']
- **`Gender`**:
 F
- **`Age`**:
 25
- **`Education`**:
 5
- **`Marital status`**:
 1
- **`Number of children`**:
 0

## Organization

- **`Id`**:
 organization--3d459486-b1b1-4886-9129-87b3458120b3
- **`Name`**:
 US National Security Agency
- **`City`**:
 
- **`State`**:
 Maryland
- **`Country`**:
 United States of America
- **`Postal code`**:
 0
- **`Small business`**:
 False
- **`Industry sector`**:
 Public Administration (*92*) &mdash; Federal/State/Local administration and the oversight of public programs.
- **`Industry subsector`**:
 National Security (*92.811*) &mdash; This industry comprises government establishments of the Armed Forces, including the National Guard, primarily engaged in national security and related activities.
- **`Business`**:
 The National Security Agency (NSA) is a critical player in the U.S. intelligence community. Its primary function is to gather and analyze foreign signals intelligence (SIGINT) to protect national security.
- **`Parent company`**:
 United States Department of Defense
- **`Incident role`**:
 Primary Victim (*V*) &mdash; The organization was the primary victim organization of the insider's actions.

## Organization

- **`Id`**:
 organization--3d459486-b1b1-4886-9129-87b3458120b4
- **`Name`**:
 Pluribus International Corporation
- **`City`**:
 Alexandria
- **`State`**:
 Virginia
- **`Country`**:
 United States of America
- **`Postal code`**:
 22,314
- **`Small business`**:
 True
- **`Industry sector`**:
 Professional Services, Scientific and Technical Services (*54*) &mdash; Services provided by trained professionals in specialized fields.
- **`Industry subsector`**:
 Professional, Scientific, and Technical Services (*54.1*) &mdash; The Professional, Scientific, and Technical Services sector comprises establishments that specialize in performing professional, scientific, and technical activities for others. These activities require a high degree of expertise and training. The establishments in this sector specialize according to expertise and provide these services to clients in a variety of industries and, in some cases, to households.
- **`Business`**:
 Pluribus International Corporation is a defense and intelligence contractor providing analysis, intelligence, and security services to various U.S. government agencies.
- **`Incident role`**:
 Other (*O*) &mdash; Other role not described by this vocabulary.

## Detection

Reality Winner was caught after the NSA identified that a classified document published by The Intercept had been printed, revealing traceable metadata. Investigators used printer tracking dots to determine the document's print date and reviewed access logs, finding that only six individuals, including Winner, had accessed it. Further evidence included her email communication with The Intercept and her confession when confronted by the FBI.

- **`Id`**:
 detection--7f05c15a-84b2-489d-a3dc-0e3c78d9cbc8
- **`First detected`**:
 2017-04-23T18:25:43.511Z
- **`Who detected`**:
   - Law Enforcement (*LE*) &mdash; Law enforcement discovered the insider's illegal activity (e.g., Police noticed that the insider was gaining access to the company after hours).
- **`Detected method`**:
   - Technical Means (*2*) &mdash; The insider's activity was detected via analysis or anomalies in technical systems and software.
- **`Logs`**:
   - Access Logs (*AC*) &mdash; File or system access logs.
  - Email Logs (*EM*) &mdash; Logs from email servers or services.

## Impact

- **`Id`**:
 impact--0e15aa3c-8d6c-4afd-bed4-c45f64c34463
- **`High`**:
 1
- **`Low`**:
 1
- **`Metric`**:
 Documents (*4*) &mdash; The number of physical or digital documents effected (stolen, deleted, modified, etc.).
- **`Estimated`**:
 False

## Target

- **`Id`**:
 target--c482c487-5bb4-4dee-abdf-2e0c207a81bd
- **`Asset type`**:
 Information (*2*) &mdash; Data/business materials which contain important details belonging to a specific target owner.
- **`Category`**:
 Government/Law Enforcement Information (*2.3*) &mdash; Classified or sensitive government or law enforcement information.
- **`Subcategory`**:
 Classified Information (*2.3.1*) &mdash; Information that is restricted by the government for reasons of national security.
- **`Format`**:
 Physical (*2*) &mdash; Tangible real world format.
- **`Owner`**:
 Organization (*O*) &mdash; The organization, rather than its employees or customers owns the target.
- **`Sensitivity`**:
   - Top Secret (TS) (*6*) &mdash; Top secret, unauthorized disclosure would cause exceptionally grave damage to national security

## Response



- **`Id`**:
 response--ab3c9833-1e6a-426a-9e48-6f74bcbc5778
- **`Investigated by`**:
   - Law Enforcement - Federal (*4*) &mdash; Federal law enforcement entity such as the FBI or USSS.
- **`Investigation events`**:
   - Insider's Residence/Workplace Searched (*['1', '2017-05-17']*) &mdash; Investigators search the insider's home or workplace for evidence related to the incident.
  - Insider Admits to Activity in Interview (*['3', '2017-05-03']*) &mdash; Insider admits to involvement in insider incident while being interviewed by investigators about the incident (or related activity).

## Court-case



- **`Id`**:
 court-case--85e8998f-080a-4764-8bab-f8e9fa3fc70d
- **`Case number`**:
 1:17-cr-034
- **`Case title`**:
 UNITED STATES of America v. Reality WINNER
- **`Court country`**:
 United States of America
- **`Court state`**:
 Georgia
- **`Court district`**:
 Southern District Court of Georgia
- **`Court type`**:
 State (*3*) &mdash; State or regional level government court.
- **`Case type`**:
 Criminal (*2*) &mdash; A case dealing with a violation of criminal law.
- **`Defendant`**:
   - Reality Winner
- **`Plaintiff`**:
   - United States of America

## Charge

- **`Id`**:
 charge--71ed72fb-9194-40af-8459-17aa881a70dc
- **`Title`**:
 18 U.S.C
- **`Section`**:
 793(e)
- **`Nature of offense`**:
 Willful Retention and Transmission of National Defense Information
- **`Count`**:
 1
- **`Plea`**:
 Guilty (*1*) &mdash; The defendant pleaed guilty to a charge.
- **`Plea bargain`**:
 True
- **`Disposition`**:
 Convicted (*2*) &mdash; Plead or been found guilty by a court.

## Sentence

- **`Id`**:
 sentence--73e8e020-5ce6-4acb-94ea-7ff3d6f1bcc5
- **`Sentence type`**:
 Incarceration (*9*) &mdash; Imprisonment.
- **`Quantity`**:
 63
- **`Metric`**:
 Month(s) (*3*) &mdash; Imposed sentence is in terms of months. E.g. 18 months imprisonment.
- **`Concurrency`**:
 False

## Sentence

- **`Id`**:
 sentence--73e8e020-5ce6-4acb-94ea-7ff3d6f1bcb6
- **`Sentence type`**:
 Supervised Release (*16*) &mdash; Defendant is released into the community, subject to special conditions and restrictions, after the completion of a prison sentence.
- **`Quantity`**:
 3
- **`Metric`**:
 Year(s) (*4*) &mdash; Imposed sentence is in terms of years. E.g. 5 years no Internet access.
- **`Concurrency`**:
 False

## Legal-response

- **`Id`**:
 legal-response--87cc68cc-6e06-4131-8732-80995f5e3ca6
- **`Law enforcement contacted`**:
 2017-05-01
- **`Insider arrested`**:
 2017-05-03
- **`Insider charged`**:
 2017-05-07
- **`Insider pleads`**:
 2017-05-21
- **`Insider judgment`**:
 2018-08-07
- **`Insider sentenced`**:
 2018-08-23

## Job

The exact date of hire and departure is unknown, but the month and year are correct.

- **`Id`**:
 job--11492807-43a6-4e50-9480-b26ecaca983d
- **`Job function`**:
 Military Specific (*55*) &mdash; Military Specific
- **`Occupation`**:
 Military Enlisted Tactical Operations, Specialists, and Crew Members (*55.3*) &mdash; Crew Members, Specialists, Infantry, Special Forces, etc.
- **`Title`**:
 Linguist
- **`Position technical`**:
 False
- **`Access authorization`**:
 Authorized Account Only (*4*) &mdash; Authorized account but not authorized access to targeted data.
- **`Employment type`**:
 Contractor (*CTR*) &mdash; Individual not directly employed by the organization whose job responsibilities they filling (self-employed or employed by a different, contracting organization).
- **`Hire date`**:
 2017-02-01
- **`Departure date`**:
 2017-07-01
- **`Tenure`**:
 2904:00:00

## Ttp

- **`Id`**:
 ttp--aabe47dc-fecb-43f9-bf77-361b06504789
- **`Date`**:
 2017-03-09T12:00:00.000Z
- **`Sequence num`**:
 1
- **`Observed`**:
 False
- **`Number of times`**:
 1
- **`Ttp vocab`**:
 IIDES
- **`Tactic`**:
 Data Exfiltration (*7*) &mdash; Data (or copies of data) is removed from the organization without permission or explicitly against permission to use in an unauthorized way.
- **`Technique`**:
 Paper (*7.1*) &mdash; Insider exfiltrates data through printed or hand-written materials (e.g., Insider takes screenshots of important data, prints the screenshots, and walks out of work with them).
- **`Location`**:
   - On-site (*1*) &mdash; Action taken while on-site at an organizational facility.
- **`Hours`**:
   - During Work Hours (*1*) &mdash; Insider took the action during their normal working hours.
- **`Device`**:
   - Company Desktop (*1*) &mdash; Organization owned desktop workstation.
  - Printer/Copier/Fax (*9*) &mdash; Printer, copier, or fax machine.
- **`Channel`**:
   - Other (*9*) &mdash; Other type of channel not listed in this vocabulary.
- **`Description`**:
 Winner printed and improperly removed classified intelligence reporting.

## Ttp

- **`Id`**:
 ttp--aabe47dc-fecb-43f9-bf77-361b06504789
- **`Date`**:
 2017-03-09T12:00:00.000Z
- **`Sequence num`**:
 2
- **`Observed`**:
 False
- **`Number of times`**:
 1
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
  - Printer/Copier/Fax (*9*) &mdash; Printer, copier, or fax machine.
- **`Channel`**:
   - Other (*9*) &mdash; Other type of channel not listed in this vocabulary.
- **`Description`**:
 Winner printed and improperly removed classified intelligence reporting.

## Org-relationship

- **`Id`**:
 org-relationship--83271b80-b5de-410e-b7ba-3c93ca5cba08
- **`Org2`**:
 organization--3d459486-b1b1-4886-9129-87b3458120b3
- **`Org1`**:
 organization--3d459486-b1b1-4886-9129-87b3458120b4
- **`Relationship`**:
 V

## Source

- **`Id`**:
 source--c989a0c4-a559-491a-ac63-2f8b0eaba126
- **`Title`**:
 United States v. Winner
- **`Source type`**:
 Court Document (*1*) &mdash; Legal document from a court case.
- **`File type`**:
 html
- **`Date`**:
 2020-04-24
- **`Public`**:
 True
- **`Document`**:
 https://casetext.com/case/united-states-v-winner-9

## Source

- **`Id`**:
 source--32c2aa75-685a-4af5-ba0f-36921b8d1c18
- **`Title`**:
 CASE STUDY Unlawful Retention and Transmission of National Defense Information
- **`Source type`**:
 Media (*5*) &mdash; News, blog, or similar publication.
- **`File type`**:
 pdf
- **`Date`**:
 
- **`Public`**:
 True
- **`Document`**:
 https://www.cdse.edu/Portals/124/Documents/casestudies/case-study-winner.pdf

## Source

- **`Id`**:
 source--d7fba1ef-193d-4826-a551-ce6aa66150c3
- **`Title`**:
 USA v. Reality Leigh Winner, No. 20-11692 (11th Cir. 2020)
- **`Source type`**:
 Court Document (*1*) &mdash; Legal document from a court case.
- **`File type`**:
 pdf
- **`Date`**:
 2020-12-07
- **`Public`**:
 True
- **`Document`**:
 https://law.justia.com/cases/federal/appellate-courts/ca11/20-11692/20-11692-2020-12-07.html

## Source

- **`Id`**:
 source--5e290802-9738-40a5-bb64-9544d8624995
- **`Title`**:
 USA v. Reality Leigh Winner, No. 20-11692 (11th Cir. 2020)
- **`Source type`**:
 DOJ Press Release (*2*) &mdash; Press release from the Department of Justice or US Attorneys' Office.
- **`File type`**:
 html
- **`Date`**:
 2018-08-23
- **`Public`**:
 True
- **`Document`**:
 https://www.justice.gov/opa/pr/federal-government-contractor-sentenced-removing-and-transmitting-classified-materials-news

## Source

- **`Id`**:
 source--1c8da449-30ed-4b7b-89f7-9c8f272207ab
- **`Title`**:
 Reality Winner, N.S.A. Contractor Accused of Leak, Was Undone by Trail of Clues
- **`Source type`**:
 Media (*5*) &mdash; News, blog, or similar publication.
- **`File type`**:
 html
- **`Date`**:
 2017-05-06
- **`Public`**:
 True
- **`Document`**:
 https://www.nytimes.com/2017/06/06/us/politics/reality-leigh-winner-leak-nsa.html

## Source

- **`Id`**:
 source--497d1b03-8c71-482f-9156-542d21e99fdf
- **`Title`**:
 Reality Winner, Former N.S.A. Translator, Gets More Than 5 Years in Leak of Russian Hacking Report
- **`Source type`**:
 Media (*5*) &mdash; News, blog, or similar publication.
- **`File type`**:
 html
- **`Date`**:
 2018-08-23
- **`Public`**:
 True
- **`Document`**:
 https://www.nytimes.com/2018/08/23/us/reality-winner-nsa-sentence.html

## Source

- **`Id`**:
 source--a6e7705d-195f-4617-a2d2-30c84aadadea
- **`Title`**:
 Original Court Documents: US v. Reality Leigh Winner
- **`Source type`**:
 Court Document (*1*) &mdash; Legal document from a court case.
- **`File type`**:
 pdf
- **`Date`**:
 2018-08-23
- **`Public`**:
 True
- **`Document`**:
 https://standwithreality.org/original-court-documents/
