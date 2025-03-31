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
        row_number() over (partition by customer_id order by order_date) as order_number
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

-- https://leetcode.com/problems/classes-more-than-5-students
select class from Courses group by class having count(student) > 4

-- https://leetcode.com/problems/find-followers-count
select user_id, count(follower_id) as followers_count from Followers group by user_id order by user_id

-- https://leetcode.com/problems/biggest-single-number
select max(num) as num
from (
    select num from MyNumbers group by num having count(num) = 1
) as once

-- https://leetcode.com/problems/customers-who-bought-all-products
select customer_id
from Customer
group by customer_id
having count(distinct product_key) = (select count(product_key) from Product)

-- https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee
select
    mng.employee_id as employee_id,
    mng.name as name,
    count(emp.employee_id) as reports_count,
    round(avg(emp.age)) as average_age
from Employees as emp
inner join Employees as mng on emp.reports_to = mng.employee_id
group by mng.employee_id
order by employee_id

-- https://leetcode.com/problems/primary-department-for-each-employee
select employee_id, department_id from Employee
where primary_flag = 'Y'
union all
select employee_id, department_id from Employee
group by employee_id
having count(department_id) = 1

-- https://leetcode.com/problems/triangle-judgement
select x, y, z,
    (case when (x + y <= z or y + z <= x or x + z <= y) then "No" else "Yes" end) as triangle
from Triangle

-- https://leetcode.com/problems/consecutive-numbers
select distinct num as ConsecutiveNums
from (
    select num,
        lag(num) over (order by id) as prev_num,
        lead(num) over (order by id) as next_num
    from Logs) as cons_nums
where num = prev_num and num = next_num

-- https://leetcode.com/problems/product-price-at-a-given-date
select product_id, 10 as price
from Products
group by product_id
having min(change_date) > "2019-08-16"
union all
select product_id, new_price as price
from Products
where (product_id, change_date) in
(
    select product_id, max(change_date)
    from Products
    where change_date <= "2019-08-16"
    group by product_id
)

-- https://leetcode.com/problems/last-person-to-fit-in-the-bus
select person_name
from (select
    *,
    sum(weight) over (order by turn) as total_weight
    from Queue
) as t
where total_weight <= 1000
order by total_weight desc
limit 1

-- https://leetcode.com/problems/count-salary-categories
select "Low Salary" as category, count(account_id) as accounts_count
from Accounts
where income < 20000
union all
select "Average Salary" as category, count(account_id) as accounts_count
from Accounts
where income >= 20000 and income <= 50000
union all
select "High Salary" as category, count(account_id) as accounts_count
from Accounts
where income > 50000

-- https://leetcode.com/problems/employees-whose-manager-left-the-company
select employee_id
from Employees
where salary < 30000 and manager_id not in (select distinct employee_id from Employees)
order by employee_id

-- https://leetcode.com/problems/exchange-seats
select (
    case when id % 2 = 0 then (id - 1)
         when id % 2 = 1 and id != (select count(distinct id) from Seat) then (id + 1)
         else id
    end) as id, student
from Seat
order by id

-- https://leetcode.com/problems/movie-rating
(select u.name as results
from MovieRating as mr join Users as u on mr.user_id = u.user_id
group by u.name
order by count(*) desc, u.name
limit 1)
union all
(select m.title as results
from MovieRating as mr join Movies as m on mr.movie_id = m.movie_id
where month(mr.created_at) = 02 and year(mr.created_at) = 2020
group by m.title
order by avg(mr.rating) desc, m.title
limit 1)

-- https://leetcode.com/problems/restaurant-growth
WITH daily_totals AS (
    SELECT
        visited_on,
        SUM(amount) AS daily_total
    FROM Customer
    GROUP BY visited_on
)
select visited_on, amount, average_amount
from (
    select visited_on,
        sum(daily_total) over (order by visited_on rows between 6 preceding and current row) as amount,
        round(avg(daily_total) over (order by visited_on rows between 6 preceding and current row), 2) as average_amount,
        COUNT(*) OVER (ORDER BY visited_on) AS row_num
    from daily_totals
) a
where row_num >= 7
ORDER BY visited_on

-- https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends
with friends_count as (
    select requester_id as id, count(accepter_id) as num
    from RequestAccepted
    group by requester_id
    union all
    select accepter_id as id, count(accepter_id) as num
    from RequestAccepted
    group by accepter_id
)
select id, sum(num) as num from friends_count group by id order by num desclimit 1

-- https://leetcode.com/problems/investments-in-2016
select round(sum(tiv_2016), 2) as tiv_2016
from Insurance
where tiv_2015 in (select tiv_2015 from Insurance group by tiv_2015 having count(pid) > 1)
    and (lat, lon) in (select lat, lon from Insurance group by lat, lon having count(pid) = 1)

-- https://leetcode.com/problems/department-top-three-salaries
select Department, Employee, Salary
    from (
        select d.name as Department, e.name as Employee, e.salary as Salary,
            dense_rank() over (partition by d.id order by e.salary desc) as salary_rank
        from Employee as e
        left join Department as d on e.departmentId = d.id
    ) a
where salary_rank <= 3
