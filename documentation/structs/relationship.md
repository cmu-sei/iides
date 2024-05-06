# Relationship

A structure for connecting two IIDES objects together.

## Properties

- **`id`** (required) *(string)* : A unique string that begins with "relationship--" and is appended with a UUIDv4.
	- Uses pattern: ^relationship--[UUIDv4]
- **`object1`** (required) *(string)* : The id of the first object.
	- Uses pattern: ^XXXX--[UUIDv4]
- **`object2`** (required) *(string)* : The id of the second object.
	- Uses pattern: ^XXXX--[UUIDv4]
