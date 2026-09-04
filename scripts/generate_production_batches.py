import pandas as pd
import random
from datetime import date, timedelta

random.seed(42)

product_ids = list(range(1, 25))    # 24 catalog products
plant_weights = {1: 0.5, 2: 0.3, 3: 0.2}   # Plant A biggest, Plant B mid, Plant C smallest
plants = list(plant_weights.keys())
weights = list(plant_weights.values())

N_ROWS = 220
END_DATE = date(2026, 8, 14)
START_DATE = END_DATE - timedelta(days=18 * 30)  # ~18 months back

rows = []
for batch_id in range(1, N_ROWS + 1):
    product_id = random.choice(product_ids)
    plant_id = random.choices(plants, weights=weights, k=1)[0]

    days_offset = random.randint(0, (END_DATE - START_DATE).days)
    production_date = START_DATE + timedelta(days=days_offset)

    quantity_produced = random.randint(50, 500)

    # normal batches: 1-4% defect rate. ~6% of batches are a "bad batch" spike: 8-15%.
    if random.random() < 0.06:
        defect_rate = random.uniform(0.08, 0.15)
    else:
        defect_rate = random.uniform(0.01, 0.04)
    defect_qty = round(quantity_produced * defect_rate)

    rows.append({
        "batch_id": batch_id,
        "product_id": product_id,
        "plant_id": plant_id,
        "production_date": production_date.isoformat(),
        "quantity_produced": quantity_produced,
        "defect_qty": defect_qty,
    })

df = pd.DataFrame(rows)
df.to_csv("production_batches.csv", index=False)
print(df.shape)
print("defect rate overall: {:.2%}".format(df["defect_qty"].sum() / df["quantity_produced"].sum()))
