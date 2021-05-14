-- employee (id, name, department_id)
-- department (id, name)
-- salary (id, employee_id, year, month, amount)


select d.name from department as d
    left join employee as e on employee.department_id = department.id
    where e.name is NULL


select (e.name, s.year, sum(s.amount)) from salary as s
    left join employee as e on employee.id = salary.employee_id
    group by (e. name, s.year)
