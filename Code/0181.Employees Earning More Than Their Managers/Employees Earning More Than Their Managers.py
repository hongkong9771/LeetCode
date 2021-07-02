# Write your MySQL query statement below


select a.Name Employee
from Employee a
inner join Employee b
on a.ManagerId=b.Id
where a.Salary>b.Salary;