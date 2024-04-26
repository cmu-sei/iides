# Source

Document that provides information about one or more aspects of the incident.

## Properties

- **`id`** (required) *(string)* : A unique string that begins with "source--" and is appended with a UUIDv4.
	- Uses pattern: ^source--[UUIDv4]
- **`title`** (required) *(string)* : The title of the document.
- **`source_type`** *(string)* : The "source" or author of the source document.
	- A constant from [source-type-vocab](#source-type-vocab)
- **`file_type`** *(string)* : File type or extension.
	- A constant from [source-file-type-vocab](#source-file-type-vocab)
- **`date`** *(date-time)* : The date the document was created or most recently modified.
- **`public`** *(boolean)* : Whether the document is publicly available.
- **`document`** *(string)* : A pointer to the document itself, whether a file path, location, url, or document object.

## Vocabularies

### source-type-vocab

Constants: `01`, `02`, `03`, `04`, `05`, `06`, `07`, `99`

| Const | Value | Description |
| --- | --- | --- |
| 01 | Court Document | Legal document from a court case.|
| 02 | DOJ Press Release | Press release from the Department of Justice or US Attorneys' Office.|
| 03 | Investigator Notes | Raw notes from an incident investigator.|
| 04 | Logs | Technical logs from network, server, or user devices.|
| 05 | Media | News, blog, or similar publication.|
| 06 | Organization Interview | Direct interview with the victim organization.|
| 07 | Insider Interview | Direct interview with the insider.|
| 99 | Other | Other type of source not listed in this vocabulary.|

### source-file-type-vocab

Values: `html`, `log`, `pdf`, `txt`, `docx`, `png`, `xlsx`, `video`, `other`

