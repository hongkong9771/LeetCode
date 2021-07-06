# Write your MySQL query statement below

select distinct Email
from Person
group by Email
having count(*)>1;