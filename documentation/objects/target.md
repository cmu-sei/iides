# Target
TODO

## Properties
- **`id`** (required) *(string)* : TODO
	- Uses pattern: ^target--[UUIDv4]
- **`asset_type`** (required) *(string)* : TODO
	- A value from [target-asset-vocab](#target-asset-vocab)
- **`category`** (required) *(string)* : TODO
	- A value from [target-category-vocab](#target-category-vocab)
- **`subcategory`** (required) *(string)* : TODO
	- A value from [target-subcategory-vocab](#target-subcategory-vocab)
- **`format`** (required) *(string)* : TODO
	- A value from [target-format-vocab](#target-format-vocab)
- **`owner`** (required) *(string)* : TODO
	- A value from [target-owner-vocab](#target-owner-vocab)
- **`sensitivity`** (required) *(string)* : TODO
	- A value from [target-sensitivity-vocab](#target-sensitivity-vocab)
- **`description`** *(string)* : TODO

## Vocabularies

### target-asset-vocab

Values: `1`, `2`, `3`, `4`, `5`, `6`

| Const | Value | Description |
| --- | --- | --- |
| 1 | Facilities | TODO|
| 2 | Information | TODO|
| 3 | Money | TODO|
| 4 | People | TODO|
| 5 | Technology | TODO|
| 6 | Other | TODO|

### target-category-vocab

Values: `1.1`, `2.1`, `2.2`, `2.3`, `3.1`, `4.1`, `4.2`, `4.3`, `4.4`, `4.5`, `5.1`, `5.2`, `5.3`, `6.1`

| Const | Value | Description |
| --- | --- | --- |
| 1.1 | Physical Property - Non-digital assets | TODO|
| 2.1 | Product Information | TODO|
| 2.2 | Business Plans | TODO|
| 2.3 | Government/Law Enforcement Plans | TODO|
| 3.1 | Money | TODO|
| 4.1 | Customer Data | TODO|
| 4.2 | Employee Data | TODO|
| 4.3 | Identification | TODO|
| 4.4 | Medical Information | TODO|
| 4.5 | Communication Systems | TODO|
| 5.1 | Network or Systems | TODO|
| 5.2 | Software | TODO|
| 5.3 | Passwords | TODO|
| 6.1 | Unknown | TODO|

### target-subcategory-vocab

Values: `1.1.1`, `1.1.2`, `1.1.3`, `2.1.1`, `2.1.2`, `2.2.1`, `2.2.2`, `2.2.3`, `2.2.4`, `2.2.5`, `2.2.6`, `2.3.1`, `2.3.2`, `3.1.1`, `3.1.2`, `3.1.3`, `3.1.4`, `3.1.5`, `3.1.6`, `3.1.7`, `3.1.8`, `3.1.9`, `3.1.10`, `3.1.11`, `3.1.12`, `3.1.13`, `3.1.14`, `4.1.1`, `4.1.2`, `4.1.3`, `4.1.4`, `4.1.5`, `4.2.1`, `4.3.1`, `4.3.2`, `4.3.3`, `4.4.1`, `4.4.2`, `4.4.3`, `4.4.4`, `4.5.1`, `4.5.2`, `5.1.1`, `5.1.2`, `5.1.3`, `5.1.4`, `5.1.5`, `5.1.6`, `5.1.7`, `5.1.8`, `5.1.9`, `5.1.10`, `5.2.1`, `5.2.2`, `5.2.3`, `5.2.4`, `5.3.1`, `5.3.2`

| Const | Value | Description |
| --- | --- | --- |
| 1.1.1 | Blueprint Plans | TODO|
| 1.1.2 | Facilities | TODO|
| 1.1.3 | Physical Products | TODO|
| 2.1.1 | Product Information | TODO|
| 2.1.2 | Proprietary Information | TODO|
| 2.2.1 | Business Plans | TODO|
| 2.2.2 | Business System | TODO|
| 2.2.3 | Commerce information | TODO|
| 2.2.4 | Contract Information | TODO|
| 2.2.5 | Design and Plans | TODO|
| 2.2.6 | Payroll Information | TODO|
| 2.3.1 | Classified Information | TODO|
| 2.3.2 | Sensitive Information | TODO|
| 3.1.1 | Accounting Records | TODO|
| 3.1.2 | ATM Withdrawal | TODO|
| 3.1.3 | Bank Account Information | TODO|
| 3.1.4 | Bitcoin | TODO|
| 3.1.5 | Company Funds | TODO|
| 3.1.6 | Gift Cards | TODO|
| 3.1.7 | Invoices | TODO|
| 3.1.8 | Issued Checks | TODO|
| 3.1.9 | Loan | TODO|
| 3.1.10 | Physical Currency | TODO|
| 3.1.11 | Refunds | TODO|
| 3.1.12 | Reimbursement Forms | TODO|
| 3.1.13 | Tax Information | TODO|
| 3.1.14 | Time Sheets | TODO|
| 4.1.1 | Client List | TODO|
| 4.1.2 | Customer Data | TODO|
| 4.1.3 | Alien Files | TODO|
| 4.1.4 | Credit Card Information | TODO|
| 4.1.5 | Insurance Claims | TODO|
| 4.2.1 | Employee Data | TODO|
| 4.3.1 | Driver's license | TODO|
| 4.3.2 | Personal Photos | TODO|
| 4.3.3 | PII | TODO|
| 4.4.1 | PHI | TODO|
| 4.4.2 | Medicare/Medicaid | TODO|
| 4.4.3 | Prescription Medication | TODO|
| 4.4.4 | Prescription Pads | TODO|
| 4.5.1 | Emails | TODO|
| 4.5.2 | Telecommunication Systems | TODO|
| 5.1.1 | Access to System | TODO|
| 5.1.2 | Backup Data | TODO|
| 5.1.3 | Backup Tapes | TODO|
| 5.1.4 | Database | TODO|
| 5.1.5 | Email Servers | TODO|
| 5.1.6 | FTP Servers | TODO|
| 5.1.7 | Network Configuration | TODO|
| 5.1.8 | Network Login Information | TODO|
| 5.1.9 | Servers | TODO|
| 5.1.10 | Website Hosting | TODO|
| 5.2.1 | Backup Software | TODO|
| 5.2.2 | Software Policy Protocol | TODO|
| 5.2.3 | Source code | TODO|
| 5.2.4 | Unreleased Software | TODO|
| 5.3.1 | Login Information | TODO|
| 5.3.2 | Passwords | TODO|

### target-format-vocab

Values: `1`, `2`, `3`, `4`, `5`

| Const | Value | Description |
| --- | --- | --- |
| 1 | Electronic | TODO|
| 2 | Physical | TODO|
| 3 | Personnel | TODO|
| 4 | Other | TODO|
| 5 | Unknown | TODO|

### target-owner-vocab

Values: `C`, `E`, `O`, `T`, `Z`

| Const | Value | Description |
| --- | --- | --- |
| C | Consumer | TODO|
| E | Employee | TODO|
| O | Organization | TODO|
| T | Third Party | TODO|
| Z | Other | TODO|

### target-sensitivity-vocab

Values: `CTI`, `FRP`, `FTI`, `GVT`, `ITP`, `LES`, `NPB`, `PCI`, `PHI`, `PII`, `NSN`

| Const | Value | Description |
| --- | --- | --- |
| CTI | Controlled Technical Information (CTI) | TODO|
| FRP | FERPA (student education records) | TODO|
| FTI | Federal Tax Information (FTI) | TODO|
| GVT | Government Sensitive | TODO|
| ITP | Intellectual Property (IP) | TODO|
| LES | Law Enforcement Sensitive | TODO|
| NPB | Non-Public | TODO|
| PCI | Credit/Payment Card (PCI) | TODO|
| PHI | Protected Health Information (PHI) | TODO|
| PII | Personally Identifiable Information (PII) | TODO|
| NSN | Not sensitive/Public | TODO|