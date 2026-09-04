-- On average, how many days pass between an order being placed and it actually shipping?

SELECT AVG(actual_ship_date - order_date)
FROM orders
