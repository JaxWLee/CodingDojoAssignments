-- Problem 1:
SELECT name,language,percentage FROM countries
JOIN languages ON languages.country_id = countries.id
WHERE countries.id in (SELECT country_id FROM languages WHERE language = 'Slovene') AND language = 'Slovene'
ORDER BY percentage DESC;

-- Problem 2:
SELECT countries.name,COUNT(cities.name) FROM countries
JOIN cities ON cities.country_id = countries.id
GROUP BY countries.name
ORDER BY count(cities.name) DESC;

-- Problem 3:
SELECT cities.name, cities.population FROM countries
JOIN cities on cities.country_id = countries.id
WHERE countries.name = 'Mexico' and cities.population > 500000
ORDER BY cities.population DESC;

-- Problem 4:
SELECT countries.name, languages.language, languages.percentage FROM countries
JOIN languages ON languages.country_id = countries.id
WHERE languages.percentage >= 89.0
ORDER BY languages.percentage DESC;

-- Problem 5:
SELECT name FROM countries
WHERE surface_area <= 501 AND population > 100000;

-- Problem 6:
SELECT name FROM countries
WHERE government_form = 'Constitutional Monarchy' AND capital > 200 AND life_expectancy > 75.0;

-- Problem 7:
SELECT countries.name, cities.name, cities.district, cities.population FROM countries
JOIN cities ON cities.country_id = countries.id
WHERE countries.name = 'Argentina' AND cities.district = 'Buenos Aires' AND cities.population > 500000
ORDER BY cities.population DESC;

-- Problem 8:
SELECT region, COUNT(name) FROM countries
GROUP BY region
ORDER BY count(name) DESC;