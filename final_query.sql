# Query Link https://console.cloud.google.com/bigquery?sq=563929104232:fbfbe695b73540a8b345afed91c39a0c
# Query takes the data on pizza sale over the past 12 month and output the top 3 types of pizza sold per state
CREATE OR REPLACE VIEW
  pizzaorderinspection.top3_pizza_category_by_state_12mon AS (
  SELECT
    *
  FROM (
    SELECT
      *,
      ROW_NUMBER() OVER (PARTITION BY state ORDER BY total_quantity DESC) AS top_type
    FROM
      `pizzaorderinspection.pizzasale12mon` )
  WHERE
    top_type <= 3 );