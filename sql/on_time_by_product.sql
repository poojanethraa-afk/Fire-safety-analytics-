--Which specific products have the worst on-time delivery rate?
SELECT product_name, AVG(CASE WHEN actual_ship_date <= requested_ship_date THEN 1 ELSE 0 END)*100  AS on_time_pct
FROM products as pro
LEFT JOIN orders as ord
ON pro.product_id=ord.product_id
GROUP BY product_name