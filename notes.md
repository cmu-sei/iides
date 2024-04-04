# Austin's Random Notes during dev

## Questions/Concerns
- How to handle location of incident?
    - is incident location always the same as the insider and/or organization location?
    - Should incident have its own location?
        - Right now, it does
- Do we need the specific lists of substances and psychological issues?


## TO DO
- Enumerations
- Incident
    - prior_planning : TextField
    - planning_comments : TextField
    - prior_deception : TextField
    - before_after_new_pos : CharField(7)
    - attack_location : MultiSelectField(16)
    - attack_time : CharField(19)
- Investigation
    unavailable_info : TextField
    interview_obtained : BooleanField
    investigator : CharField
- observable
    - observation_class: CharField
    - observation_cat : CharField(3)
    - grouping_id : CharField(3)
    - begin_date: datetime
    - end_date: datetime
    - times: PositiveIntegerField
    - description: TextField
    - observed: BooleanField
- Note handling of inexact dates

## References
- color palette https://www.cmu.edu/brand/brand-guidelines/visual-identity/colors.html
- Plant UML: https://plantuml.com/class-diagram
- STIX: https://stixproject.github.io/getting-started/whitepaper/#guiding-principles
- MISP: https://www.misp-project.org/documentation/