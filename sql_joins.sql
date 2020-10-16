-- 1.Напишите запрос, который бы использовал оператор INNER JOIN для получения всех Заказов для покупателя с фамилией Краснов.
SELECT onum, amt, odate, cname
FROM orders
INNER JOIN customers on orders.cnum = customers.cnum and cname = 'Краснов'
-- 2.Напишите запрос, который бы вывел фамилии и города продавцов, комиссия которых составляет более 20%.
SELECT DISTINCT(sname), city, comm
FROM salespeople
INNER JOIN orders on orders.snum = salespeople.snum and comm > 20
-- 3.Напишите запрос, который бы вывел суммарную сумму заказов для городов в которых работают продавцы.
SELECT SUM(amt), salespeople.city
FROM orders
INNER JOIN salespeople on orders.snum = salespeople.snum 
GROUP BY salespeople.city
-- 4.Повторите предыдущий запрос, но выведите все города, даже если в них не совершалась сделка.
SELECT SUM(amt), salespeople.city
FROM orders
RIGHT OUTER JOIN salespeople on orders.snum = salespeople.snum 
GROUP BY salespeople.city
-- 5.Напишите запрос, который бы вывел максимальную сумму заказов для городов в которых проживают покупатели, даже если в этих городах не было произведено сделки.
SELECT customers.city, MAX(amt)
FROM customers
LEFT OUTER JOIN orders on orders.cnum = customers.cnum 
GROUP BY customers.city