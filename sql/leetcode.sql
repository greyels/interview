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

-- 577. Employee Bonus
select e.name, b.bonus
from Employee as e
left join Bonus as b on e.empId = b.empId
where b.bonus < 1000 or b.bonus is NULL

-- 1280. Students and Examinations
select s.student_id, s.student_name, sub.subject_name, count(e.subject_name) as attended_exams
from Students as s
cross join Subjects as sub
left join Examinations as e on s.student_id = e.student_id and sub.subject_name = e.subject_name
group by s.student_id, s.student_name, sub.subject_name
order by s.student_id, sub.subject_name

-- 570. Managers with at Least 5 Direct Reports
select e2.name
from Employee as e1
inner join Employee as e2 on e1.managerId = e2.id
group by e1.managerId, e2.name
having count(e1.id) >= 5

-- 1934. Confirmation Rate
select
    s.user_id,
    round(avg(case when action = 'confirmed' then 1 else 0 end), 2) as confirmation_rate
from Signups as s
left join Confirmations as c on s.user_id = c.user_id
group by s.user_id

-- 620. Not Boring Movies
select id, movie, description, rating
from Cinema
where mod(id, 2) <> 0 and description <> 'boring'
order by rating desc

-- 1251. Average Selling Price
select p.product_id, coalesce(round(cast(sum(p.price * u.units) as decimal) / sum(u.units), 2), 0) as average_price
from Prices as p
left join UnitsSold as u on u.product_id = p.product_id and (u.purchase_date between p.start_date and p.end_date)
group by p.product_id
