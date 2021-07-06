# Write your MySQL query statement below

select D.Name `Department`, E.Name `Employee`, E.Salary
from (
    select *, dense_rank() over(partition by DepartmentId order by Salary desc) ranking 
    from Employee
) E
inner join Department D on E.DepartmentId=D.Id
where E.ranking<4;