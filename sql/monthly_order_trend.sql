--How has monthly order volume changed over the last 18 months — is it trending up, down, or flat?
SELECT DATE_TRUNC('month', order_date) as month_order,COUNT(order_id) AS num_orders
FROM orders
GROUP BY month_order
ORDER BY month_order