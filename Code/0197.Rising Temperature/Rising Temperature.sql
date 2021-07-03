# Write your MySQL query statement below

select w1.id Id
from Weather w1
inner join Weather w2 on datediff(w1.recordDate,w2.recordDate)=1       # datediff为前面参数减去后面参数
and w1.Temperature > w2.Temperature;