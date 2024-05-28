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
- [ ] Conclusion (@abwhisnant)

### Examples

Example 1 (@nammerman):
- [X] json
- [ ] markdown
- [ ] wsd

Example 2:
- [X] json
- [ ] markdown
- [ ] wsd

Example 3:
- [X] json
- [ ] markdown
- [ ] wsd

Example 4:
- [X] json
- [ ] markdown
- [ ] wsd


### Schema updates and issues (@nammerman) - DONE

-  Remove leading zeros from constants in vocabularies:
	- charge disposition
	- impact metric
	- insider motive
	- response tech controls vocab
	- response behavioral controls vocab
	- response investigation events
	- response investigated by vocab
	- sentence type vocab
	- source type vocab
-  change “cb-type-vocab” to “concerning-behavior-type-vocab”
-  add bundle definition to the schema
-  stressor cat/subcat vocabs - change constants to digits only (x and x.y)
-  target category vocab 2.3 title - change “plans” to “information”
#### Schema changes:
1. court-case.json, charge.json: changes curly quotes to \" as it was an unsupported character for json parsing
2. insider.json, target.json, : nested arrays for predisp and concern behav, any fields with tuples
3. response.json: corrected spelling errors (reponse in id and beahvioral in behavioral controls reference), additionally added nested arrays for behavioral controls, techniacl controls, and investigation events like insider.json (disallowed additional items as well)
4. insider-relationship-vocab.json: type to string instead of object
5. sentences.json: from H,D,M,Y,D to 1,2,3,4,5

### JSON formatting and validation - DONE

Assigned: @nammerman

Ensuring the IIDES json schema docs are valid under the 2020 json schema

- [X] Accomplice
- [X] Charge
- [X] Court Case
- [X] Detection
- [X] Impact
- [X] Incident
- [X] Insider
- [X] Job
- [X] Legal Response
- [X] Note
- [X] Organization
- [X] Person
- [X] Response
- [X] Sentence
- [X] Source
- [X] Sponsor
- [X] Stressor
- [X] Target
- [X] TTP
- [X] Insider relationship vocab
- [X] Org Relationship
- [X] Collusion
- [X] Org Owner
- [X] Relationship
