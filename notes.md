# Development Status

1. Schema development status: fixing minor issues and testing/validating schema
2. Documentation status: in progress
3. MERIT data updates: not started
4. Final team review: not started
5. External review (Dan, Bill, etc.): not started
6. Comms review: not started
7. Release review: not started


## Open Issues

### Documentation

White paper
- [ ] Intro (@losterritter)
- [ ] Background (@losterritter)
- [ ] Related Standards (@mpaes)
- [ ] Benefits (@mpaes)
- [ ] Relationships (@abwhisnant)
- [ ] Using IIDES (@abwhisnant)
  - Include guidance on:
    - handling inexact dates
    - handling lifetime sentences
- [ ] Conclusion (@abwhisnant)
- [ ] References (@abwhisnant)
- [ ] Licensing and RRO (@abwhisnant)

### Examples

Example 1 (@nammerman):
- [ ] json
- [ ] markdown
- [ ] wsd

Example 2:
- [ ] json
- [ ] markdown
- [ ] wsd

Example 3:
- [ ] json
- [ ] markdown
- [ ] wsd

Example 4:
- [ ] json
- [ ] markdown
- [ ] wsd


### Schema updates and issues

- (@abwhisnant) add deception to TTPs
- (@abwhisnant) go back through codebook and list missing/skipped fields
- (??) Remove leading zeros from constants in vocabularies:
	- charge disposition
	- impact metric
	- insider motive
	- response tech controls vocab
	- response behavioral controls vocab
	- response investigation events
	- response investigated by vocab
	- sentence type vocab
	- source type vocab
- (??) change “cb-type-vocab” to “concerning-behavior-type-vocab”
- (??) add bundle definition to the schema
- (??) stressor cat/subcat vocabs - change constants to digits only (x and x.y)
- (??) target category vocab 2.3 title - change “plans” to “information”

### JSON formatting and validation

Assigned: @nammerman

Ensuring the IIDES json schema docs are valid under the 2020 json schema

- [ ] Accomplice
- [ ] Charge
- [ ] Court Case
- [ ] Detection
- [ ] Impact
- [ ] Incident
- [ ] Insider
- [ ] Job
- [ ] Legal Response
- [ ] Note
- [ ] Organization
- [ ] Person
- [ ] Response
- [ ] Sentence
- [ ] Source
- [ ] Sponsor
- [ ] Stressor
- [ ] Target
- [ ] TTP
- [ ] Insider relationship vocab
- [ ] Org Relationship
- [ ] Collusion
- [ ] Org Owner
- [ ] Relationship
