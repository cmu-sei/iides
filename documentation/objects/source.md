# Source

Document that provides information about one or more aspects of the incident.

## Properties

- **`id`** (required) *(string)* : A unique string that begins with "source--" and is appended with a UUIDv4.
  - Uses pattern: ^source--[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
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

Constants: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `99`

| Const | Value | Description |
| --- | --- | --- |
| 1 | Court Document | Legal document from a court case.|
| 2 | DOJ Press Release | Press release from the Department of Justice or US Attorneys' Office.|
| 3 | Investigator Notes | Raw notes from an incident investigator.|
| 4 | Logs | Technical logs from network, server, or user devices.|
| 5 | Media | News, blog, or similar publication.|
| 6 | Organization Interview | Direct interview with the victim organization.|
| 7 | Insider Interview | Direct interview with the insider.|
| 99 | Other | Other type of source not listed in this vocabulary.|

### source-file-type-vocab

Constants: `html`, `log`, `pdf`, `txt`, `docx`, `png`, `xlsx`, `video`, `other`

| Const | Value | Description |
| --- | --- | --- |
| html | HTML File | A file in HTML format.|
| log | Log File | A log file containing event or transaction logs.|
| pdf | PDF File | A file in Portable Document Format.|
| txt | Text File | A plain text file.|
| docx | DOCX File | A Microsoft Word document.|
| png | PNG Image | An image file in PNG format.|
| xlsx | Excel File | A Microsoft Excel spreadsheet.|
| video | Video File | A video file.|
| other | Other File | A file of another type not listed in this vocabulary.|
