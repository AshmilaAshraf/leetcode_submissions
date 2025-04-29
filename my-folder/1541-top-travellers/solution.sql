# Write your MySQL query statement below
select u.name, coalesce(sum(r.distance),0) as travelled_distance from Rides r 
right join Users u on u.id = r.user_id
group by user_id
order by travelled_distance desc,name asc;
