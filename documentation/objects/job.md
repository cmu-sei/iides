# Job

This contains details of the employment relationship between an individual and an organization. A job may be connected to only one organization and may be connected to only one insider or accomplice.

## Properties

- **`id`** (required) *(string)* : A unique string that begins with "job--" and is appended with a UUIDv4
  - Uses pattern: ^job--[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
- **`job_function`** *(string)* : Functional category of the individual's job. job_function and occupation vocabularies are based in large part on the 2018 Standard Occupational Classification system published by the Bureau of Labor Statistics
	- A constant from [job-function-vocab](#job-function-vocab)
  - Required if `occupation` exists
- **`occupation`** *(string)* : The subcategory of the individual's job. When present, `job_function` should also be present. The chosen constant for occupation MUST match the constant for job_function
	- A constant from [occupation-vocab](#occupation-vocab)
  - Required if `title` exists
- **`title`** *(string)* : The individual's job title. If title is specified, `occupation` should be as well
- **`position_technical`** *(boolean)* : The individual had access to technical areas of the organization as part of their job role (e.g., IT admin, network engineer, help desk associate)
- **`access_authorization`** *(string)* : The level of access control given by this job role
	- A constant from [access-auth-vocab](#access-auth-vocab)
- **`employment_type`** *(string)* : The individual's employment arrangement at the time of the incident
	- A constant from [employment-type-vocab](#employment-type-vocab)
- **`hire_date`** *(date)* : Date the individual was hired into this position
- **`departure_date`** *(date)* : Date the individual departed from this position
- **`tenure`** *(timedelta)* : The amount of time the individual spent in this particular job role
- **`comment`** *(string)* : Clarifying comments or details about the job or the individual's employment with the organization

## Vocabularies

### job-function-vocab

Constants: `11`, `13`, `15`, `17`, `19`, `21`, `22`, `23`, `25`, `27`, `29`, `31`, `33`, `35`, `37`, `39`, `41`, `43`, `45`, `47`, `49`, `51`, `53`, `55`, `99`

| Const | Value | Description |
| --- | --- | --- |
| 11 | Management | Management|
| 13 | Business and Financial Operations | Business and Financial Operations|
| 15 | Computer and Mathematical | Computer and Mathematical|
| 17 | Architecture and Engineering | Architecture and Engineering|
| 19 | Life, Physical, and Social Science | Life, Physical, and Social Science|
| 21 | Community and Social Service | Community and Social Service|
| 22 | Student | Student|
| 23 | Legal | Legal|
| 25 | Educational Instruction and Library | Educational Instruction and Library|
| 27 | Arts, Design, Entertainment, Sports, and Media | Arts, Design, Entertainment, Sports, and Media|
| 29 | Healthcare Practitioners and Technical | Healthcare Practitioners and Technical|
| 31 | Healthcare Support | Healthcare Support|
| 33 | Protective Service | Protective Service|
| 35 | Food Preparation and Serving Related | Food Preparation and Serving Related|
| 37 | Building and Grounds Cleaning and Maintenance | Building and Grounds Cleaning and Maintenance|
| 39 | Personal Care and Service Occupations | Personal Care and Service Occupations|
| 41 | Sales and Related | Sales and Related|
| 43 | Office and Administrative Support | Office and Administrative Support|
| 45 | Farming, Fishing, and Forestry Occupations | Farming, Fishing, and Forestry Occupations|
| 47 | Construction and Extraction Occupations | Construction and Extraction Occupations|
| 49 | Installation, Maintenance, and Repair | Installation, Maintenance, and Repair|
| 51 | Production | Production|
| 53 | Transportation and Material Moving | Transportation and Material Moving|
| 55 | Military Specific | Military Specific|
| 99 | Other | Other job function not listed in this vocabulary.|

### occupation-vocab

Constants: `11.1`, `11.2`, `11.3`, `11.9`, `13.1`, `13.2`, `15.1`, `15.2`, `17.1`, `17.2`, `17.3`, `19.1`, `19.2`, `19.3`, `19.4`, `19.5`, `21.1`, `21.2`, `23.1`, `23.2`, `25.2`, `25.3`, `25.4`, `25.9`, `27.1`, `27.2`, `27.3`, `27.4`, `29.1`, `29.2`, `29.9`, `31.1`, `31.2`, `31.9`, `33.1`, `33.2`, `33.3`, `33.9`, `35.1`, `35.2`, `35.3`, `35.9`, `37.1`, `37.2`, `37.3`, `39.1`, `39.2`, `39.3`, `39.4`, `39.5`, `39.6`, `39.7`, `39.9`, `41.1`, `41.2`, `41.3`, `41.4`, `41.9`, `43.1`, `43.2`, `43.3`, `43.4`, `43.5`, `43.6`, `43.9`, `45.1`, `45.2`, `45.3`, `45.4`, `47.1`, `47.2`, `47.3`, `47.4`, `47.5`, `49.1`, `49.2`, `49.3`, `49.9`, `51.1`, `51.2`, `51.3`, `51.4`, `51.5`, `51.6`, `51.7`, `51.8`, `51.9`, `53.1`, `53.2`, `53.3`, `53.4`, `53.5`, `53.6`, `53.7`, `55.1`, `55.2`, `55.3`, `99.1`, `99.9`

| Const | Value | Description |
| --- | --- | --- |
| 11.1 | Top Executives | Chief Executives, General and Operations Managers, Legislators|
| 11.2 | Advertising, Public Relations, and Sales Managers | Advertising and Promotions Managers, Marketing Managers, Sales Managers, Public Relations Managers, Fundraising Managers|
| 11.3 | Operations Specialties Managers | Administrative Services Managers, Facilities Managers, Computer and Information Systems Managers, Financial Managers, Industrial Production Managers, Purchasing Managers, Transportation and Distribution Managers, Compensation and Benefits Managers, Human Resources Managers, Training and Development Managers|
| 11.9 | Other Management Occupations | Construction Managers, Education Administrators, Food Service Managers, Entertainment and Recreation Managers, Postmasters, Property and Community Association Managers, Social and Community Service Managers, Emergency Management Directors, Funeral Home Managers, Personal Service Managers, etc.|
| 13.1 | Business Operations Specialists | Agents and Business Managers, Buyers and Purchasing Agents, Claims Adjusters, Compliance Officers, Human Resources Specialists, Project Managers, Management Analysts, Event Planners, Fundraisers, Benefits and Job Analysts, Training and Development Specialists, Market Research Analysts, etc.|
| 13.2 | Financial Specialists | Accountants, Auditors, Appraisers, Credit Analysts, Financial Analysts, Financial Advisors, Insurance Underwriters, Credit Counselors, Loan Officers, Tax Preparers, etc.|
| 15.1 | Computer Occupations | Computer Systems Analysts, Information Security Analysts, Network Support Specialists, User Support Specialists, Network Architects, Systems Administrators, Software Developers, Web Developers, Interface Designers, etc.|
| 15.2 | Mathematical Science Occupations | Actuaries, Mathematicians, Operations Research Analysts, Statisticians, Data Scientists, etc.|
| 17.1 | Architects, Surveyors, and Cartographers | Architects, Landscape Architects, Cartographers, Surveyors, etc.|
| 17.2 | Engineers | Aerospace Engineers, Bioengineers Engineers, Chemical Engineers, Civil Engineers, Electrical Engineers, Electronics Engineers, Environmental Engineers, Industrial Engineers, Marine Engineers, Naval Architects, Mechanical Engineers, Geological Engineers, etc.|
| 17.3 | Drafters, Engineering Technicians, and Mapping Technicians | Architectural Drafters, Mechanical Drafters, Other Drafters, Aerospace Technicians, Civil Engineering Technicians, Environmental Engineering Technicians, Industrial Engineering Technicians, Mechanical Engineering Technicians, Engineering Technicians, Surveying Technicians, etc.|
| 19.1 | Life Scientists | Food Scientists and Technologists, Microbiologists, Zoologists, Biological Scientists, Conservation Scientists, Epidemiologists, Medical Scientists, etc.|
| 19.2 | Physical Scientists | Astronomers, Physicists, Atmospheric and Space Scientists, Chemists, Materials Scientists, Environmental Scientists and Specialists, Geoscientists, Hydrologists, etc.|
| 19.3 | Social Scientists and Related Workers | Economists, Survey Researchers, Psychologists, Sociologists, Urban Planners, Anthropologists, Archeologists, Geographers, Historians, Political Scientists, etc.|
| 19.4 | Life, Physical, and Social Science Technicians | Biological Technicians, Chemical Technicians, Environmental Science Technicians, Geological Technicians, Nuclear Technicians, Social Science Research Assistants, Forest and Conservation Technicians, Forensic Science Technicians, etc.|
| 19.5 | Occupational Health and Safety Specialists and Technicians | Occupational Health and Safety Specialists and Technicians|
| 21.1 | Social Service Specialists | Guidance Counselors, Marriage and Family Therapists, Mental Health Counselors, Rehabilitation Counselors, Social Workers, Health Education Specialists, Probation Officers, Social Service Assistants, Community Health Workers, etc.|
| 21.2 | Religious Workers | Clergy, Religious Activities Directors, Religious Education Directors, etc.|
| 23.1 | Lawyers, Judges, and Related Workers | Lawyers, Judicial Law Clerks, Hearing Officers, Arbitrators, Judges, Magistrates, etc.|
| 23.2 | Legal Support Workers | Paralegals, Legal Assistants, Title Examiners, Abstractors, etc.|
| 25.2 | K12 and Special Education Teachers | Preschool, Elementary, Middle, Secondary, and Special Education Teachers|
| 25.3 | Other Teachers and Instructors | Adult Education, English as a Second Language Instructors, Self-Enrichment Teachers, Substitute Teachers, Tutors, etc.|
| 25.4 | Librarians, Curators, and Archivists | Archivists, Curators, Museum Technicians and Conservators,Librarians, Media Collections Specialists, Library Technicians|
| 25.9 | Other Educational Instruction and Library Occupations | Farm and Home Management Educators, Instructional Coordinators, Teaching Assistants, Library Workers, etc.|
| 27.1 | Art and Design Workers | Art Directors, Fine Artists, Animators, Fashion Designers, Graphic Designers, Interior Designers, etc.|
| 27.2 | Entertainers and Performers, Sports and Related Workers | Actors, Producers, Directors, Athletes, Coaches, Scouts, Referees, Dancers, Choreographers, Composers, Musicians, etc.|
| 27.3 | Media and Communication Workers | Broadcast Announcers, Radio Disc Jockeys, News Analysts, Reporters, Journalists, Public Relations Specialists, Editors, Technical Writers, Writers and Authors, Interpreters and Translators, Court Reporters and Simultaneous Captioners, etc.|
| 27.4 | Media and Communication Equipment Workers | Audio and Video Technicians, Broadcast Technicians, Sound Engineering Technicians, Lighting Technicians, Photographers, Camera Operators, Film Editors, etc.|
| 29.1 | Healthcare Practitioners | Chiropractors, Dentists, Dietitians, Pharmacists, Physician Assistants, Physical and Occupational Therapists, Veterinarians, Nurses, Psychiatrists, Radiologists, Physicians, Surgeons, etc.|
| 29.2 | Health Technologists and Technicians | Laboratory Technicians, Sonographers, Radiologic Technicians, Paramedics, Pharmacy Technicians, Psychiatric Technicians, Veterinary Technicians, Vocational Nurses, Medical Records Specialists, Orthotists and Prosthetists, etc.|
| 29.9 | Other Healthcare Practitioners and Technical Occupations | Health Information Technologists and Medical Registrars, Athletic Trainers, Genetic Counselors, Surgical Assistants, etc.|
| 31.1 | Home Health Aides, Nursing Assistants, and Psychiatric Aides | Home Health Aides, Personal Care Aides, Nursing Assistants, Orderlies, Psychiatric Aides, etc.|
| 31.2 | Occupational and Physical Therapist Assistants and Aides | Occupational Therapy Assistants and Aides, Physical Therapist Assistants Aides|
| 31.9 | Other Healthcare Support Occupations | Massage Therapists, Dental Assistants, Medical Assistants, Medical Transcriptionists, Pharmacy Aides, Veterinary Assistants and Laboratory Animal Caretakers, Phlebotomists, etc.|
| 33.1 | Supervisors of Protective Service Workers | First-Line Supervisors of Protective Service Workers|
| 33.2 | Firefighting and Prevention Workers | Firefighters, Fire Investigators, Forest Fire Prevention Specialists, etc.|
| 33.3 | Law Enforcement Workers | Bailiffs, Correctional Officers, Detectives and Criminal Investigators, Fish and Game Wardens, Parking Enforcement Workers, Police and Sheriff's Patrol Officers, etc.|
| 33.9 | Other Protective Service Workers | Animal Control Workers, Private Detectives and Investigators, Security Guards, Lifeguards and Other Recreational Protective Service Workers, Transportation Security Screeners, etc.|
| 35.1 | Supervisors of Food Preparation and Serving Workers | Chefs and Head Cooks, First-Line Supervisors of Food Preparation and Serving Workers|
| 35.2 | Cooks and Food Preparation Workers | Cooks and Food Preparation Workers, etc.|
| 35.3 | Food and Beverage Serving Workers | Bartenders, Fast Food and Counter Workers, Waiters and Waitresses, Food Servers (Nonrestaurant), etc.|
| 35.9 | Other Food Preparation and Serving Related Workers | Dining Room and Cafeteria Attendants and Bartender Helpers, Dishwashers, Hosts and Hostesses, etc.|
| 37.1 | Supervisors of Building and Grounds Cleaning and Maintenance Workers | First-Line Supervisors of Housekeeping, Janitorial Workers, and Groundskeeping Workers|
| 37.2 | Building Cleaning and Pest Control Workers | Janitors and Cleaners, Maids and Housekeeping Cleaners, Building Cleaning Workers, Pest Control Workers, etc.|
| 37.3 | Grounds Maintenance Workers | Landscaping and Groundskeeping Workers, Tree Trimmers, etc.|
| 39.1 | Supervisors of Personal Care and Service Workers | First-Line Supervisors of Personal Care and Service Workers|
| 39.2 | Animal Care and Service Workers | Animal Trainers, Animal Caretakers, etc.|
| 39.3 | Entertainment Attendants and Related Workers | Gambling Dealers, Sports Book Writers and Runners, Ushers and Ticket Takers, Amusement and Recreation Attendants, Dressing Room Attendants, etc.|
| 39.4 | Funeral Service Workers | Embalmers, Crematory Operators, Funeral Attendants, Morticians, Undertakers, and Funeral Arrangers, etc.|
| 39.5 | Personal Appearance Workers | Barbers, Hairdressers, Hairstylists, Cosmetologists, Makeup Artists, Manicurists, Skincare Specialists, etc.|
| 39.6 | Baggage Porters, Bellhops, and Concierges | Baggage Porters and Bellhops, Concierges, etc.|
| 39.7 | Tour and Travel Guides | Tour Guides and Escorts, Travel Guides, etc.|
| 39.9 | Other Personal Care and Service Workers | Childcare Workers, Exercise Trainers and Group Fitness Instructors, Recreation Workers, Residential Advisors, etc.|
| 41.1 | Supervisors of Sales Workers | First-Line Supervisors of Sales Workers|
| 41.2 | Retail Sales Workers | Cashiers, Counter and Rental Clerks, Parts Salespersons, Retail Salespersons, etc.|
| 41.3 | Sales Representatives, Services | Advertising Sales Agents, Insurance Sales Agents, Securities and Commodities Sales Agents, Financial Services Sales Agents, Travel Agents, etc.|
| 41.4 | Sales Representatives, Wholesale and Manufacturing | Sales Representatives for Wholesale and Manufacturing|
| 41.9 | Other Sales and Related Workers | Demonstrators and Product Promoters, Real Estate Brokers, Real Estate Sales Agents, Sales Engineers, Telemarketers, Door-to-Door Sales Workers, News and Street Vendors, etc.|
| 43.1 | Supervisors of Office and Administrative Support Workers | First-Line Supervisors of Office and Administrative Support Workers|
| 43.2 | Communications Equipment Operators | Telephone Operators, Communications Equipment Operators, etc.|
| 43.3 | Financial Clerks | Bill Collectors, Bookkeeping and Accounting Clerks, and Auditing Clerks, Payroll and Timekeeping Clerks, Procurement Clerks, Tellers, Financial Clerks, etc.|
| 43.4 | Information and Record Clerks | Court Clerks, Customer Service Representatives, Eligibility Interviewers, File Clerks, Hotel Desk Clerks, Library Assistants, Accounts Clerks, Order Clerks, Human Resources Assistants, Receptionists, Information Clerks, Ticket Agents and Travel Clerks, etc.|
| 43.5 | Material Recording, Scheduling, Dispatching, and Distributing Workers | Cargo and Freight Agents, Couriers, Messengers, Dispatchers, Meter Readers, Postal Service Clerks and Carriers, Mail Sorters, Shipping and Receiving Clerks, Inventory Clerks, etc.|
| 43.6 | Administrative Assistants | Executive Administrative Assistants, Legal Secretaries, Administrative Assistants, etc.|
| 43.9 | Other Office and Administrative Support Workers | Data Entry Clerks, Insurance Claims Clerks, Mail Clerks, Office Clerks, Proofreaders, Statistical Assistants, etc.|
| 45.1 | Supervisors of Farming, Fishing, and Forestry Workers | First-Line Supervisors of Farming, Fishing, and Forestry Workers|
| 45.2 | Agricultural Workers | Agricultural Inspectors, Animal Breeders, Graders and Sorters, Equipment Operators, Farmworkers and Laborers, etc.|
| 45.3 | Fishing and Hunting Workers | Fishing and Hunting Workers|
| 45.4 | Forest, Conservation, and Logging Workers | Forest and Conservation Workers, Logging Workers, etc.|
| 47.1 | Supervisors of Construction and Extraction Workers | First-Line Supervisors of Construction Trades and Extraction Workers |
| 47.2 | Construction Trades Workers | Masons, Carpenters, Floor Layers, Construction Laborers, Equipment Operators, Drywall Installers, Electricians, Painters, Paperhangers, Plumbers, Pipefitters, Roofers, etc.|
| 47.3 | Helpers, Construction Trades | Helpers of Masons, Carpenters, Electricians, Painters, Paperhangers, Pipelayers, Plumbers, Pipefitters, and Steamfitters, Roofers, etc.|
| 47.4 | Other Construction and Related Workers | Construction and Building Inspectors, Elevator and Escalator Installers and Repairers, Fence Erectors, Hazardous Materials Removal Workers, Highway Maintenance Workers, Rail-Track Laying and Maintenance Equipment Operators, Septic Tank Servicers and Sewer Pipe Cleaners, etc.|
| 47.5 | Extraction Workers | Oil and Gas Operators, Explosives Workers, Ordnance Handling Experts, Blasters, Mining Machine Operators, Quarry Rock Splitters, Extraction Workers, etc.|
| 49.1 | Supervisors of Installation, Maintenance, and Repair Workers | First-Line Supervisors of Mechanics, Installers, and Repairers|
| 49.2 | Electrical and Electronic Equipment Mechanics, Installers, and Repairers | Computer and Office Machine Repairers, Radio and Cellular Equipment Installers, Avionics Technicians, Electric Motor and Power Tool Repairers, Electrical and Electronics Repairers and Installers, Audiovisual Equipment Technicicans, Security and Fire Alarm Systems Installers, etc.|
| 49.3 | Vehicle and Mobile Equipment Mechanics, Installers, and Repairers | Aircraft Mechanics and Service Technicians, Automotive Body Repairers, Automotive Service Technicians and Mechanics, Mobile Heavy Equipment Mechanics, Motorboat Mechanics, Outdoor Power Equipment and Other Small Engine Mechanics, Tire Repairers and Changers, etc.|
| 49.9 | Other Installation, Maintenance, and Repair Occupations | HVAC and Refrigeration Mechanics, Home Appliance Repairers, Machinery Maintenance Workers, Power-Line Installers and Repairers, Precision Instrument and Equipment Repairers, General Maintenance and Repair Workers, Service Technicians, Signal and Track Switch Repairers, etc.|
| 51.1 | Supervisors of Production Workers | First-Line Supervisors of Production and Operating Workers|
| 51.2 | Assemblers and Fabricators | Electrical and Electronic Equipment Assemblers, Engine and Other Machine Assemblers, Structural Metal Fabricators and Fitters, Fiberglass Laminators and Fabricators, etc.|
| 51.3 | Food Processing Workers | Bakers, Butchers and Meat Cutters, Meat Packers, Machine Operators, etc.|
| 51.4 | Metal Workers and Plastic Workers | Machinists, Furnace Operators, Casters, Model Makers, Patternmakers, Tool and Die Makers, Welders, Cutters, Solderers, Brazers, Layout Workers, Machine Setters and Operators, Tool Sharpeners, etc.|
| 51.5 | Printing Workers | Prepress Technicians and Workers, Printing Press Operators, Print Binding and Finishing Workers|
| 51.6 | Textile, Apparel, and Furnishings Workers | Laundry and Dry-Cleaning Workers, Shoe and Leather Workers, Sewers, Tailors, Dressmakers, Textile Operators and Machine Setters, Patternmakers, Upholsterers, etc.|
| 51.7 | Woodworkers | Cabinetmakers and Bench Carpenters, Furniture Finishers, Model Makers, Patternmakers, Machine Setters and Operators, etc.|
| 51.8 | Plant and System Operators | Nuclear Power Reactor Operators, Power Distributors and Dispatchers, Plant Operators, Stationary Engineers and Boiler Operators, Petroleum Pump System Operators, Refinery Operators, Gaugers, etc.|
| 51.9 | Other Production Occupations | Chemical Equipment Operators, Appliance Technicians, Inspectors, Testers, Sorters, Jewelers, Metal Workers, Laboratory Technicians, Machine Operators, Painting Workers, Production Workers, etc.|
| 53.1 | Supervisors of Transportation and Material Moving Workers | Aircraft Cargo Handling Supervisors, First-Line Supervisors of Helpers, Laborers, Material Movers, Vehicle Operators, Passenger Attendants, Transportation Workers, etc.|
| 53.2 | Air Transportation Workers | Pilots, Copilots, Flight Engineers, Air Traffic Controllers, Airfield Operations Specialists, Flight Attendants, etc.|
| 53.3 | Motor Vehicle Operators | Drivers and other motor vehicle operators.|
| 53.4 | Rail Transportation Workers | Engineers, Operators, Hostlers, Locomotive Firers, Conductors, Yardmasters, etc.|
| 53.5 | Water Transportation Workers | Sailors and Marine Oilers, Captains, Mates, and Pilots of Water Vessels, Motorboat Operators, Ship Engineers, etc.|
| 53.6 | Other Transportation Workers | Bridge and Lock Tenders, Parking Attendants, Service Attendants, Traffic Technicians, Transportation Inspectors, Passenger Attendants, etc.|
| 53.7 | Material Moving Workers | Packers, Stockers, Refuse Collectors, Loaders, Crane Operators, Truck and Tractor Operators, Laborers, etc.|
| 55.1 | Military Officer Special and Tactical Operations Leaders | Crew Officers, Infantry Officers, Special Forces Officers, All Other Military Officer Special and Tactical Operations Leaders|
| 55.2 | First-Line Enlisted Military Supervisors | Supervisors of Crew Members, Supervisors of Tactical Operations Specialists, In-Flight Refueling Manager, Superintendent, Intelligence Chief, etc.|
| 55.3 | Military Enlisted Tactical Operations, Specialists, and Crew Members | Crew Members, Specialists, Infantry, Special Forces, etc.|
| 99.1 | Student | Student|
| 99.9 | Other | Other occupation not listed|

### access-auth-vocab

Constants: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`

| Const | Value | Description |
| --- | --- | --- |
| 1 | Access Revoked | Access was revoked after departing or as a disciplinary action|
| 2 | Administrator/Root | Authorized full administrative access|
| 3 | Authorized Account & Data | Authorized account and access to targeted data|
| 4 | Authorized Account Only | Authorized account but not authorized access to targeted data|
| 5 | Authorized Privileged User | Authorized privileged access|
| 6 | Authorized Unprivileged User | Authorized unprivileged access|
| 7 | Former Employee, Access not Deactivated | Access was not properly revoked after departure from the organization|
| 8 | Never Given Access | Never given system access|
| 9 | Unauthorized | Unauthorized access|

### employment-type-vocab

Constants: `CTR`, `FLT`, `PRT`, `INT`, `TMP`, `VOL`, `OTH`

| Const | Value | Description |
| --- | --- | --- |
| CTR | Contractor | Individual not directly employed by the organization whose job responsibilities they are filling (self-employed or employed by a different, contracting organization)|
| FLT | Full-time | Individual who is directly employed by the organization and works at least 35 hours per week or is classified by the organization as a full-time employee|
| PRT | Part-time | Individual who is directly employed by the organization and works less than 35 hours per week or is classified by the organization as a part-time employee|
| INT | Intern/Trainee/Aprentice | An advanced student or graduate gaining supervised practical experience in a particular field or job role, sometimes without pay|
| TMP | Temporary Employee | Individual hired for a brief period of time or until a certain project is completed|
| VOL | Volunteer | Individual not employed by the organization, but who donates their time to working on projects without receiving pay or benefits|
| OTH | Other | Other employment type not listed in this vocabulary|

## License
This file is a part of the Insider Incident Data Exchange Standard (IIDES) - see https://github.com/cmu-sei/IIDES

Copyright 2024 Carnegie Mellon University.

[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution.  Please see Copyright notice for non-US Government use and distribution.

This work is provided "AS-IS" with "NO WARRANTIES OF ANY KIND - EXPRESS OR IMPLIED" and is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.

Requests for permission for non-licensed uses should be directed to the Software Engineering Institute at permission@sei.cmu.edu.

CERT® is registered in the U.S. Patent and Trademark Office by Carnegie Mellon University.

DM24-0776
