## uml: sequence diagram
reference: https://plantuml.com/class-diagram

Django models
- court case
- charge
- sentence
- motive
- substance abuse
- psycological factors
- Incident
- source
- observable
- impact
- target

TODO 
- make sure all of the "CHOICES" options are in the enumerations 

```plantuml
@startuml
package "Incident" #DDDDDD {

    abstract Person {
        + first_name : string
        + middle_name : string
        + last_name : string
        + suffix : Suffix
        + city : string
        + state : State
        + country : Country
        + postalCode : integer
        + alias : string[0..*]
        + country_of_citizenship : Country
        + nationality
        + residency
        + gender
        + age
        + education
        + marital_status
        + number_of_children
        + comments
    }

    class Insider <<Person>> {
        * id : insider--<<UUID>>
        * incident_role : IncidentRole
        --
        + comments
    }
    class Accomplice <<Person>> {
        * id : accomplice--<<UUID>>
        --
        + relationship_to_insider : RelationshipType
    }
    struct Collusion {
        relationship : RelationshipType
        recruitment : RecruitmentType
        recruitment_direction : (Insider1,Insider2)
    }

    class Organization {
        * id : org--<<UUID>>
        --
        + name : string
        + city : string
        + state : StateCode
        + country : CountryCode
        + postalCode : integer
        + small_business : boolean
        + industry_sector_tier1
        + industry_sector_tier2
        + business
        + parent_company
    }

    class Sponsor {
        * id : sponsor--<<UUID>>
        --
        + sponsor_type : SponsorType
        + name : string
    }

    class Incident {
        * id : incident--<<UUID>>
        --
        + outcome : OutcomeType[0..*]
        + comments
    }

    class Job {
        * id : job--<<UUID>>
        --
        + job_function
        + occupation
        + title
        + position_technical
        + access_authorization
        + employment_type
        + hire_date
        + departure_date
        + tenure
        + comment
    }

    Insider ||--o{ Accomplice : Relationship
    Incident ||--|{ Insider : commits <
    Accomplice -- Job : has >
    Job -- Organization : employs <
    Insider -- Job : has >
    Organization }|--|{ Incident : OrgRole
    Organization }o--o{ Organization : OrgRelationship
    Insider }o--o| Sponsor : sponsors <
    Accomplice }o--o| Sponsor : sponsors <
    Insider |o--o| Organization : owns >
    Insider -- Collusion : Insider2 <
    Collusion -- Insider : Insider1 <

}
@enduml
```