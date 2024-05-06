# Incident

Description and summary details of the incident.

## Properties

- **`id`** (required) *(string)* : A unique string that begins with "incident--" and is appended with a UUIDv4.
  - Uses pattern: ^incident--[UUIDv4]
- **`cia_effect`** *(array)* : CIA triad components which were affected.
  - One or more constants from [cia-vocab](#cia-vocab)
- **`incident_type`** *(array)* : Categorization of the incident.
  - One or more constants from [incident-type-vocab](#incident-type-vocab)
  - Required if `incident_subtype` exists.
- **`incident_subtype`** *(array)* : The subtype that the incident fits. MUST match the specified incident_type.
  - One or more constants from [incident-subtype-vocab](#incident-subtype-vocab)
- **`outcome`** *(array)* : Consequences suffered by the victim organization as a result of the insider's attack. This is NOT the outcome or consequences imposed on the insider.
  - One or more constants from [outcome-type-vocab](#outcome-type-vocab)
- **`status`** *(string)* : The current status of the incident.
	- A constant from [incident-status-vocab](#incident-status-vocab)
- **`summary`** *(string)* : A brief prose explanation of the incident. This summary should serve as a stand-alone explanation of the incident and should include the following information as a general rule: who, what, when, where, why, and how.
- **`brief_summary`** *(string)* : A shortened version of the summary (2-4 sentences, max 500 characters) with anonymized data.
- **`comment`** *(string)* : Clarifying details about the incident or any of the above properties.

## Vocabularies

### incident-status-vocab

Constants: `P`, `I`, `R`, `C`

| Const | Value | Description |
| --- | --- | --- |
| P | Open | A case has been opened for the incident.|
| I | Under Investigation | The incident is being investigated.|
| R | Referred out | Incident has been referred to another team or organization.|
| C | Closed | All investigations and legal proceedings are closed.|

### cia-vocab

Constants: `C`, `I`, `A`

| Const | Value | Description |
| --- | --- | --- |
| C | Confidentiality | The protection of information from unauthorized access or disclosure.|
| I | Integrity | The protection of information from unauthorized modification or destruction.|
| A | Availability | The protection of information and information systems from unauthorized disruption.|

### outcome-type-vocab

Constants: `BR`, `DC`, `DD`, `DR`, `DS`, `MD`, `ML`, `MS`, `NN`, `OT`, `RO`, `SI`, `IT`

| Const | Value | Description |
| --- | --- | --- |
| BR | Bankruptcy | One or more victim organizations filed for bankruptcy.|
| DC | Data Created | Newly created data that is a direct result of the insider's attack.|
| DD | Data Deleted | Data was deleted from the victim organization's systems.|
| DR | Data Read | Organizational data was read by the insider.|
| DS | Data Stolen | Any organizational information or assets that are stolen.|
| MD | Monetary Damages | The court ordered a sum of money to be paid by the victim organization for the purpose of replacing the monetary value of property or rights which have been lost or damaged, or to cover expenses, loss, pain and suffering relating to a victim's injury or death.|
| ML | Monetary Losses | Indirect loss of money through damage, detriment, or suffering related to the incident.|
| MS | Money Stolen | The insider directly stole money from the victim organization.|
| NN | No net negative | Though an incident occurred, there were no negative consequences to the victim organization as a result.|
| OT | Other | Other type of outcome not listed in this vocabulary.|
| RO | Restituion Ordered | The organizatiion was ordered by a court to pay restitution to additional victims of the incident.|
| SI | Safety Impact | There was an impact, or potential for impact to safety, as a result of the incident.|
| IT | Used in Identity Theft | Identity theft of one or more individuals resulted from the incident. E.g., The insider used stolen PII to file fraudulent tax returns.|

### incident-type-vocab

Constants: `F`, `S`, `E`, `V`, `U`

| Const | Value | Description |
| --- | --- | --- |
| F | Fraud | Deceiving the organization for personal gain at the organization's expense.|
| S | Sabotage | Deliberate actions to harm an organization's physical or virtual infrastructure, including noncompliance with maintenance or IT procedures, contaminating clean spaces, physically damaging facilities, or deleting code to prevent regular operations.|
| E | Espionage | The covert or illicit practice of spying on a foreign government, organization, entity, or person to obtain confidential information for military, political, strategic, or financial advantage.|
| V | Violence | Includes the threat of violence, as well as other threatening behaviors that create an intimidating, hostile, or abusive environment.|
| U | Unintentional | The insider unwittingly causes harm or substantially increases the probability of future serious harm to the organization through action or inaction without malicious intent.|

### incident-subtype-vocab

Constants: `F1`, `F2`, `F3`, `S1`, `S2`, `E1`, `E2`, `V1`, `V2`, `U1`, `U2`

| Const | Value | Description |
| --- | --- | --- |
| F1 | Embezzlement | The fraudulent appropriation of the organization's property (financial or otherwise) by someone who has been entrusted with its possession.|
| F2 | Corruption | Conflict of interest, bribery, illegal gratuities, and economic extortion.|
| F3 | False Statements | Knowingly and willfully making false or fraudulent statements, or concealing information.|
| S1 | Virtual | Taking malicious actions through technical means to disrupt or stop an organization's normal business operations.|
| S2 | Physical | Taking deliberate actions aimed at harming an organization's physical infrastructure (e.g., facilities or equipment).|
| E1 | Intellectual Property Theft | Theft or robbery of an individual's or organization's ideas, inventions, or creative expressions, including trade secrets and proprietary products, even if the concepts or items being stolen originated from the thief.|
| E2 | Government | Covert intelligence-gathering activities to obtain government or military secrets for the benefit of another government to obtain political or military advantage.|
| V1 | Workplace Violence | Any action or threat of physical violence, harassment, sexual harassment, intimidation, bullying, offensive jokes, or other threatening behavior by a co-worker or associate that occurs in a person's place of employment or while a person is working.|
| V2 | Self Harm | An incident where an insider attempts, or indicates a desire to attempt, self harm or suicide.|
| U1 | Negligence | Threat caused by carelessness. Negligent insiders are generally familiar with security and/or IT policies but choose to ignore them, creating risk for the organization.|
| U2 | Accidental | An incident of this type results from an insider mistakenly causing an unintended risk to an organization.|
