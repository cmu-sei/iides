# Example2

## Incident

- **`Id`**:
  - incident--0e339a3d-37fa-455c-b818-7aae0e34a2a8
- **`Cia effect`**:

  - _C_: Confidentiality - The protection of information from unauthorized access or disclosure.

- **`Incident type`**:

  - _E_: Espionage - The covert or illicit practice of spying on a foreign government, organization, entity, or person to obtain confidential information for military, political, strategic, or financial advantage.

- **`Incident subtype`**:

  - _E2_: Government - Covert intelligence-gathering activities to obtain government or military secrets for the benefit of another government to obtain political or military advantage.

- **`Outcome`**:

  - _DR_: Data Read - Organizational data was read by the insider.
  - _DS_: Data Stolen - Any organizational information or assets that are stolen.

- **`Status`**:
  - _C_: Closed - All investigations and legal proceedings are closed.
- **`Summary`**:
  - The insider, an ex-Air Force member, worked as a translater for the National Security Agency in May 2017. During this time, she printed a report from her work computer that detailed hacking attempts by a Russian intelligence service against local election officers and voter registration databases. She then shared this Top Secret information with an online news outlet. This report revealed the sources and methods used to acquire the information contained on the report, which, if disclosed, could be harmful to the United States. The FBI investigated and later arrested the insider in June 2017. The insider pleaded guilty in June 2018 to one felony count of unauthorized transmission of national defense information and was convicted.
- **`Brief summary`**:
  - The insider leaked Top Secret information to an online news outlet. The insider pleaded guilty to one felony count of unauthorized transmission of national defense information in June 2018, and was convicted.

## Insider

The insider previously had a very clean record, and was an unlikely suspect. The insider was a 'good kid' who had no apparent history of leaking or any disciplinary proceedings during their military service in the Air Force.

- **`Id`**:
  - insider--04548271-8e9f-4e40-8bad-9cf77c858070
- **`Incident role`**:
  - _1_: Primary - Insider is the primary perpetrator of the incident.
- **`Motive`**:

  - _6_: Freedom of Information - The insider held the belief that it is in the best interest of the public to share the victim organization's confidential information with the public. E.g., sharing unfavorable test results of a product or unfavorable information about an organization's internal practices.

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
  - organization--3d459486-b1b1-4886-9129-87b3458120b3
- **`Name`**:
  - US National Security Agency
- **`City`**:
  -
- **`State`**:
  - Maryland
- **`Country`**:
  - United States of America
- **`Postal code`**:
  0
- **`Small business`**:
  False
- **`Industry sector`**:
  - _92_: Public Administration - Federal/State/Local administration and the oversight of public programs.
- **`Industry subsector`**:
  - _92.811_: National Security - This industry comprises government establishments of the Armed Forces, including the National Guard, primarily engaged in national security and related activities.
- **`Business`**:
  - The National Security Agency (NSA) is a critical player in the U.S. intelligence community. Its primary function is to gather and analyze foreign signals intelligence (SIGINT) to protect national security.
- **`Parent company`**:
  - United States Department of Defense
- **`Incident role`**:
  - _V_: Primary Victim - The organization was the primary victim organization of the insider's actions.

## Organization

- **`Id`**:
  - organization--3d459486-b1b1-4886-9129-87b3458120b4
- **`Name`**:
  - Pluribus International Corporation
- **`City`**:
  - Alexandria
- **`State`**:
  - Virginia
- **`Country`**:
  - United States of America
- **`Postal code`**:
  22,314
- **`Small business`**:
  True
- **`Industry sector`**:
  - _54_: Professional Services, Scientific and Technical Services - Services provided by trained professionals in specialized fields.
- **`Industry subsector`**:
  - _54.1_: Professional, Scientific, and Technical Services - The Professional, Scientific, and Technical Services sector comprises establishments that specialize in performing professional, scientific, and technical activities for others. These activities require a high degree of expertise and training. The establishments in this sector specialize according to expertise and provide these services to clients in a variety of industries and, in some cases, to households.
- **`Business`**:
  - Pluribus International Corporation is a defense and intelligence contractor providing analysis, intelligence, and security services to various U.S. government agencies.
- **`Incident role`**:
  - _O_: Other - Other role not described by this vocabulary.

## Detection

Reality Winner was caught after the NSA identified that a classified document published by The Intercept had been printed, revealing traceable metadata. Investigators used printer tracking dots to determine the document's print date and reviewed access logs, finding that only six individuals, including Winner, had accessed it. Further evidence included her email communication with The Intercept and her confession when confronted by the FBI.

- **`Id`**:
  - detection--7f05c15a-84b2-489d-a3dc-0e3c78d9cbc8
- **`First detected`**:
  - 2017-04-23T18:25:43.511Z
- **`Who detected`**:

  - _LE_: Law Enforcement - Law enforcement discovered the insider's illegal activity (e.g., Police noticed that the insider was gaining access to the company after hours).

- **`Detected method`**:

  - _2_: Technical Means - The insider's activity was detected via analysis or anomalies in technical systems and software.

- **`Logs`**:
  - _AC_: Access Logs - File or system access logs.
  - _EM_: Email Logs - Logs from email servers or services.

## Impact

- **`Id`**:
  - impact--0e15aa3c-8d6c-4afd-bed4-c45f64c34463
- **`High`**:
  1
- **`Low`**:
  1
- **`Metric`**:
  - _4_: Documents - The number of physical or digital documents effected (stolen, deleted, modified, etc.).
- **`Estimated`**:
  False

## Target

- **`Id`**:
  - target--c482c487-5bb4-4dee-abdf-2e0c207a81bd
- **`Asset type`**:
  - _2_: Information - Data/business materials which contain important details belonging to a specific target owner.
- **`Category`**:
  - _2.3_: Government/Law Enforcement Information - Classified or sensitive government or law enforcement information.
- **`Subcategory`**:
  - _2.3.1_: Classified Information - Information that is restricted by the government for reasons of national security.
- **`Format`**:
  - _2_: Physical - Tangible real world format.
- **`Owner`**:
  - _O_: Organization - The organization, rather than its employees or customers owns the target.
- **`Sensitivity`**:
  - _6_: Top Secret (TS) - Top secret, unauthorized disclosure would cause exceptionally grave damage to national security

## Response

- **`Id`**:
  - response--ab3c9833-1e6a-426a-9e48-6f74bcbc5778
- **`Investigated by`**:

  - _4_: Law Enforcement - Federal - Federal law enforcement entity such as the FBI or USSS.

- **`Investigation events`**:
  - _['1', '2017-05-17']_: Insider's Residence/Workplace Searched - Investigators search the insider's home or workplace for evidence related to the incident.
  - _['3', '2017-05-03']_: Insider Admits to Activity in Interview - Insider admits to involvement in insider incident while being interviewed by investigators about the incident (or related activity).

## Court-case

- **`Id`**:
  - court-case--85e8998f-080a-4764-8bab-f8e9fa3fc70d
- **`Case number`**:
  - 1:17-cr-034
- **`Case title`**:
  - UNITED STATES of America v. Reality WINNER
- **`Court country`**:
  - _United States of America_:
- **`Court state`**:
  - _Georgia_:
- **`Court district`**:
  - Southern District Court of Georgia
- **`Court type`**:
  - _3_: State - State or regional level government court.
- **`Case type`**:
  - _2_: Criminal - A case dealing with a violation of criminal law.
- **`Defendant`**:

  - Reality Winner

- **`Plaintiff`**:
  - United States of America

## Charge

- **`Id`**:
  - charge--71ed72fb-9194-40af-8459-17aa881a70dc
- **`Title`**:
  - 18 U.S.C
- **`Section`**:
  - 793(e)
- **`Nature of offense`**:
  - Willful Retention and Transmission of National Defense Information
- **`Count`**:
  1
- **`Plea`**:
  - _1_: Guilty - The defendant pleaed guilty to a charge.
- **`Plea bargain`**:
  True
- **`Disposition`**:
  - _2_: Convicted - Plead or been found guilty by a court.

## Sentence

- **`Id`**:
  - sentence--73e8e020-5ce6-4acb-94ea-7ff3d6f1bcc5
- **`Sentence type`**:
  - _9_: Incarceration - Imprisonment.
- **`Quantity`**:
  63
- **`Metric`**:
  - _3_: Month(s) - Imposed sentence is in terms of months. E.g. 18 months imprisonment.
- **`Concurrency`**:
  False

## Sentence

- **`Id`**:
  - sentence--73e8e020-5ce6-4acb-94ea-7ff3d6f1bcb6
- **`Sentence type`**:
  - _16_: Supervised Release - Defendant is released into the community, subject to special conditions and restrictions, after the completion of a prison sentence.
- **`Quantity`**:
  3
- **`Metric`**:
  - _4_: Year(s) - Imposed sentence is in terms of years. E.g. 5 years no Internet access.
- **`Concurrency`**:
  False

## Legal-response

- **`Id`**:
  - legal-response--87cc68cc-6e06-4131-8732-80995f5e3ca6
- **`Law enforcement contacted`**:
  - 2017-05-01
- **`Insider arrested`**:
  - 2017-05-03
- **`Insider charged`**:
  - 2017-05-07
- **`Insider pleads`**:
  - 2017-05-21
- **`Insider judgment`**:
  - 2018-08-07
- **`Insider sentenced`**:
  - 2018-08-23

## Job

The exact date of hire and departure is unknown, but the month and year are correct.

- **`Id`**:
  - job--11492807-43a6-4e50-9480-b26ecaca983d
- **`Job function`**:
  - _55_: Military Specific - Military Specific
- **`Occupation`**:
  - _55.3_: Military Enlisted Tactical Operations, Specialists, and Crew Members - Crew Members, Specialists, Infantry, Special Forces, etc.
- **`Title`**:
  - Linguist
- **`Position technical`**:
  False
- **`Access authorization`**:
  - _4_: Authorized Account Only - Authorized account but not authorized access to targeted data.
- **`Employment type`**:
  - _CTR_: Contractor - Individual not directly employed by the organization whose job responsibilities they filling (self-employed or employed by a different, contracting organization).
- **`Hire date`**:
  - 2017-02-01
- **`Departure date`**:
  - 2017-07-01
- **`Tenure`**:
  - 2904:00:00

## Ttp

- **`Id`**:
  - ttp--aabe47dc-fecb-43f9-bf77-361b06504789
- **`Date`**:
  - 2017-03-09T12:00:00.000Z
- **`Sequence num`**:
  1
- **`Observed`**:
  False
- **`Number of times`**:
  1
- **`Ttp vocab`**:
  - IIDES
- **`Tactic`**:
  - _7_: Data Exfiltration - Data (or copies of data) is removed from the organization without permission or explicitly against permission to use in an unauthorized way.
- **`Technique`**:
  - _7.1_: Paper - Insider exfiltrates data through printed or hand-written materials (e.g., Insider takes screenshots of important data, prints the screenshots, and walks out of work with them).
- **`Location`**:

  - _1_: On-site - Action taken while on-site at an organizational facility.

- **`Hours`**:

  - _1_: During Work Hours - Insider took the action during their normal working hours.

- **`Device`**:

  - _1_: Company Desktop - Organization owned desktop workstation.
  - _9_: Printer/Copier/Fax - Printer, copier, or fax machine.

- **`Channel`**:

  - _9_: Other - Other type of channel not listed in this vocabulary.

- **`Description`**:
  - Winner printed and improperly removed classified intelligence reporting.

## Ttp

- **`Id`**:
  - ttp--aabe47dc-fecb-43f9-bf77-361b06504789
- **`Date`**:
  - 2017-03-09T12:00:00.000Z
- **`Sequence num`**:
  2
- **`Observed`**:
  False
- **`Number of times`**:
  1
- **`Ttp vocab`**:
  - IIDES
- **`Tactic`**:
  - _7_: Data Exfiltration - Data (or copies of data) is removed from the organization without permission or explicitly against permission to use in an unauthorized way.
- **`Technique`**:
  - _7.3_: Email - Insider exfiltrates data through electronic mail (e.g., Insider e-mailed confidential information to competitor).
- **`Location`**:

  - _o_:
  - _n_:
  - _-_:
  - _s_:
  - _i_:
  - _t_:
  - _e_:

- **`Hours`**:

  - _D_:
  - _u_:
  - _r_:
  - _i_:
  - _n_:
  - _g_:
  - - \*:
  - _w_:
  - _o_:
  - _r_:
  - _k_:
  - - \*:
  - _h_:
  - _o_:
  - _u_:
  - _r_:
  - _s_:

- **`Device`**:

  - _1_: Company Desktop - Organization owned desktop workstation.
  - _9_: Printer/Copier/Fax - Printer, copier, or fax machine.

- **`Channel`**:

  - _9_: Other - Other type of channel not listed in this vocabulary.

- **`Description`**:
  - Winner printed and improperly removed classified intelligence reporting.

## Org-relationship

- **`Id`**:
  - org-relationship--83271b80-b5de-410e-b7ba-3c93ca5cba08
- **`Org2`**:
  - organization--3d459486-b1b1-4886-9129-87b3458120b3
- **`Org1`**:
  - organization--3d459486-b1b1-4886-9129-87b3458120b4
- **`Relationship`**:
  - _V_:

## Source

- **`Id`**:
  - source--c989a0c4-a559-491a-ac63-2f8b0eaba126
- **`Title`**:
  - United States v. Winner
- **`Source type`**:
  - _1_: Court Document - Legal document from a court case.
- **`File type`**:
  - _html_:
- **`Date`**:
  - 2020-04-24
- **`Public`**:
  True
- **`Document`**:
  - https://casetext.com/case/united-states-v-winner-9

## Source

- **`Id`**:
  - source--32c2aa75-685a-4af5-ba0f-36921b8d1c18
- **`Title`**:
  - CASE STUDY Unlawful Retention and Transmission of National Defense Information
- **`Source type`**:
  - _5_: Media - News, blog, or similar publication.
- **`File type`**:
  - _pdf_:
- **`Date`**:
  -
- **`Public`**:
  True
- **`Document`**:
  - https://www.cdse.edu/Portals/124/Documents/casestudies/case-study-winner.pdf

## Source

- **`Id`**:
  - source--d7fba1ef-193d-4826-a551-ce6aa66150c3
- **`Title`**:
  - USA v. Reality Leigh Winner, No. 20-11692 (11th Cir. 2020)
- **`Source type`**:
  - _1_: Court Document - Legal document from a court case.
- **`File type`**:
  - _pdf_:
- **`Date`**:
  - 2020-12-07
- **`Public`**:
  True
- **`Document`**:
  - https://law.justia.com/cases/federal/appellate-courts/ca11/20-11692/20-11692-2020-12-07.html

## Source

- **`Id`**:
  - source--5e290802-9738-40a5-bb64-9544d8624995
- **`Title`**:
  - USA v. Reality Leigh Winner, No. 20-11692 (11th Cir. 2020)
- **`Source type`**:
  - _2_: DOJ Press Release - Press release from the Department of Justice or US Attorneys' Office.
- **`File type`**:
  - _html_:
- **`Date`**:
  - 2018-08-23
- **`Public`**:
  True
- **`Document`**:
  - https://www.justice.gov/opa/pr/federal-government-contractor-sentenced-removing-and-transmitting-classified-materials-news

## Source

- **`Id`**:
  - source--1c8da449-30ed-4b7b-89f7-9c8f272207ab
- **`Title`**:
  - Reality Winner, N.S.A. Contractor Accused of Leak, Was Undone by Trail of Clues
- **`Source type`**:
  - _5_: Media - News, blog, or similar publication.
- **`File type`**:
  - _html_:
- **`Date`**:
  - 2017-05-06
- **`Public`**:
  True
- **`Document`**:
  - https://www.nytimes.com/2017/06/06/us/politics/reality-leigh-winner-leak-nsa.html

## Source

- **`Id`**:
  - source--497d1b03-8c71-482f-9156-542d21e99fdf
- **`Title`**:
  - Reality Winner, Former N.S.A. Translator, Gets More Than 5 Years in Leak of Russian Hacking Report
- **`Source type`**:
  - _5_: Media - News, blog, or similar publication.
- **`File type`**:
  - _html_:
- **`Date`**:
  - 2018-08-23
- **`Public`**:
  True
- **`Document`**:
  - https://www.nytimes.com/2018/08/23/us/reality-winner-nsa-sentence.html

## Source

- **`Id`**:
  - source--a6e7705d-195f-4617-a2d2-30c84aadadea
- **`Title`**:
  - Original Court Documents: US v. Reality Leigh Winner
- **`Source type`**:
  - _1_: Court Document - Legal document from a court case.
- **`File type`**:
  - _pdf_:
- **`Date`**:
  - 2018-08-23
- **`Public`**:
  True
- **`Document`**:
  - https://standwithreality.org/original-court-documents/
