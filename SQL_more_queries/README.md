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

## Author
* **Luis Gonzalez** - Holberton School
