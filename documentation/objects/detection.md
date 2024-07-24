# Detection

Detection describes details about how, when, and by whom the incident was detected. An incident may have only one detection entity.

## Properties

- **`id`** (required) _(string)_ : A unique string that begins with "detection--" and is appended with a UUIDv4
  - Uses pattern: ^detection--[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
- **`first_detected`** _(date-time)_ : The date and time the victim organization first became aware of the incident
- **`who_detected`** _(array)_ : The individual entities or team(s) that first detected the incident
  - One or more constants from [detection-team-vocab](#detection-team-vocab)
- **`detected_method`** _(array)_ : The system or process that led to the first detection of the incident
  - One or more constants from [detection-method-vocab](#detection-method-vocab)
- **`logs`** _(array)_ : The type(s) of logs used by the detection team and/or method used to first detect the incident
  - One or more constants from [detection-log-vocab](#detection-log-vocab)
- **`comment`** _(string)_ : Clarifying comments about who, what, when, or how the incident was detected

## Vocabularies

### detection-team-vocab

Constants: `LE`, `OR`, `CU`, `CO`, `AU`, `SR`, `IR`, `ST`, `MG`, `II`, `RR`

| Const | Value                  | Description                                                                                                                                                                                                                     |
| ----- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| LE    | Law Enforcement        | Law enforcement discovered the insider's illegal activity (e.g., police noticed that the insider was gaining access to the company after hours)                                                                                 |
| OR    | Organization           | The victim organization discovered the insider's activity (e.g., IT noticed that the insider had downloaded dozens of company trade secrets to their workstation)                                                               |
| CU    | Customer               | A customer of the victim organization discovered the insider's activity                                                                                                                                                         |
| CO    | Competitor             | An organization competing with the victim organization discovered the insider's activity (e.g., the insider approached a competing organization with company trade secrets, and the competitor alerted the victim organization) |
| AU    | Auditor                | Internal or external auditor assigned to assess the organization's security, risk, or threat posture                                                                                                                            |
| SR    | Self-Reported          | The insider reported their activity to their organization                                                                                                                                                                       |
| IR    | Incident Response Team | The incident response team (IRT) discovered the insider's activity                                                                                                                                                              |
| ST    | Security Team          | Technical or personnel security team discovered the insider's activity                                                                                                                                                          |
| MG    | Management             | A member of the organization's management or the insider's management chain discovered the insider's activities                                                                                                                 |
| II    | Internal Investigators | Investigators internal to the victim organization                                                                                                                                                                               |
| RR    | Researcher             | Researcher external to the organization                                                                                                                                                                                         |

### detection-method-vocab

Constants: `1`, `2`, `3`, `4`, `5`

| Const | Value               | Description                                                                                                                                                               |
| ----- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Audit               | The insider's activity was spotted during an internal or third-party auditing process                                                                                     |
| 2     | Technical Means     | The insider's activity was detected via analysis or anomalies in technical systems and software                                                                           |
| 3     | Non-Technical Means | The insider's activity was detected in a non-technical fashion (e.g., the insider had personal items purchased with a company credit card sent to the office by accident) |
| 4     | Security Software   | The insider's activity was detected by security software (e.g., the insider tried to download a document with trade secrets and an automatic alert detected the download) |
| 5     | System Failure      | The insider's activity resulted in a system going down within the organization, which led to the detection of the insider's activities                                    |

### detection-log-vocab

Constants: `AC`, `AU`, `BR`, `DB`, `EM`, `FS`, `IS`, `RA`, `SF`, `VD`, `WB`

| Const | Value                | Description                                                                            |
| ----- | -------------------- | -------------------------------------------------------------------------------------- |
| AC    | Access Logs          | File or system access logs                                                             |
| AU    | Audit Logs           | Logs generated specifically for auditing purposes                                      |
| BR    | Bank Records         | Financial transaction or account records                                               |
| DB    | Database Logs        | Logs from traditional or non-traditional database servers or services                  |
| EM    | Email Logs           | Logs from email servers or services                                                    |
| FS    | Financial Statements | Statements or records from an individual's financial account(s)                        |
| IS    | ISP Logs             | Logs from internet service providers (ISPs)                                            |
| RA    | Remote Access Logs   | Logs from remote access servers or clients                                             |
| SF    | System File Logs     | File logs (create, delete, modify, etc.) from workstations, servers, and other systems |
| VD    | Video Logs           | Video, security cam, webcam, screen capture recordings                                 |
| WB    | Web Logs             | Logs from web servers or web proxies                                                   |

## License

This file is a part of the Insider Incident Data Exchange Standard (IIDES) - see https://github.com/cmu-sei/IIDES

Copyright 2024 Carnegie Mellon University.

[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution. Please see Copyright notice for non-US Government use and distribution.

This work is provided \"AS-IS\" with \"NO WARRANTIES OF ANY KIND - EXPRESS OR IMPLIED\" and is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.

Requests for permission for non-licensed uses should be directed to the Software Engineering Institute at permission@sei.cmu.edu.

CERT® is registered in the U.S. Patent and Trademark Office by Carnegie Mellon University.

DM24-0776
