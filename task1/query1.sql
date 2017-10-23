select p.name from PERSON p
join RELATIONSHIP r on p.id = r.friend_id
where r.person_id = 1;
