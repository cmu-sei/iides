## Schema changes:
1. court-case.json, charge.json: changes curly quotes to \" as it was an unsupported character for json parsing
2. insider.json, target.json, : nested arrays for predisp and concern behav, any fields with tuples
3. response.json: corrected spelling errors (reponse in id and beahvioral in behavioral controls reference), additionally added nested arrays for behavioral controls, techniacl controls, and investigation events like insider.json (disallowed additional items as well)
4. insider-relationship-vocab.json: type to string instead of object
5. sentences.json: from H,D,M,Y,D to 1,2,3,4,5

## Possible issues:
1. missing field 'additionalItems: false' in most fields which would restrict users from having additional items not constrained to the vocab in the jsons, not sure if we would need this rigidity or if having more flexibility is a good thing. 
2. Need to implement a bundle schema with core IIDES components as requirements