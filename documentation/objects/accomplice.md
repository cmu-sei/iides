# Accomplice

An outsider who conspired with the insider(s) to accomplish the objectives of the incident. An accomplice was not part of the victim organization at the time of the incident. An insider may have one or more accomplices. An accomplice may have one or more jobs (job history).

## Properties

- **`id`** (required) *(string)* : A unique string that begins with "accomplice--" and is appended with a UUIDv4.
  - Uses pattern: ^accomplice--[UUIDv4]
- **`relationship_to_insider`** *(string)* : The type of relationship between this accomplice and the insider to which it is connected.
	- A constant from [insider-relationship-vocab](../common/insider-relationship-vocab.md)
- **Inherits properties from [Person](person)**
