# Write your MySQL query statement below
SELECT A.activity_date AS day, count(*) AS active_users from
    (select distinct user_id, activity_date 
    FROM Activity
    where activity_date between '2019-06-28' and '2019-07-27') A
GROUP BY A.activity_date
ORDER BY A.activity_date;

