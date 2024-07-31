# Insider Incident Data Exchange Standard

Author: CERT Insider Threat Team  
Date: August 2024  
Version: 1, Revision 1

## Introduction

Insider threat and risk management are not themselves new phenomena, but they do represent a relatively nascent field of study. While the CERT Division's research in the field was already a decade old when the Software Engineering Institute (SEI) published _The CERT Guide to Insider Threats_ in 2012 [[Cappelli 2012](#references)], the area as a field of study is itself still relatively young, encompassing many different fields, disparate sources of legal and policy mandates, and several schools of thought. In much the same way that research around insider threat is still growing and coalescing, practitioners are still working out best practices around technical defenses, behavioral and human elements mitigations, and methods for storing and exchanging incident data.

The Insider Incident Data Exchange Standard (IIDES) exists to expand on that last point&mdash;how can we best store and exchange insider threat case data? What are the best ways to craft and apply the appropriate taxonomy to case data? Perhaps most importantly, which types of individuals stand to benefit from this work, and how might they best use such a framework to assure mutually intelligible information sharing?

While practitioners have performed some work around information schema and information portability as it relates to general cybersecurity data, we seek in this paper and the associated standard to provide guidance and structure around the coding, storage, and sharing of data related specifically to insider incidents of all kinds. This work is built upon the work of _The CERT Guide to Insider Threats_, our continually updated collection of best practices in the _Common Sense Guide to Mitigating Insider Threats_ [[Software Engineering Institute 2022](#references)], as well as two decades of work and corpus curation around MERIT, our insider threat case database.

## Background

The study and management of insider threat and risk remain areas of increasingly growing attention, prevalence, and concern. According to the _2024 Verizon Data Breach Incident Report_, 35% of breaches are perpetrated by organizational insiders [[Verizon 2024](#references)]. Further, the Ponemon Institute has attempted to assign costs to these phenomena: malicious insider incidents cost organizations an annual average of $701,500. At roughly seven events per year per organization, the average annualized costs of malicious insider incidents become $4,840,350. Add in non-malicious and credential theft, and the average annualized costs jumps to $16,226,605 [[Ponemon Institute 2023](#references)]. Taken together, we can state confidently that in terms of both occurrence and costs, the threat posed by trusted insiders is as grave an issue as ever.

Several classes of stakeholders stand to benefit from this work. Research into insider threat is often stymied early by a lack of data. A standard of case classification and information sharing could allow researchers to build, maintain, and share insider threat case data. Similarly, practitioners&mdash;namely analysts, investigators, and those responsible for risk management&mdash;stand to benefit from ways in which to build internal case corpora and share that data with other practitioners, other similar businesses or entities, and third-party organizations such as law enforcement, governmental agencies, or research organizations. Such methods would also be of benefit for sharing case information with those who create models and simulations, training, education, and best practices.

## Guiding Principles

The development of IIDES, as with the development of many standards, required a tradeoff between a fully articulated, tightly constrained schema and a language flexible enough to be useful across a range of potential applications and users. We balanced these tradeoffs by adhering to the following set of guidelines when deciding on each particular element of IIDES.

**Simplicity**&mdash;Support the individuals and organizations who do the hard work of analyzing insider incidents by providing the tools and language to do their work as efficiently as possible and without unnecessary constraints, abstractions, or requirements.

**Expertise**&mdash;The elements that make up IIDES should be based on a mix of direct experience, empirical data, analysis, and theoretical observations. IIDES should be directly applicable to current operational practice and support the advancement of the state of the art.

**Flexibility**&mdash;Support different users, use cases, and needs by not over constraining the schema or adding too many requirements. Allow for different users to facilitate their use cases by adding their own constraints, fields, or vocabularies in local implementations. Respond to and incorporate community feedback regarding changes to IIDES or the schema.

**Interoperability**&mdash;Be aware of related work and, when possible, allow for compatibility and interoperability with existing standards. Support referencing of other standards rather than redefining existing work within the schema.

## Related Standards

An array of frameworks, standards, and guidelines aimed at mitigating risks supports current landscape of insider threat management. Notable among these are

- _Common Sense Guide to Mitigating Insider Threats_ developed by the SEI [[Software Engineering Institue 2022](#references)], which offers valuable guidelines for organizations to safeguard against internal threats
- _An Insider Threat Indicator Ontology (CMU/SEI-2016-TR-007)_ [[Costa 2016](#references)], which provides a method for describing indicators of insider risk
- the MITRE ATT&CK framework [[MITRE 2024](#references)], which provides a comprehensive matrix of tactics and techniques used by adversaries
- the insider-threat-specific version of ATT&CK [[MITRE Engenuity 2024](#references)]

The Cybersecurity and Infrastructure Security Agency’s (CISA’s) _Insider Threat Mitigation Guide_ [[CISA 2020](#references)] and the Department of Homeland Security's (DHS's) Insider Threat Program (ITP) [[DHS 2020](#references)] further contribute by delivering strategic insights and structured methodologies for threat detection and prevention. Additionally, the DHS Privacy Impact Assessment (PIA) for _Insider Threat Reporting Mobile Platform (DHS/ALL/PIA-068)_ [[DHS 2018](#references)] emphasizes the importance of privacy considerations in threat reporting.

Standards that facilitate the standardized exchange of cyber threat intelligence and simulation data include

- Structured Threat Information eXchange/Trusted Automated eXchange of Indicator Information (STIX/TAXII) [[OASIS Open 2024](#references)]
- MISP Threat Sharing [[Wagner 2024](#references)]
- _Cyber Data Exchange Model (DEM) (SISO-STD-025-2023)_ [[SISO 2023](#references)]
- _Cyber Incident Reporting Framework (CIRF)_ outlines protocols for incident documentation and communication [[Cyber Threat Alliance 2023](#references)].

Furthermore, technical standards such as the following provide detailed specifications for identifying and reporting various cyber threats and vulnerabilities

- Open Indicators of Compromise (OpenIOC) [[Mandiant Corporation 2013](#references)]
- Malware Attribute Enumeration and Characterization (MAEC) [[MAEC 2024](#references)]
- Common Attack Pattern Enumerations and Classifications (CAPEC) [[MITRE 2024b](#references)]
- Common Vulnerabilities and Exposures (CVE)) [[Common Vulnerabilities and Exposures 2024](#references)] .

Notably, the bulk of these works are focused on the most technical aspects of cyber and insider incidents. Though some, such as _SOFIT: Sociotechnical and Organizational Factors for Insider Threat_ [[Greitzer 2018](#references)], focus on sociotechnical, organizational, or behavioral factors of insider threats. At a higher level, risk management frameworks such as NIST's _Risk Management Framework for Information Systems and Organizations_ [[Ross 2018](#references)], _The NIST Cybersecurity Framework (CSF) 2.0_ [[NIST 2024](#references)], and the _CERT Resilience Management Model (CERT-RMM) Version 1.2_ [[Caralli 2016](#references)] focus on identifying organizational risks and addressing the gaps that lead to those risks. IIDES provides a standard for addressing the gap left by existing frameworks and ontologies to connect the technical, cyber, behavioral, and risk components of the insider threat domain into one easily referenced standard.

The IIDES schema builds off of lessons learned from the frameworks and standards described above and also references more general standards where appropriate, such as North American Industry Classification System (NAICS) standards for industry and occupation [[Executive Office of the President 2022](#references)] and the International Organization for Standardization (ISO) [[International Organization for Standardization 2024](#references)] for location codes. It leverages some of CISA's insider threat categories [[CISA 2024](#references)] and leaves room to reference any of the existing cyber frameworks and repositories.

## Benefits

IIDES is designed to provide a range of benefits across a broad array of potential users in both research and operational environments. Ideally, IIDES will support efficient sharing of incident data among practitioners, organizations, and researchers by providing a shared naming convention for details that may be included in incident data. We hope that this will support a more consistent mapping of recommendations and best practices for response, detection, and mitigation of insider threats in the future.

IIDES also provides a foundational vocabulary for organizations collecting their own incident data and eases development of new data collection and case management systems for reporting and tracking incidents. Without clear and consistent reporting mechanisms, organizations risk delays in detecting and responding to insider threats as well as inconsistencies in data collection and analysis. Additionally, inadequate reporting procedures may result in missed opportunities for early intervention and mitigation, leaving organizations vulnerable to insider attacks. By implementing IIDES, organizations can streamline reporting processes, improve data accuracy and reliability, and enhance their overall resilience against insider threats.

## IIDES Architecture

IIDES is split into four different sections: the seven core components, additional subcomponents, relationships, and vocabularies.

### Core Components

The core components of IIDES are Incident, Insider, Organization, Job, Detection, Response, and TTP. Figure 1 describes the relationships between these core components.

![IIDES Core Diagram](../UML/out/IIDES_Core.png "IIDES Core")  
_Figure 1: IIDES Core Components_

None of the components in IIDES are required by the schema. An organization using IIDES may choose to use one, all, or some subset of the available components. To have a valid schema, the relationships must be implemented as described in the schema [documentation](../).

An insider threat [Incident](objects/incident.md) can be associated with one or more [Insiders](objects/insider.md) who committed the incident. Those insiders may either be employed by or own one or more [Organizations](objects/organization.md) involved in the incident. The specific details of an employment relationship are contained in the [Job](objects/job.md) entity.

When multiple organizations are involved in an incident, they may have relationships to one another, such as a vendor relationship or a competitor relationship. Organizations may also have different roles within an incident, such as a primary victim or even a beneficiary of the incident.

A [Detection entity](objects/detection.md) describes details about how, when, and by whom the incident was detected. An incident has only one detection entity.

A [Response entity](objects/response.md) describes the organization's response to the incident, including technical and behavioral controls, investigation, and legal response. An incident has only one Response entity.

An incident can have zero, one, or multiple [TTPs](objects/ttp.md), each of which details a specific action the insider took during the course of the incident.

### Full Architecture

The full architecture of IIDES includes a number of subcomponents that are associated with one or more of the IIDES core components as outlined in Figure 2.

![IIDES Entity Relationships](../UML/out/IIDES_Entity_Relationships.png "IIDES Relationships")  
_Figure 2: IIDES Full Relationship Diagram_

The Incident core component includes the subcomponents [Target](objects/target.md), [Impact](objects/impact.md), [Note](objects/note.md), and [Source](objects/source.md). An Incident can have zero, one, or more of each of these subcomponents. A Target is the system, data, person, or physical property that the insider targeted. An Impact is a quantitative measurement of the impact of the incident on the victim organization. A Note is used for keeping details unrelated to the incident, such as case management notes or research references. Sources are documents and files related to the incident or its investigation.

The Response core component can have a [Legal Response](objects/legal-response.md) subcomponent, which in turn has one or more [Court Case](objects/court-case.md) components, each of which can have one or more [Charge](objects/charge.md) or [Sentence](objects/sentence.md) components. These subcomponents are intended to capture specific details about incidents that go through the legal system.

An Organization can be connected to one or more employment [Stressors](objects/stressor.md) that impact an insider within the organization. These Stressors are defined by the stressor vocabularies and include stressors such as getting passed over for a promotion.

An Insider can be connected to one or more other insiders through the [Collusion](structs/collusion.md) structure and may have one or more [Accomplices](objects/accomplice.md) external to the organization. An Accomplice may be tied to an organization through a Job entity when relevant to the incident. Both Accomplice and Insider inherit many of their properties&mdash;such as name, gender, and location&mdash;from the [Person](objects/person.md) subcomponent. Accomplices and insiders may have a [Sponsor](objects/sponsor.md), such as a foreign government or corporate competitor.

The Detection and TTP core components do not have any additional subcomponents.

### Relationships

IIDES components are connected to one another through relationships. We have tried not to over specify the relationships in IIDES, as doing so would be a violation of our guiding principles of simplicity and flexibility. However, we do specify as part of the schema which relationships we believe are important to facilitating a clear understanding of an insider incident.

We refer to a group of components all related to one another through a particular incident as an &#8220;Incident Bundle&#8221;. Though we understand that it is theoretically possible to have an insider or organization connected to more than one incident (e.g., an organization that has an incident in one year, then a separate incident the next year), we recommend that implementations only include one incident in each bundle. This simplifies the technical implementation of the schema and ensures the data remains readable by human analysts and researchers.

The schema does not require inclusion of an Incident entity. However, we strongly recommend including the Incident entity&mdash;with null fields if necessary (except for `id`)&mdash;as it provides the connective glue between the other components of IIDES and will allow for organizations to consistently share incidents, should the need arise.

The relationships specified in IIDES are detailed in the description of each component as well as in the IIDES [ERD](../UML/out/) files. Implementations can more tightly constrain the relationships, should they have a need to do so&mdash;for example, by requiring every incident to have at least one insider, organization, and target. Implementations should not define the relationships more loosely&mdash;for example, by allowing an incident to have multiple detection components. Doing so would result in a non-conformant implementation.

We provided a generic [Relationship struct](structs/relationship.md) for connecting entities to one another as specified by the relationships in the schema. For example, the generic Relationship struct would be used to connect an Insider entity with a Job entity. Some relationships have additional properties relevant to the relationship and are therefore specified separately from the generic Relationship struct in IIDES. These include [Collusion](structs/collusion.md), organization [Ownership](structs/org-owner.md) by an insider, and [relationships between organizations](structs/org-relationship.md).

The existing generic relationship struct should not be used for connecting entities that do not have relationships specified by the schema. For example, an implementation may require a way to connect a specific impact to a specific TTP or to connect a specific source to a specific target. These relationships are not specified in IIDES. Before implementing a custom relationship for such entities, we suggest making a request for inclusion of such a new relationship in IIDES via the IIDES GitHub page.

### Vocabularies

Many of the components in IIDES include properties that require values from specific vocabularies (enumerations) included with IIDES. For example, the `incident_type` property of the [Incident](objects/incident.md) component requires a value from the [incident-type-vocab](objects/incident.md#incident-type-vocab), which lists Fraud, Sabotage, Espionage, Violence, and Unintentional as the options for `incident_type`. The vocabularies in IIDES are based on our own extensive experience working with insider incidents as well as on a large collection of incident data. We expect some of these vocabularies to grow and change over time to better suit the needs of the IIDES user community.

Most vocabularies in the IIDES schema are specified as subschemas with a mapping of constants to their titles and description, as opposed to a simple list of values (i.e., an enumeration). For example, the allowed values for the `incident_type` propertiy are only &#8220;F,&#8221; &#8220;S,&#8221; &#8220;E,&#8221; &#8220;V,&#8221; and &#8220;U.&#8221; This specification of constants is intended to keep the stored data as small as possible as well as to provide consistent definitions of the vocabulary terms across the IIDES user base and insider threat community at large.

Using subschemas also provides flexibility for local implementations that may wish to use different value titles without breaking the schema requirements or affecting shareability. For example, an organization wishing to use the term &#8220;non-malicious&#8221; instead of &#8220;unintentional&#8221; may swap out the mapping of the title to the constant &#8220;U&#8221; from &#8220;unintentional&#8221; to &#8220;non-malicious&#8221; without invalidating their implementation. Another organization may use a translation of the titles and descriptions to another language, while keeping the constants as is. Organizations may also clarify descriptions for their own internal purposes in the same way (e.g., by adding guidance for analysts deciding which value to use).

It is difficult to provide full coverage for all possible vocabulary terms across all use cases of a data standard. We request that organizations that find that the necessary vocabulary terms are missing for their use case provide feedback via the IIDES GitHub page before considering making internal changes to the vocabularies. This way, we may consider including new terms in an updated version of IIDES, making them available for other organizations with similar use cases.

## Using IIDES

We recognize that not all components of IIDES will be useful to all users. To that end, we have tried to provide a flexible schema that covers as many use cases as possible without limiting its application in use cases that we have not thought of.

To assist with understanding the JSON schema and IIDES itself, we provide a set of [examples](../examples/), which covers several mock insider threat example cases. The examples are not intended to be exhaustive of all possible use cases. Rather, they are intended to provide insight into what valid IIDES data looks like, and to provide a small set of test cases to assist with testing alternative implementations of IIDES.

### General Guidance

No matter how well a standard is defined, there will always be cases where the data does not perfectly match the fields that the standard provides. This section includes some guidance on how to code edge cases where the incident data does not perfectly match IIDES.

- **Inexact dates**&mdash;Sometimes incident coders or analysts do not have an exact date available, but instead have something like &#8220;May 2024,&#8221; &#8220;fall of 2020,&#8221; or &#8220;early 2023.&#8221; For these instances, we suggest using the beginning date of the time frame. For example, &#8220;May 2024&#8221; would be &#8220;2024-05-01,&#8221; whereas &#8220;fall of 2023&#8221; would be &#8220;2023-09-01,&#8221; and &#8220;early 2023&#8221; would be &#8220;2023-01-01.&#8221;
  - Note: Those conducting analysis on large incident data sets with a lot of inexact dates will need to control for any resulting cyclicality in time series data.
- **Lifetime sentences**&mdash;Sentencing information requires a specific numeric quantity that &#8220;lifetime&#8221; does not conform to. To comply with the schema and support quantitative analysis of IIDES-specified incidents, we suggest using the integer &#8220;60&#8221; as the quantity in the sentencing entity.

### Implementation Guidance

We chose to use JSON to define the IIDES schema, as JSON is one of the most widely used data interchange formats and is arguably easier to use than XML. However, JSON does have its drawbacks as a language for defining schemas. For example, it is difficult to directly specify many-to-many relationships, and it assumes that undefined entities are allowed by default. Explicitly stating that additional properties and objects are disallowed would violate our guiding principle of flexibility. For this reason, the IIDES schema is defined only in part by its JSON specification. Additional details for implementation can be found in this white paper, the descriptions of each component (found in the [documentation](.) folder), and the entity relationship diagrams (ERDs) located in the [UML](../UML/out/) files.

We also provide a separate reference implementation of IIDES called PyIIDES, which is written in Python for those who wish to reference a complete schema-conformant implementation. PyIIDES is a Python package available for download and use in other tools or IIDES implementations. One such example of a tool using PyIIDES is Termite, a lightweight, IIDES-compliant insider threat case management solution.

For those writing implementations of IIDES in other languages, we suggest conforming as tightly as possible to the IIDES schema as specified in these documents and the reference implementations. We request that community members requiring a non-standard or non-conformant implementation of IIDES make a request to the IIDES development team via the GitHub page before implementing a custom schema. Doing so provides the team an opportunity to improve IIDES and its associated implementations for the community's use.

## Conclusion

Though extensive, existing tools and guidelines do not collectively address the need for a unified insider threat data exchange standard. Other frameworks and standards are often focused on specific aspects of threat management&mdash;such as external attacks, cyber threat intelligence sharing, or procurement regulations&mdash;rather than on creating a holistic, standardized approach to collecting and reporting insider threat incidents. This fragmentation leads to inconsistencies in how insider threats are reported, analyzed, and mitigated across different organizations and sectors.

IIDES addresses the critical need for an insider threat data standard that integrates these disparate elements into a cohesive framework, ensuring uniformity and effectiveness in addressing insider threats.
It provides a mechanism for information sharing and collaboration among stakeholders by leveraging best practices and lessons learned from existing policies and frameworks.

It is our hope that IIDES will serve as a valuable tool for enhancing insider threat management capabilities across organizations. We welcome community feedback and suggestions for enhancement, which can be submitted via the IIDES GitHub page as issues, discussions, or pull requests.

## References

URLs are valid as of the publication date of this report.

[Cappelli 2012]  
Cappelli, Dawn; Moore, Andrew; & Trzeciak, Randall. The CERT Guide to Insider Threats: How to Prevent, Detect, and Respond to Information Technology Crimes (Theft, Sabotage, Fraud). Addison-Wesley Professional. 2012. ISBN 978-0-321-81257-5. https://insights.sei.cmu.edu/library/the-cert-guide-to-insider-threats-how-to-prevent-detect-and-respond-to-information-technology-crimes-theft-sabotage-fraud/

[Caralli 2016]  
Caralli, Richard A.; Allen, Julia H.; White, David W.; Young, Lisa R.; Mehravari, Nader; & Curtis, Pamela D. CERT Resilience Management Model, Version 1.2. Software Engineering Institute, Carnegie Mellon University. 2016. https://insights.sei.cmu.edu/documents/1629/2016_002_001_514462.pdf

[CISA 2020]  
Cybersecurity and Infrastructure Security Agency (CISA). Insider Threat Mitigation Guide. CISA. 2020. https://www.cisa.gov/resources-tools/resources/insider-threat-mitigation-guide

[CISA 2024]  
Cybersecurity and Infrastructure Security Agency (CISA). Defining Insider Threats. CISA Website. May 2024 [accessed]. https://www.cisa.gov/topics/physical-security/insider-threat-mitigation/defining-insider-threats

[Common Vulnerabilities and Exposures 2024]  
Common Vulnerabilities and Exposures (CVE). CVE Program. CVE Website. June 2024 [ac-cessed]. https://www.cve.org/

[Costa 2016]  
Costa, Daniel L.; Albrethsen, Michael J.; Collins, Matthew L.; Perl, Samuel J.; Silowash, George J.; & Spooner, Derrick L. An Insider Threat Indicator Ontology. CMU/SEI-2016-TR-007. Software Engineering Institute, Carnegie Mellon University. 2016. https://insights.sei.cmu.edu/documents/1260/2016_005_001_454627.pdf

[Cyber Threat Alliance 2023]  
Cyber Threat Alliance; Institute for Security and Technology; Chainalysis; Ciphertrace; CREST; Cybera; Cybercrime Support Network; & Cyber Peace Institute. Cyber Incident Re-porting Framework: Global Edition. Cyber Threat Alliance. 2023. https://www.cyberthreatalliance.org/wp-content/uploads/2023/04/Cyber-Incident-Reporting-Framework-Global-Edition.pdf

[DHS 2018]  
Department of Homeland Security (DHS). Privacy Impact Assessment for the Insider Threat Reporting Mobile Platform. DHS/ALL/PIA-068. Department of Homeland Security. 2018. https://www.dhs.gov/sites/default/files/publications/privacy-pia-all-livesafe068-september2018.pdf

[DHS 2020]  
Department of Homeland Security (DHS). Privacy Impact Assessment Update for the Insider Threat Program. DHS/ALL/PIA-052(b). Department of Homeland Security. 2020. https://www.dhs.gov/publication/dhs-all-pia-052-dhs-insider-threat-program

[Executive Office of the President 2022]  
Executive Office of the President, Office of Management and Budget. North American Indus-try Classification System. Executive Office of the President of the United States. 2022. https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf

[Greitzer 2018]  
Greitzer, Frank; Purl, Justin; Leong, Yung Mei; & Sunny Becker, D. E. SOFIT: Sociotech-nical and Organizational Factors for Insider Threat. Pages 197–206. 2018 IEEE Security and Privacy Workshops (SPW). May 2018. https://ieeexplore.ieee.org/document/8424651

[International Organization for Standardization 2024]  
International Organization for Standardization. ISO 3166 Country Codes. International Or-ganization for Standardization (ISO). May 2024 [accessed]. https://www.iso.org/iso-3166-country-codes.html

[MAEC 2024]  
Malware Attribute Enumeration and Characterization (MAEC). MAEC Documentation. MAEC Project GitHub Website. June 2024 [accessed]. https://maecproject.github.io/documentation/maec5-docs/#introduction

[Mandiant Corporation 2013]  
Mandiant Corporation. FireEye / OpenIOC_1.1. GitHub Website. 2013. https://github.com/fireeye/OpenIOC_1.1

[MITRE 2024a]  
MITRE. MITRE ATT&CK. MITRE Website. June 2024 [accessed]. https://attack.mitre.org/

[MITRE 2024b]  
MITRE. Common Attack Pattern Enumerations and Classifications (CAPEC). MITRE Web-site. June 2024 [accessed]. https://capec.mitre.org/

[MITRE Engenuity 2024]  
MITRE Engenuity. Insider Threat TTP Knowledge Base v2.0.0. Center for Threat Informed Defense GitHub Website. June 2024 [accessed]. https://center-for-threat-informed-defense.github.io/insider-threat-ttp-kb/

[NIST 2024]  
National Institute of Standards and Technology (NIST). The NIST Cybersecurity Framework (CSF) 2.0. NIST. 2024. https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf

[OASIS Open 2024]  
OASIS Open. Cyber Threat Intelligence Documentation. OASIS Open GitHub Website. June 2024 [accessed]. https://oasis-open.github.io/cti-documentation/

[Ponemon Institute 2023]  
Ponemon Institute. 2023 Cost of Insider Risks Global Report. DTEX. 2023. https://www.dtexsystems.com/resource-ponemon-insider-risks-global-report/

[Ross 2018]  
Ross, Ronald S. Risk Management Framework for Information Systems and Organizations: A System Life Cycle Approach for Security and Privacy. NIST SP 800-37 Rev. 2. National Insti-tute of Standards and Technology (NIST). 2018. https://www.nist.gov/publications/risk-management-framework-information-systems-and-organizations-system-life-cycle

[SISO 2023]  
Simulation Interoperability Standards Organization (SISO). Cyber Data Exchange Model (DEM). SISO-STD-025-2023. SISO. 2023. https://cdn.ymaws.com/www.sisostandards.org/resource/resmgr/standards_products/siso-std-025-2023_cyberdem.pdf

[Software Engineering Institute 2022]  
Software Engineering Institute. Common Sense Guide to Mitigating Insider Threats, Seventh Edition. Software Engineering Institute, Carnegie Mellon University. 2022. https://insights.sei.cmu.edu/library/common-sense-guide-to-mitigating-insider-threats-seventh-edition/

[Verizon 2024]  
Verizon. 2024 Data Breach Investigations Report. Verizon Business. 2024. https://www.verizon.com/business/resources/T2f2/reports/2024-dbir-data-breach-investigations-report.pdf

[Wagner 2024]  
Wagner, Cynthia; Dulaunoy, Alexandre; Wagener, Gérard; & Iklody, Andras. MISP Threat Sharing. MISP Project Website. June 2024 [accessed]. https://www.misp-project.org/

## Acknowledgments

The following individuals have made significant contributions to the development of IIDES. Thank you for your time and effort.

Austin Whisnant  
Nathan Ammerman  
Gaberiel Sha  
Marco Paes  
Luke Osterritter

## Licensing

This file is a part of the Insider Incident Data Exchange Standard (IIDES) – see [https://github.com/cmu-sei/IIDES](https://github.com/cmu-sei/IIDES)

Copyright 2024 Carnegie Mellon University.

[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution. Please see Copyright notice for non-US Government use and distribution.

This work is provided "AS-IS" with "NO WARRANTIES OF ANY KIND – EXPRESS OR IMPLIED" and is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.

Requests for permission for non-licensed uses should be directed to the Software Engineering Institute at permission@sei.cmu.edu.

CERT® is registered in the U.S. Patent and Trademark Office by Carnegie Mellon University.

DM24-0776
