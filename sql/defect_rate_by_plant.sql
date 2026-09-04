--What is the defect rate (%) for each plant, calculated separately per plant, using the production_batches table?

SELECT pl.plant_name,(SUM(pr.defect_qty)::numeric/SUM(pr.quantity_produced))*100 AS defect_rate
FROM plants AS pl
LEFT JOIN production_batches AS pr
ON pl.plant_id=pr.plant_id
GROUP BY pl.plant_name