# Write your MySQL query statement below
update salary
set sex = 
case sex
when 'm' then 'f'
when 'f' then 'm'
end;

