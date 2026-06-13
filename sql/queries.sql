SELECT scheme_name,
       SUM(aum) AS total_aum
FROM fact_aum
GROUP BY scheme_name
ORDER BY total_aum DESC;

SELECT
strftime('%Y-%m',date) month,
AVG(nav)
FROM fact_nav
GROUP BY month;

SELECT
year,
SUM(amount)
FROM fact_transactions
WHERE transaction_type='SIP'
GROUP BY year;

SELECT
state,
COUNT(*)
FROM fact_transactions
GROUP BY state;

SELECT *
FROM fact_performance
WHERE expense_ratio < 1;

SELECT *
FROM fact_performance
ORDER BY return_1y DESC;

SELECT *
FROM fact_performance
ORDER BY expense_ratio;

SELECT
date,
SUM(aum)
FROM fact_aum
GROUP BY date;

SELECT
SUM(amount)
FROM fact_transactions
WHERE transaction_type='REDEMPTION';

SELECT
category,
SUM(aum)
FROM fact_aum
GROUP BY category;