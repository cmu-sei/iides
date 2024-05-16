# Org Owner

Describes the relationship for a person owning an organization. The person can be either an accomplice or an insider to the incident.

## Properties

- **`id`** (required) *(string)* : A unique string that begins with "org-owner--" and is appended with a UUIDv4.
  - Uses pattern: ^org-owner--[UUIDv4]
- **`person`** (required) *(string)* : The id of the insider or accomplice who owns the organization.
  - Uses pattern: ^insider--[UUIDv4] or ^accomplice--[UUIDv4]
- **`org`** (required) *(string)* : The id of the organization object that is owned by the insider or accomplice.
  - Uses pattern: ^organization--[UUIDv4]
