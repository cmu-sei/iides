# Collusion

Collusion represents the relationship between insiders. For the purposes of the `recruitment` property, insider1 recruited insider2.

## Properties

- **`id`** (required) _(string)_ : A unique string that begins with "collusion--" and is appended with a UUIDv4
  - Uses pattern: ^collusion--[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
- **`insider1`** (required) _(string)_ : The `id` of the first insider
  - Uses pattern: ^insider--[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
- **`insider2`** (required) _(string)_ : The `id` of the second insider
  - Uses pattern: ^insider--[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
- **`relationship`** (required) _(string)_ : The type of relationship between insider1 and insider2
  - A constant from [insider-relationship-vocab](../common/insider-relationship-vocab.md)
- **`recruitment`** _(string)_ : The reason insider1 recruited insider2
  - A constant from [recruitment-vocab](#recruitment-vocab)

## Vocabularies

### recruitment-vocab

Constants: `1`, `2`, `3`, `4`, `5`, `9`

| Const | Value                | Description                                                                                                                               |
| ----- | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Avoid Detection      | Insider1 needed insider2's access or authorization to avoid detection                                                                     |
| 2     | Greater Payoff       | Insider1 received a greater payoff by recruiting insider2                                                                                 |
| 3     | Insider Resigned     | Insider1 no longer worked at the victim organization and needed insider2 to finish the incident                                           |
| 4     | Separation of Duties | Insider1 could not conduct acheive their goals without insider2 due to a separation of duties which limited their access of authorization |
| 5     | Share the Wealth     | Insider1 recruited insider2 due to a desire to share the wealth                                                                           |
| 9     | Other                | Insider1 recruited insider2 for unknown reasons                                                                                           |

## License

This file is a part of the Insider Incident Data Exchange Standard (IIDES) - see https://github.com/cmu-sei/IIDES

Copyright 2024 Carnegie Mellon University.

[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution. Please see Copyright notice for non-US Government use and distribution.

This work is provided \"AS-IS\" with \"NO WARRANTIES OF ANY KIND - EXPRESS OR IMPLIED\" and is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.

Requests for permission for non-licensed uses should be directed to the Software Engineering Institute at permission@sei.cmu.edu.

CERT® is registered in the U.S. Patent and Trademark Office by Carnegie Mellon University.

DM24-0776
