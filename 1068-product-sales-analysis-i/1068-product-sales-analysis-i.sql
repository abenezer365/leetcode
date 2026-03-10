# Write your MySQL query statement below
SELECT Product.product_name , Sales.year,Sales.price from Sales
INNER JOIN Product WHErE Product.product_id = Sales.product_id;