CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    declare row_offset INT;
    set row_offset = N-1;
    RETURN (
        # Write your MySQL query statement below.
        select distinct salary as getNthHighestSalary
        from Employee
        order by salary desc
        limit 1 offset row_offset
    );
END
