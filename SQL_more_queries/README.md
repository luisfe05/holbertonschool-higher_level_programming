# SQL - More Queries

## Description
This directory contains tasks for working with advanced SQL features, user management, granting database permissions, setting primary/foreign key constraints, using `NOT NULL` and `UNIQUE` constraints, performing various types of `JOIN` queries, and working with subqueries and `UNION` clauses in MySQL 8.0.

## Tasks

| Task | Description | Source Code / File |
| --- | --- | --- |
| **0. My privileges!** | Script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on localhost. | [0-privileges.sql](./0-privileges.sql) |
| **1. Root user** | Script that creates the user `user_0d_1` with all privileges and password `user_0d_1_pwd`. | [1-create_user.sql](./1-create_user.sql) |
| **2. Read user** | Script that creates database `hbtn_0d_2` and user `user_0d_2` with `SELECT` privilege. | [2-create_read_user.sql](./2-create_read_user.sql) |
| **3. Always a name** | Script that creates the table `force_name` with a `NOT NULL` `name` column. | [3-force_name.sql](./3-force_name.sql) |
| **4. ID can't be null** | Script that creates the table `id_not_null` with `id` defaulting to `1`. | [4-never_empty.sql](./4-never_empty.sql) |
| **5. Unique ID** | Script that creates the table `unique_id` with a default `1` and `UNIQUE` constraint on `id`. | [5-unique_id.sql](./5-unique_id.sql) |
| **6. States table** | Script that creates database `hbtn_0d_usa` and table `states` with `AUTO_INCREMENT` `PRIMARY KEY`. | [6-states.sql](./6-states.sql) |
| **7. Cities table** | Script that creates database `hbtn_0d_usa` and table `cities` with `FOREIGN KEY` referencing `states(id)`. | [7-cities.sql](./7-cities.sql) |
| **8. Cities of California** | Script that lists all cities of California using a subquery (without `JOIN`). | [8-cities_of_california_subquery.sql](./8-cities_of_california_subquery.sql) |
| **9. Cities by States** | Script that lists all cities with their respective state names using a `JOIN`. | [9-cities_by_state_join.sql](./9-cities_by_state_join.sql) |
| **10. Genre ID by show** | Script that lists all TV shows with at least one genre linked. | [10-genre_id_by_show.sql](./10-genre_id_by_show.sql) |
| **11. Genre ID for all shows** | Script that lists all TV shows including those without a genre using `LEFT JOIN`. | [11-genre_id_all_shows.sql](./11-genre_id_all_shows.sql) |
| **12. No genre** | Script that lists all TV shows without a genre linked using `LEFT JOIN` and `WHERE IS NULL`. | [12-no_genre.sql](./12-no_genre.sql) |
| **13. Number of shows by genre** | Script that lists all genres and the number of shows linked to each. | [13-count_shows_by_genre.sql](./13-count_shows_by_genre.sql) |
| **14. My genres** | Script that lists all genres of the show Dexter using joins. | [14-my_genres.sql](./14-my_genres.sql) |
| **15. Only Comedy** | Script that lists all Comedy shows using joins. | [15-comedy_only.sql](./15-comedy_only.sql) |

## Author
* **Luis Gonzalez** - Holberton School
