-- Parduotų produktų kiekis
SELECT product.id, product.name, SUM(bill_line.quantity) AS total_sold
FROM product
JOIN bill_line ON product.id = bill_line.product_id
GROUP BY product.id
ORDER BY total_sold DESC
LIMIT 1;

--Produktų apyvartos
SELECT product.id, product.name, SUM(product.price * bill_line.quantity) AS total_revenue
FROM product
JOIN bill_line ON product.id = bill_line.product_id
GROUP BY product.id
ORDER BY total_revenue DESC
LIMIT 1;

--Daugiausiai nupirkę klientai
SELECT costumer.id as customer_id, costumer.first_name, costumer.last_name, SUM(product.price * bill_line.quantity) AS total_spent
FROM costumer
JOIN bill ON costumer.id = bill.custumer_id
JOIN bill_line ON bill.id = bill_line.bill_id
LEFT JOIN product ON bill_line.product_id = product.id
GROUP BY costumer.id
ORDER BY total_spent DESC
LIMIT 1;

--Didžiausia sąskaita
SELECT bill.id as bill_id, bill.purchase_datetime AS purchase_time, costumer.first_name AS customer_first_name, costumer.last_name AS customer_last_name,
       SUM(product.price * bill_line.quantity) AS total_amount
FROM bill
JOIN costumer ON bill.custumer_id = costumer.id
JOIN bill_line ON bill.id = bill_line.bill_id
JOIN product ON bill_line.product_id = product.id
GROUP BY bill.id
ORDER BY total_amount DESC
LIMIT 1;