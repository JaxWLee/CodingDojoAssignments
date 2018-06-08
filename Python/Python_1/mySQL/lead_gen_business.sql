-- Problem 1
SELECT SUM(amount) as March_2012_revenue FROM billing
WHERE charged_datetime like '2012-03%';

-- Problem 2
SELECT SUM(amount), client_id as client_2_revenue FROM billing
WHERE client_id = 2;

-- Problem 3
SELECT domain_name, client_id FROM sites
WHERE client_id = 10;

-- Problem 4
SELECT client_id, COUNT(site_id),YEAR(created_datetime), MONTHNAME(created_datetime) FROM sites
WHERE client_id = 1 
GROUP BY YEAR(created_datetime), MONTH(created_datetime)
ORDER BY YEAR(created_datetime), MONTH(created_datetime);
SELECT client_id, COUNT(site_id),YEAR(created_datetime), MONTHNAME(created_datetime) FROM sites
WHERE client_id = 20 
GROUP BY YEAR(created_datetime), MONTH(created_datetime)
ORDER BY YEAR(created_datetime), MONTH(created_datetime);

-- Problem 5
SELECT site_id, count(leads_id) FROM leads
WHERE YEAR(registered_datetime),MONTHNAME(registered_datetime),DAY(registered_datetime) IN ('2011 January ,'2011-02-15')