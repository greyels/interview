Есть таблицы:
Список департаментов: DEPARTMENT, содержит ID и NAME
Список сотрудников: EMPLOYEE, содержит ID, DEPARTMENT_ID, MANAGER_ID, NAME, SALARY

Задание 1.Вывести список сотрудников, получающих заработную плату большую чем у непосредственного руководителя

select e.*
from employee e, employee b
where e.manager_id = b.id and e.salary > b.salary

Задание 2.Вывести список сотрудников, получающих максимальную заработную плату в своем отделе

select *
from employee a
where salary = (select dep_id, max(salary) from employee group by department_id) b
where a.dep_id = b.dep_id

Задание 3.Вывести список ID отделов, количество сотрудников в которых не превышает 3 человек

select department_id
from employee
group by department_id
having count(id) <= 3

Задание 4.Вывести список сотрудников, не имеющих назначенного руководителя, работающего в том же отделе

select a.*
from employee a, employee b
where (a.manager_id = b.id and a.department_id <> b.department_id) or a.manager_id is null

Задание 5.Найти список ID отделов с максимальной суммарной зарплатой сотрудников

WITH dept_salaries AS (
    SELECT department_id, SUM(salary) AS total_salary
    FROM employee
    GROUP BY department_id
)
SELECT department_id
FROM dept_salaries
WHERE total_salary = (SELECT MAX(total_salary) FROM dept_salaries);
