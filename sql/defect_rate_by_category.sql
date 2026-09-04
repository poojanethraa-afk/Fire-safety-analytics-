--Which product category (not individual product) has the highest overall defect rate?
SELECT cat.category_name, SUM(prodb.defect_qty)::numeric/SUM(prodb.quantity_produced)*100 AS defect_rate
FROM categories AS cat
LEFT JOIN products AS prod
ON cat.category_id=prod.category_id
LEFT JOIN production_batches as prodb
on prod.product_id=prodb.product_id
GROUP BY cat.category_name
