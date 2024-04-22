# Incident

Description and summary details of the incident.

## Properties

- **`id`** (required) *(string)* : A unique string that begins with "incident--" and is appended with a UUIDv4.
	- Uses pattern: ^incident--[UUIDv4]
- **`cia_effect`** *(array)* : CIA triad components which were affected.
	- One or more values from [cia-vocab](#cia-vocab)
- **`incident_type`** *(array)* : Categorization of the incident.
	- One or more values from [incident-type-vocab](#incident-type-vocab)
- **`outcome`** *(array)* : Consequences suffered by the victim organization as a result of the insider's attack. This is NOT the outcome or consequences imposed on the insider.
	- One or more values from [outcome-type-vocab](#outcome-type-vocab)
- **`status`** *(string)* : The current status of the incident.
	- A constant from [incident-status-vocab](#incident-status-vocab)
- **`summary`** *(string)* : A brief prose explanation of the incident. This summary should serve as a stand-alone explanation of the incident and should include the following information as a general rule: who, what, when, where, why, and how.
- **`brief_summary`** *(string)* : A shortened version of the summary (2-4 sentences, max 500 characters) with anonymized data.
- **`comment`** *(string)* : Clarifying details about the incident or any of the above properties.

## Vocabularies

### incident-status-vocab

Constants: `P`, `I`, `L`, `C`

| Const | Value | Description |
| --- | --- | --- |
| P | Open | A case has been opened for the incident.|
| I | Under Investigation | The incident is being investigated.|
| L | In Legal Proceedings | Investigation is complete, but the case is at trial or in appeals.|
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

Constants: `F`, `S`, `T`, `M`

| Const | Value | Description |
| --- | --- | --- |
| F | Fraud | An insider's use of IT for the unauthorized modification, addition, or deletion of an organization's data (not programs or systems) for personal gain, or the theft of information which could be used to commit fraud (identity theft or credit card fraud). In other words, the insider misrepresents their intent or exceeds their access to protected information in order to commit fraud. Incidents involving fraud often involve attempted or successful identity theft.|
| S | Sabotage | The insider directs specific harm to the organization or an individual. Instances of sabotage may include deployment of malicious code to networks or systems resulting in system downtime. Targets of sabotage may include physical property as well. Common to this category are Denial of Service attacks (DoS) and deletion of critical files.|
| T | Theft of IP | An insider's use of IT to steal intellectual property from the organization, which may be done to benefit individuals or external organizations at the expense of the victim organization(s). This category includes industrial espionage involving insiders as well as insiders who seek to steal intellectual property to start competing organizations. Theft of IP, depending on the organization, may actually include PII if customer information is a source of competitive advantage for the organization (i.e., an insider makes an unauthorized download of customer database in order to create a cold call list).|
| M | Misuse | The unauthorized use of organizational devices, networks, and resources that is not better classified as theft of IP, sabotage, or fraud. Common examples of other misuse include unauthorized personal use of organizational resources (e.g., harvesting bitcoin), privacy violations (e.g., accessing co-worker's emails), committing a crime (e.g., stalking, purchasing drugs, or accessing child pornography), or other organizational policy violations.|
