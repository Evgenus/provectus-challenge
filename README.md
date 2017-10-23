# provectus-challenge

Usage to task2

    python load_data.py alice_crm_dump.csv --domain alice
    python load_data.py bob_crm_dump.csv --domain bob
    python load_data.py carol_crm_dump.csv --domain carol


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

## task2

Project:
Attached are 3 csv files. Think of them as fake data dumps from 3 customers' CRMs (the 3 customers are Alice, Bob and Carol).  Each csv file has 2 columns, Company Name and Revenue.

Your task:
 - load data from these 3 files into a single relational database table
 - I recommend using sqlite, unless you strongly prefer another db
 - do this task keeping in mind a future requirement to be able to query and compare numerical revenue data across the 3 customers
