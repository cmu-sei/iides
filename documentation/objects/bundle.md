# Bundle

A bundle holds the objects relating an incident, i.e. court cases, insider, targets and impacts.

## Properties

- **`id`** (required) *(string)* : A unique identifier for the bundle
  - Uses pattern: ^bundle--[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
- **`objects`** (required) *(array)* : Array of IIDES objects
  - One or more object values
