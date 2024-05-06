# Organization

The organization(s) involved in the incident. At least one organization, the victim organization, should be included as part of an incident bundle. There may be other organizations involved, such as a competitor organization that benefitted from stolen data or pass through organization that received kickbacks. The victim organization(s) include all organizations negatively impacted by the incident, not just the organization(s) that employed the insider.

## Properties

- **`id`** (required) *(string)* : A unique string that begins with "organization--" and is appended with a UUIDv4.
	- Uses pattern: ^organization--[UUIDv4]
- **`name`** *(string)* : The name of the organization. E.g., "Company XYZ, Inc."
- **`city`** *(string)* : The city where the organization is located. Use the address of the headquarters if the whole organization was affected or use the address of the local branch if only that local branch was affected.
- **`state`** *(string)* : The state where the organization is located. Use the address of the headquarters if the whole organization was affected or use the address of the local branch if only that local branch was affected.
- **`country`** *(string)* : The country where the organization is located. Use the address of the headquarters if the whole organization was affected or use the address of the local branch if only that local branch was affected. Public implementations should use the standard codes provided by ISO 3166-1 alpha-2.
- **`postal_code`** *(integer)* : The postal code of the organization. Use the address of the headquarters if the whole organization was affected or use the address of the local branch if only that local branch was affected.
- **`small_business`** *(boolean)* : TRUE if the organization is a privately owned business with 500 or fewer employees.
- **`industry_sector`** *(string)* : Top level category for the economic sector the organization belongs to.
	- A constant from [industry-sector-vocab](#industry-sector-vocab)
	- Required if `industry_subsector` exists.
- **`industry_subsector`** *(string)* : Second level category for the economic sector the organization belongs to. This value MUST map back to industry_sector. E.g., if sector is "9", subsector must be "9.x"
	- A constant from [industry-subsector-vocab](#industry-subsector-vocab)
- **`business`** *(string)* : Description of the organization's business.
- **`parent_company`** *(string)* : Name of the organization's parent company, if applicable.
- **`incident_role`** (required) *(string)* : The organization's role in the incident.
	- A constant from [org-role-vocab](#org-role-vocab)

## Vocabularies

### industry-sector-vocab

Constants: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`, `16`

| Const | Value | Description |
| --- | --- | --- |
| 1 | Agriculture and Mining | Growing crops, raising animals, harvesting timber, or extraction of naturally occurring minerals.|
| 2 | Utilities | Provisioning of services for the public (e.g., energy, water, and waste collection).|
| 3 | Construction | Construction and engineering of buildings and associated support services or trades.|
| 4 | Manufacturing | Mechanical, Chemical, Physical changes to material.|
| 5 | Trade | The exchange of goods and services.|
| 6 | Transportation and Support Services | Services directly or indirectly involved in the movement of people.|
| 7 | Information Technology | Hardware or software systems related to the processing, communications, and accessing of information.|
| 8 | Finance and Insurance | Financial services, payment processors, and insurance.|
| 9 | Real Estate and Rental/Leasing | Property sales and renting/leasing of assets.|
| 10 | Professional Services | Services provided by trained professionals in specialized fields.|
| 11 | Education | Instruction and training of individuals.|
| 12 | Healthcare and Social Services | Medical care and social advocacy/assistance.|
| 13 | Arts, Entertainment, Recreation, and Hospitality | Industries that meet the entertainment needs of patrons.|
| 14 | Religious Institutions, Charities, and Non-Profits | Any religious organization, charity, or non-profit.|
| 15 | Public Administration | Federal/State/Local administration and the oversight of public programs.|
| 16 | Other | Other sector not listed in this vocabulary.|

### industry-subsector-vocab

Constants: `1.1`, `1.2`, `1.3`, `1.4`, `2.1`, `2.2`, `2.2`, `2.3`, `2.5`, `3.1`, `3.2`, `3.3`, `3.4`, `4.1`, `4.2`, `4.3`, `4.4`, `4.5`, `5.1`, `5.2`, `5.3`, `6.1`, `6.2`, `6.3`, `6.4`, `6.5`, `6.6`, `6.7`, `6.8`, `7.1`, `7.2`, `7.3`, `8.1`, `8.2`, `8.3`, `9.1`, `9.2`, `9.3`, `10.1`, `10.2`, `10.3`, `10.4`, `10.5`, `10.6`, `11.1`, `11.2`, `11.3`, `12.1`, `12.2`, `12.3`, `12.4`, `12.5`, `12.6`, `12.7`, `12.8`, `13.1`, `13.2`, `13.3`, `13.4`, `14.1`, `14.2`, `14.3`, `14.4`, `15.1`, `15.2`, `15.3`, `15.4`, `15.5`, `15.6`, `15.7`, `15.8`

| Const | Value | Description |
| --- | --- | --- |
| 1.1 | Agriculture and Forestry | Establishments primarily engaged in growing crops, raising animals, and harvesting timber from a farm or natural habitat.|
| 1.2 | Fishing and Hunting | Establishments concerned with expediting, guiding, and transporting hunting/fishing adventures, as well as those involved lodging operations, shooting preserves and fishing charters.|
| 1.3 | Mining and Quarrying | Establishments that engage in mining, mine site development, and beneficiating metallic and nonmetallic minerals.|
| 1.4 | Oil and Gas Extraction | Establishments that operate and/or develop oil and gas field properties.|
| 2.1 | Energy | Providing sources of energy to physical facilities or residences.|
| 2.2 | Water (Distribution and Sewage) | Providing water to physical faciities or residences, and the extraction of waste water from such locations.|
| 2.2 | Waste Collection | The collection of disposed materials from physical facilities or residences.|
| 2.3 | Nuclear (Power, Materials, and Waste) | Provisioning of services for power, materials, and waste disposal related to nuclear facilities.|
| 2.5 | Dams | Industrial water dam facilities for managing irrigation, drinking water, flood control, etc.|
| 3.1 | Residential | The construction of physical structures for residential use.|
| 3.2 | Non-Residential | The construction of physical structures for non-residential commercial or public use.|
| 3.3 | Civil | The construction of physical infrastructure for the facilitation of societal use (i.e. bridges, roads, dams).|
| 3.4 | Architecture | The planning and design of physical structures.|
| 4.1 | Food and Beverage | The manufacturing of human consumables.|
| 4.2 | Chemical | The manufacturing of substances used for industrial purposes (i.e. cleaning products, agricultural practices)|
| 4.3 | Aerospace, Auto, Marine, and Machinery | The manufacturing of large scale complex technological physical systems (i.e. cars, ships, planes, sattelites).|
| 4.4 | Electronics | The construction of small scale complex technological systems (i.e. phones, computers, appliances)|
| 4.5 | General Manufacturing | Manufacturing of general products.|
| 5.1 | Retail Trade | The exchange of individual goods to consumers at merchant store locations.|
| 5.2 | Wholesale Trade | The exchange of bulk goods to other vendors for downstream retail trade.|
| 5.3 | E-Commerce | The exchange of individual or bulk goods to consumers or other vendors facilitated by the internet.|
| 6.1 | Air | Transportation and related services facilitated via air travel (i.e. planes).|
| 6.2 | Rail | Transportation and related services facilitated via rail travel (i.e. trains).|
| 6.3 | Water | Transportation and related services facilitated via water travel (i.e. ships).|
| 6.4 | Truck | Transportation and related services of goods via road travel for supply chains, done with large vehicles.|
| 6.5 | Transit | Transportation and related services for the movement of people (i.e. metropolitan busses, ferries, subways).|
| 6.6 | Pipeline | The transportation of resources via underground pipes (i.e. gas, water, sewage).|
| 6.7 | Courier Services | The delivery and related services for the distribution of goods or physical messages.|
| 6.8 | Supply Chain Services | Services related to the logistics for acquiring, processing, and transporting materials.|
| 7.1 | Software Publishers and Web Developers | Organizations that create and distribute software products and internet websites.|
| 7.2 | Telecommunications | Facilitation of the transfer and communication of information via technology (i.e. landline, 5g, ISP).|
| 7.3 | IT, Data Processing, Hosting, Etc. | Services that facilitate the operations of information systems.|
| 8.1 | Banks and Credit Unions | Organizations which provide banking and credit services|
| 8.2 | Insurance | Organizations that provide contracts for remediating unforeseen losses.|
| 8.3 | Other Financial Services | Other organizations that provide financial adjecent services (i.e. accounting, auditing, consulting, advisory).|
| 9.1 | Real Estate Sales/Rentals | Facilities that can be permanently or temporarliy made available for residential or commercial use.|
| 9.2 | Warehousing & Storage | Facilities that are used for the safekeeping of physical assets.|
| 9.3 | Automotive & Machinery Rental/Leasing | Vehicles and industrial machinery that can be temporarily lent out or leased.|
| 10.1 | Legal | Legal advice and representation by professionals.|
| 10.2 | Consulting | Expert advice in a specific field for clients.|
| 10.3 | Scientific Research and Development | Discovering new science or creating new technology.|
| 10.4 | Manual Labor and Related Services | Physical work done by hand or with simple tools.|
| 10.5 | Business Services (Marketing, PR, etc.) |  Services that help businesses function (accounting, marketing, etc.).|
| 10.6 | Labor Unions | Groups representing workers in bargaining with employers (wages, benefits).|
| 11.1 | Elementary/High Schools | Formal education after primary school.|
| 11.2 | Colleges/Universities | Higher education leading to a degree.|
| 11.3 | Technical/Industry Training | Job-specific skills training.|
| 12.1 | Private Practices, Walk-in Clinics, Etc. | Outpatient medical care by individual providers.|
| 12.2 | Advocacy Services | Support for people's rights in healthcare.|
| 12.3 | Psychological Practice | Mental health diagnosis and treatment by psychologists.|
| 12.4 | Pharmacology | Study of drugs and their effects.|
| 12.5 | Hospitals | Inpatient care facilities providing medical and surgical services.|
| 12.6 | Health Network | Coalition of healthcare providers working together.|
| 12.7 | Healthcare Insurance | Financial protection for medical expenses.|
| 12.8 | Diagnostics, Support Services, and Medical Manufacturing | Tests, equipment, and supplies used in healthcare.|
| 13.1 | Performing Arts & SPectator Sports | Live entertainment (theater, concerts, sports) for audiences.|
| 13.2 | Museums & Historical Sites | Places that preserve and exhibit objects or locations of interest.|
| 13.3 | Content Publishers | Create and distribute information (books, newspapers, websites).|
| 13.4 | Hotels, Amusement, Gambling, and Restaurants | Hospitality, entertainment, and leisure services (accommodation, theme parks, casinos, dining).|
| 14.1 | Religious Institutions | Places of worship (churches, mosques, etc.).|
| 14.2 | Charities |  Organizations helping others (donations, volunteering).|
| 14.3 | Non-Profit Organizations | Groups focused on social good, not profit.|
| 14.4 | Civic Associations | Community groups promoting civic engagement.|
| 15.1 | Federal Government | National government of the United States.|
| 15.2 | State Government | Government of a particular state or region of a country.|
| 15.3 | Local Government | Government of a city, county, etc.|
| 15.4 | Defense Industrial Base | Businesses supplying the a military.|
| 15.5 | Correctional Facilities | Prisons, jails, and other detention centers.|
| 15.6 | Emergency Services | Police, fire departments, and ambulance services.|
| 15.7 | Postal Services | Delivery of mail and packages.|
| 15.8 | Department of Defense | Military or government agency that oversees the military.|

### org-role-vocab

Constants: `B`, `V`, `S`, `T`, `O`

| Const | Value | Description |
| --- | --- | --- |
| B | Beneficiary | The organization accepted trade secrets, customer lists, intellectual property, etc. that the insider obtained through the incident.|
| V | Primary Victim | The organization was the primary victim organization of the insider's actions.|
| S | Secondary Victim | The organization was a secondary victim to the incident. E.g., An organization that relied on the primary victim's services in order to conduct their business.|
| T | Trusted Business Partner | The organization has an alliance (contractually, bonded, etc.) with the victim organization.|
| O | Other | Other role not described by this vocabulary.|
