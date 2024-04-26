# Insider Incident Data Exchange Standard
Author: [TEAM]
Date: April 3, 2024
Version: 0.1, Revision 1

## Introduction



## Background

- bit about MERIT
- bit about our other research
- users: researchers, analysts, risk managers, practitioners, investigators, simulations/exercises
- general happenings in the InT world


## Guiding Principles

The development of IIDES, as with the development of many standards, required a trade off between a fully articulated, tightly constrained schema and a language flexible enough to be useful across a range of potential applications. We balanced these trade offs by adhering to the following set of guidelines when deciding on each particular element of IIDES.

**Simplicity** - 
Support the individuals and organizations who do the hard work of analyzing insider incidents by providing the tools and language to do their work as efficiently as possible, without unncessary constraints, abstractions, or requirements.

**Expertise** - 
The elements that make up the standard should be based on a mix of direct experience, emprical data, analysis, and theoretical observations. The standard should be directly applicable to current operational practice but also support the advancement of the state of the art.

**Flexibility** - 
Support different users, use cases, and needs by not overconstraining the schema and limiting requirements. Allow for different users to facilitate their use cases by adding their own constraints, fields, or  vocabularies in local implementations. Respond to and incorporate community feedback regarding changes to the standard or the schema.

**Interoperability** - 
Be aware of related work and, when possible, allow for compatibility and interoperability with existing standards. Support referencing of other standards rather than redefining existing work within the schema.

## Related Standards

Insider Threat
- Indicator Ontology

Cyber:
- ATT&CK and InT ATT&CK
- STIX/TAXII
- MISP
- SISO CyberDEM

Risk:
- NIST Risk framework and/or incident framework
- RMM
- SOFIT: https://ieeexplore.ieee.org/document/8424651


- https://ieeexplore.ieee.org/abstract/document/9311246
- https://dl.acm.org/doi/abs/10.1145/3465481.3470024

Other General Standards
Insider threat is nichee, but it touches a variety of other domains... 
- NIACS, ANSI, ISO

## Benefits
TODO

IIDES is designed to provide a range of beneifts across a broad array of potential users in both research and operational environments.

- Supports efficient sharing of incident data among practioners, organizations, and researchers by providing a standard... . Sharing insider incident data is useful for ... 

- researchers recreating a database of cases
- maintaining an internal database of an org's own cases
- influenceing what to collect to support further research and improve their own metrics and lessons learned
- Map recommended best practices for response, detection, and mitigation to incidents... 

## IIDES Architecture

IIDES is split into four different sections: the seven core components, additional subcomponents, relationshps, and vocabularies. 

### Core Components

The core components of IIDES are Incident, Insider, Organization, Job, Detection, Response, and TTP. Figure X describes the relationships between these core components. 

![IIDES Core Diagram](../UML/out/IIDES_Core.png "IIDES Core")

None of the components in IIDES are required. An organization using IIDES may choose to one, all, or some subset of the avaialable components. To have a valid schema, the relationships are required as described in the schema [documentation](../).

An insider threat [Incident](objects/incident.md) can be associated with one or more [Insiders](objects/insider.md) who commited the incident. Those insiders may either be employed by, or own, one or more [Organizations](objects/organization.md) involved in the incident. The specific details of an employment relationship are contained in the [Job](objects/job.md) entity.

When multiple organizations are involved in an incident, they may have relationships to one another, such as a vendor relationship, or a competitor relationship. Organizations may also have different roles within an incident, such as a primary victim, or even a beneficiary of the incident.

A [Detection entity](objects/detection.md) describes details about how, when, and by whom the incident was detected. An incident has only one detection entity.

A [Response entity](objects/response.md) describes the organization's response to the incident, including technical and behavioral controls, investigation, and legal response. An incident has only one response entity. 

An incident can have zero, one, or multiple [TTPs](objects/ttp.md), each of which details a specific action the insider took during the course of the incident.

### Full Architecture

The full architecture of IIDES includes a number of subcomponents that are associated with one or more of the IIDES core components.

![IIDES Entity Relationships](../UML/out/IIDES_Entity_Relationships.png "IIDES Relationships")

The Incident core component includes the subcomponents [Target](objects/target.md), [Impact](objects/impact.md), [Note](objects/note.md), and [Source](objects/source.md). An incident can have zero, one, or more of each of these subcomponents.

The Response core component can have a [legal response](objects/legal-response.md) subcomponent, which in turn has one or more [court case](objects/court-case.md) components, each of which can have one or more [charge](objects/charge.md) and/or [sentence](objects/sentence.md) components. 

An organization can be connected to one or more employment [stressors](objects/stressor.md) which impact an insider within the organization. These stressors are defined by the stressor vocabularies, and include stressors such as getting passed over for a promotion.

TODO

Insider.... person...

Job...

The Detection and TTP core components do not have any additional subcomponents.

### Relationships

TODO

### Vocabularies

TODO

## Using IIDES
TODO
- Where to send feedback
- Existing implementations (Termite, pyIides) and advice for implementing
- Using the schema
- Examples (link to examples dirs)

## Conclusion
TODO

## References
TODO
- https://www.cisa.gov/topics/physical-security/insider-threat-mitigation/defining-insider-threats
- https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6758854
Legal
- Coding Case Law for Public Health Evaluation (Hall)
- Supreme court database codebook (http://scdb.wustl.edu/_brickFiles/2019_01/SCDB_2019_01_codebook.pdf)
- Measuring law for evaluation research (https://journals.sagepub.com/doi/epdf/10.1177/0193841X10370018

## Licensing and RRO
TODO

