-- How many orders came from each customer industry?
SELECT ind.industry_name, COUNT(ord.order_id)
FROM industries as ind
LEFT JOIN orders as ord
ON ind.industry_id= ord.industry_id
GROUP BY ind.industry_name