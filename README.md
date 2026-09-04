# Fire Safety Analytics

A SQL database + Power BI dashboard project analyzing product catalog, production quality, and logistics data for a fire-safety equipment company scenario.

Built as a portfolio project to demonstrate an end-to-end data analyst workflow: raw data → a normalized PostgreSQL database → SQL queries for key business metrics → an interactive Power BI dashboard.

## What this project shows

- **Database design**: 8 tables in PostgreSQL, covering a product catalog (categories, products, industries, sectors) and operational data (production batches, orders, inventory).
- **SQL**: 9+ queries covering core reporting patterns — joins, `GROUP BY` + aggregates, `HAVING`, subqueries, and window functions.
- **Power BI dashboard**: 3 pages — Catalog Overview, Production & Quality, and Logistics & Delivery — with DAX measures, a working slicer, and multiple chart types chosen to fit the question being asked (bar for category comparisons, line for trends, cards for headline numbers).
- **Synthetic data generation**: Python scripts that generate realistic operational data (production batches, orders, inventory snapshots) with deliberately built-in patterns — a quality spike at one plant, slower delivery to specific countries, and products with recurring stockout risk — so the dashboard has real, explainable findings to surface, not just random numbers.

## Data

- **Catalog data** (`data/categories.csv`, `products.csv`, `sectors.csv`, `industries.csv`): a realistic fire-safety product catalog and customer-industry structure, modeled on how a fire protection equipment company organizes its technology categories and the industries it serves (automotive, logistics, data centers, hospitals, and similar).
- **Operational data** (`data/production_batches.csv`, `orders.csv`, `inventory_snapshots.csv`): synthetic data generated with the scripts in `scripts/`, simulating production quality, order fulfillment, and inventory levels across three plants over ~18-20 months.

## Repo structure

```
data/       CSV source data (catalog + generated operational data)
scripts/    Python scripts that generate the operational data
sql/        Database schema (schema.sql) and the individual KPI queries
dashboard/  Power BI file (.pbix)
```

## Key SQL queries

| File | What it answers |
|---|---|
| `on_time_by_country.sql` | On-time delivery rate by destination country |
| `on_time_by_product.sql` | On-time delivery rate by product |
| `defect_rate_by_plant.sql` | Defect rate by production plant |
| `defect_rate_by_category.sql` | Defect rate by product category |
| `production_by_plant.sql` | Total units produced per plant |
| `lead_time.sql` | Average lead time between order and shipment |
| `orders_by_industry.sql` | Order volume by customer industry |
| `monthly_order_trend.sql` | Order volume trend over time |
| `stockout_risk.sql` | Products currently below their reorder threshold |

## Dashboard findings (from the synthetic data)

- One product at one plant showed a sharp, temporary defect-rate spike in a single month — surfaced clearly by the trend chart, with the underlying cause traceable to that specific batch.
- On-time delivery is noticeably worse for two specific destination countries than for the rest — a realistic distance-driven logistics pattern.
- Three specific products show a recurring pattern of dipping below their reorder threshold across many months, pointing to a systemic reorder-level issue rather than a one-off event.

## Tech stack

PostgreSQL · Python (pandas) · Power BI (DAX, Power Query)

## How to run it

1. Create a PostgreSQL database and run `sql/schema.sql` to create the tables.
2. Load the CSVs in `data/` into their matching tables.
3. Open `dashboard/fire_safety_analytics_dashboard.pbix` in Power BI Desktop and point the data source at your local database.
