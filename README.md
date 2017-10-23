# provectus-challenge

## task1

Given two tables, person and relationship,  person table has id and name columns, relationship table has person_id and friend_id:

    PERSON
    INTEGER id
    TEXT name

    RELATIONSHIP
    INTEGER person_id
    INTEGER friend_id

Write the following queries:
 - Given a person, return the list of friend’s names.
 - Given a person, return the list of the friend’s friends’ names, but exclude any direct friends.  I.e. Alice has friend Bob, and Bob has friends Carol and David; given Alice, return Carol and David.
