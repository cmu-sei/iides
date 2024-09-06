# Legal Response

This is information about the legal response to the incident, particularly the dates of important milestones in the legal process. A response may have one legal response. A legal response may have multiple charges and may have multiple sentences.

## Properties

- **`id`** (required) *(string)* : A unique string that begins with "legal-response--" and is appended with a UUIDv4
  - Uses pattern: ^legal-response--[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
- **`law_enforcement_contacted`** *(date)* : Organization contacts law enforcement to aid in the investigation of the incident (e.g., police are called to respond to the insider's violent behavior in the workplace)
- **`insider_arrested`** *(date)* : Insider is taken into custody (e.g., police arrest insider in their home)
- **`insider_charged`** *(date)* : Insider is formally charged. Charges must relate to the incident. This category also covers a waiver of indictment and subsequent filing of information (e.g., the insider was indicted on computer fraud charges)
- **`insider_pleads`** *(date)* : Insider puts forth a plea to the court, including guilty, not guilty, or nolo contendere (no contest) (e.g., the insider pleads guilty to computer intrusion)
- **`insider_judgment`** *(date)* : Insider is found guilty, not guilty, or liable or not liable in a court of law (e.g., the insider is found guilty in a jury trial)
- **`insider_sentenced`** *(date)* : Insider is given a legally mandated punishment (e.g., the insider is sentenced to five months in jail, then supervised release, community service, and restitution)
- **`insider_charges_dropped`** *(date)* : The plaintiff drops their case against the insider (e.g., the organization in a civil suit decides to drop the suit)
- **`insider_charges_dismissed`** *(date)* : The plaintiff dismiss their case against the insider (e.g., upon discovery of further evidence, the judge decided to drop the charges against the insider)
- **`insider_settled`** *(date)* : The case against the insider is settled outside of the courtroom (e.g., the victim organization reached an agreement with the insider to not file formal charges in return for financial compensation)
- **`comment`** *(string)* : Comments clarifying the details or dates of the legal response

## License
This file is a part of the Insider Incident Data Exchange Standard (IIDES) - see https://github.com/cmu-sei/IIDES

Copyright 2024 Carnegie Mellon University.

[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution.  Please see Copyright notice for non-US Government use and distribution.

This work is provided "AS-IS" with "NO WARRANTIES OF ANY KIND - EXPRESS OR IMPLIED" and is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.

Requests for permission for non-licensed uses should be directed to the Software Engineering Institute at permission@sei.cmu.edu.

CERT® is registered in the U.S. Patent and Trademark Office by Carnegie Mellon University.

DM24-0776
