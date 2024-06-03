# Development Status

1. Schema development status: Complete
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
- [X] markdown
- [ ] wsd

Example 2:
- [X] json
- [X] markdown
- [ ] wsd

Example 3:
- [X] json
- [X] markdown
- [ ] wsd

Example 4:
- [X] json
- [X] markdown
- [ ] wsd

#### Schema changes:
1. court-case.json, charge.json: changes curly quotes to \" as it was an unsupported character for json parsing
2. insider.json, target.json, : nested arrays for predisp and concern behav, any fields with tuples
3. response.json: corrected spelling errors (reponse in id and beahvioral in behavioral controls reference), additionally added nested arrays for behavioral controls, techniacl controls, and investigation events like insider.json (disallowed additional items as well)
4. insider-relationship-vocab.json: type to string instead of object
5. sentences.json: from H,D,M,Y,D to 1,2,3,4,5
