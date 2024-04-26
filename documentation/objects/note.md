# Note

A freeform text space for holding notes about the incident as it is being investigated, such as current status or a checklist to follow up on. Notes are not intended to be used to hold details about the incident itself. An incident may have one or more notes.

## Properties

- **`id`** (required) *(string)* : A unique string that begins with "note--" and is appended with a UUIDv4.
	- Uses pattern: ^note--[UUIDv4]
- **`author`** (required) *(string)* : Individual, group, or organization that authored the note.
- **`date`** (required) *(date-time)* : Date and time the note was authored or most recently modified.
- **`comment`** (required) *(string)* : Notes, comments, details as needed.
