--How many units were produced in total, per plant?
SELECT plant_name,SUM(quantity_produced) AS units_produced
FROM PLANTS AS pl
LEFT JOIN production_batches AS pro
ON pl.plant_id= pro.plant_id
GROUP BY plant_name

