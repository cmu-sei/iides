# Note

This is a freeform text space for holding notes related to the case management of the incident as it is being investigated, such as a checklist to follow up on or comments related to the current status. Notes are not intended to be used to hold details about the incident itself. An incident may have one or more notes.

## Properties

- **`id`** (required) *(string)* : A unique string that begins with "note--" and is appended with a UUIDv4
  - Uses pattern: ^note--[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
- **`author`** (required) *(string)* : Individual, group, or organization that authored the note
- **`date`** (required) *(date-time)* : Date and time the note was authored or most recently modified
- **`comment`** (required) *(string)* : Notes, comments, and details as needed

## License
This file is a part of the Insider Incident Data Exchange Standard (IIDES) - see https://github.com/cmu-sei/IIDES

Copyright 2024 Carnegie Mellon University.

[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution.  Please see Copyright notice for non-US Government use and distribution.

This work is provided "AS-IS" with "NO WARRANTIES OF ANY KIND - EXPRESS OR IMPLIED" and is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.

Requests for permission for non-licensed uses should be directed to the Software Engineering Institute at permission@sei.cmu.edu.

CERT® is registered in the U.S. Patent and Trademark Office by Carnegie Mellon University.

DM24-0776
