# Write your MySQL query statement below

# 查找重复的邮箱
delete from 
Person P
where P.Id in
(
    select Id 
    from 
(
select Id, Email, rank() over (partition by Email order by Id) ranking
from Person
) new_t
where new_t.ranking !=1
);