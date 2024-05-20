# Relationship

A structure for connecting two IIDES objects together.

## Properties

- **`id`** (required) *(string)* : A unique string that begins with "relationship--" and is appended with a UUIDv4.
  - Uses pattern: ^relationship--[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
- **`object1`** (required) *(string)* : The id of the first object.
  - Uses pattern: ^[a-z]*--[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
- **`object2`** (required) *(string)* : The id of the second object.
  - Uses pattern: ^[a-z]*--[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
