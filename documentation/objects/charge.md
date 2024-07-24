# Charge

A charge is an accusation brought against the insider when the incident is pursued in the legal system. For example, "two counts of unauthorized access to company systems." A charge must be connected to only one court case. A court case may have one or more charges.

## Properties

- **`id`** (required) _(string)_ : A unique string that begins with "charge--" and is appended with a UUIDv4
  - Uses pattern: ^charge--[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
- **`title`** (required) _(string)_ : Broad subject matter area of the legal code. For U.S. cases, these are often titled "18 U.S.C."
- **`section`** _(string)_ : Section (and subsection) of the law that the subject is accused of violating. For U.S. cases, for example, wire fraud is section 1343 of Title 18.
- **`nature_of_offense`** _(string)_ : Description of the title and section of the law being violated
- **`count`** _(integer)_ : Number of times the subject is accused of violating the law associated with this charge. Note that multiple violations of a law are often listed as a range of counts (e.g., 'Count 2-6' would have count=5 for this property).
- **`plea`** _(string)_ : Plea entered by the defendant for this charge
  - A constant from [charge-plea-vocab](#charge-plea-vocab)
- **`plea_bargain`** _(boolean)_ : Whether the charge indicated here is a lesser charge based on a previous plea agreement
- **`disposition`** _(string)_ : The decision in the case or the final result
  - A constant from [charge-disposition-vocab](#charge-disposition-vocab)

## Vocabularies

### charge-plea-vocab

Constants: `1`, `2`, `3`, `4`

| Const | Value                   | Description                                              |
| ----- | ----------------------- | -------------------------------------------------------- |
| 1     | Guilty                  | The defendant pleaed guilty to the charge                |
| 2     | No Contest              | The defendant did not contest to the charge              |
| 3     | Not Guilty              | The defendant pleaded not guilty to the charge           |
| 4     | Refused to Enter a Plea | The defendant refused to enter into a plea to the charge |

### charge-disposition-vocab

Constants: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`

| Const | Value                            | Description                                                                                                                                       |
| ----- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Acquitted                        | Found not guilty by a court of law in a criminal trial                                                                                            |
| 2     | Convicted                        | Pleaded or found guilty by a court                                                                                                                |
| 3     | Dismissed                        | The court or prosecutor decided the charge should not go forward                                                                                  |
| 4     | Diversion/Deferred Prosecution   | The court delayed prosecution pending the successful completion of a treatment program, at which point the charges will be dismissed              |
| 5     | Expunged                         | The deletion of non-conviction information (such as arrest data)                                                                                  |
| 6     | No charges filed/Charges dropped | The prosecutor declined to pursue the case                                                                                                        |
| 7     | Pending                          | The case is still being investigated or prosecuted                                                                                                |
| 8     | Pled down                        | Pled guilty to a lesser charge                                                                                                                    |
| 9     | Sealed                           | The court has restricted access to all or some of the content of the record; however, the existence of the record will still be public record     |
| 10    | Suspended sentence               | The court has delayed the sentencing pending the successful completion of a period of probation and/or treatment program                          |
| 11    | Vacated                          | The court has withdrawn the guilty plea or set aside the guilty verdict, and the defendant may state they have never been convicted of that crime |

## License

This file is a part of the Insider Incident Data Exchange Standard (IIDES) - see https://github.com/cmu-sei/IIDES

Copyright 2024 Carnegie Mellon University.

[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution. Please see Copyright notice for non-US Government use and distribution.

This work is provided \"AS-IS\" with \"NO WARRANTIES OF ANY KIND - EXPRESS OR IMPLIED\" and is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.

Requests for permission for non-licensed uses should be directed to the Software Engineering Institute at permission@sei.cmu.edu.

CERT® is registered in the U.S. Patent and Trademark Office by Carnegie Mellon University.

DM24-0776
