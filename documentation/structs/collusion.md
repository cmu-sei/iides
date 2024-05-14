# Collusion

Represents the relationship between insiders. For the purposes of the `recruitment` property, insider 1 recruited insider 2.

## Properties

- **`id`** (required) *(string)* : A unique string that begins with "collusion--" and is appended with a UUIDv4.
  - Uses pattern: ^collusion--[UUIDv4]
- **`insider1`** (required) *(string)* : The id of the first insider.
  - Uses pattern: ^insider--[UUIDv4]
- **`insider2`** (required) *(string)* : The id of the second insider
  - Uses pattern: ^insider--[UUIDv4]
- **`relationship`** (required) *(string)* : The type of relationship between insider1 and insider2.
	- A constant from [insider-relationship-vocab](../common/insider-relationship-vocab.md)
- **`recruitment`** *(string)* : The reason insider1 recruited insider2.
	- A constant from [recruitment-vocab](#recruitment-vocab)

## Vocabularies

### recruitment-vocab

Constants: `1`, `2`, `3`, `4`, `5`, `9`

| Const | Value | Description |
| --- | --- | --- |
| 1 | Avoid Detection | Insider 1 needed insider 2's access or authorization to avoid detection.|
| 2 | Greater Payoff | Insider 1 received a greater payoff by recruiting insider 2.|
| 3 | Insider Resigned | Insider 1 no longer worked at the victim organization and needed insider 2 to finish the incident.|
| 4 | Separation of Duties | Insider 1 could not conduct acheive their goals without insider 2 due to a separationi of duties which limited their access of authorization.|
| 5 | Share the Wealth | Insider 1 recruited insider 2 due to a desire to share the wealth.|
| 9 | Other | Insider 1 recruited insider 2 for unknown reasons.|
