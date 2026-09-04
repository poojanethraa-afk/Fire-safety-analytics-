-- Which destination country has the worst on-time delivery rate?
SELECT destination_country, AVG (CASE WHEN actual_ship_date <= requested_ship_date THEN 1 ELSE 0 END)*100 AS on_time_pct
FROM orders
GROUP BY destination_country;