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

-- https://leetcode.com/problems/project-employees-i/
select p.project_id, round(avg(e.experience_years), 2) as average_years
from Project as p
left join Employee as e on p.employee_id = e.employee_id
group by p.project_id

-- https://leetcode.com/problems/percentage-of-users-attended-a-contest
select contest_id, round(100 * count(distinct user_id) / (select count(user_id) from Users), 2) as percentage
from Register
group by contest_id
order by percentage desc, contest_id asc

-- https://leetcode.com/problems/queries-quality-and-percentage
select
    query_name,
    round(avg(rating/position), 2) as quality,
    round(100 * sum(case when rating < 3 then 1 else 0 end) / count(*), 2) as poor_query_percentage
from Queries
group by query_name

-- https://leetcode.com/problems/monthly-transactions-i
select date_format(trans_date, '%Y-%m') as month,   -- select substr(trans_date, 1, 7) as month
    country,
    count(id) as trans_count,
    sum(case when state = "approved" then 1 else 0 end) as approved_count,
    sum(amount) as trans_total_amount,
    sum(case when state = "approved" then amount else 0 end) as approved_total_amount
from Transactions
group by month, country

-- https://leetcode.com/problems/immediate-food-delivery-ii
with delivery_num as (
    select
        *,
        row_number() over(partition by customer_id order by order_date) as order_number
    from Delivery
)
select round(100 * sum(case when order_date = customer_pref_delivery_date then 1 else 0 end) / count(*), 2) as immediate_percentage
-- select ROUND(AVG(order_date = customer_pref_delivery_date) * 100, 2) as immediate_percentage
from delivery_num
where order_number = 1

-- https://leetcode.com/problems/game-play-analysis-iv
select round(count(player_id) / (select count(distinct player_id) from Activity), 2) as fraction
from Activity
where (player_id, date_sub(event_date, interval 1 day))
    in (select player_id, min(event_date) from Activity group by player_id)

-- https://leetcode.com/problems/not-boring-movies
select id, movie, description, rating
from Cinema
where id % 2 != 0 and description != "boring"
order by rating desc

-- https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher
select teacher_id, count(distinct subject_id) as cnt
from Teacher
group by teacher_id

-- https://leetcode.com/problems/user-activity-for-the-past-30-days-i
select activity_date as day, count(distinct user_id) as active_users
from Activity
group by activity_date
having activity_date between date_sub("2019-07-27", interval 29 day) and "2019-07-27"

-- https://leetcode.com/problems/product-sales-analysis-iii
select a.product_id, b.first_year, a.quantity, a.price
from Sales as a
left join (select product_id, min(year) as first_year from Sales group by product_id) as b
on a.product_id = b.product_id
where a.year = b.first_year
