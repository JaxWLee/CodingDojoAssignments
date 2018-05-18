-- Problem 1
SELECT customer.first_name, customer.last_name, customer.email, address.address FROM customer
JOIN address ON address.address_id = customer.address_id
JOIN city on city.city_id = address.city_id
WHERE city.city_id = 312;

-- Problem 2
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre FROM film
JOIN film_category ON film_category.film_id = film.film_id
JOIN category ON category.category_id = film_category.category_id
WHERE category.name = 'Comedy';

-- Problem 3
SELECT actor.actor_id, concat_ws(' ',actor.first_name,actor.last_name) AS actor_name, film.title, film.description, film.release_year FROM film
JOIN film_actor ON film_actor.film_id = film.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE actor.actor_id = 5;

-- Problem 4
SELECT customer.first_name, customer.last_name, customer.email, address.address FROM customer
JOIN address on address.address_id = customer.address_id
JOIN city on city.city_id = address.city_id
JOIN store on store.store_id = customer.store_id
WHERE store.store_id = 1 AND city.city_id IN (1, 42, 312,459);

-- Problem 5 
SELECT film.title, film.description, film.release_year, film.rating, film.special_features from film
JOIN film_actor ON film_actor.film_id = film.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE film.rating = 'G' and film.special_features LIKE '%Behind the scenes%' and actor.actor_id = 15;

-- Problem 6
SELECT film.film_id,film.title, actor.actor_id, concat_ws(' ', actor.first_name, actor.last_name) AS actor_name from film
JOIN film_actor ON film_actor.film_id = film.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE film.film_id = 369; 

-- Problem 7
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre, film.rental_rate FROM film
JOIN film_category ON film_category.film_id = film.film_id
JOIN category ON category.category_id = film_category.category_id
WHERE film.rental_rate = 2.99 and category.name = 'Drama';

-- Problem 8
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre, actor.first_name, actor.last_name FROM film
JOIN film_category ON film_category.film_id = film.film_id
JOIN category ON category.category_id = film_category.category_id
JOIN film_actor ON film_actor.film_id = film.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE category.name = 'Action' AND concat_ws(' ',actor.first_name, actor.last_name) LIKE 'SANDRA KILMER';