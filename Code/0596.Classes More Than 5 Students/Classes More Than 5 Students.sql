# Write your MySQL query statement below
/*
select class from
(
    select distinct student, class
    from courses
) new_t
group by class
having count(*)>=5;

*/

# 去重简单版
# 防止学生在同一门课上，多次选择，即一个人多次选同一门课
select class
from courses
group by class
having count(distinct student)>=5;