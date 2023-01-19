#Query Link: https://console.cloud.google.com/bigquery?sq=563929104232:477a81d886664ddfb495172503bee7e1
#Query aggregates order table into sale statistics

SELECT
  *
FROM
  EXTERNAL_QUERY("torqatapizzageorge-374705.us.pizzaorderquery",
    """SELECT state, type,
    SUM(quantity) AS total_quantity,
    SUM(quantity * price) AS gross_sale,
    SUM(quantity * price) / (SELECT population FROM states
                            WHERE states.state = orders.state)
    AS gross_sale_per_capita,
    COUNT(DISTINCT customer_id) AS unique_customers
    FROM orders
    WHERE EXTRACT(YEAR FROM AGE(NOW(), order_time)) < 1
    GROUP BY state, type""");