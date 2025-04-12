-- Write your PostgreSQL query statement below
select P1.product_name, S1.year, S1.price
from Sales S1
JOIN Product P1
on S1.product_id = P1.product_id;
