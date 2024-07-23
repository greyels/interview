-- 197. Rising Temperature
select w1.id
from Weather as w1
inner join Weather as w2 on w1.recordDate = w2.recordDate + 1
where w1.temperature > w2.temperature

-- 1661. Average Time of Process per Machine
select a1.machine_id, round(avg(cast(a2.timestamp - a1.timestamp as decimal)), 3) as processing_time
from Activity as a1
inner join Activity a2 on a1.machine_id = a2.machine_id
and a1.process_id = a2.process_id and a2.timestamp > a1.timestamp
group by a1.machine_id
