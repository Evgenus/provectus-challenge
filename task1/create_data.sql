drop table if exists RELATIONSHIP;
drop table if exists PERSON;

create table PERSON(
  id INTEGER,
  name TEXT
);

insert into PERSON (id, name) values 
 (1, "Alice"),
 (2, "Bob"),
 (3, "Carol"),
 (4, "David")
;

create table RELATIONSHIP(
  person_id INTEGER,
  friend_id INTEGER
);

insert into RELATIONSHIP (person_id, friend_id) values
	(1, 2),
  (2, 3),
  (2, 4)
;
