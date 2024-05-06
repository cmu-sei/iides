# Insider

Information about the insider involved in the incident. An incident can have multiple insiders.

## Properties

- **`id`** (required) *(string)* : A unique string that begins with "insider--" and is appended with a UUIDv4.
	- Uses pattern: ^insider--[UUIDv4]
- **`incident_role`** (required) *(string)* : whether the insider was the primary actor, or had a different role in the incident (e.g. co-conspirator, looked the other way, approved insider’s actions).
	- A constant from [incident-role-vocab](#incident-role-vocab)
- **`motive`** *(array)* : The insider's motive(s) for the incident.
	- One or more constants from [motive-vocab](#motive-vocab)
- **`substance_abuse`** *(array)* : Substances the insider was using or abusing.
	- One or more constants from [substance-abuse-vocab](#substance-abuse-vocab)
- **`substance_use_during_incident`** *(boolean)* : Insider was using or abusing substance(s) at the time they took one or more actions during the event.
- **`psychological_issues`** *(array)* : Psychological issue(s) the insider experienced during or before the incident.
	- One or more constants from [psych-issues-vocab](#psych-issues-vocab)
- **`predispositions`** *(array)* : Insider's tendancy toward certain actions or qualities.
	- One or more tuple values of the format ([predisposition-type-vocab](#predisposition-type-vocab), [predisposition-subtype-vocab](#predisposition-subtype-vocab))
- **`concerning_behaviors`** *(array)* : Insider's history of past behavior that could indicate future issues.
	- One or more tuple values of the format ([cb-type-vocab](#cb-type-vocab), [cb-subtype-vocab](#cb-subtype-vocab))
- **`comment`** *(string)* : Any additional comments to clarify responses to any of the fields in the Insider entity.
- **Inherits properties from [Person](person)**

## Vocabularies

### incident-role-vocab

Constants: `1`, `2`, `3`, `4`

| Const | Value | Description |
| --- | --- | --- |
| 1 | Primary | Insider is the primary perpetrator of the incident.|
| 2 | Co-Conspirator | Insider is a co-conspirator in the incident|
| 3 | Looked the other way | Insider looked the other way while the primary perpetrator conducted the incident.|
| 4 | Approved primary insider's actions | Insider knowingly approved the primary perpetrator's actions, such as by signing off on a fraudulent invoice.|

### motive-vocab

Constants: `01`, `02`, `03`, `04`, `05`, `06`, `07`, `08`, `99`

| Const | Value | Description |
| --- | --- | --- |
| 01 | Benefit Foreign Entity | Insider committed their attack to benefit a foreign entity, such as a foreign government or military.|
| 02 | Benefit New Employer | Insider committed their attack to benefit their new employer, such as by stealing a client list when they left the victim organization.|
| 03 | Competitive Business Advantage | Insider committed their attack in order to gain a business advantage for a competing company. Often, this is the insider starting their own company.|
| 04 | Curiosity | Insider committed the incident out of curiosity. E.g., Insider accessed medical records of a celebrity because they were curious of that celebrity's age.|
| 05 | Financial Gain | Insider committed their attack to make a profit.|
| 06 | Freedom of Information | The insider held the belief that it is in the best interest of the public to share the victim organization's confidential information with the public. E.g., sharing unfavorable test results of a product or unfavorable information about an organization's internal practices.|
| 07 | Recognition | The insider wanted to be recognized (e.g. for being smart, talented, capable, powerful, etc.)|
| 08 | Revenge | The insider wanted revenge for an actual or perceived wrong.|
| 99 | Other | Other motive not listed in this vocabulary.|

### substance-abuse-vocab

Constants: ``, ``, ``, ``, ``, ``, ``, ``, ``, ``

| Const | Value | Description |
| --- | --- | --- |
|  | alcohol | Evidence entered into the record that alleges that the insider abused alcohol.|
|  | marijuana | Evidence entered into the record that alleges that the insider used or abused marijuana.|
|  | legal_perscription_opiate | Legally prescribed opiate medication taken in excess.|
|  | illegal_perscription_opiate | Abuse of opiate medications (illegally obtained) such morphine, oxycodone, fentanyl, and hydromorphone or other opiate medications.|
|  | non_perscription_opiate | Abuse of non-prescription or illegal opiates such as heroin.|
|  | opiate_unknown | Unspecified opiate abuse.|
|  | non_opiate_perscription | The misuse/dependence on prescribed non-opiate medications. This frequently includes medication prescribed for ADHD such as Ritalin and Adderall.|
|  | stimulant | Evidence the insider abused stimulants such as cocaine or methamphetamines.|
|  | Street Drugs | Evidence the insider abused illicit substances not otherwise specified – may include designer drugs such as Molly, bath salts, and synthetic cannabinoids.|
|  | Other | Evidence of the insider abusing a substance of a type not listed in the above categories|

### psych-issues-vocab

Constants: ``, ``, ``, ``, ``, ``

| Const | Value | Description |
| --- | --- | --- |
|  | outpatient_treatment | Treatment in which they are not hospitalized overnight, but rather visits a hospital, clinic, or associated facility for diagnosis or treatment.|
|  | inpatient_treatment | Treatment that involved 24-hour (including overnight) supervision at a hospital or dedicated psychiatric facility.|
|  | medication_noncompliance | The insider not taking a prescribed medication or following a prescribed course of treatment for a particular medical or mental health condition which, in turn, could have impacted their mental faculties.|
|  | experienced_acted_on_delusions | The insider experiencing delusions and/or acting on them at some point during their employment within the organization.|
|  | threatened_attempted_suicide | The insider either threatening or attempting to commit suicide at some point during their employment within the organization.|
|  | other | The insider experienced specific psychological issues not specified in this list or not specified in the court documents.|

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
| 1.1.1 | Possible Psychological Issues | observed behaviors that indicate the insider may have a mental health condition or psychological problem (e.g., Insider shared they were feeling depressed)|
| 1.1.2 | Diagnosed Psychological Issues | facts that indicates the insider was diagnosed with a mental health problem (e.g., Insider put on medication for depression and antipsychotics).|
| 1.1.3 | Gambling Problems | the insider’s gambling negatively affecting other areas of his or her life (e.g., Insider frequently spends multiple hours at the casino every week.)|
| 1.1.4 | Substance Abuse | facts that indicate that the insider may have a history of alcohol or drugs, either previous or ongoing (e.g., Insider showed up to work intoxicated).|
| 1.1.5 | A History Of Financial Problems | existing monetary issues experienced by the insider, including medical bills for family members (e.g., Insider had previously filed for bankruptcy).|
| 1.1.6 | Poor Hygiene | the insider being known for having poor general hygiene|
| 1.1.7 | Risk Taker | the insider being known as a generally reckless individual|
| 1.2.1 | Previous Arrest/Conviction For Related Crime | the insider’s involvement or conviction in a previous crime which is similar in nature to the current case (e.g., Insider executed similar fraud six years earlier. Misdemeanor conviction for the same conduct with probation sentence).|
| 1.2.2 | Previous Arrest/Conviction for Unrelated Crime | the insider’s involvement in a previous crime which is unrelated to the current case (e.g., Insider was previously arrested for assault).|
| 1.2.3 | Previous Perpetrator of Domestic Violence | the insider previously convicted or charged on a crime involving domestic violence (e.g., Insider was previously arrested for abusing spouse).|
| 1.2.4 | Hacking Related Activities | insider involvement in activities focused on obtaining unauthorized access to or otherwise harming IT systems (e.g., Insider often discussed their hacking related activities on their website).|
| 1.2.5 | Previous Attempts to Disclose Through Illegitimate Means | The insider disclosing or attempting to disclose information through illegitimate means (i.e., not legally protected as a whistleblower)|
| 1.2.6 | Pending or Previous Defendant in Civil Action | The insider was previously found liable in a civil action, outside of the specific incident (i.e. where a insider was sued previously, which may be a motivation for the insider’s actions).|
| 1.3.1 | Criminal Association | TODO|
| 1.3.2 | Internet Underground Association | TODO|
| 2.4.1 | Medical Problems | health issues experienced by anyone involved in the event since the Insider’s hire date (e.g., Insider contracted lupus and was put on medication).|
| 2.4.2 | Relationship Problems | a problem in one of the insider’s relationships which affects the insider, including family and romantic relationships developed after the Insider’s hire date (e.g., Insider was going through a divorce).|
| 2.4.3 | Emerging Financial Problems | monetary issues experienced by or relevant to the Insider (including medical bills for family members) known to have developed after the Insider’s hire date (e.g., The insider claimed they stole from the organization in order to pay for their child’s education).|
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
| 3.1.1 | Theft Of Physical Company Property | The insider stealing their employer’s physical property (e.g., Insider reported a company laptop as stolen, but had it when they were arrested).|
| 3.1.2 | Insider Expressed Ownership Of Work | The insider acting as if they had personal right to any work done for the organization, despite knowledge of organizational right to employee work (e.g., Insider refused to return copy of code that they wrote because they felt entitled to it).|
| 3.1.3 | Repeated Security Violations - Non-Technical | The insider violating organization security policies not related to IT systems (e.g., Insider broke into the school on multiple occasions and was also caught cheating).|
| 3.2.1 | Other Unauthorized Software Acquisition | A user acquiring any sort of unauthorized software on an organizational system (e.g., The insider downloaded a password recovery tool from a website).|
| 3.2.2 | Repeated Security Violations - Technical | Multiple instances of security violations related to organizational IT systems, which are committed by the insider (e.g., Insider repeatedly let co-workers use their workstation).|
| 3.2.3 | Unauthorized Download - Remotely | An unapproved download from a remote distance (e.g., Insider logged into his company account from home on his personal laptop and downloaded torrents).|
| 3.2.4 | Unauthorized Download - On Site | An unapproved download from within the company’s confines (e.g., Insider used his company-issued workstation to download torrents).|
| 3.2.5 | IP Policy Violation | An violation of the policies put in place by the company regarding their IP (i.e. trade secrets, patents, copyright, etc.).|
| 3.2.6 | Violation of Need to Know | The insider accessed organizational information which is not needed for their work, as defined by organizational policy|
| 3.3.1 | Employee Extortion, Threats, or Legal Demands | An insider action towards the organization that amounts to extortion, threats (physical, technical, legal, etc.) or actual legal demands (e.g., Insider threatened to sue company unless they agreed to the terms of their demands).|
| 3.3.2 | Conflict With Supervisor | The insider having personal or work-related disputes with their supervisor (e.g., Insider was unhappy with their new boss, because the boss modified the organization’s bonus system).|
| 3.3.3 | Conflict With Coworker(s) | The insider having personal or work-related disputes with a coworker (e.g., Insider yelled at coworker for repeatedly parking in their spot).|
| 3.3.4 | Work Attendance Problems | The insider being late for work or having unexcused/unplanned absences from work, generally multiple times (e.g., Insider reports late to work 7 times during the month of April).|
| 3.3.5 | Human Resource Policy Violations or Complaints | the insider violating the organization’s Human Resource Policy, or the Insider making a formal complaint about something/someone within the organization (e.g., Insider made several complaints to management about their co-worker’s noise level).|
| 3.3.6 | Disgruntled Employee | an insider who is upset with the organization and desires to get a measure of revenge against the organization (e.g., Insider grew disgruntled because of losing their 'star' status at the organization as it grew larger).|
| 3.3.7 | Bragging | The insider boasting about a concerning behavior to co-workers or online (e.g., Insider boasted about being able to shut down the organization’s system anytime they wanted).|
| 3.3.8 | Concurrent Crimes | The insider commits a second illegal action, while committing the unrelated illegal insider incident (e.g., Insider indicted for domestic abuse while Insider committed the insider incident).|
| 3.3.9 | Formal Complaint | The insider received complaints from a coworker that were officially documented within the organization|
| 3.3.10 | Informal Complaint | The insider received complaints from a coworker that were not officially documented within the organization|
| 3.3.11 | Insubordination | The insider was defiant and refused to follow commands or instructions|
| 3.3.12 | Physical Abuse/Harassment | The insider engaged in any type of physical abuse and/or harassment against another employee|
| 3.3.13 | Sexual Harassment | The insider engaged in any type of sexual harassment against another employee|
| 3.4.1 | Unexplained Wealth | A sudden increase in the amount of money the insider appears to have (e.g., Insider purchased $436,000 in personal items even though their annual salary was $50,000).|
| 3.4.2 | Employee Forms New Competing Business | An insider maintaining a financial stake in another business or scheme that conflicts with their present employer (e.g., Insider invests in stocks of the victim organization’s competitor).|
| 3.4.3 | Financial Conflict of Interest | The insider starting a business in the same area as his or her previous employer (e.g., Insider left one law firm to start their own law firm).|
| 3.5.1 | Planning/Contact with Competing Organization | The insider conspiring with a competitor of the current employer in any way, including communication through an IT system (e.g., Insider e-mailed competing organization detailing plans to steal trade secrets).|
| 3.5.2 | Employee Went To Work For A Competing Organization | the insider leaving his or her current employer and joining a competing organization (e.g., Insider accepted a position at a competing technical firm before resigning from their current position).|
| 3.5.3 | Employee Sought Other Employment | the insider seeking another job while still employed with their current employer (e.g., Insider sent their resume to another organization).|
| 3.5.4 | Group Resignation | two or more employees leaving the organization at approximately the same time for similar reasons (e.g., All five insiders resigned simultaneously, then went to work for a competitor).|
| 3.5.5 | Insider Creates Legal Entity for Illegitimate Purpose | The insider creates a legal entity in order to move forward with scheme, or hide assets as a result of the scheme (e.g., insider creates a shell company to protect assets).|
| 3.5.6 | Falsified Background Information | the insider having any tie(s) to foreign nation(s) in any way, such as company or independent travel, family members, telephone records, etc. (e.g., Insider consistently calls former co-worker who now works in China).|
| 3.6.1 | Suspicious Foreign Contact | the insider having any tie(s) to foreign nation(s) in any way, such as company or independent travel, family members, telephone records, etc. (e.g., Insider consistently calls former co-worker who now works in China).|
| 3.6.2 | Suspicious Foreign Travel | the insider traveling to foreign nations that, if the travel was known, should raise concerns with the organization (e.g., Insider, a government employee, frequently traveled to Russia).|
| 3.6.3 | Foreign Travel - Work Related | travel undertaken by the insider as required for his or her job (e.g., The insider's job required frequent travel to Middle Eastern countries).|
| 3.6.4 | Planning/Contact with Conspirator | the insider conspiring with a conspirator in order to begin or further their particular scheme (e.g., Insider calls their partner-in-crime in order to establish attack details).|
| 3.7.1 | Geographic Relocation | TODO|
