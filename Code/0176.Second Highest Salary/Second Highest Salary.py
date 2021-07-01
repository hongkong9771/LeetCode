select ifnull(
(
select distinct salary
from Employee
order by Salary desc
limit 1,1),null) SecondHighestSalary;