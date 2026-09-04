import pandas as pd
import random
from datetime import date

random.seed(21)

product_ids = list(range(1, 25))
plant_ids = [1, 2, 3]

# one snapshot per product per plant per month, for the last 20 months
END_DATE = date(2026, 8, 1)
months = []
y, m = END_DATE.year, END_DATE.month
for _ in range(20):
    months.append(date(y, m, 1))
    m -= 1
    if m == 0:
        m = 12
        y -= 1
months = sorted(months)

# each product gets a fixed "typical" reorder level, so it's consistent across months/plants
reorder_level_by_product = {p: random.randint(20, 60) for p in product_ids}

# a handful of products are chronically under-stocked (stockout risk story)
risky_products = {4, 11, 19}

rows = []
snapshot_id = 1
for snap_date in months:
    for plant_id in plant_ids:
        for product_id in product_ids:
            reorder_level = reorder_level_by_product[product_id]

            if product_id in risky_products:
                # frequently dips near/under reorder level
                stock_qty = random.randint(max(0, reorder_level - 25), reorder_level + 15)
            else:
                # comfortably stocked most of the time
                stock_qty = random.randint(reorder_level, reorder_level + 120)

            rows.append({
                "snapshot_id": snapshot_id,
                "snapshot_date": snap_date.isoformat(),
                "product_id": product_id,
                "plant_id": plant_id,
                "stock_qty": stock_qty,
                "reorder_level": reorder_level,
            })
            snapshot_id += 1

df = pd.DataFrame(rows)
df.to_csv("inventory_snapshots.csv", index=False)

below = (df["stock_qty"] < df["reorder_level"]).mean()
print(df.shape)
print("share of snapshot-rows below reorder level: {:.1%}".format(below))
