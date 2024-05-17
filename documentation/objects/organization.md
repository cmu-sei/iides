# Organization

The organization(s) involved in the incident. At least one organization, the victim organization, should be included as part of an incident bundle. There may be other organizations involved, such as a competitor organization that benefitted from stolen data or pass through organization that received kickbacks. The victim organization(s) include all organizations negatively impacted by the incident, not just the organization(s) that employed the insider.

## Properties

- **`id`** (required) *(string)* : A unique string that begins with "organization--" and is appended with a UUIDv4.
  - Uses pattern: ^organization--[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
- **`name`** *(string)* : The name of the organization. E.g., "Company XYZ, Inc."
- **`city`** *(string)* : The city where the organization is located. Use the address of the headquarters if the whole organization was affected or use the address of the local branch if only that local branch was affected.
- **`state`** *(string)* : The state where the organization is located. Use the address of the headquarters if the whole organization was affected or use the address of the local branch if only that local branch was affected.
- **`country`** *(string)* : The country where the organization is located. Use the address of the headquarters if the whole organization was affected or use the address of the local branch if only that local branch was affected. Public implementations should use the standard codes provided by ISO 3166-1 alpha-2.
- **`postal_code`** *(integer)* : The postal code of the organization. Use the address of the headquarters if the whole organization was affected or use the address of the local branch if only that local branch was affected.
- **`small_business`** *(boolean)* : TRUE if the organization is a privately owned business with 500 or fewer employees.
- **`industry_sector`** *(string)* : Top level category for the economic sector the organization belongs to. Note, sectors are dervied from the North American Industry Classification System (NAICS) version 2022 published by the United States Office of Management and Budget.
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

Constants: `11`, `22`, `22`, `23`, `31`, `42`, `44`, `48`, `51`, `52`, `53`, `54`, `55`, `56`, `61`, `62`, `71`, `92`, `81`, `99`

| Const | Value | Description |
| --- | --- | --- |
| 11 | Agriculture and Mining | Growing crops, raising animals, harvesting timber, or extraction of naturally occurring minerals.|
| 22 | Mining, Quarrying, and Oil and Gas Extraction | Establishments that extract naturally occurring mineral solids, liquid minerals, and gases, to include quarrying, well operations, beneficiating, and other preparation customarily performed at the mine site, or as a part of mining activity.|
| 22 | Utilities | Provisioning of services for the public (e.g., energy, water, and waste collection).|
| 23 | Construction | Construction and engineering of buildings and associated support services or trades.|
| 31 | Manufacturing | Mechanical, Chemical, Physical changes to material.|
| 42 | Wholesale Trade | The exchange of goods and services.|
| 44 | Retail Trade | The exchange of goods and services.|
| 48 | Transportation and Warehousing | Services directly or indirectly involved in the movement of people.|
| 51 | Information | Hardware or software systems related to the processing, communications, and accessing of information.|
| 52 | Finance and Insurance | Financial services, payment processors, and insurance.|
| 53 | Real Estate and Rental/Leasing | Property sales and renting/leasing of assets.|
| 54 | Professional Services, Scientific and Technical Services | Services provided by trained professionals in specialized fields.|
| 55 | Management of Companies and Enterprises | Establishments that administer, oversee, and manage may hold the securities of the company or enterprise.|
| 56 | Administrative and Support and Waste Management and Remediation Services | Establishments performing routine support activities for the day-to-day operations of other organizations.|
| 61 | Educational Services | Instruction and training of individuals.|
| 62 | Healthcare and Social Assistance | Medical care and social advocacy/assistance.|
| 71 | Arts, Entertainment, Recreation | Industries that meet the entertainment needs of patrons.|
| 92 | Public Administration | Federal/State/Local administration and the oversight of public programs.|
| 81 | Other Services | Other services defined in NAICS.|
| 99 | Other | Other sector not listed in this vocabulary.|

### industry-subsector-vocab

Constants: `11.1`, `11.2`, `11.3`, `11.4`, `11.5`, `21.1`, `21.2`, `21.3`, `22.1`, `23.6`, `23.7`, `23.8`, `31.1`, `31.2`, `31.3`, `31.4`, `31.5`, `31.6`, `31.21`, `31.22`, `31.23`, `31.24`, `31.25`, `31.26`, `31.27`, `31.31`, `31.32`, `31.33`, `31.34`, `31.35`, `31.36`, `31.37`, `31.39`, `42.3`, `42.4`, `42.5`, `44.1`, `44.4`, `44.5`, `44.9`, `44.55`, `44.56`, `44.57`, `44.58`, `44.59`, `48.1`, `48.2`, `48.3`, `48.4`, `48.5`, `48.6`, `48.7`, `48.8`, `48.91`, `48.92`, `48.93`, `51.2`, `51.3`, `51.6`, `51.7`, `51.8`, `51.9`, `52.1`, `52.2`, `52.3`, `52.4`, `52.5`, `53.1`, `53.2`, `53.3`, `54.1`, `55.1`, `56.1`, `56.2`, `61.1`, `62.1`, `62.2`, `62.3`, `62.4`, `71.1`, `71.2`, `71.3`, `72.1`, `72.2`, `81.1`, `81.2`, `81.3`, `81.4`, `92.1`, `92.2`, `92.3`, `92.4`, `92.5`, `92.6`, `92.7`, `92.811`, `92.812`

| Const | Value | Description |
| --- | --- | --- |
| 11.1 | Crop Production | Industries in the Crop Production subsector grow crops mainly for food and fiber. The subsector comprises establishments, such as farms, orchards, groves, greenhouses, and nurseries, primarily engaged in growing crops, plants, vines, or trees and their seeds.|
| 11.2 | Animal Production and Aquaculture | Industries in the Animal Production and Aquaculture subsector raise or fatten animals for the sale of animals or animal products and/or raise aquatic plants and animals in controlled or selected aquatic environments for the sale of aquatic plants, animals, or their products. The subsector includes establishments, such as ranches, farms, and feedlots, primarily engaged in keeping, grazing, breeding, or feeding animals.|
| 11.3 | Forestry and Logging | Industries in the Forestry and Logging subsector grow and harvest timber on a long production cycle (i.e., of 10 years or more).|
| 11.4 | Fishing, Hunting and Trapping | Industries in the Fishing, Hunting and Trapping subsector harvest fish and other wild animals from their natural habitats and are dependent upon a continued supply of the natural resource.|
| 11.5 | Support Activities for Agriculture and Forestry | Industries in the Support Activities for Agriculture and Forestry subsector provide support services that are an essential part of agricultural and forestry production. These support activities may be performed by the agriculture or forestry producing establishment or conducted independently as an alternative source of inputs required for the production process for a given crop, animal, or forestry industry.|
| 21.1 | Oil and Gas Extraction | TODO|
| 21.2 | Mining (except Oil and Gas) | TODO|
| 21.3 | Support Activities for Mining | TODO|
| 22.1 | Utilities | TODO|
| 23.6 | Construction of Buildings | TODO|
| 23.7 | Heavy and Civil Engineering Construction | TODO|
| 23.8 | Specialty Trade Contractors | TODO|
| 31.1 | Food Manufacturing | TODO|
| 31.2 | Beverage and Tobacco Product Manufacturing | TODO|
| 31.3 | Textile Mills | TODO|
| 31.4 | Textile Product Mills | TODO|
| 31.5 | Apparel Manufacturing | TODO|
| 31.6 | Leather and Allied Product Manufacturing | TODO|
| 31.21 | Wood Product Manufacturing | TODO|
| 31.22 | Paper Manufacturing | TODO|
| 31.23 | Printing and Related Support Activities . | TODO|
| 31.24 | Petroleum and Coal Products Manufacturing | TODO|
| 31.25 | Chemical Manufacturing | TODO|
| 31.26 | Plastics and Rubber Products Manufacturing | TODO|
| 31.27 | Nonmetallic Mineral Product Manufacturing | TODO|
| 31.31 | Primary Metal Manufacturing | TODO|
| 31.32 | Fabricated Metal Product Manufacturing | TODO|
| 31.33 | Machinery Manufacturing | TODO|
| 31.34 | Computer and Electronic Product Manufacturing | TODO|
| 31.35 | Electrical Equipment, Appliance, and Component Manufacturing | TODO|
| 31.36 | Transportation Equipment Manufacturing | TODO|
| 31.37 | Furniture and Related Product Manufacturing | TODO|
| 31.39 | Miscellaneous Manufacturing | TODO|
| 42.3 | Merchant Wholesalers, Durable Goods | TODO|
| 42.4 | Merchant Wholesalers, Nondurable Goods | TODO|
| 42.5 | Wholesale Trade Agents and Brokers | TODO|
| 44.1 | Motor Vehicle and Parts Dealers | TODO|
| 44.4 | Building Material and Garden Equipment and Supplies Dealers | TODO|
| 44.5 | Food and Beverage Retailers | TODO|
| 44.9 | Furniture, Home Furnishings, Electronics, and Appliance Retailers | TODO|
| 44.55 | General Merchandise Retailers | TODO|
| 44.56 | Health and Personal Care Retailers | TODO|
| 44.57 | Gasoline Stations and Fuel Dealers | TODO|
| 44.58 | Clothing, Clothing Accessories, Shoe, and Jewelry Retailers | TODO|
| 44.59 | Sporting Goods, Hobby, Musical Instrument, Book, and Miscellaneous Retailers | TODO|
| 48.1 | Air Transportation | TODO|
| 48.2 | Rail Transportation | TODO|
| 48.3 | Water Transportation | TODO|
| 48.4 | Truck Transportation | TODO|
| 48.5 | Transit and Ground Passenger Transportation | TODO|
| 48.6 | Pipeline Transportation | TODO|
| 48.7 | Scenic and Sightseeing Transportation | TODO|
| 48.8 | Support Activities for Transportation | TODO|
| 48.91 | Postal Service | TODO|
| 48.92 | Couriers and Messengers | TODO|
| 48.93 | Warehousing and Storage | TODO|
| 51.2 | Motion Picture and Sound Recording Industries | TODO|
| 51.3 | Publishing Industries | TODO|
| 51.6 | Broadcasting and Content Providers | TODO|
| 51.7 | Telecommunications | TODO|
| 51.8 | Computing Infrastructure Providers, Data Processing, Web Hosting, and Related Services | TODO|
| 51.9 | Web Search Portals, Libraries, Archives, and Other Information Services | TODO|
| 52.1 | Monetary Authorities-Central Bank | TODO|
| 52.2 | Credit Intermediation and Related Activities | TODO|
| 52.3 | Securities, Commodity Contracts, and Other Financial Investments and Related Activities | TODO|
| 52.4 | Insurance Carriers and Related Activities | TODO|
| 52.5 | Funds, Trusts, and Other Financial Vehicles | TODO|
| 53.1 | Real Estate | TODO|
| 53.2 | Rental and Leasing Services | TODO|
| 53.3 | Lessors of Nonfinancial Intangible Assets (except Copyrighted Works) | TODO|
| 54.1 | Professional, Scientific, and Technical Services | TODO|
| 55.1 | Management of Companies and Enterprises | TODO|
| 56.1 | Administrative and Support Services | TODO|
| 56.2 | Waste Management and Remediation Services | TODO|
| 61.1 | Educational Services . | TODO|
| 62.1 | Ambulatory Health Care Services  | TODO|
| 62.2 | Hospitals | TODO|
| 62.3 | Nursing and Residential Care Facilities | TODO|
| 62.4 | Social Assistance | TODO|
| 71.1 | Performing Arts, Spectator Sports, and Related Industries | TODO|
| 71.2 | Museums, Historical Sites, and Similar Institutions | TODO|
| 71.3 | Amusement, Gambling, and Recreation Industries | TODO|
| 72.1 | Accommodation | TODO|
| 72.2 | Food Services and Drinking Places | TODO|
| 81.1 | Repair and Maintenance | TODO|
| 81.2 | Personal and Laundry Services | TODO|
| 81.3 | Religious, Grantmaking, Civic, Professional, and Similar Organizations | TODO|
| 81.4 | Private Households | TODO|
| 92.1 | Executive, Legislative, and Other General Government Support | TODO|
| 92.2 | Justice, Public Order, and Safety Activities | TODO|
| 92.3 | Administration of Human Resource Programs | TODO|
| 92.4 | Administration of Environmental Quality Programs | TODO|
| 92.5 | Administration of Housing Programs, Urban Planning, and Community Development | TODO|
| 92.6 | Administration of Economic Programs | TODO|
| 92.7 | Space Research and Technology | TODO|
| 92.811 | National Security | This industry comprises government establishments of the Armed Forces, including the National Guard, primarily engaged in national security and related activities.|
| 92.812 | International Affairs | This industry comprises establishments of U.S. and foreign governments primarily engaged in international affairs and programs relating to other nations and peoples.|

### org-role-vocab

Constants: `B`, `V`, `S`, `T`, `O`

| Const | Value | Description |
| --- | --- | --- |
| B | Beneficiary | The organization accepted trade secrets, customer lists, intellectual property, etc. that the insider obtained through the incident.|
| V | Primary Victim | The organization was the primary victim organization of the insider's actions.|
| S | Secondary Victim | The organization was a secondary victim to the incident. E.g., An organization that relied on the primary victim's services in order to conduct their business.|
| T | Trusted Business Partner | The organization has an alliance (contractually, bonded, etc.) with the victim organization.|
| O | Other | Other role not described by this vocabulary.|
