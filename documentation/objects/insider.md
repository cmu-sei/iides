# Insider

This is information about the insider involved in the incident. An incident can have multiple insiders.

## Properties

- **`id`** (required) _(string)_ : A unique string that begins with "insider--" and is appended with a UUIDv4
  - Uses pattern: ^insider--[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
- **`incident_role`** (required) _(string)_ : Whether the insider was the primary actor or had a different role in the incident
  - A constant from [incident-role-vocab](#incident-role-vocab)
- **`motive`** _(array)_ : The insider's motive(s) for the incident
  - One or more constants from [motive-vocab](#motive-vocab)
- **`substance_use_during_incident`** _(boolean)_ : Insider was using or abusing substance(s) at the time they took one or more actions related to the incident
- **`psychological_issues`** _(array)_ : Psychological issue(s) the insider experienced during or before the incident
  - One or more constants from [psych-issues-vocab](#psych-issues-vocab)
- **`predispositions`** _(array)_ : Insider's tendency toward certain actions or qualities
  - One or more tuple values of the format ([predisposition-type-vocab](#predisposition-type-vocab), [predisposition-subtype-vocab](#predisposition-subtype-vocab))
- **`concerning_behaviors`** _(array)_ : Insider's history of past behavior that could indicate future issues
  - One or more tuple values of the format ([concerning-behavior-vocab](#concerning-behavior-vocab), [cb-subtype-vocab](#cb-subtype-vocab))
- **Inherits properties from [Person](person)**

## Vocabularies

### incident-role-vocab

Constants: `1`, `2`, `3`, `4`

| Const | Value                              | Description                                                                                                  |
| ----- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| 1     | Primary                            | Insider is the primary perpetrator of the incident                                                           |
| 2     | Co-Conspirator                     | Insider is a co-conspirator in the incident                                                                  |
| 3     | Looked the other way               | Insider looked the other way while the primary perpetrator conducted the incident                            |
| 4     | Approved primary insider's actions | Insider knowingly approved the primary perpetrator's actions, such as by signing off on a fraudulent invoice |

### motive-vocab

Constants: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `99`

| Const | Value                          | Description                                                                                                                                                                                                                                                                       |
| ----- | ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Benefit Foreign Entity         | Insider committed their attack to benefit a foreign entity, such as a foreign government or military                                                                                                                                                                              |
| 2     | Benefit New Employer           | Insider committed their attack to benefit their new employer, such as by stealing a client list when they left the victim organization                                                                                                                                            |
| 3     | Competitive Business Advantage | Insider committed their attack in order to gain a business advantage for a competing company. Often, this is the insider starting their own company                                                                                                                               |
| 4     | Curiosity                      | Insider committed the incident out of curiosity. E.g., Insider accessed medical records of a celebrity because they were curious of that celebrity's age                                                                                                                          |
| 5     | Financial Gain                 | Insider committed their attack to make a profit                                                                                                                                                                                                                                   |
| 6     | Freedom of Information         | The insider held the belief that it is in the best interest of the public to share the victim organization's confidential information with the public (e.g., sharing unfavorable test results of a product or unfavorable information about an organization's internal practices) |
| 7     | Recognition                    | The insider wanted to be recognized (e.g., for being smart, talented, capable, powerful, etc.)                                                                                                                                                                                    |
| 8     | Revenge                        | The insider wanted revenge for an actual or perceived wrong                                                                                                                                                                                                                       |
| 99    | Other                          | Other motive not listed in this vocabulary                                                                                                                                                                                                                                        |

### psych-issues-vocab

Constants: `1`, `2`, `3`, `4`, `5`, `6`, `99`

| Const | Value                        | Description                                                                                                                                                                                                     |
| ----- | ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Outpatient Treatment         | Insider received treatment in which they were not hospitalized overnight, but rather visited a hospital, clinic, or associated facility for diagnosis or treatment                                              |
| 2     | Inpatient Treatment          | Insider received treatment that involved 24-hour (including overnight) supervision at a hospital or dedicated psychiatric facility                                                                              |
| 3     | Medication Noncompliance     | The insider stopped taking a prescribed medication or following a prescribed course of treatment for a particular medical or mental health condition which, in turn, could have impacted their mental faculties |
| 4     | Delusions                    | The insider experienced or acted on delusions at some point during their employment within the organization                                                                                                     |
| 5     | Threatened/Attempted Suicide | Insider threatened or attempted to commit suicide at some point during their employment within the organization                                                                                                 |
| 6     | Depression/Anxiety           | Insider expressed issues with or was diagnosed with depression or anxiety                                                                                                                                       |
| 99    | Other                        | Insider experienced specific psychological issues not specified in this vocabulary                                                                                                                              |

### predisposition-type-vocab

Constants: `1`, `2`, `3`, `4`

| Const | Value                           | Description                                                                                                                           |
| ----- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Social and Mental Health Issues | A history of behaviors related to the insider's mental health or unacceptable social behavior                                         |
| 2     | A History of Rule Violations    | A history of violating the law or violating rules at other organizations                                                              |
| 3     | Suspicious Associations         | A history of associating with criminal or otherwise objectionable persons or entities                                                 |
| 4     | Personal Stressful Events       | Events in the insider's personal life that could lead to additional stress or further motivate the insider to harm their organization |

### predisposition-subtype-vocab

Constants: `1.1`, `1.2`, `1.3`, `1.4`, `1.5`, `1.6`, `1.7`, `2.1`, `2.2`, `2.3`, `2.4`, `2.5`, `2.6`, `2.7`, `3.1`, `3.2`, `4.1`, `4.2`, `4.3`, `4.4`

| Const | Value                                                    | Description                                                                                                                                                                                                                                                           |
| ----- | -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.1   | Possible Psychological Issues                            | Possible or confirmed mental health condition or psychological problem (e.g., the insider shared they were feeling depressed)                                                                                                                                         |
| 1.2   | Diagnosed Psychological Issues                           | Insider is diagnosed with a mental health problem (e.g., the insider put on medication for depression and antipsychotics)                                                                                                                                             |
| 1.3   | Gambling Problems                                        | Gambling activity that negatively affects other areas of their life (e.g., the insider frequently spends multiple hours at the casino every week)                                                                                                                     |
| 1.4   | Substance Abuse                                          | A history of alcohol or drugs, either previous or ongoing (e.g., the insider showed up to work intoxicated)                                                                                                                                                           |
| 1.5   | A History Of Financial Problems                          | Existing financial issues, including medical bills for family members (e.g., the insider had previously filed for bankruptcy)                                                                                                                                         |
| 1.6   | Poor Hygiene                                             | Insider had poor general hygiene                                                                                                                                                                                                                                      |
| 1.7   | Risk Taker                                               | Insider was referred to by co-workers, supervisors, or friends as a reckless or risk-taking individual                                                                                                                                                                |
| 2.1   | Previous Arrest/Conviction For Related Crime             | Involvement or conviction in a previous crime which is similar in nature to the current case (e.g., the insider executed similar fraud six years earlier. Misdemeanor conviction for the same conduct with probation sentence)                                        |
| 2.2   | Previous Arrest/Conviction for Unrelated Crime           | Involvement in a previous crime which is unrelated to the current case (e.g., the insider was previously arrested for assault)                                                                                                                                        |
| 2.3   | Previous Perpetrator of Domestic Violence                | Previously convicted or charged on a crime involving domestic violence (e.g., the insider was previously arrested for abusing spouse)                                                                                                                                 |
| 2.4   | Hacking Related Activities                               | Involvement in activities focused on obtaining unauthorized access to or otherwise harming IT systems (e.g., the insider often discussed their hacking related activities on their website)                                                                           |
| 2.5   | Previous Attempts to Disclose Through Illegitimate Means | Disclosing or attempting to disclose information through illegitimate means (i.e., not legally protected as a whistleblower)                                                                                                                                          |
| 2.6   | Pending or Previous Defendant in Civil Action            | The insider was previously found liable in a civil action outside of the specific incident (i.e. where a insider was sued previously, which may be a motivation for the insider's actions)                                                                            |
| 2.7   | Previous use of illegal substances                       | Known use of illegal narcotics or illegal use of prescribed medications                                                                                                                                                                                               |
| 3.1   | Criminal Association                                     | Insider associates with known criminals or criminal organizations                                                                                                                                                                                                     |
| 3.2   | Internet Underground Association                         | Insider associates with or participates in darkweb groups or activities                                                                                                                                                                                               |
| 4.1   | Medical Problems                                         | Health issues experienced by anyone involved in the event since the insider's hire date (e.g., the insider contracted lupus and was put on medication)                                                                                                                |
| 4.2   | Relationship Problems                                    | A problem in one of the insider's relationships that affects the insider, including family and romantic relationships developed after the insider's hire date (e.g., the insider was going through a divorce)                                                         |
| 4.3   | Emerging Financial Problems                              | Monetary issues experienced by or relevant to the insider (including medical bills for family members) known to have developed after the insider's hire date (e.g., the insider claimed they stole from the organization in order to pay for their child's education) |
| 4.4   | Family Health Issues                                     | Someone in the insider's family, or otherwise close to the insider, has health or medical issues                                                                                                                                                                      |

### concerning-behavior-vocab

Constants: `3.1`, `3.2`, `3.3`, `3.4`, `3.5`, `3.6`, `3.7`

| Const | Value                       | Description                                                                                                                          |
| ----- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| 3.1   | Misuse of Company Resources | Using or abusing company resources in an unauthorized manner                                                                         |
| 3.2   | Technical Policy Abuse      | Violating policies regarding the use of the organization's IT systems                                                                |
| 3.3   | Interpersonal Issues        | Conflicts with others in the organization or human resources (HR) issues                                                             |
| 3.4   | Financial                   | Financial conflicts of interest or significant changes to financial status                                                           |
| 3.5   | Organizational Conflict     | Competitive conflicts of interest with the organization                                                                              |
| 3.6   | Suspicious Contact          | Suspicious communication with or travel to entities, areas, or individuals that present a conflict of interest with the organization |
| 3.7   | Relocation                  | Physical relocation                                                                                                                  |

### cb-subtype-vocab

Constants: `3.1.1`, `3.1.2`, `3.1.3`, `3.2.1`, `3.2.2`, `3.2.3`, `3.2.4`, `3.2.5`, `3.2.6`, `3.3.1`, `3.3.2`, `3.3.3`, `3.3.4`, `3.3.5`, `3.3.6`, `3.3.7`, `3.3.8`, `3.3.9`, `3.3.10`, `3.3.11`, `3.3.12`, `3.3.13`, `3.4.1`, `3.4.2`, `3.4.3`, `3.5.1`, `3.5.2`, `3.5.3`, `3.5.4`, `3.5.5`, `3.5.6`, `3.6.1`, `3.6.2`, `3.6.3`, `3.6.4`, `3.7.1`

| Const  | Value                                                 | Description                                                                                                                                                                                                                                |
| ------ | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 3.1.1  | Theft Of Physical Company Property                    | Stealing their employer's physical property (e.g., the insider reported a company laptop as stolen, but had it when they were arrested)                                                                                                    |
| 3.1.2  | Insider Expressed Ownership Of Work                   | Acting as if they had personal right to any work done for the organization, despite knowledge of organizational right to employee work (e.g., the insider refused to return copy of code that they wrote because they felt entitled to it) |
| 3.1.3  | Repeated Security Violations - Non-Technical          | Violating organizational security policies not related to IT systems (e.g., the insider broke into the school on multiple occasions and was also caught cheating)                                                                          |
| 3.2.1  | Other Unauthorized Software Acquisition               | Acquiring any sort of unauthorized software on an organizational system (e.g., the insider downloaded a password recovery tool from a website)                                                                                             |
| 3.2.2  | Repeated Security Violations - Technical              | Multiple instances of security violations related to organizational IT systems (e.g., the insider repeatedly let co-workers use their workstation)                                                                                         |
| 3.2.3  | Unauthorized Download - Remotely                      | Unapproved download from offsite (e.g., the insider logged into their company account from home on their personal laptop and downloaded torrents)                                                                                          |
| 3.2.4  | Unauthorized Download - On Site                       | Unapproved download from within the organization (e.g., the insider used their company-issued workstation to download torrents)                                                                                                            |
| 3.2.5  | IP Policy Violation                                   | Violating any of the policies put in place by the company regarding their IP (i.e. trade secrets, patents, copyright, etc.)                                                                                                                |
| 3.2.6  | Violation of Need to Know                             | Accessing organizational information which is not needed for their work, as defined by organizational policy                                                                                                                               |
| 3.3.1  | Employee Extortion, Threats, or Legal Demands         | Extortion, threats (physical, technical, legal, etc.) or legal demands against the organization (e.g., the insider threatened to sue company unless they agreed to the terms of their demands)                                             |
| 3.3.2  | Conflict With Supervisor                              | Personal or work-related disputes with their supervisor (e.g., the insider was unhappy with their new boss because the boss modified the organization's bonus system)                                                                      |
| 3.3.3  | Conflict With Coworker(s)                             | Personal or work-related disputes with a coworker (e.g., the insider yelled at a coworker for repeatedly parking in their spot)                                                                                                            |
| 3.3.4  | Work Attendance Problems                              | Being late for work or having unexcused/unplanned absences from work, generally multiple times (e.g., the insider reports late to work 7 times during the month of April)                                                                  |
| 3.3.5  | Human Resource Policy Violations or Complaints        | Violating the organization's human resource policy or making a formal complaint about something/someone within the organization (e.g., the insider made several complaints to management about their co-worker's noise level)              |
| 3.3.6  | Disgruntled Employee                                  | One who is upset with the organization and desires to get a measure of revenge against the organization (e.g., the insider grew disgruntled because of losing their 'star' status at the organization as it grew larger)                   |
| 3.3.7  | Bragging                                              | The insider boasts about a concerning behavior to co-workers or online (e.g., the insider boasted about being able to shut down the organization's system anytime they wanted)                                                             |
| 3.3.8  | Concurrent Crimes                                     | The insider commits a second illegal action while committing the unrelated illegal insider incident (e.g., the insider was indicted for domestic abuse while committing the insider incident)                                              |
| 3.3.9  | Formal Complaint                                      | Organization receives complaints about the insider from a coworker which were officially documented                                                                                                                                        |
| 3.3.10 | Informal Complaint                                    | Organization receives complaints about the insider from a coworker which were not officially documented                                                                                                                                    |
| 3.3.11 | Insubordination                                       | Defiance or refusal to follow commands or instructions                                                                                                                                                                                     |
| 3.3.12 | Physical Abuse/Harassment                             | Engaging in any type of physical abuse and/or harassment against another employee                                                                                                                                                          |
| 3.3.13 | Sexual Harassment                                     | Engaging in any type of sexual harassment against another employee                                                                                                                                                                         |
| 3.4.1  | Unexplained Wealth                                    | A sudden increase in the amount of money the insider appears to have (e.g., the insider purchased $400,000 in personal items even though their annual salary was $50,000)                                                                  |
| 3.4.2  | Employee Forms New Competing Business                 | Maintains a financial stake in another business or scheme that conflicts with their present employer (e.g., the insider invests in stocks of the victim organization's competitor)                                                         |
| 3.4.3  | Financial Conflict of Interest                        | Starting a business in the same area as their previous employer (e.g., the insider left one law firm to start their own law firm)                                                                                                          |
| 3.5.1  | Planning/Contact with Competing Organization          | Conspiring with a competitor of the current employer in any way (e.g., the insider e-mailed a competing organization detailing plans to steal trade secrets)                                                                               |
| 3.5.2  | Employee Went To Work For A Competing Organization    | Leaving their current employer and joining a competing organization. E.g., Insider accepted a position at a competing technical firm before resigning from their current position.                                                         |
| 3.5.3  | Employee Sought Other Employment                      | Seeking another job while still employed with their current employer (e.g., the insider sent their resume to another organization)                                                                                                         |
| 3.5.4  | Group Resignation                                     | Two or more employees leave the organization at approximately the same time for similar reasons (e.g., all five insiders resigned simultaneously, then went to work for a competitor)                                                      |
| 3.5.5  | Insider Creates Legal Entity for Illegitimate Purpose | Creates a legal entity in order to move forward with scheme or to hide assets as a result of the scheme (e.g., the insider creates a shell company to protect assets)                                                                      |
| 3.5.6  | Falsified Background Information                      | Lies about or otherwise manipulates information about their background: personal or financial history, contacts, groups, etc.                                                                                                              |
| 3.6.1  | Suspicious Foreign Contact                            | Tie(s) to foreign nation(s) such as company or independent travel, family members, telephone records, etc. (e.g., the insider consistently calls former co-worker who now works in a non-allied country)                                   |
| 3.6.2  | Suspicious Foreign Travel                             | Traveling to foreign nations that, if the travel was known, should raise concerns with the organization                                                                                                                                    |
| 3.6.3  | Foreign Travel - Work Related                         | Travel undertaken by the insider as required for their job (e.g., the insider's job required frequent travel to non-allied countries)                                                                                                      |
| 3.6.4  | Planning/Contact with Conspirator                     | Conspiring with a conspirator in order to begin or further their particular scheme (e.g., the insider calls their partner-in-crime in order to establish attack details)                                                                   |
| 3.7.1  | Geographic Relocation                                 | Permanent move to a new physical location                                                                                                                                                                                                  |

## License

This file is a part of the Insider Incident Data Exchange Standard (IIDES) - see https://github.com/cmu-sei/IIDES

Copyright 2024 Carnegie Mellon University.

[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution. Please see Copyright notice for non-US Government use and distribution.

This work is provided \"AS-IS\" with \"NO WARRANTIES OF ANY KIND - EXPRESS OR IMPLIED\" and is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.

Requests for permission for non-licensed uses should be directed to the Software Engineering Institute at permission@sei.cmu.edu.

CERT® is registered in the U.S. Patent and Trademark Office by Carnegie Mellon University.

DM24-0776
