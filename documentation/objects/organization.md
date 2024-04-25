# Organization

The organization(s) involved in the incident. At least one organization, the victim organization, should be included as part of an incident bundle. There may be other organizations involved, such as a competitor organization that benefitted from stolen data or pass through organization that received kickbacks. The victim organization(s) include all organizations negatively impacted by the incident, not just the organization(s) that employed the insider.

## Properties

- **`id`** (required) *(string)* : A unique string that begins with "organization--" and is appended with a UUIDv4.
	- Uses pattern: ^organization--[UUIDv4]
- **`name`** *(string)* : The name of the organization. E.g., "Company XYZ, Inc."
- **`city`** *(string)* : The city where the organization is located. Use the address of the headquarters if the whole organization was affected or use the address of the local branch if only that local branch was affected.
- **`state`** *(string)* : The state where the organization is located. Use the address of the headquarters if the whole organization was affected or use the address of the local branch if only that local branch was affected.
	- A constant from [state-vocab](../common/state-vocab.md)
- **`country`** *(string)* : The country where the organization is located. Use the address of the headquarters if the whole organization was affected or use the address of the local branch if only that local branch was affected.
	- A constant from [country-vocab](../common/country-vocab.md)
- **`postal_code`** *(integer)* : The postal code of the organization. Use the address of the headquarters if the whole organization was affected or use the address of the local branch if only that local branch was affected.
- **`small_business`** *(boolean)* : TRUE if the organization is a privately owned business with 500 or fewer employees.
- **`industry_sector_tier1`** *(string)* : Top level category for the economic sector the organization belongs to.
	- A constant from [industry-sector-tier1-vocab](#industry-sector-tier1-vocab)
- **`industry_sector_tier2`** *(string)* : Second level category for the economic sector the organization belongs to. This value MUST map back to industry_sector_tier1. E.g., if tier 1 is "9", tier 2 must be "9.x"
	- A constant from [industry-sector-tier2-vocab](#industry-sector-tier2-vocab)
- **`business`** *(string)* : Description of the organization's business.
- **`parent_company`** *(string)* : Name of the organization's parent company, if applicable.
- **`incident_role`** (required) *(string)* : The organization's role in the incident.
	- A constant from [org-role-vocab](#org-role-vocab)

## Vocabularies

### industry-sector-tier1-vocab

Constants: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`, `16`

| Const | Value | Description |
| --- | --- | --- |
| 1 | Agriculture and Mining | TODO|
| 2 | Utilities | TODO|
| 3 | Construction | TODO|
| 4 | Manufacturing | TODO|
| 5 | Trade | TODO|
| 6 | Transportation and Support Services | TODO|
| 7 | Information Technology | TODO|
| 8 | Finance and Insurance | TODO|
| 9 | Real Estate and Rental/Leasing | TODO|
| 10 | Professional Services | TODO|
| 11 | Education | TODO|
| 12 | Healthcare and Social Services | TODO|
| 13 | Arts, Entertainment, Recreation, and Hospitality | TODO|
| 14 | Religious Institutions, Charities, and Non-Profits | TODO|
| 15 | Public Administration | TODO|
| 16 | Unknown | TODO|

### industry-sector-tier2-vocab

Constants: `1.1`, `1.2`, `1.3`, `1.4`, `2.1`, `2.2`, `2.2`, `2.3`, `2.5`, `3.1`, `3.2`, `3.3`, `3.4`, `4.1`, `4.2`, `4.3`, `4.4`, `4.5`, `5.1`, `5.2`, `5.3`, `6.1`, `6.2`, `6.3`, `6.4`, `6.5`, `6.6`, `6.7`, `6.8`, `7.1`, `7.2`, `7.3`, `8.1`, `8.2`, `8.3`, `9.1`, `9.2`, `9.3`, `10.1`, `10.2`, `10.3`, `10.4`, `10.5`, `10.6`, `11.1`, `11.2`, `11.3`, `12.1`, `12.2`, `12.3`, `12.4`, `12.5`, `12.6`, `12.7`, `12.8`, `13.1`, `13.2`, `13.3`, `13.4`, `14.1`, `14.2`, `14.3`, `14.4`, `15.1`, `15.2`, `15.3`, `15.4`, `15.5`, `15.6`, `15.7`, `15.8`

| Const | Value | Description |
| --- | --- | --- |
| 1.1 | Agriculture and Forestry | TODO|
| 1.2 | Fishing and Hunting | TODO|
| 1.3 | Mining and Quarrying | TODO|
| 1.4 | Oil and Gas Extraction | TODO|
| 2.1 | Energy | TODO|
| 2.2 | Water (Distribution and Sewage) | TODO|
| 2.2 | Waste Collection | TODO|
| 2.3 | Nuclear (Power, Materials, and Waste) | TODO|
| 2.5 | Dams | TODO|
| 3.1 | Residential | TODO|
| 3.2 | Non-Residential | TODO|
| 3.3 | Civil | TODO|
| 3.4 | Architecture | TODO|
| 4.1 | Food and Beverage | TODO|
| 4.2 | Chemical | TODO|
| 4.3 | Aerospace, Auto, Marine, and Machinery | TODO|
| 4.4 | Electronics | TODO|
| 4.5 | General Manufacturing | TODO|
| 5.1 | Retail Trade | TODO|
| 5.2 | Wholesale Trade | TODO|
| 5.3 | E-Commerce | TODO|
| 6.1 | Air | TODO|
| 6.2 | Rail | TODO|
| 6.3 | Water | TODO|
| 6.4 | Truck | TODO|
| 6.5 | Transit | TODO|
| 6.6 | Pipeline | TODO|
| 6.7 | Courier Services | TODO|
| 6.8 | Supply Chain Services | TODO|
| 7.1 | Software Publishers and Web Developers | TODO|
| 7.2 | Telecommunications | TODO|
| 7.3 | IT, Data Processing, Hosting, Etc. | TODO|
| 8.1 | Banks and Credit Unions | TODO|
| 8.2 | Insurance | TODO|
| 8.3 | Other Financial Services | TODO|
| 9.1 | Real Estate Sales/Rentals | TODO|
| 9.2 | Warehousing & Storage | TODO|
| 9.3 | Automotive & Machinery Rental/Leasing | TODO|
| 10.1 | Legal | TODO|
| 10.2 | Consulting | TODO|
| 10.3 | Scientific Research and Development | TODO|
| 10.4 | Manual Labor and Related Services | TODO|
| 10.5 | Business Services (Marketing, PR, etc.) | TODO|
| 10.6 | Labor Unions | TODO|
| 11.1 | Elementary/High Schools | TODO|
| 11.2 | Colleges/Universities | TODO|
| 11.3 | Technical/Industry Training | TODO|
| 12.1 | Private Practices, Walk-in Clinics, Etc. | TODO|
| 12.2 | Advocacy Services | TODO|
| 12.3 | Psychological Practice | TODO|
| 12.4 | Pharmacology | TODO|
| 12.5 | Hospitals | TODO|
| 12.6 | Health Network | TODO|
| 12.7 | Healthcare Insurance | TODO|
| 12.8 | Diagnostics, Support Services, and Medical Manufacturing | TODO|
| 13.1 | Performing Arts & SPectator Sports | TODO|
| 13.2 | Museums & Historical Sites | TODO|
| 13.3 | Content Publishers | TODO|
| 13.4 | Hotels, Amusement, Gambling, and Restaurants | TODO|
| 14.1 | Religious Institutions | TODO|
| 14.2 | Charities | TODO|
| 14.3 | Non-Profit Organizations | TODO|
| 14.4 | Civic Associations | TODO|
| 15.1 | Federal Government | TODO|
| 15.2 | State Government | TODO|
| 15.3 | Local Government | TODO|
| 15.4 | Defense Industrial Base | TODO|
| 15.5 | Correctional Facilities | TODO|
| 15.6 | Emergency Services | TODO|
| 15.7 | Postal Services | TODO|
| 15.8 | Department of Defense | TODO|

### org-role-vocab

Constants: `B`, `V`, `S`, `T`, `O`

| Const | Value | Description |
| --- | --- | --- |
| B | Beneficiary | The organization accepted trade secrets, customer lists, intellectual property, etc. that the insider obtained through the incident.|
| V | Primary Victim | The organization was the primary victim organization of the insider's actions.|
| S | Secondary Victim | The organization was a secondary victim to the incident.|
| T | Trusted Business Partner | The organization has an alliance (contractually, bonded, etc.) with the victim organization.|
| O | Other | Other role not described by this vocabulary.|
