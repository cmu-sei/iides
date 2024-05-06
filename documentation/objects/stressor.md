# Stressor

Events that occur within the victim organization and precipitate insider activity.

## Properties

- **`id`** (required) *(string)* : A unique string that begins with "stressor--" and is appended with a UUIDv4.
	- Uses pattern: ^stressor--[UUIDv4]
- **`date`** *(date)* : The date the stressor first occurred.
- **`category`** *(string)* : The category to which the stressor belongs.
	- A constant from [stressor-category-vocab](#stressor-category-vocab)
	- Required if `subcategory` exists.
- **`subcategory`** *(string)* : The subcategory to which the stressor belongs. When subcategory is specified, category MUST also be specified. The subcategory constant MUST map to the specified category constant.
	- A constant from [stressor-subcategory-vocab](#stressor-subcategory-vocab)
- **`comment`** *(string)* : Clarifying comments about the stressor.

## Vocabularies

### stressor-category-vocab

Constants: `S1`, `S2`, `S3`, `S4`

| Const | Value | Description |
| --- | --- | --- |
| S1 | Employment Status | The insider's employment status changed.|
| S2 | Organizational Issues | The insider's employer had problems or changes that directly or indirectly affected the insider.|
| S3 | Unmet Expectations | Insider's expectations of/from their employer were not met.|
| S4 | Consequences for Previous Violations | Consequences resulting from the insider's previous behavior or violations, not resulting from the incident itself.|

### stressor-subcategory-vocab

Constants: `S1.1`, `S1.2`, `S1.3`, `S1.4`, `S1.5`, `S1.6`, `S1.7`, `S1.8`, `S1.9`, `S1.10`, `S1.11`, `S1.12`, `S2.1`, `S2.2`, `S2.3`, `S2.4`, `S2.5`, `S2.6`, `S2.7`, `S2.8`, `S2.9`, `S2.10`, `S2.11`, `S2.12`, `S2.13`, `S3.1`, `S3.2`, `S3.3`, `S3.4`, `S4.1`, `S4.2`, `S4.3`, `S4.4`, `S4.5`, `S4.6`

| Const | Value | Description |
| --- | --- | --- |
| S1.1 | Insider Hired | Insider is hired by the victim organization or another organization.|
| S1.2 | Insider Promoted | The insider is promoted within any organization, including the victim organization.|
| S1.3 | Insider Demoted | The insider is demoted within any organization, including the victim organization.|
| S1.4 | Insider Notified of Pending Termination | The insider is informed that they will be terminated from the organization in the near future.|
| S1.5 | Insider Suspended | The insider is suspended from work for any reason.|
| S1.6 | Insider Laid Off | The insider is laid off from their position within the organization.|
| S1.7 | Insider Put on Paid/Unpaid Leave | The insider is put on a temporary leave from a job assignment, with or without pay and benefits.|
| S1.8 | Insider Terminated | The insider is fired from any organization, including the victim organization|
| S1.9 | Insider Resigned | The insider resigns from any organization, including the victim organization.|
| S1.10 | Change of Employment Status | The insider's status within the organization being changes from what it originally was (e.g., Insider took a full-time position at the organization after graduating college).|
| S1.11 | Insider Changed Positions Internally | The insider changes positions within the organization (e.g., Insider transferred to the Accounting department).|
| S1.12 | Insider Submits Resignation Notice | The insider submits notice of resignation to the organization.|
| S2.1 | Mergers And Acquisitions | A change in the structure of the insider's employer organization (e.g., The insider's organization was in the process of being bought out by another company).|
| S2.2 | Reorganization Of Organization Or Outsourcing | A change in the internal structure of the insider's employer (e.g., The division of the victim organization that the insider worked in was closing).|
| S2.3 | Significant Financial Stress (non-bankruptcy) | The organization was undergoing significant financial stress, but did not declare bankruptcy.|
| S2.4 | Previous Insider Incident | Organization has previously had an insider incident unrelated to this one|
| S2.5 | Layoffs | Temporary suspension or permanent termination of one or more employees.|
| S2.6 | Personnel Changes | Staffing changes of employees other than the insider within the employing organization.|
| S2.7 | Supervisor Ambiguity | The insider expressed a lack of clarity in the organization's supervisory hierarchy.|
| S2.8 | Organization Filed for Bankruptcy | The organization filed for bankruptcy.|
| S2.9 | Lack of Background Checks | The organizational failure to sufficiently review the past history of potential candidates.|
| S2.10 | Inadequate Training | An organizational failure to administer the proper training for its employees.|
| S2.11 | Lax Controls | The organizational failure to restrict access to what is necessary for the insider to perform work related activities.|
| S2.12 | Hostile Work Environment | A work environment that is difficult or uncomfortable for another person to work in due to discrimination of any kind.|
| S2.13 | Problematic Leader | A supervisor or other leader who is abusive or difficult to work with, for example, by ignoring input from subordinates, excessively criticizing, or taking credit for subordinates' work.|
| S3.1 | Compensation/Benefit Issues | Insider expressed dissatisfaction with current compensation or benefits.|
| S3.2 | Poor Performance Review | Insider received a review of their work performance, which is deemed below average.|
| S3.3 | Request Denied By Organization | The employing organization refused a request from the insider (e.g., The insider's request to work from home is denied due to unproductivity in past work from home).|
| S3.4 | Passed Over For Promotion | Insider's employer chooses to promote someone other than the insider.|
| S4.1 | Counseling | Insider was sent to counseling of any kind as a result of their actions|
| S4.2 | Referred to EAP | Insider was referred to the Employee Assistance Program (EAP) as a result of their actions|
| S4.3 | Reported to HR | Insider was reported to Human Resources as a result of their actions|
| S4.4 | Transferred | Insider was transferred to another location or another team as a result of their actions.|
| S4.5 | Verbal Reprimand | Insider received a verbal reprimand from their supervisor as a result of their actions.|
| S4.6 | Written Reprimand | Insider received a written reprimand from their supervisor as a result of their actions.|
