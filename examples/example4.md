# Example4


## Incident

- **`Id`**: incident--843c85b1-6f2d-4a64-a959-d9880905114f
- **`Cia effect`**: 
  - Confidentiality (*C*) &mdash; The protection of information from unauthorized access or disclosure.
- **`Incident type`**: 
  - Espionage (*E*) &mdash; The covert or illicit practice of spying on a foreign government, organization, entity, or person to obtain confidential information for military, political, strategic, or financial advantage.
- **`Incident subtype`**: 
  - Government (*E2*) &mdash; Covert intelligence-gathering activities to obtain government or military secrets for the benefit of another government to obtain political or military advantage.
- **`Outcome`**: 
  - Data Stolen (*DS*) &mdash; Any organizational information or assets that are stolen.
  - Data Read (*DR*) &mdash; Organizational data was read by the insider.
- **`Status`**: Closed (*C*) &mdash; All investigations and legal proceedings are closed.
- **`Summary`**: The insider was a former CIA officer. They were involved in a espionage case where they were convicted of providing classified U.S. Defence information to Chinese intelligence agents, which began in 2017. The insider was motivated by financial gain: the Chinese officials would exchange top secret information for money. Once the FBI became aware, they investigated the insider, and found evidence of espionage in their home. The insider was then tried and found guilty of several espionage charges, and sentenced to 20 years of federal prison.
- **`Brief summary`**: The insider was a former CIA officer who began to communicate with Chinese intelligence agents in 2017. They began communicating, and the insider would receive money for trasmitting classified U.S. defense information to Chinese intelligence agents. The insider was later investigated and brought to court, where he was convicted of multiple counts of espionage.

## Insider

- **`Id`**: insider--80fea631-33e6-440b-b86d-2d49c8d7fcd2
- **`Incident role`**: Primary (*1*) &mdash; Insider is the primary perpetrator of the incident.
- **`Motive`**: 
  - Benefit Foreign Entity (*1*) &mdash; Insider committed their attack to benefit a foreign entity, such as a foreign government or military.
- **`Substance use during incident`**: False
- **`Predispositions`**: 
  - Personal Stressful Events (*['4', '4.3']*) &mdash; Events in the insider's personal life that could lead to additional stress or futher motivate the insider to harm their organization.
- **`Concerning behaviors`**: 
  - Suspicious Contact (*['3.6', '3.6.1']*) &mdash; Suspicious communication with or travel to entities, areas, or individuals that present a conflict of interest with the organization.
- **`First name`**:
 Kevin
- **`Middle name`**:
 Patrick
- **`Last name`**:
 Mallory
- **`Alias`**:
 ['Patrick Mallory', 'Kevin P. Mallory']
- **`City`**:
 Leesburg
- **`State`**:
 VA
- **`Country`**:
 US
- **`Postal code`**:
 20175
- **`Country of citizenship`**:
 ['US']
- **`Nationality`**:
 ['US']
- **`Gender`**:
 M
- **`Age`**:
 60
- **`Education`**:
 5
- **`Marital status`**:
 2
- **`Number of children`**:
 3

## Organization

- **`Id`**: organization--9b495e20-ae37-4df3-920e-88338b1298b5
- **`Name`**: U.S. Central Intelligence Agency
- **`City`**: Washington
- **`State`**: D.C.
- **`Country`**: US
- **`Postal code`**: 20,505
- **`Small business`**: False
- **`Industry sector`**: Public Administration (*92*) &mdash; Federal/State/Local administration and the oversight of public programs.
- **`Industry subsector`**: National Security (*92.811*) &mdash; This industry comprises government establishments of the Armed Forces, including the National Guard, primarily engaged in national security and related activities.
- **`Business`**: The CIA, or Central Intelligence Agency, is an independent U.S. government agency focused on foreign intelligence and national security. They collect information about other countries, analyze it, and deliver it to policymakers to help them make decisions.
- **`Parent company`**: U.S. Intelligence Community
- **`Incident role`**: Primary Victim (*V*) &mdash; The organization was the primary victim organization of the insider's actions.

## Organization

- **`Id`**: organization--df77b634-a57b-4654-8e1e-77fd5220fe81
- **`Name`**: Chinese Intelligence Agency
- **`Country`**: CN
- **`Small business`**: False
- **`Industry sector`**: Public Administration (*92*) &mdash; Federal/State/Local administration and the oversight of public programs.
- **`Industry subsector`**: National Security (*92.811*) &mdash; This industry comprises government establishments of the Armed Forces, including the National Guard, primarily engaged in national security and related activities.
- **`Business`**: The Chinese Intelligence Agency is a Chinese agency focused on foreign intelligence and national security. 
- **`Parent company`**: Chinese National Government
- **`Incident role`**: Beneficiary (*B*) &mdash; The organization accepted trade secrets, customer lists, intellectual property, etc. that the insider obtained through the incident.

## Detection

The insider willingly contacted an acquaintance who worked in the CIA to get in touch with CIA security, indicating to the acquaintance that they had been approached by Chinese intelligence agents. There were CIA and FBI agents present during the interview, and the insider was 'visibly surprised' when secure chat messages showing their espionage appeared on the screen. The FBI agents then realized that something was astray and investigated the insider thoroughly.

- **`Id`**: detection--28ab62a7-ef29-478d-9fcd-b06bd11dfbc6
- **`First detected`**: date-time
- **`Who detected`**: 
  - Law Enforcement (*LE*) &mdash; Law enforcement discovered the insider's illegal activity (e.g., Police noticed that the insider was gaining access to the company after hours).
- **`Detected method`**: 
  - Non-Technical Means (*3*) &mdash; The insider's activity was detected in a non-technical fashion (e.g., The insider had personal items purchased with a company credit card sent to the office by accident).
- **`Logs`**: 
  - Email Logs (*EM*) &mdash; Logs from email servers or services.

## Impact

- **`Id`**: impact--1d3ccef3-2975-4d62-84c9-d798ec888ae6
- **`High`**: 12
- **`Low`**: 3
- **`Metric`**: Documents (*4*) &mdash; The number of physical or digital documents effected (stolen, deleted, modified, etc.).
- **`Estimated`**: True

## Target

- **`Id`**: target--54d887da-7f59-47e1-ad5a-d611f78030da
- **`Asset type`**: Information (*2*) &mdash; Data/business materials which contain important details belonging to a specific target owner.
- **`Category`**: Government/Law Enforcement Information (*2.3*) &mdash; Classified or sensitive government or law enforcement information.
- **`Subcategory`**: Classified Information (*2.3.1*) &mdash; Information that is restricted by the government for reasons of national security.
- **`Format`**: Electronic (*1*) &mdash; Technological digital format.
- **`Owner`**: Organization (*O*) &mdash; The organization, rather than its employees or customers owns the target.
- **`Sensitivity`**: 
  - Top Secret (TS) (*6*) &mdash; Top secret, unauthorized disclosure would cause exceptionally grave damage to national security

## Response

- **`Id`**: response--eb4d3760-213c-4f3b-81c2-b7805376c369
- **`Technical controls`**:
 [['2', '2012-01-01']]
- **`Investigated by`**:
 ['3']
- **`Investigation events`**:
 [['1', '2017-06-22'], ['2', '2017-06-22'], ['3', '2017-05-24']]

## Court-case



- **`Id`**: court-case--4715b227-cee7-49b4-95a0-f418ceb31ae5
- **`Case number`**: 1:17-cr-154
- **`Case title`**: United States v. Mallory
- **`Court country`**: United States of America
- **`Court state`**: Virginia
- **`Court district`**: Eastern District of Virginia
- **`Court type`**: Federal (*1*) &mdash; Top level government court.
- **`Case type`**: Criminal (*2*) &mdash; A case dealing with a violation of criminal law.
- **`Defendant`**: 
  - United States of America
- **`Plaintiff`**: 
  - Kevin Patrick Mallory

## Charge

- **`Id`**: charge--80e9f464-867a-4c2d-a0d5-da3303fef9f8
- **`Title`**: 18 U.S.C.
- **`Section`**: 794(c)
- **`Nature of offense`**: Conspiracy to gather or deliver defense information to aid a foreign government.
- **`Count`**: 1
- **`Plea`**: Not Guilty (*3*) &mdash; The defendant pleaed not guilty to a charge.
- **`Plea bargain`**: False
- **`Disposition`**: Convicted (*2*) &mdash; Plead or been found guilty by a court.

## Charge

- **`Id`**: charge--de9ef24e-dd8e-4c1b-b55f-7431c324e2ad
- **`Title`**: 18 U.S.C
- **`Section`**: 794(a)
- **`Nature of offense`**: Delivery of defense information to aid a foreign government.
- **`Count`**: 1
- **`Plea`**: Not Guilty (*3*) &mdash; The defendant pleaed not guilty to a charge.
- **`Plea bargain`**: False
- **`Disposition`**: Convicted (*2*) &mdash; Plead or been found guilty by a court.

## Charge

- **`Id`**: charge--b5f8ebff-7449-4919-8e83-712df4dbbd28
- **`Title`**: 18 U.S.C
- **`Section`**: 794(a)
- **`Nature of offense`**: Attempted delivery of defense information to aid a foreign government.
- **`Count`**: 1
- **`Plea`**: Not Guilty (*3*) &mdash; The defendant pleaed not guilty to a charge.
- **`Plea bargain`**: False
- **`Disposition`**: Convicted (*2*) &mdash; Plead or been found guilty by a court.

## Charge

- **`Id`**: charge--8f108155-293c-4c7b-b780-eba524e55c9c
- **`Title`**: 18 U.S.C
- **`Section`**: 1001(a)(2)
- **`Nature of offense`**: Making material false statements.
- **`Count`**: 1
- **`Plea`**: Not Guilty (*3*) &mdash; The defendant pleaed not guilty to a charge.
- **`Plea bargain`**: False
- **`Disposition`**: Convicted (*2*) &mdash; Plead or been found guilty by a court.

## Sentence

- **`Id`**: sentence--7b9161b8-ee82-4e11-945a-31af4e284ddd
- **`Sentence type`**: Incarceration (*9*) &mdash; Imprisonment.
- **`Quantity`**: 20
- **`Metric`**: Year(s) (*4*) &mdash; Imposed sentence is in terms of years. E.g. 5 years no Internet access.
- **`Concurrency`**: False

## Legal-response

- **`Id`**: legal-response--037be7c2-d741-4153-8c85-1483bc7b2e9d
- **`Law enforcement contacted`**: 2017-05-12
- **`Insider arrested`**: 2017-06-22
- **`Insider charged`**: 2017-07-27
- **`Insider pleads`**: 2017-07-28
- **`Insider judgment`**: 2018-06-08
- **`Insider sentenced`**: 2019-05-17
- **`Insider charges dropped`**: 
- **`Insider charges dismissed`**: 
- **`Insider settled`**: 

## Job

- **`Id`**: job--ca6321b3-c176-4c2a-af6f-c825c5e1a823
- **`Job function`**: Protective Service (*33*) &mdash; Protective Service
- **`Occupation`**: Supervisors of Protective Service Workers (*33.1*) &mdash; First-Line Supervisors of Protective Service Workers
- **`Title`**: Case Officer/Contractor
- **`Position technical`**: False
- **`Access authorization`**: Authorized Privileged User (*5*) &mdash; Authorized privileged access.
- **`Employment type`**: Full-time (*FLT*) &mdash; Individual who is directly employed by the organization and works at least 35 hours per week (or is classified by the organization as a full-time employee).
- **`Hire date`**: 1992-01-01
- **`Departure date`**: 2012-01-01
- **`Tenure`**: 175200:00:00

## Job

- **`Id`**: job--79bce694-5bd1-4fb3-bcb1-258d09fca301
- **`Job function`**: Other (*99*) &mdash; Other job function not listed in this vocabulary.
- **`Occupation`**: Other (*99.9*) &mdash; Other occupation not listed.
- **`Title`**: Consultant
- **`Position technical`**: False
- **`Access authorization`**: Former Employee, Access not Deactivated (*7*) &mdash; Access was not properly revoked after departure from the organization.
- **`Employment type`**: Contractor (*CTR*) &mdash; Individual not directly employed by the organization whose job responsibilities they filling (self-employed or employed by a different, contracting organization).
- **`Hire date`**: 2012-01-01
- **`Departure date`**: 2017-07-01
- **`Tenure`**: 48192:00:00

## Stressor

Insider was behind 2 mortgage payments and had debt they wished to pay.

- **`Id`**: stressor--40650474-f431-4ddb-9e3a-417bab254ac1
- **`Date`**: 2017-02-01
- **`Category`**: Unmet Expectations (*3*) &mdash; Insider's expectations of/from their employer were not met.
- **`Subcategory`**: Compensation/Benefit Issues (*3.1*) &mdash; Insider expressed dissatisfaction with current compensation or benefits.

## Ttp

- **`Id`**: ttp--c130b8ca-6d8f-4696-a835-4d35448e8607
- **`Date`**: 2017-02-21
- **`Sequence num`**: 2
- **`Observed`**: False
- **`Number of times`**: 7
- **`Ttp vocab`**: IIDES
- **`Tactic`**: Data Exfiltration (*7*) &mdash; Data (or copies of data) is removed from the organization without permission or explicitly against permission to use in an unauthorized way.
- **`Technique`**: Own Account After Termination/Resignation (*1.6*) &mdash; Insider gains access to their company account after their termination date.
- **`Location`**: 
  - 
  - 
  - 
  - 
  - 
  - 
- **`Hours`**: 
  - Outside of Work Hours (*2*) &mdash; Insider took the action outside of their normal working hours.
- **`Device`**: 
  - Personal Mobile Device (*8*) &mdash; Personally owned moble device.
- **`Channel`**: 
  - Personal Phone (*6*) &mdash; A phone the organization does not control or monitor.
- **`Description`**: The insider communicated repeatedly with Chinese Intelligence officers to exchange top secret information for money.

## Ttp

- **`Id`**: ttp--def6dff4-cbf6-4cc5-adf6-a6880c9dc1c2
- **`Date`**: 2017-02-01
- **`Sequence num`**: 1
- **`Observed`**: False
- **`Number of times`**: 1
- **`Ttp vocab`**: IIDES
- **`Tactic`**: Recruitment (*2*) &mdash; Insider recruits, or is recruited by others.
- **`Technique`**: Outsider Recruits Insider (*2.1*) &mdash; An outside entity that is not a competing organization encourages the insider to become an insider. E.g., Insider is contacted by known hacking specialist who asks insider to divulge company secrets to the hacker.
- **`Location`**: 
  - 
  - 
  - 
  - 
  - 
  - 
- **`Hours`**: 
  - Outside of Work Hours (*2*) &mdash; Insider took the action outside of their normal working hours.
- **`Device`**: 
  - Personal Computer (*7*) &mdash; Personally owned computer.
- **`Channel`**: 
  - Online Forum (*4*) &mdash; Private or public forum accessed via the Internet.
- **`Description`**: The insider was initially recruited by a Chinese Intelligence Agent reaching out on LinkedIn asking to meet in China.

## Ttp

- **`Id`**: ttp--820373f2-e55f-45bf-9a75-6a6b5e38cc3c
- **`Date`**: 2017-03-01
- **`Sequence num`**: 1
- **`Observed`**: False
- **`Number of times`**: 1
- **`Ttp vocab`**: IIDES
- **`Tactic`**: Recruitment (*2*) &mdash; Insider recruits, or is recruited by others.
- **`Technique`**: Outsider Recruits Insider (*2.1*) &mdash; An outside entity that is not a competing organization encourages the insider to become an insider. E.g., Insider is contacted by known hacking specialist who asks insider to divulge company secrets to the hacker.
- **`Location`**: 
  - 
  - 
  - 
  - 
  - 
  - 
- **`Hours`**: 
  - Outside of Work Hours (*2*) &mdash; Insider took the action outside of their normal working hours.
- **`Device`**: 
  - Personal Computer (*7*) &mdash; Personally owned computer.
- **`Channel`**: 
  - Online Forum (*4*) &mdash; Private or public forum accessed via the Internet.
- **`Description`**: The insider was initially recruited by a Chinese Intelligence Agent reaching out on LinkedIn asking to meet in China.

## Source

- **`Id`**: source--370b7bf9-46a4-44f4-8229-dce1c0824b62
- **`Title`**: Former C.I.A. Officer Sentenced to 20 Years After Spying for China
- **`Source type`**: Media (*5*) &mdash; News, blog, or similar publication.
- **`File type`**: html
- **`Date`**: 2019-05-17
- **`Public`**: True
- **`Document`**: https://www.nytimes.com/2019/05/17/us/politics/cia-spying-china.html

## Source

- **`Id`**: source--43dfd29e-60c0-4aaa-933f-a96c2845887e
- **`Title`**: US v. Kevin Mallory, No. 19-4385 (4th Cir. 2022)
- **`Source type`**: Court Document (*1*) &mdash; Legal document from a court case.
- **`File type`**: pdf
- **`Date`**: 2022-07-11
- **`Public`**: True
- **`Document`**: https://law.justia.com/cases/federal/appellate-courts/ca4/19-4385/19-4385-2022-07-11.html#:~:text=Kevin%20Mallory%2C%20No.-,19%2D4385%20(4th%20Cir.,2022)&text=A%20jury%20convicted%20Defendant%20of,in%20violation%20of%2018%20U.S.C.

## Source

- **`Id`**: source--0ae6419b-66e3-4d9f-bcb6-531cc8a4e53a
- **`Title`**: United States of America v. Kevin Patrick Mallory
- **`Source type`**: Court Document (*1*) &mdash; Legal document from a court case.
- **`File type`**: pdf
- **`Date`**: 2017-06-21
- **`Public`**: True
- **`Document`**: https://www.justice.gov/opa/press-release/file/975671/dl

## Source

- **`Id`**: source--ada0e3cc-5048-4509-ad62-c06c7d34594f
- **`Title`**: United States v. Mallory (2020)
- **`Source type`**: Court Document (*1*) &mdash; Legal document from a court case.
- **`File type`**: html
- **`Date`**: 2020-10-05
- **`Public`**: True
- **`Document`**: https://caselaw.findlaw.com/court/us-dis-crt-e-d-vir-ale-div/2173526.html

## Source

- **`Id`**: source--9fe4a90d-abf1-4db6-a4e1-a30e37b3ffe6
- **`Title`**: United States v. Mallory (2022)
- **`Source type`**: Court Document (*1*) &mdash; Legal document from a court case.
- **`File type`**: html
- **`Date`**: 2022-07-11
- **`Public`**: True
- **`Document`**: https://caselaw.findlaw.com/court/us-4th-circuit/2178971.html

## Source

- **`Id`**: source--265815a9-494f-4034-b2cf-2d28e01b1318
- **`Title`**: United States v. Mallory, Criminal No. 1:17-CR-154
- **`Source type`**: Court Document (*1*) &mdash; Legal document from a court case.
- **`File type`**: html
- **`Date`**: 2018-10-15
- **`Public`**: True
- **`Document`**: https://case-law.vlex.com/vid/united-states-v-mallory-888386269

## Sponsor

- **`Id`**: sponsor--0378da70-22a9-4998-ab9f-3fdd9f690247
- **`Name`**: Chinese Intelligence Agency
- **`Sponsor type`**: Foreign National (*FN*) &mdash; An individual whose objectives are aligned with either the political, commercial, or military interests of a country other than where the incident originated.
