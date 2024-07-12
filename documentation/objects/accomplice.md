# Accomplice

An accomplice is an outsider who conspired with the insider(s) to accomplish the objectives of the incident. An accomplice was not part of the victim organization at the time of the incident. An insider may have one or more accomplices. An accomplice may have one or more jobs (job history).

## Properties

- **`id`** (required) *(string)* : A unique string that begins with "accomplice--" and is appended with a UUIDv4
  - Uses pattern: ^accomplice--[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
- **`relationship_to_insider`** *(string)* : The type of relationship between this accomplice and the insider to whom they are connected
	- A constant from [insider-relationship-vocab](../common/insider-relationship-vocab.md)
- **Inherits properties from [Person](person)**

## License
This file is a part of the Insider Incident Data Exchange Standard (IIDES) - see https://github.com/cmu-sei/IIDES

Copyright 2024 Carnegie Mellon University.

[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution.  Please see Copyright notice for non-US Government use and distribution.

This work is provided “AS-IS” with “NO WARRANTIES OF ANY KIND - EXPRESS OR IMPLIED” and is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.

Requests for permission for non-licensed uses should be directed to the Software Engineering Institute at permission@sei.cmu.edu.

CERT® is registered in the U.S. Patent and Trademark Office by Carnegie Mellon University.

DM24-0776
