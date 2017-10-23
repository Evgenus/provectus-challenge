select p.name from PERSON p
join RELATIONSHIP r1 on p.id = r1.friend_id
join RELATIONSHIP r2 on r1.person_id = r2.friend_id
where r2.person_id = 1;
