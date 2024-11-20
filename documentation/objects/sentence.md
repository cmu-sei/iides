# Sentence

Generally, sentence is the amount of punishment for an offense. It could refer to the term of imprisonment or probation, the amount of fines imposed on a convicted defendant for criminal wrongdoing, or the amount of damages imposed for civil cases. Generally, the amount of punishment for an offense. A sentence must be connected to only one court case. A court case may have one or more sentences.

## Properties

- **`id`** (required) *(string)* : A unique string that begins with "sentence--" and is appended with a UUIDv4
  - Uses pattern: ^sentence--[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
- **`sentence_type`** (required) *(string)* : The type of sentence that was ordered
	- A constant from [sentence-type-vocab](#sentence-type-vocab)
- **`quantity`** *(integer)* : The quantity of the sentence type imposed. MUST be used with the `metric` property if used
  - Required if `metric` exists
- **`metric`** *(string)* : The measurement type of the sentence imposed. MUST be used with the `quantity` property if used
	- A constant from [sentence-metric-vocab](#sentence-metric-vocab)
  - Required if `quantity` exists
- **`concurrency`** *(boolean)* : Whether the sentence is to run concurrently (at the same time as) other sentences within the same case

## Vocabularies

### sentence-type-vocab

Constants: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`, `16`

| Const | Value | Description |
| --- | --- | --- |
| 1 | Assessment/Special Assessment | A type of fine that always applies to each count of a convicted crime|
| 2 | Community Service | Unpaid work that benefits the community|
| 3 | Damages | An attempt to measure in financial terms the extent of harm a plaintiff has suffered because of the defendant's actions. Damges can be compensatory, punative, or statutory, and are usually attached to civil cases.|
| 4 | Deportation | Defendant is ordered to leave the country where the case is being tried|
| 5 | Drug Testing | Regular screening ordered to test for drugs|
| 6 | Fine | A financial punishment for violating a criminal law. Usually attached to criminal cases rather than civil.|
| 7 | Forfeiture | Loss of property, right, or privilege without compensation|
| 8 | House Arrest | Confinement to a particular location for the duration of the sentence|
| 9 | Incarceration | Imprisonment|
| 10 | Injunction/Restraining Order | Defendant is ordered to cease a particular action (e.g., using stolen IP in their business)|
| 11 | Mental Health Treatment | Defendant is ordered to an inpatient or outpatient mental health facility or is ordered to attend therapy for mental health issues|
| 12 | No Internet Access | Defendant is not allowed to access the Internet via any type of device|
| 13 | Probation | Defendant is released into the community in lieu of a prison sentence, but is subject to sepcial conditions and restrictions such as other types of sentences in this vocabulary|
| 14 | Restitution | An attempt to measure in financial terms the extent of the gains or profits the defendant obtained through harming the victim|
| 15 | Substance Abuse Treatment | Defendant is ordered to attend inpatient or outpatient treatment for substance abuse issues|
| 16 | Supervised Release | Defendant is released into the community, subject to special conditions and restrictions, after the completion of a prison sentence|

### sentence-metric-vocab

Constants: `1`, `2`, `3`, `4`, `5`

| Const | Value | Description |
| --- | --- | --- |
| 1 | Hour(s) | Imposed sentence is in terms of hours (e.g. 20 hours community service)|
| 2 | Day(s) | Imposed sentence is in terms of days (e.g. 30 days in a substance abuse treatment facility)|
| 3 | Month(s) | Imposed sentence is in terms of months (e.g. 18 months imprisonment)|
| 4 | Year(s) | Imposed sentence is in terms of years (e.g. five years no Internet access)|
| 5 | Dollar(s) | Imposed sentence is in terms of dollars (e.g. $10,000 in damages)|

## License
This file is a part of the Insider Incident Data Exchange Standard (IIDES) - see https://github.com/cmu-sei/IIDES

Copyright 2024 Carnegie Mellon University.

[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution.  Please see Copyright notice for non-US Government use and distribution.

This work is provided "AS-IS" with "NO WARRANTIES OF ANY KIND - EXPRESS OR IMPLIED" and is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.

Requests for permission for non-licensed uses should be directed to the Software Engineering Institute at permission@sei.cmu.edu.

CERT® is registered in the U.S. Patent and Trademark Office by Carnegie Mellon University.

DM24-0776
