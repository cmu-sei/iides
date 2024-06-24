# Org Owner

Describes the relationship for a person owning an organization. The person can be either an accomplice or an insider to the incident.

## Properties

- **`id`** (required) *(string)* : A unique string that begins with "org-owner--" and is appended with a UUIDv4.
  - Uses pattern: ^org-owner--[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
- **`person`** (required) *(string)* : The id of the insider or accomplice who owns the organization.
  - Uses pattern: ^(insider|accomplice)--[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
- **`org`** (required) *(string)* : The id of the organization object that is owned by the insider or accomplice.
  - Uses pattern: ^organization--[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$

## License
This file is a part of the Insider Incident Data Exchange Standard (IIDES) - see https://github.com/cmu-sei/IIDES

Copyright 2024 Carnegie Mellon University.

[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution.  Please see Copyright notice for non-US Government use and distribution.

This work is provided “AS-IS” with “NO WARRANTIES OF ANY KIND - EXPRESS OR IMPLIED” and is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.

Requests for permission for non-licensed uses should be directed to the Software Engineering Institute at permission@sei.cmu.edu.

CERT® is registered in the U.S. Patent and Trademark Office by Carnegie Mellon University.

DM24-0776
