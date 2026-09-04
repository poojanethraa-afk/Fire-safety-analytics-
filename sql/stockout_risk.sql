--Which products are currently below their reorder level (at risk of running out), and at which plant?

SELECT pr.product_name,pl.plant_name
FROM products AS pr
LEFT JOIN inventory_snapshots AS inv
ON pr.product_id= inv.product_id
LEFT JOIN plants as pl
ON inv.plant_id= pl.plant_id
WHERE inv.reorder_level>inv.stock_qty AND inv.snapshot_date=(SELECT MAX(inv.snapshot_date) FROM inventory_snapshots AS inv)