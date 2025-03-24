# Write your MySQL query statement below
-- delete p1
-- from Person p1
-- join Person p2
-- on p1.email = p2.email and p1.id>p2.id;

delete from Person
where id not in (
    select min(id) from (select * from Person) as temp group by email 
);
