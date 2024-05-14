# Sentence

Term of imprisonment or probation, or amount of fines, imposed on a convicted defendant for criminal wrongdoing, or the amount of damages imposed for civil cases. Generally, the amount of punishment for an offense. A sentence must be connected to only one court case. A court case may have one or more sentences.

## Properties

- **`id`** (required) *(string)* : A unique string that begins with "sentence--" and is appended with a UUIDv4.
  - Uses pattern: ^sentence--[UUIDv4]
- **`sentence_type`** (required) *(string)* : The type of sentence that was ordered.
	- A constant from [sentence-type-vocab](#sentence-type-vocab)
- **`quantity`** *(integer)* : The quantity of the sentence type imposed. MUST be used with the `metric` property if used.
  - Required if `metric` exists.
- **`metric`** *(string)* : The measurement type of the sentence imposed. MUST be used with the `quantity` property if used.
	- A constant from [sentence-metric-vocab](#sentence-metric-vocab)
  - Required if `quantity` exists.
- **`concurrency`** *(boolean)* : Whether the sentence is to run concurrently (at the same time as) other sentences within the same case.

## Vocabularies

### sentence-type-vocab

Constants: `01`, `02`, `03`, `04`, `05`, `06`, `07`, `08`, `09`, `10`, `11`, `12`, `13`, `14`, `15`, `16`

| Const | Value | Description |
| --- | --- | --- |
| 01 | Assessment/Special Assessment | A type of fine that always applies to each count of a convicted crime.|
| 02 | Community Service | Unpaid work that benefits the community.|
| 03 | Damages | An attempt to measure in financial terms the extent of harm a plaintiff has suffered because of the defendant's actions. Damges can be compensatory, punative, or statutory, and are usually attached to civil cases.|
| 04 | Deportation | Defendant is ordered to leave the country where the case is being tried.|
| 05 | Drug Testing | Regular screening ordered to test for drugs.|
| 06 | Fine | A financial punishment for violating a criminal law. Usually attached to criminal cases rather than civil.|
| 07 | Forfeiture | Loss of property, right, or privilege without compensation.|
| 08 | House Arrest | Confinement to a particular location for the duration of the sentence.|
| 09 | Incarceration | Imprisonment.|
| 10 | Injunction/Restraining Order | Defendant is ordered to cease doing a particular action. E.g., using stolen IP in their business.|
| 11 | Mental Health Treatment | Defendant is ordered to an inpatient or outpatient mental health facility, or is ordered to attend therapy for mental health issues.|
| 12 | No Internet Access | Defendant is not allowed to access the Internet via any type of device.|
| 13 | Probation | Defendant is released into the community in lieu of a prison sentence, but is subject to sepcial conditions and restrictions such as other types of sentences in this vocabulary.|
| 14 | Restitution | An attempt to measure in financial terms the extent of the gains or profits the defendant obtained through harming the victim.|
| 15 | Substance Abuse Treatment | Defendant is ordered to attend inpatient or outpatient treatment for substance abuse issues.|
| 16 | Supervised Release | Defendant is released into the community, subject to special conditions and restrictions, after the completion of a prison sentence.|

### sentence-metric-vocab

Constants: `H`, `D`, `M`, `Y`, `D`

| Const | Value | Description |
| --- | --- | --- |
| H | Hour(s) | Imposed sentence is in terms of hours. E.g. 20 hours community service.|
| D | Day(s) | Imposed sentence is in terms of days. E.g. 30 days in a substance abuse treatment facility.|
| M | Month(s) | Imposed sentence is in terms of months. E.g. 18 months imprisonment.|
| Y | Year(s) | Imposed sentence is in terms of years. E.g. 5 years no Internet access.|
| D | Dollar(s) | Imposed sentence is in terms of dollars. E.g. $10,000 in damages.|
