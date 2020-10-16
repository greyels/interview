-- 1. Напишите запрос, который бы использовал подзапрос для получения всех Заказов для покупателя с фамилией Краснов. 
-- Предположим, что вы не знаете номера этого покупателя, указываемого в поле cnum.
SELECT *
FROM orders
where cnum = (SELECT cnum
              FROM customers
              WHERE cname = 'Краснов')
-- 2. Напишите запрос, который вывел бы имена и рейтинг всех покупателей, которые имеют Заказы, сумма которых выше средней.
SELECT cname, rating
FROM customers
where cnum IN (SELECT cnum
              FROM orders
              WHERE amt > (SELECT AVG(amt) FROM orders))
-- 3. Напишите запрос, который бы выбрал общую сумму всех приобретений в Заказах для каждого продавца, у которого эта общая сумма больше, чем сумма наибольшего Заказа в таблице.
SELECT snum, SUM(AMT) 
FROM orders 
GROUP BY snum 
HAVING SUM(amt) > (SELECT MAX(amt) FROM orders)
-- 4. Напишите запрос, который бы использовал подзапрос для получения всех Заказов для покупателей проживающих в Москве.
SELECT *
FROM orders
where cnum IN (SELECT cnum
              FROM customers
              WHERE city =  'Москва')
-- 5. Используя подзапрос определить дату заказа, имеющего максимальное значение суммы приобретений (вывести даты и суммы приобретений).
SELECT amt, odate
FROM orders
WHERE AMT = (SELECT MAX(AMT) FROM orders)
-- 6. Определить покупателей, совершивших сделки с максимальной суммой приобретений.
SELECT cname
FROM customers
WHERE cnum IN (SELECT cnum
               FROM orders
               WHERE amt = (SELECT MAX(amt) FROM orders))