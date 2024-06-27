# Target

The system, data, person, or physical property that was targeted by the insider. An incident may have many targets.

## Properties

- **`id`** (required) *(string)* : A unique string that begins with "target--" and is appended with a UUIDv4.
  - Uses pattern: ^target--[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
- **`asset_type`** (required) *(string)* : The type of target.
	- A constant from [target-asset-vocab](#target-asset-vocab)
  - Required if `category` exists.
- **`category`** (required) *(string)* : The classification group a target belongs to.
	- A constant from [target-category-vocab](#target-category-vocab)
  - Required if `subcategory` exists.
- **`subcategory`** (required) *(string)* : The lower-level classification group a target belongs to.
	- A constant from [target-subcategory-vocab](#target-subcategory-vocab)
- **`format`** (required) *(string)* : The data type of the target.
	- A constant from [target-format-vocab](#target-format-vocab)
- **`owner`** (required) *(string)* : Who the data is about. For assets, the owner of the asset. In cases where the owner and subject of the data/asset is unclear, pick the person/group most responsible for safeguarding the data/asset.
	- A constant from [target-owner-vocab](#target-owner-vocab)
- **`sensitivity`** (required) *(array)* : The level of sensitivity and controls applied to a target.
  - One or more constants from [target-sensitivity-vocab](#target-sensitivity-vocab)
- **`description`** *(string)* : Brief description of the target.

## Vocabularies

### target-asset-vocab

Constants: `1`, `2`, `3`, `4`, `5`, `6`

| Const | Value | Description |
| --- | --- | --- |
| 1 | Facilities | Buildings, offices, areas of buildings, or functions of buildings (such as disabling a door).|
| 2 | Information | Data/business materials which contain important details belonging to a specific target owner.|
| 3 | Money | Currency, digital or physical, or materials, goods, or data that will be converted to currency or are currency equivalent.|
| 4 | People | Employees, customers, individuals.|
| 5 | Technology | Hardware, software, or firmware intended for the storage or transmission of data or the operation of equipment (as in computers running a manufacturing line).|
| 6 | Other | Other asset type not listed in this vocabulary.|

### target-category-vocab

Constants: `1.1`, `2.1`, `2.2`, `2.3`, `3.1`, `4.1`, `4.2`, `4.3`, `4.4`, `4.5`, `5.1`, `5.2`, `5.3`, `5.4`, `6.1`

| Const | Value | Description |
| --- | --- | --- |
| 1.1 | Physical Property - Non-digital assets | Physical property such as blue prints or material goods.|
| 2.1 | Product Information | Information about products or services the organization sells|
| 2.2 | Business Plans | Data or documents having to do with the everyday course of the business.|
| 2.3 | Government/Law Enforcement Information | Classified or sensitive government or law enforcement information.|
| 3.1 | Money | Currency, digital or physical, or materials, goods, or data that will be converted to currency or are currency equivalent.|
| 4.1 | Customer Data | Information provided by customers or describing customers.|
| 4.2 | Employee Data | Information collected from employees or describing employees.|
| 4.3 | Identification | Digital or physical means of verifying identity.|
| 4.4 | Medical Information | Information about an individuals' Protected Health Information (PHI), Medicare/Medicaid, prescription medication, etc.|
| 4.5 | Person(s) | Individual person or persons.|
| 5.1 | Network or Systems | Platforms in which information is shared or processes are run.|
| 5.2 | Software | Software or applications running on the organization's devices or systems.|
| 5.3 | Passwords | Text strings which authenticate access to a system.|
| 5.4 | Communication Systems | Servers, routers, phone systems, etc. that enable communication within the organization, or between the organization and external entities.|
| 6.1 | Unknown | Unclear what was targeted.|

### target-subcategory-vocab

Constants: `1.1.1`, `1.1.2`, `1.1.3`, `2.1.1`, `2.1.2`, `2.2.1`, `2.2.2`, `2.2.3`, `2.2.4`, `2.2.5`, `2.2.6`, `2.3.1`, `2.3.2`, `3.1.1`, `3.1.2`, `3.1.3`, `3.1.4`, `3.1.5`, `3.1.6`, `3.1.7`, `3.1.8`, `3.1.9`, `3.1.10`, `3.1.11`, `3.1.12`, `3.1.13`, `3.1.14`, `4.1.1`, `4.1.2`, `4.1.3`, `4.1.4`, `4.1.5`, `4.2.1`, `4.3.1`, `4.3.2`, `4.3.3`, `4.4.1`, `4.4.2`, `4.4.3`, `4.4.4`, `4.5.1`, `4.5.2`, `5.1.1`, `5.1.2`, `5.1.3`, `5.1.4`, `5.1.5`, `5.1.6`, `5.1.7`, `5.1.8`, `5.1.9`, `5.2.1`, `5.2.2`, `5.2.3`, `5.2.4`, `5.3.1`, `5.3.2`, `5.4.1`, `5.4.2`

| Const | Value | Description |
| --- | --- | --- |
| 1.1.1 | Blueprint Plans | Schematics for facility layout or products/devices.|
| 1.1.2 | Facilities | Buildings, offices, areas of buildings, or functions of buildings (such as disabling a door).|
| 1.1.3 | Physical Products | Tangible objects owned or managed by the organization.|
| 2.1.1 | Product Information | Information about products or services offered by the organization.|
| 2.1.2 | Proprietary Information | Information that gives the organization a competitive advantage, such as trade secrets, formulas, designs, or processes, which could be exposed or sold to a competitor.|
| 2.2.1 | Business Plans | Pitches or anything having to do with the everyday course of business.|
| 2.2.2 | Business System | System which the organization requires to operate the business.|
| 2.2.3 | Commerce information | Data related to the organization's business dealings, such as customer lists, pricing strategies, supplier contracts, or marketing plans.|
| 2.2.4 | Contract Information | Information related to legal agreements made between the organization and other organizations or individuals such as employees or contractors.|
| 2.2.5 | Design and Plans | Product design or information for a business plan.|
| 2.2.6 | Payroll Information | Data relating to employee salaries, benefits, and tax information.|
| 2.3.1 | Classified Information | Information that is restricted by the government for reasons of national security.|
| 2.3.2 | Sensitive Information | Data that could cause harm to the organization or its stakeholders if leaked or misused.|
| 3.1.1 | Accounting Records | Records tracking money, inventory, or purchases.|
| 3.1.2 | ATM Withdrawal | Money that withdrawn from an ATM.|
| 3.1.3 | Bank Account Information | Bank account information for a peculiar person or entity.|
| 3.1.4 | Bitcoin | Money in the form of virtual currency.|
| 3.1.5 | Company Funds | Monetary assets used for financing operations and initiatives of the organization.|
| 3.1.6 | Gift Cards | Money in the form of prepaid debit cards for use at a specific vendor.|
| 3.1.7 | Invoices | Money in the form of receiving funds from fraudulent invoices.|
| 3.1.8 | Issued Checks | Money in the form of receiving funds from fraudulent checks.|
| 3.1.9 | Loan | Money in the form of temporary funds given with the expectation of being repaid with interest.|
| 3.1.10 | Physical Currency | Money in the form of tangible paper bills, coins, or other means of circulation that holds direct monetary value.|
| 3.1.11 | Refunds | Money in the form of reimbursements for returend goods or services.|
| 3.1.12 | Reimbursement Forms | Information related to reports of incurred transaction expenses.|
| 3.1.13 | Tax Information | Tax forms, documentation, or identifiers.|
| 3.1.14 | Time Sheets | Digital or analog forms for employees to report hours worked.|
| 4.1.1 | Client List | Listing of organizations or individuals which are provided services by the organization.|
| 4.1.2 | Customer Data | Information about customers or provided by customers|
| 4.1.3 | Immigration Records | Records of individuals who are unaturalized immigrants.|
| 4.1.4 | Credit Card Information | Information relating to a credit card, such as the card number, the cardholder's name, when the card expires and the card's security code.|
| 4.1.5 | Insurance Claims | Information relating to monetary claims made in request to an insurance policy.|
| 4.2.1 | Employee Data | Information about employees or belonging to employees of an organization.|
| 4.3.1 | Driver's license | Information related to a legal identification that provides a permit to operate a motor vehicle.|
| 4.3.2 | Personal Photos | Images of a personal nature or unrelated to the organization's business.|
| 4.3.3 | PII | Sensitive information that can be used to identify an individual.|
| 4.4.1 | PHI | Sensitive information that is indicative of an individual's health condition.|
| 4.4.2 | Medicare/Medicaid | Information related to health insurance provided by the state to the elderly or financially limited populations.|
| 4.4.3 | Prescription Medication | Iinformation that relates to doctors notes permiting the purchase of controlled medical substances.|
| 4.4.4 | Prescription Pads | Secured stationery notes that doctors use for writing prescriptions.|
| 4.5.1 | Self | The insider is targeting themself.|
| 4.5.2 | Others | Indivdual or individuals other than the insider.|
| 5.1.1 | Backup Data | Data that can be used to restore a system or dataset if it becomes compromised.|
| 5.1.2 | Backup Tapes | Stored backup data copied to a tape cartridge.|
| 5.1.3 | Database | Structured electronic digital information repository.|
| 5.1.4 | Email Servers | Systems used to host and deliver email services.|
| 5.1.5 | FTP Servers | Systems which allow the exchange of files between two or more computers.|
| 5.1.6 | Network Configuration | Routing or network access configuration.|
| 5.1.7 | Network Login Information | Information related to access credentials for a network.|
| 5.1.8 | Servers | System(s) which host information or digital services for end users.|
| 5.1.9 | Website Hosting | System(s) for delivering websites over the internet.|
| 5.2.1 | Backup Software | Software designed to create copies of data for safe storage.|
| 5.2.2 | Software Policy Protocol | Rules developed by an organization for the ideal deployment of a software.|
| 5.2.3 | Source code | Underlying codebase for a product or system.|
| 5.2.4 | Unreleased Software | Software that has not yet been made available.|
| 5.3.1 | Login Information | Credentials used for access to a technological system.|
| 5.3.2 | Passwords | Access credentials in the form of a text string.|
| 5.4.1 | Emails | Electronic communications in the form of static messages shared to specified user addresses via a network.|
| 5.4.2 | Telecommunication Systems | Networks that facilitate digital or voice communications.|

### target-format-vocab

Constants: `1`, `2`, `3`, `4`, `5`

| Const | Value | Description |
| --- | --- | --- |
| 1 | Electronic | Technological digital format.|
| 2 | Physical | Tangible real world format.|
| 3 | Personnel | People or individuals.|
| 4 | Other | Other format not listed in this vocabulary.|
| 5 | Unknown | Unclear what was targeted.|

### target-owner-vocab

Constants: `C`, `E`, `O`, `T`, `Z`

| Const | Value | Description |
| --- | --- | --- |
| C | Consumer | An individual that purchases and makes use of a product or service.|
| E | Employee | An individual internal to an organization who facilitates the disbursement of products or services.|
| O | Organization | The organization, rather than its employees or customers owns the target.|
| T | Third Party | Parties external to an organization and consumers.|
| Z | Other | Other owner not listed in this vocabulary.|

### target-sensitivity-vocab

Constants: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`, `16`, `17`, `18`, `19`, `20`, `21`, `22`, `23`, `24`, `25`, `26`

| Const | Value | Description |
| --- | --- | --- |
| 1 | Unclassified | No classification|
| 2 | Confidential | Public disclosure would damage national security|
| 3 | FOUO | For official use only|
| 4 | Secret | Public disclosure would cause serious damage to national security|
| 5 | SecretNoForn | Secret / restricted to country of source|
| 6 | Top Secret (TS) | Top secret, unauthorized disclosure would cause exceptionally grave damage to national security|
| 7 | TS/SCI | Top secret / Sensitive compartmented information|
| 8 | NATORestricted | North Atlantic Treaty Organization Restricted|
| 9 | NATOConfidential | North Atlantic Treaty Organization Confidential|
| 10 | NATOSecret | North Atlantic Treaty Organization Secret|
| 11 | CosmicTopSecret | Top Secret documents managed by a COSMIC registry|
| 12 | FVEYProprietary | Five eyes proprietary|
| 13 | Proprietary | Information a company wishes to keep confidential (e.g. trade secrets)|
| 14 | Personal identifiable information (PII) | Information which can be used to distinguish or trace an individual's identity, such as their name, social security number, biometric records, etc. alone, or when combined with other personal or identifying information which is linked or linkable to a specific individual, such as date and place of birth, mother's maiden name, etc.|
| 15 | HIPPA/Protected Health Information (PHI) | Individually identifiable health information, held or maintained by a covered entity or its business associates acting for the covered entity, that is transmitted or maintained in any form or medium. This includes identifiable demographic and other information relating to the past, present, or future physical or mental health or condition of an individual, or the provision or payment of health care to an individual that is created or received by a health care provider, health plan, employer, or health care clearinghouse.|
| 16 | GDPR | General data protection regulation|
| 17 | Public | Unrestricted/open to the public|
| 18 | CUI | Controlled Unclassified Information|
| 19 | Controlled Technical Information (CTI) | Technical information subject to controls to access, use, reproduction, or dissemination.|
| 20 | FERPA (student education records) | Information subject to sensitity due to relevance to student educational privacy.|
| 21 | Federal Tax Information (FTI) | Information that subject to sensitivty that is derived from tax returns.|
| 22 | Government Sensitive | Classified or sensitive information used by and only available to the government.|
| 23 | Intellectual Property (IP) | Information that has been created and is subject to protection of its creativity.|
| 24 | Law Enforcement Sensitive | Information, software, or device used by and only available to law enforcement.|
| 25 | Non-Public | Information not made available to the public.|
| 26 | Credit/Payment Card (PCI) | Credit/payment card information.|

## License
This file is a part of the Insider Incident Data Exchange Standard (IIDES) - see https://github.com/cmu-sei/IIDES

Copyright 2024 Carnegie Mellon University.

[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution.  Please see Copyright notice for non-US Government use and distribution.

This work is provided “AS-IS” with “NO WARRANTIES OF ANY KIND - EXPRESS OR IMPLIED” and is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.

Requests for permission for non-licensed uses should be directed to the Software Engineering Institute at permission@sei.cmu.edu.

CERT® is registered in the U.S. Patent and Trademark Office by Carnegie Mellon University.

DM24-0776
