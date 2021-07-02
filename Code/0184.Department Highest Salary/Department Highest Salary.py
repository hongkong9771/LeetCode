# Write your MySQL query statement below
select D.Name `Department`, E.Name `Employee`, E.Salary
from Employee E
inner join (select DepartmentId, max(Salary) max_sal
            from Employee
            group by DepartmentId
            ) max_dep
on E.DepartmentId=max_dep.DepartmentId
inner join Department D
on E.DepartmentId=D.Id
where E.Salary=max_dep.max_sal;