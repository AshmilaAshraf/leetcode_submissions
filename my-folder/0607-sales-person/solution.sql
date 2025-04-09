-- Write your PostgreSQL query statement below
select S1.name from SalesPerson S1
where S1.name not in
(select S2.name from SalesPerson S2
join Orders O1 on S2.sales_id=O1.sales_id
join Company C1 on C1.com_id=O1.com_id
where C1.name='RED'
);
