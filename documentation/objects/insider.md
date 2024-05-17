# Insider

Information about the insider involved in the incident. An incident can have multiple insiders.

## Properties

- **`id`** (required) *(string)* : A unique string that begins with "insider--" and is appended with a UUIDv4.
  - Uses pattern: ^insider--[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
- **`incident_role`** (required) *(string)* : Whether the insider was the primary actor, or had a different role in the incident.
	- A constant from [incident-role-vocab](#incident-role-vocab)
- **`motive`** *(array)* : The insider's motive(s) for the incident.
  - One or more constants from [motive-vocab](#motive-vocab)
- **`substance_use_during_incident`** *(boolean)* : Insider was using or abusing substance(s) at the time they took one or more actions related to the incident.
- **`psychological_issues`** *(array)* : Psychological issue(s) the insider experienced during or before the incident.
  - One or more constants from [psych-issues-vocab](#psych-issues-vocab)
- **`predispositions`** *(array)* : Insider's tendancy toward certain actions or qualities.
  - One or more tuple values of the format ([predisposition-type-vocab](#predisposition-type-vocab), [predisposition-subtype-vocab](#predisposition-subtype-vocab))
- **`concerning_behaviors`** *(array)* : Insider's history of past behavior that could indicate future issues.
  - One or more tuple values of the format ([cb-type-vocab](#cb-type-vocab), [cb-subtype-vocab](#cb-subtype-vocab))
- **`comment`** *(string)* : Comments or clarifications to any of the Insider properties.
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

### psych-issues-vocab

Constants: `01`, `02`, `03`, `04`, `05`, `99`

| Const | Value | Description |
| --- | --- | --- |
| 01 | Outpatient Treatment | Insider received treatment in which they were not hospitalized overnight, but rather visited a hospital, clinic, or associated facility for diagnosis or treatment.|
| 02 | Inpatient Treatment | Insider received treatment that involved 24-hour (including overnight) supervision at a hospital or dedicated psychiatric facility.|
| 03 | Medication Noncompliance | The insider stopped taking a prescribed medication or following a prescribed course of treatment for a particular medical or mental health condition which, in turn, could have impacted their mental faculties.|
| 04 | Delusions | The insider experienced or acted on delusions at some point during their employment within the organization.|
| 05 | Threatened/Attempted Suicide | Insider threatened or attempted to commit suicide at some point during their employment within the organization.|
| 99 | Other | Insider experienced specific psychological issues not specified in this vocabulary.|

### predisposition-type-vocab

Constants: `1`, `2`, `3`, `4`

| Const | Value | Description |
| --- | --- | --- |
| 1 | Social and Mental Health Issues | A history of behaviors related to the insider's mental health or unacceptable social behavior.|
| 2 | A History of Rule Violations | A history of violating the law or violating rules at other organizations.|
| 3 | Suspicious Associations | A history of associating with criminal or otherwise objectionable persons or entities.|
| 4 | Personal Stressful Events | Events in the insider's personal life that could lead to additional stress or futher motivate the insider to harm their organization.|

### predisposition-subtype-vocab

Constants: `1.1`, `1.2`, `1.3`, `1.4`, `1.5`, `1.6`, `1.7`, `2.1`, `2.2`, `2.3`, `2.4`, `2.5`, `2.6`, `2.7`, `3.1`, `3.2`, `4.1`, `4.2`, `4.3`, `4.4`

| Const | Value | Description |
| --- | --- | --- |
| 1.1 | Possible Psychological Issues | Possible or confirmed mental health condition or psychological problem. E.g., Insider shared they were feeling depressed.|
| 1.2 | Diagnosed Psychological Issues | Insider is diagnosed with a mental health problem. E.g., Insider put on medication for depression and antipsychotics.|
| 1.3 | Gambling Problems | Gambling activity that negatively affects other areas of their life. E.g., Insider frequently spends multiple hours at the casino every week.|
| 1.4 | Substance Abuse | A history of alcohol or drugs, either previous or ongoing. E.g., Insider showed up to work intoxicated.|
| 1.5 | A History Of Financial Problems | Existing financial issues, including medical bills for family members. E.g., Insider had previously filed for bankruptcy.|
| 1.6 | Poor Hygiene | Insider has poor general hygiene.|
| 1.7 | Risk Taker | Insider is referred to by co-workers, supervisors, or friends as a reckless or risk-taking individual.|
| 2.1 | Previous Arrest/Conviction For Related Crime | Involvement or conviction in a previous crime which is similar in nature to the current case. E.g., Insider executed similar fraud six years earlier. Misdemeanor conviction for the same conduct with probation sentence.|
| 2.2 | Previous Arrest/Conviction for Unrelated Crime | Involvement in a previous crime which is unrelated to the current case. E.g., Insider was previously arrested for assault.|
| 2.3 | Previous Perpetrator of Domestic Violence | Previously convicted or charged on a crime involving domestic violence. E.g., Insider was previously arrested for abusing spouse.|
| 2.4 | Hacking Related Activities | Involvement in activities focused on obtaining unauthorized access to or otherwise harming IT systems. E.g., Insider often discussed their hacking related activities on their website.|
| 2.5 | Previous Attempts to Disclose Through Illegitimate Means | Disclosing or attempting to disclose information through illegitimate means (i.e., not legally protected as a whistleblower).|
| 2.6 | Pending or Previous Defendant in Civil Action | The insider was previously found liable in a civil action, outside of the specific incident (i.e. where a insider was sued previously, which may be a motivation for the insider's actions).|
| 2.7 | Previous use of illegal substances | Known use of illegal narcotics, or illegal use of prescribed medications.|
| 3.1 | Criminal Association | Insider associates with known criminals or criminal organizations.|
| 3.2 | Internet Underground Association | Insider associates with or participates in darkweb groups or activities.|
| 4.1 | Medical Problems | Health issues experienced by anyone involved in the event since the insider's hire date. E.g., Insider contracted lupus and was put on medication.|
| 4.2 | Relationship Problems | A problem in one of the insider's relationships which affects the insider, including family and romantic relationships developed after the insider's hire date. E.g., Insider was going through a divorce.|
| 4.3 | Emerging Financial Problems | Monetary issues experienced by or relevant to the insider (including medical bills for family members) known to have developed after the insider's hire date. E.g., The insider claimed they stole from the organization in order to pay for their child's education.|
| 4.4 | Family Health Issues | Someone in the insider's family, or otherwise close to the insider, has health or medical issues.|

### cb-type-vocab

Constants: `3.1`, `3.2`, `3.3`, `3.4`, `3.5`, `3.6`, `3.7`

| Const | Value | Description |
| --- | --- | --- |
| 3.1 | Misuse of Company Resources | Using or abusing company resources in an unauthorized manner.|
| 3.2 | Technical Policy Abuse | Violating policies regarding the use of the organization's IT systems.|
| 3.3 | Interpersonal Issues | Conflicts with others in the organization or human resources (HR) issues.|
| 3.4 | Financial | Financial conflicts of interest or significant changes to financial status.|
| 3.5 | Organizational Conflict | Competitive conflicts of interest with the organization.|
| 3.6 | Suspicious Contact | Suspicious communication with or travel to entities, areas, or individuals that present a conflict of interest with the organization.|
| 3.7 | Relocation | Physical relocation.|

### cb-subtype-vocab

Constants: `3.1.1`, `3.1.2`, `3.1.3`, `3.2.1`, `3.2.2`, `3.2.3`, `3.2.4`, `3.2.5`, `3.2.6`, `3.3.1`, `3.3.2`, `3.3.3`, `3.3.4`, `3.3.5`, `3.3.6`, `3.3.7`, `3.3.8`, `3.3.9`, `3.3.10`, `3.3.11`, `3.3.12`, `3.3.13`, `3.4.1`, `3.4.2`, `3.4.3`, `3.5.1`, `3.5.2`, `3.5.3`, `3.5.4`, `3.5.5`, `3.5.6`, `3.6.1`, `3.6.2`, `3.6.3`, `3.6.4`, `3.7.1`

| Const | Value | Description |
| --- | --- | --- |
| 3.1.1 | Theft Of Physical Company Property | Stealing their employer's physical property. E.g., Insider reported a company laptop as stolen, but had it when they were arrested.|
| 3.1.2 | Insider Expressed Ownership Of Work | Acting as if they had personal right to any work done for the organization, despite knowledge of organizational right to employee work. E.g., Insider refused to return copy of code that they wrote because they felt entitled to it.|
| 3.1.3 | Repeated Security Violations - Non-Technical | Violating organizational security policies not related to IT systems. E.g., Insider broke into the school on multiple occasions and was also caught cheating.|
| 3.2.1 | Other Unauthorized Software Acquisition | Acquiring any sort of unauthorized software on an organizational system. E.g., The insider downloaded a password recovery tool from a website.|
| 3.2.2 | Repeated Security Violations - Technical | Multiple instances of security violations related to organizational IT systems, which are committed by the insider. E.g., Insider repeatedly let co-workers use their workstation.|
| 3.2.3 | Unauthorized Download - Remotely | Unapproved download from a remote distance. E.g., Insider logged into their company account from home on their personal laptop and downloaded torrents.|
| 3.2.4 | Unauthorized Download - On Site | Unapproved download from within the organization E.g., Insider used their company-issued workstation to download torrents.|
| 3.2.5 | IP Policy Violation | Violating any of the policies put in place by the company regarding their IP (i.e. trade secrets, patents, copyright, etc.).|
| 3.2.6 | Violation of Need to Know | Accessing organizational information which is not needed for their work, as defined by organizational policy.|
| 3.3.1 | Employee Extortion, Threats, or Legal Demands | Extortion, threats (physical, technical, legal, etc.) or legal demands against the organization. E.g., Insider threatened to sue company unless they agreed to the terms of their demands.|
| 3.3.2 | Conflict With Supervisor | Personal or work-related disputes with their supervisor. E.g., Insider was unhappy with their new boss, because the boss modified the organization's bonus system.|
| 3.3.3 | Conflict With Coworker(s) | Personal or work-related disputes with a coworker. E.g., Insider yelled at coworker for repeatedly parking in their spot.|
| 3.3.4 | Work Attendance Problems | Being late for work or having unexcused/unplanned absences from work, generally multiple times E.g., Insider reports late to work 7 times during the month of April.|
| 3.3.5 | Human Resource Policy Violations or Complaints | Violating the organization's Human Resource Policy, or making a formal complaint about something/someone within the organization. E.g., Insider made several complaints to management about their co-worker's noise level.|
| 3.3.6 | Disgruntled Employee | One who is upset with the organization and desires to get a measure of revenge against the organization. E.g., Insider grew disgruntled because of losing their 'star' status at the organization as it grew larger.|
| 3.3.7 | Bragging | The insider boasts about a concerning behavior to co-workers or online E.g., Insider boasted about being able to shut down the organization's system anytime they wanted.|
| 3.3.8 | Concurrent Crimes | The insider commits a second illegal action, while committing the unrelated illegal insider incident E.g., Insider indicted for domestic abuse while Insider committed the insider incident.|
| 3.3.9 | Formal Complaint | Organization receives complaints about the insider from a coworker that were officially documented.|
| 3.3.10 | Informal Complaint | Organization receives complaints about the insider from a coworker that were not officially documented.|
| 3.3.11 | Insubordination | Defiance or refusal to follow commands or instructions.|
| 3.3.12 | Physical Abuse/Harassment | Engaging in any type of physical abuse and/or harassment against another employee.|
| 3.3.13 | Sexual Harassment | Engaging in any type of sexual harassment against another employee.|
| 3.4.1 | Unexplained Wealth | A sudden increase in the amount of money the insider appears to have. E.g., Insider purchased $436,000 in personal items even though their annual salary was $50,000.|
| 3.4.2 | Employee Forms New Competing Business | Maintains a financial stake in another business or scheme that conflicts with their present employer. E.g., Insider invests in stocks of the victim organization's competitor.|
| 3.4.3 | Financial Conflict of Interest | Starting a business in the same area as their previous employer. E.g., Insider left one law firm to start their own law firm.|
| 3.5.1 | Planning/Contact with Competing Organization | onspiring with a competitor of the current employer in any way, including communication through an IT system. E.g., Insider e-mailed competing organization detailing plans to steal trade secrets.|
| 3.5.2 | Employee Went To Work For A Competing Organization | Leaving their current employer and joining a competing organization. E.g., Insider accepted a position at a competing technical firm before resigning from their current position.|
| 3.5.3 | Employee Sought Other Employment | Seeking another job while still employed with their current employer. E.g., Insider sent their resume to another organization.|
| 3.5.4 | Group Resignation | Two or more employees leave the organization at approximately the same time for similar reasons. E.g., All five insiders resigned simultaneously, then went to work for a competitor.|
| 3.5.5 | Insider Creates Legal Entity for Illegitimate Purpose | Creates a legal entity in order to move forward with scheme, or hide assets as a result of the scheme. E.g., insider creates a shell company to protect assets.|
| 3.5.6 | Falsified Background Information | Lies about or otherwise manipulates information about their background: personal or financial history, contacts, groups, etc.|
| 3.6.1 | Suspicious Foreign Contact | Tie(s) to foreign nation(s), such as company or independent travel, family members, telephone records, etc. E.g., Insider consistently calls former co-worker who now works in a non-allied country.|
| 3.6.2 | Suspicious Foreign Travel | Traveling to foreign nations that, if the travel was known, should raise concerns with the organization.|
| 3.6.3 | Foreign Travel - Work Related | Travel undertaken by the insider as required for their job. E.g., The insider's job required frequent travel to non-allied countries.|
| 3.6.4 | Planning/Contact with Conspirator | Conspiring with a conspirator in order to begin or further their particular scheme. E.g., Insider calls their partner-in-crime in order to establish attack details.|
| 3.7.1 | Geographic Relocation | Permanent move to a new physical location.|
