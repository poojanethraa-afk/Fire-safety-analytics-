import pandas as pd
import random
from datetime import date, timedelta

random.seed(7)

product_ids = list(range(1, 25))
industry_ids = list(range(1, 17))

# weight some industries to order more often — logistics centers, data centers,
# automotive plants are exactly the kind of high-fire-risk, high-throughput sites
# that would order fire protection systems more frequently
industry_weights = {i: 1.0 for i in industry_ids}
industry_weights[10] = 3.0   # Logistic centers
industry_weights[13] = 2.5   # Data Center
industry_weights[1] = 2.0    # Automotive plants
industry_weights[3] = 1.8    # Aluminium and Steel plants
industry_weights[6] = 1.5    # Combined cycle power plants

industries_list = list(industry_weights.keys())
industry_w = list(industry_weights.values())

countries = ["Germany", "Belgium", "Netherlands", "France", "Poland",
             "Austria", "Singapore", "United Kingdom", "Italy", "Sweden"]
# a couple of countries get slower/less reliable logistics on purpose
slow_countries = {"Singapore", "Sweden"}

N_ROWS = 420
END_DATE = date(2026, 8, 14)
START_DATE = END_DATE - timedelta(days=18 * 30)

# a few product_ids get flagged as "problem products" with worse on-time rates
problem_products = {9, 15, 21}  # arbitrary but consistent products

rows = []
for order_id in range(1, N_ROWS + 1):
    product_id = random.choice(product_ids)
    industry_id = random.choices(industries_list, weights=industry_w, k=1)[0]
    destination_country = random.choice(countries)

    order_days_offset = random.randint(0, (END_DATE - START_DATE).days - 30)
    order_date = START_DATE + timedelta(days=order_days_offset)

    lead_time = random.randint(10, 25)
    requested_ship_date = order_date + timedelta(days=lead_time)

    # base on-time probability ~88%, worse for problem products and slow countries
    on_time_prob = 0.88
    if product_id in problem_products:
        on_time_prob -= 0.25
    if destination_country in slow_countries:
        on_time_prob -= 0.15

    if random.random() < on_time_prob:
        delay_days = random.randint(-3, 0)  # on time or a bit early
    else:
        delay_days = random.randint(1, 12)  # late

    actual_ship_date = requested_ship_date + timedelta(days=delay_days)

    quantity = random.randint(1, 40)

    rows.append({
        "order_id": order_id,
        "product_id": product_id,
        "industry_id": industry_id,
        "order_date": order_date.isoformat(),
        "requested_ship_date": requested_ship_date.isoformat(),
        "actual_ship_date": actual_ship_date.isoformat(),
        "quantity": quantity,
        "destination_country": destination_country,
    })

df = pd.DataFrame(rows)
df.to_csv("orders.csv", index=False)

on_time = (pd.to_datetime(df["actual_ship_date"]) <= pd.to_datetime(df["requested_ship_date"])).mean()
print(df.shape)
print("overall on-time rate: {:.1%}".format(on_time))
