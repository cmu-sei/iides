# IIDES Repository

The Insider Incident Data Exchange Standard (IIDES) is a new standard for collecting and sharing insider threat incidents. IIDES is intended to support a community of practitioners, analysts, and researchers in their efforts to reduce threats from insiders across organizations of all sizes and in all sectors. View the [IIDES white paper](documentation/WhitePaper.md) for a deeper understanding of the goals of IIDES and the guiding principles for its development.

The schema itself is written in JSON. All of the IIDES schema components can be found in the [JSON](json/) folder. The schema files have also been combined into one complete schema file, [iides_full_schema.json](iides_full_schema.json), for direct use in IIDES implementations. We also have a Python-based reference implementation of IIDES called [PyIIDES](https://github.com/cmu-sei/PyIIDES) in a separate repository.

You can find easy-to-read documentation for each component of the schema in the [documentation folder](documentation/) of this repository. The complete [entity diagram](UML/out/IIDES.png) and the [entity relationship diagram](UML/out/IIDES_Entity_Relationships.png) may also be useful.

We also have a set of [IIDES examples](examples/README.md) to help provide an understanding of how IIDES can be used.

We encourage feedback from our user community and welcome requests for improvements to IIDES, which can be submitted through GitHub.

![IIDES Core Diagram](UML/out/IIDES_Core.png "IIDES Core")

## Licensing

This file is a part of the Insider Incident Data Exchange Standard (IIDES) – see [https://github.com/cmu-sei/IIDES](https://github.com/cmu-sei/IIDES)

Copyright 2024 Carnegie Mellon University.

[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution. Please see Copyright notice for non-US Government use and distribution.

This work is provided "AS-IS" with "NO WARRANTIES OF ANY KIND – EXPRESS OR IMPLIED" and is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.

Requests for permission for non-licensed uses should be directed to the Software Engineering Institute at permission@sei.cmu.edu.

CERT® is registered in the U.S. Patent and Trademark Office by Carnegie Mellon University.

DM24-0776
