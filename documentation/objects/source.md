# Source

Source describes a document that provides information about one or more aspects of the incident.

## Properties

- **`id`** (required) _(string)_ : A unique string that begins with "source--" and is appended with a UUIDv4
  - Uses pattern: ^source--[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
- **`title`** (required) _(string)_ : The title of the document
- **`source_type`** _(string)_ : The "source" or author of the source document
  - A constant from [source-type-vocab](#source-type-vocab)
- **`file_type`** _(string)_ : File type or extension
  - A constant from [source-file-type-vocab](#source-file-type-vocab)
- **`date`** _(date-time)_ : The date the document was created or most recently modified
- **`public`** _(boolean)_ : Whether the document is publicly available
- **`document`** _(string)_ : A pointer to the document itself, whether a file path, location, URL, or document object

## Vocabularies

### source-type-vocab

Constants: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `99`

| Const | Value                  | Description                                                            |
| ----- | ---------------------- | ---------------------------------------------------------------------- |
| 1     | Court Document         | Legal document from a court case                                       |
| 2     | DOJ Press Release      | Press release from the Department of Justice or U.S. Attorneys' Office |
| 3     | Investigator Notes     | Raw notes from an incident investigator                                |
| 4     | Logs                   | Technical logs from network, server, or user devices                   |
| 5     | Media                  | News, blog, or similar publication                                     |
| 6     | Organization Interview | Direct interview with the victim organization                          |
| 7     | Insider Interview      | Direct interview with the insider                                      |
| 99    | Other                  | Other type of source not listed in this vocabulary                     |

### source-file-type-vocab

Constants: `html`, `log`, `pdf`, `txt`, `docx`, `png`, `xlsx`, `video`, `other`

| Const | Value      | Description                                               |
| ----- | ---------- | --------------------------------------------------------- |
| html  | HTML File  | A file in HTML format                                     |
| log   | Log File   | A log file containing technical event or transaction logs |
| pdf   | PDF File   | A file in Portable Document Format                        |
| txt   | Text File  | A plain text file                                         |
| docx  | DOCX File  | A Microsoft Word document                                 |
| png   | PNG Image  | An image file in PNG format                               |
| xlsx  | Excel File | A Microsoft Excel spreadsheet                             |
| video | Video File | A video file                                              |
| other | Other File | A file of another type not listed in this vocabulary      |

## License

This file is a part of the Insider Incident Data Exchange Standard (IIDES) - see https://github.com/cmu-sei/IIDES

Copyright 2024 Carnegie Mellon University.

[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution. Please see Copyright notice for non-US Government use and distribution.

This work is provided \"AS-IS\" with \"NO WARRANTIES OF ANY KIND - EXPRESS OR IMPLIED\" and is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.

Requests for permission for non-licensed uses should be directed to the Software Engineering Institute at permission@sei.cmu.edu.

CERT® is registered in the U.S. Patent and Trademark Office by Carnegie Mellon University.

DM24-0776
