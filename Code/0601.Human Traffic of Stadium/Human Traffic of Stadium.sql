# Write your MySQL query statement below

# 将表中people数大于或等于100的 按照id进行排序，得到列为rank_row
# 然后id列减去rank_row列得到新的列 rank_continue，用于判断是否连续
# 下面简写



# select id, visit_date, people
# from

select id, visit_date, people
from 
(
    select *, id - row_number() over (order by id) rank_continue
    from Stadium
    where people>=100
) new_t

where  rank_continue in

(select rank_continue
    from
    (
        select *, id - row_number() over (order by id) rank_continue
        from Stadium
        where people>=100
    ) new_t
    group by rank_continue
    having count(rank_continue)>=3
)
;