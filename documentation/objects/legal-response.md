# Legal Response

Information about the legal response to the incident, particularly the dates of important milestones in the legal process. A response may have one legal response. A legal response may have multiple charges, and may have multiple sentences.

## Properties

- **`id`** (required) _(string)_ : A unique string that begins with "legal-response--" and is appended with a UUIDv4.
  - Uses pattern: ^legal-response--[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
- **`law_enforcement_contacted`** _(date)_ : Organization contacts law enforcement to aid in the investigation of the incident. E.g., Police are called to respond to the Insider's violent behavior in the workplace).
- **`insider_arrested`** _(date)_ : Insider is taken into custody. E.g., Police arrest insider in their home.
- **`insider_charged`** _(date)_ : Insider is formally charged. Charges must relate to the incident. This category also covers a waiver of indictment and subsequent filing of information. E.g., Insider was indicted on computer fraud charges.
- **`insider_pleads`** _(date)_ : Insider puts forth a plea to the court, including guilty, not guilty, nolo contendere (no contest). E.g., Insider pleads guilty to computer intrusion.
- **`insider_judgment`** _(date)_ : Insider is found guilty, not guilty, or liable or not liable in a court of law. E.g., Insider is found guilty in a jury trial.
- **`insider_sentenced`** _(date)_ : Insider is given a legally mandated punishment. E.g., Insider sentenced to 5 months in jail, then supervised release, community service, and restitution.
- **`insider_charges_dropped`** _(date)_ : The plaintiff drops their case against the insider. E.g., The organization in a civil suit decides to drop the suit.
- **`insider_charges_dismissed`** _(date)_ : The plaintiff dismiss their case against the insider. E.g., Upon discovery of further evidence, the judge decided to drop the charges against the insider.
- **`insider_settled`** _(date)_ : The case against the insider is settled outside of the courtroom. E.g., The victim organization reached an agreement with the insider to not file formal charges in return for financial compensation.
- **`comment`** _(string)_ : Comments clarifying the details or dates of the legal response.
