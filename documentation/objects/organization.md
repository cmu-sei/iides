# Organization
TODO

## Properties
- **`id`** (required) *(string)* : TODO . Uses pattern 'organization--[UUIDv4]'
	- pattern: ^organization--[UUIDv4]
- **`name`** *(string)* : TODO
- **`city`** *(string)* : TODO
- **`state`** *(string)* : TODO
- **`country`** *(string)* : TODO
	- A value from [country-vocab](#country-vocab)
- **`postal_code`** *(integer)* : TODO
- **`small_business`** *(boolean)* : TODO
- **`industry_sector_tier1`** *(string)* : TODO
	- A value from [industry-sector-tier1-vocab](#industry-sector-tier1-vocab)
- **`industry_sector_tier2`** *(string)* : TODO
	- A value from [industry-sector-tier2-vocab](#industry-sector-tier2-vocab)
- **`business`** *(string)* : TODO
- **`parent_company`** *(string)* : TODO
- **`incident_role`** *(string)* : TODO
	- A value from [org-role-vocab](#org-role-vocab)

## Vocabularies

### industry-sector-tier1-vocab
Values: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`, `16`
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
Values: `1.1`, `1.2`, `1.3`, `1.4`, `2.1`, `2.2`, `2.2`, `2.3`, `2.5`, `3.1`, `3.2`, `3.3`, `3.4`, `4.1`, `4.2`, `4.3`, `4.4`, `4.5`, `5.1`, `5.2`, `5.3`, `6.1`, `6.2`, `6.3`, `6.4`, `6.5`, `6.6`, `6.7`, `6.8`, `7.1`, `7.2`, `7.3`, `8.1`, `8.2`, `8.3`, `9.1`, `9.2`, `9.3`, `10.1`, `10.2`, `10.3`, `10.4`, `10.5`, `10.6`, `11.1`, `11.2`, `11.3`, `12.1`, `12.2`, `12.3`, `12.4`, `12.5`, `12.6`, `12.7`, `12.8`, `13.1`, `13.2`, `13.3`, `13.4`, `14.1`, `14.2`, `14.3`, `14.4`, `15.1`, `15.2`, `15.3`, `15.4`, `15.5`, `15.6`, `15.7`, `15.8`
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

### country-vocab
Values: `AD`, `AE`, `AF`, `AG`, `AI`, `AL`, `AM`, `AO`, `AQ`, `AR`, `AS`, `AT`, `AU`, `AW`, `AX`, `AZ`, `BA`, `BB`, `BD`, `BE`, `BF`, `BG`, `BH`, `BI`, `BJ`, `BL`, `BM`, `BN`, `BO`, `BQ`, `BR`, `BS`, `BT`, `BV`, `BW`, `BY`, `BZ`, `CA`, `CC`, `CD`, `CF`, `CG`, `CH`, `CI`, `CK`, `CL`, `CM`, `CN`, `CO`, `CR`, `CU`, `CV`, `CW`, `CX`, `CY`, `CZ`, `DE`, `DJ`, `DK`, `DM`, `DO`, `DZ`, `EC`, `EE`, `EG`, `EH`, `ER`, `ES`, `ET`, `FI`, `FJ`, `FK`, `FM`, `FO`, `FR`, `GA`, `GB`, `GD`, `GE`, `GF`, `GG`, `GH`, `GI`, `GL`, `GM`, `GN`, `GP`, `GQ`, `GR`, `GS`, `GT`, `GU`, `GW`, `GY`, `HK`, `HM`, `HN`, `HR`, `HT`, `HU`, `ID`, `IE`, `IL`, `IM`, `IN`, `IO`, `IQ`, `IR`, `IS`, `IT`, `JE`, `JM`, `JO`, `JP`, `KE`, `KG`, `KH`, `KI`, `KM`, `KN`, `KP`, `KR`, `KW`, `KY`, `KZ`, `LA`, `LB`, `LC`, `LI`, `LK`, `LR`, `LS`, `LT`, `LU`, `LV`, `LY`, `MA`, `MC`, `MD`, `ME`, `MF`, `MG`, `MH`, `MK`, `ML`, `MM`, `MN`, `MO`, `MP`, `MQ`, `MR`, `MS`, `MT`, `MU`, `MV`, `MW`, `MX`, `MY`, `MZ`, `NA`, `NC`, `NE`, `NF`, `NG`, `NI`, `NL`, `NO`, `NP`, `NR`, `NU`, `NZ`, `OM`, `PA`, `PE`, `PF`, `PG`, `PH`, `PK`, `PL`, `PM`, `PN`, `PR`, `PS`, `PT`, `PW`, `PY`, `QA`, `RE`, `RO`, `RS`, `RU`, `RW`, `SA`, `SB`, `SC`, `SD`, `SE`, `SG`, `SH`, `SI`, `SJ`, `SK`, `SL`, `SM`, `SN`, `SO`, `SR`, `SS`, `ST`, `SV`, `SX`, `SY`, `SZ`, `TC`, `TD`, `TF`, `TG`, `TH`, `TJ`, `TK`, `TL`, `TM`, `TN`, `TO`, `TR`, `TT`, `TV`, `TW`, `TZ`, `UA`, `UG`, `UM`, `US`, `UY`, `UZ`, `VA`, `VC`, `VE`, `VG`, `VI`, `VN`, `VU`, `WF`, `WS`, `YE`, `YT`, `ZA`, `ZM`, `ZW`
| Const | Value | Description |
| --- | --- | --- |
| AD | Andorra | |
| AE | United Arab Emirates | |
| AF | Afghanistan | |
| AG | Antigua and Barbuda | |
| AI | Anguilla | |
| AL | Albania | |
| AM | Armenia | |
| AO | Angola | |
| AQ | Antarctica | |
| AR | Argentina | |
| AS | American Samoa | |
| AT | Austria | |
| AU | Australia | |
| AW | Aruba | |
| AX | Åland Islands | |
| AZ | Azerbaijan | |
| BA | Bosnia and Herzegovina | |
| BB | Barbados | |
| BD | Bangladesh | |
| BE | Belgium | |
| BF | Burkina Faso | |
| BG | Bulgaria | |
| BH | Bahrain | |
| BI | Burundi | |
| BJ | Benin | |
| BL | Saint Barthélemy | |
| BM | Bermuda | |
| BN | Brunei Darussalam | |
| BO | Bolivia | |
| BQ | Bonaire | |
| BR | Brazil | |
| BS | Bahamas | |
| BT | Bhutan | |
| BV | Bouvet Island | |
| BW | Botswana | |
| BY | Belarus | |
| BZ | Belize | |
| CA | Canada | |
| CC | Cocos (Keeling) Islands | |
| CD | Congo, Democratic Republic of the | |
| CF | Central African Republic | |
| CG | Congo | |
| CH | Switzerland | |
| CI | Côte d'Ivoire | |
| CK | Cook Islands | |
| CL | Chile | |
| CM | Cameroon | |
| CN | China | |
| CO | Colombia | |
| CR | Costa Rica | |
| CU | Cuba | |
| CV | Cabo Verde | |
| CW | Curaçao | |
| CX | Christmas Island | |
| CY | Cyprus | |
| CZ | Czechia | |
| DE | Germany | |
| DJ | Djibouti | |
| DK | Denmark | |
| DM | Dominica | |
| DO | Dominican Republic | |
| DZ | Algeria | |
| EC | Ecuador | |
| EE | Estonia | |
| EG | Egypt | |
| EH | Western Sahara | |
| ER | Eritrea | |
| ES | Spain | |
| ET | Ethiopia | |
| FI | Finland | |
| FJ | Fiji | |
| FK | Falkland Islands (Malvinas) | |
| FM | Micronesia, Federated States of | |
| FO | Faroe Islands | |
| FR | France | |
| GA | Gabon | |
| GB | United Kingdom of Great Britain and Northern Ireland | |
| GD | Grenada | |
| GE | Georgia | |
| GF | French Guiana | |
| GG | Guernsey | |
| GH | Ghana | |
| GI | Gibraltar | |
| GL | Greenland | |
| GM | Gambia | |
| GN | Guinea | |
| GP | Guadeloupe | |
| GQ | Equatorial Guinea | |
| GR | Greece | |
| GS | South Georgia and the South Sandwich Islands | |
| GT | Guatemala | |
| GU | Guam | |
| GW | Guinea-Bissau | |
| GY | Guyana | |
| HK | Hong Kong | |
| HM | Heard Island and McDonald Islands | |
| HN | Honduras | |
| HR | Croatia | |
| HT | Haiti | |
| HU | Hungary | |
| ID | Indonesia | |
| IE | Ireland | |
| IL | Israel | |
| IM | Isle of Man | |
| IN | India | |
| IO | British Indian Ocean Territory | |
| IQ | Iraq | |
| IR | Iran, Islamic Republic of | |
| IS | Iceland | |
| IT | Italy | |
| JE | Jersey | |
| JM | Jamaica | |
| JO | Jordan | |
| JP | Japan | |
| KE | Kenya | |
| KG | Kyrgyzstan | |
| KH | Cambodia | |
| KI | Kiribati | |
| KM | Comoros | |
| KN | Saint Kitts and Nevis | |
| KP | Korea, Democratic People's Republic of | |
| KR | Korea, Republic of | |
| KW | Kuwait | |
| KY | Cayman Islands | |
| KZ | Kazakhstan | |
| LA | Lao People's Democratic Republic | |
| LB | Lebanon | |
| LC | Saint Lucia | |
| LI | Liechtenstein | |
| LK | Sri Lanka | |
| LR | Liberia | |
| LS | Lesotho | |
| LT | Lithuania | |
| LU | Luxembourg | |
| LV | Latvia | |
| LY | Libya | |
| MA | Morocco | |
| MC | Monaco | |
| MD | Moldova, Republic of | |
| ME | Montenegro | |
| MF | Saint Martin (French part) | |
| MG | Madagascar | |
| MH | Marshall Islands | |
| MK | North Macedonia | |
| ML | Mali | |
| MM | Myanmar | |
| MN | Mongolia | |
| MO | Macao | |
| MP | Northern Mariana Islands | |
| MQ | Martinique | |
| MR | Mauritania | |
| MS | Montserrat | |
| MT | Malta | |
| MU | Mauritius | |
| MV | Maldives | |
| MW | Malawi | |
| MX | Mexico | |
| MY | Malaysia | |
| MZ | Mozambique | |
| NA | Namibia | |
| NC | New Caledonia | |
| NE | Niger | |
| NF | Norfolk Island | |
| NG | Nigeria | |
| NI | Nicaragua | |
| NL | Netherlands, Kingdom of the | |
| NO | Norway | |
| NP | Nepal | |
| NR | Nauru | |
| NU | Niue | |
| NZ | New Zealand | |
| OM | Oman | |
| PA | Panama | |
| PE | Peru | |
| PF | French Polynesia | |
| PG | Papua New Guinea | |
| PH | Philippines | |
| PK | Pakistan | |
| PL | Poland | |
| PM | Saint Pierre and Miquelon | |
| PN | Pitcairn | |
| PR | Puerto Rico | |
| PS | Palestine, State of | |
| PT | Portugal | |
| PW | Palau | |
| PY | Paraguay | |
| QA | Qatar | |
| RE | Réunion | |
| RO | Romania | |
| RS | Serbia | |
| RU | Russian Federation | |
| RW | Rwanda | |
| SA | Saudi Arabia | |
| SB | Solomon Islands | |
| SC | Seychelles | |
| SD | Sudan | |
| SE | Sweden | |
| SG | Singapore | |
| SH | Saint Helena, Ascension and Tristan da Cunha | |
| SI | Slovenia | |
| SJ | Svalbard and Jan Mayen | |
| SK | Slovakia | |
| SL | Sierra Leone | |
| SM | San Marino | |
| SN | Senegal | |
| SO | Somalia | |
| SR | Suriname | |
| SS | South Sudan | |
| ST | Sao Tome and Principe | |
| SV | El Salvador | |
| SX | Sint Maarten (Dutch part) | |
| SY | Syrian Arab Republic | |
| SZ | Eswatini | |
| TC | Turks and Caicos Islands | |
| TD | Chad | |
| TF | French Southern Territories | |
| TG | Togo | |
| TH | Thailand | |
| TJ | Tajikistan | |
| TK | Tokelau | |
| TL | Timor-Leste | |
| TM | Turkmenistan | |
| TN | Tunisia | |
| TO | Tonga | |
| TR | Türkiye | |
| TT | Trinidad and Tobago | |
| TV | Tuvalu | |
| TW | Taiwan, Province of China | |
| TZ | Tanzania, United Republic of | |
| UA | Ukraine | |
| UG | Uganda | |
| UM | United States Minor Outlying Islands | |
| US | United States of America | |
| UY | Uruguay | |
| UZ | Uzbekistan | |
| VA | Holy See | |
| VC | Saint Vincent and the Grenadines | |
| VE | Venezuela, Bolivarian Republic of | |
| VG | Virgin Islands (British) | |
| VI | Virgin Islands (U.S.) | |
| VN | Viet Nam | |
| VU | Vanuatu | |
| WF | Wallis and Futuna | |
| WS | Samoa | |
| YE | Yemen | |
| YT | Mayotte | |
| ZA | South Africa | |
| ZM | Zambia | |
| ZW | Zimbabwe | |

### org-role-vocab
Values: `B`, `V`, `T`, `O`
| Const | Value | Description |
| --- | --- | --- |
| B | Beneficiary | TODO|
| V | Victim | TODO|
| T | Trusted Business Partner | TODO|
| O | Other | TODO|
