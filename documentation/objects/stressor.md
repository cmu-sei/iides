# Stressor

A sressor is an event(s) that occurred within the victim organization and precipitated insider activity.

## Properties

- **`id`** (required) *(string)* : A unique string that begins with "stressor--" and is appended with a UUIDv4
  - Uses pattern: ^stressor--[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
- **`date`** *(date)* : The date the stressor first occurred
- **`category`** *(string)* : The category to which the stressor belongs
	- A constant from [stressor-category-vocab](#stressor-category-vocab)
  - Required if `subcategory` exists
- **`subcategory`** *(string)* : The subcategory to which the stressor belongs. When subcategory is specified, category MUST also be specified. The subcategory constant MUST map to the specified category constant.
	- A constant from [stressor-subcategory-vocab](#stressor-subcategory-vocab)
- **`comment`** *(string)* : Clarifying comments about the stressor

## Vocabularies

### stressor-category-vocab

Constants: `1`, `2`, `3`, `4`

| Const | Value | Description |
| --- | --- | --- |
| 1 | Employment Status | The insider's employment status changed|
| 2 | Organizational Issues | The insider's employer had problems or changes that directly or indirectly affected the insider|
| 3 | Unmet Expectations | Insider's expectations of their employer were not met|
| 4 | Consequences for Previous Violations | Consequences against the insider resulting from the insider's previous behavior or violations, not resulting from the incident itself|

### stressor-subcategory-vocab

Constants: `1.1`, `1.2`, `1.3`, `1.4`, `1.5`, `1.6`, `1.7`, `1.8`, `1.9`, `1.10`, `1.11`, `1.12`, `2.1`, `2.2`, `2.3`, `2.4`, `2.5`, `2.6`, `2.7`, `2.8`, `2.9`, `2.10`, `2.11`, `2.12`, `2.13`, `3.1`, `3.2`, `3.3`, `3.4`, `4.1`, `4.2`, `4.3`, `4.4`, `4.5`, `4.6`

| Const | Value | Description |
| --- | --- | --- |
| 1.1 | Insider Hired | Insider is hired by the victim organization or another organization|
| 1.2 | Insider Promoted | The insider is promoted within any organization, including the victim organization|
| 1.3 | Insider Demoted | The insider is demoted within any organization, including the victim organization|
| 1.4 | Insider Notified of Pending Termination | The insider is informed that they will be terminated from the organization in the near future|
| 1.5 | Insider Suspended | The insider is suspended from work for any reason|
| 1.6 | Insider Laid Off | The insider is laid off from their position within the organization|
| 1.7 | Insider Put on Paid/Unpaid Leave | The insider is put on a temporary leave from a job assignment, with or without pay and benefits|
| 1.8 | Insider Terminated | The insider is fired from any organization, including the victim organization|
| 1.9 | Insider Resigned | The insider resigns from any organization, including the victim organization|
| 1.10 | Change of Employment Status | The insider's status within the organization changes from what it originally was (e.g., the insider took a full-time position at the organization after graduating college)|
| 1.11 | Insider Changed Positions Internally | The insider changes positions within the organization (e.g., the insider transferred to the accounting department)|
| 1.12 | Insider Submits Resignation Notice | The insider submits notice of resignation to the organization.|
| 2.1 | Mergers And Acquisitions | A change in the structure of the insider's employer organization (e.g., the insider's organization was in the process of being bought out by another company)|
| 2.2 | Reorganization Of Organization Or Outsourcing | A change in the internal structure of the insider's employer (e.g., the division of the victim organization that the insider worked in was closing)|
| 2.3 | Significant Financial Stress (non-bankruptcy) | The organization was undergoing significant financial stress, but did not declare bankruptcy|
| 2.4 | Previous Insider Incident | Organization has previously had an insider incident unrelated to this one|
| 2.5 | Layoffs | Temporary suspension or permanent termination of one or more employees|
| 2.6 | Personnel Changes | Staffing changes of employees other than the insider within the employing organization|
| 2.7 | Supervisor Ambiguity | The insider expressed a lack of clarity in the organization's supervisory hierarchy|
| 2.8 | Organization Filed for Bankruptcy | The organization filed for bankruptcy|
| 2.9 | Lack of Background Checks | The organizational failure to sufficiently review the past history of potential candidates|
| 2.10 | Inadequate Training | An organizational failure to administer the proper training for its employees|
| 2.11 | Lax Controls | The organizational failure to restrict access to what is necessary for the insider to perform work related activities|
| 2.12 | Hostile Work Environment | A work environment that is difficult or uncomfortable for another person to work in due to discrimination of any kind|
| 2.13 | Problematic Leader | A supervisor or other leader who is abusive or difficult to work with, for example, by ignoring input from subordinates, excessively criticizing, or taking credit for subordinates' work.|
| 3.1 | Compensation/Benefit Issues | Insider expressed dissatisfaction with current compensation or benefits|
| 3.2 | Poor Performance Review | Insider received a review of their work performance that was deemed below average|
| 3.3 | Request Denied By Organization | The employing organization refused a request rom the insider (e.g., the insider's request to work from home is denied due to unproductivity in past work from home).|
| 3.4 | Passed Over For Promotion | Insider's employer chooses to promote someone other than the insider|
| 4.1 | Counseling | Insider was sent to counseling of any kind as a result of their actions|
| 4.2 | Referred to EAP | Insider was referred to the Employee Assistance Program (EAP) as a result of their actions|
| 4.3 | Reported to HR | Insider was reported to human resources as a result of their actions|
| 4.4 | Transferred | Insider was transferred to another location or another team as a result of their actions|
| 4.5 | Verbal Reprimand | Insider received a verbal reprimand from their supervisor as a result of their actions|
| 4.6 | Written Reprimand | Insider received a written reprimand from their supervisor as a result of their actions|

## License
This file is a part of the Insider Incident Data Exchange Standard (IIDES) - see https://github.com/cmu-sei/IIDES

Copyright 2024 Carnegie Mellon University.

[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution.  Please see Copyright notice for non-US Government use and distribution.

This work is provided “AS-IS” with “NO WARRANTIES OF ANY KIND - EXPRESS OR IMPLIED” and is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.

Requests for permission for non-licensed uses should be directed to the Software Engineering Institute at permission@sei.cmu.edu.

CERT® is registered in the U.S. Patent and Trademark Office by Carnegie Mellon University.

DM24-0776
