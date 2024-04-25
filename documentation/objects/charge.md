# Charge

The charges or accusations brought against the insider when the incident is pursued in the legal system. E.g., "2 counts of Unauthorized Access to Company Systems"

## Properties

- **`id`** (required) *(string)* : A unique string that begins with "charge--" and is appended with a UUIDv4.
	- Uses pattern: ^charge--[UUIDv4]
- **`title`** (required) *(string)* : Broad subject matter area of the legal code. For U.S. cases, these are often title “18 U.S.C.”.
- **`section`** *(string)* : TODO
- **`nature_of_offense`** *(string)* : Description of the law being violated. Maps back to the title and section.
- **`count`** *(integer)* : Number of times the subject is accused of violating the law associated with this charge. Note that multiple violations of a law are often listed as a range of counts (e.g. “Count 2-6” would be 5 counts for this property).
- **`plea`** *(string)* : Plea entered by the defendant for this charge.
	- A constant from [charge-plea-vocab](#charge-plea-vocab)
- **`plea_bargain`** *(boolean)* : Whether the charge indicated here is a lesser charge based on a previous plea agreement.
- **`disposition`** *(string)* : The decision in the case or the final result.
	- A constant from [charge-disposition-vocab](#charge-disposition-vocab)

## Vocabularies

### charge-plea-vocab

Constants: `1`, `2`, `3`, `4`

| Const | Value | Description |
| --- | --- | --- |
| 1 | Guilty | TODO|
| 2 | No Contest | TODO|
| 3 | Not Guilty | TODO|
| 4 | Refused to Enter a Plea | TODO|

### charge-disposition-vocab

Constants: `01`, `02`, `03`, `04`, `05`, `06`, `07`, `08`, `09`, `10`, `11`

| Const | Value | Description |
| --- | --- | --- |
| 01 | Acquitted | Found not guilty by a court of law in a criminal trial.|
| 02 | Convicted | Plead or been found guilty by a court.|
| 03 | Dismissed | The court or prosecutor has decided the charge should not go forward.|
| 04 | Diversion/Deferred Prosecution | The court has delayed prosecution pending the successful completion of a treatment program, at which point the charges will be dismissed.|
| 05 | Expunged | The deletion of non-conviction information (such as arrest data).|
| 06 | No charges filed/Charges dropped | The prosecutor has declined to pursue the case.|
| 07 | Pending | The case is still being investigated or prosecuted.|
| 08 | Pled down | Pled guilty to a lesser charge.|
| 09 | Sealed | The court has restricted access to all or some of the content of the record; however, the existence of the record will still be public record.|
| 10 | Suspended sentence | The court has delayed the sentencing pending the successful completion of a period of probation and/or treatment program.|
| 11 | Vacated | The court has withdrawn the guilty plea or set aside the guilty verdict, and the defendant may state they have never been convicted of that crime.|
