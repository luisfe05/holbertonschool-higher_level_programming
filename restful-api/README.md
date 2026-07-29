# Python - RESTful API

## Description
This directory contains tasks for exploring RESTful API concepts, understanding fundamental web protocols (HTTP/HTTPS), testing network requests using command-line tools like `curl`, consuming external API endpoints with Python's `requests` module, constructing custom web servers using standard Python libraries, developing REST APIs with Flask, and implementing API security techniques (Basic Auth, JWT, and Role-Based Access Control).

## Tasks

| Task | Description | Source Code / File |
| --- | --- | --- |
| **0. Basics of HTTP/HTTPS** | Overview of HTTP vs HTTPS, request/response structures, common HTTP methods (GET, POST, PUT, DELETE), and status code categories. | *Conceptual / Documentation* |
| **1. Consume data from an API using command line tools (curl)** | Commands and techniques for using `curl` to send GET/POST requests, view response headers, and inspect API endpoints. | *Command-line Interface (curl)* |
| **2. Consuming and processing data from an API** | Fetch posts from JSONPlaceholder using Python's `requests` library, print response details, and save formatted post data into a CSV file. | [task_02_requests.py](./task_02_requests.py) |
| **3. Develop a simple API using http.server** | Implement a custom HTTP web server using Python's `http.server` module to serve plain text, JSON data, status endpoints, and handle 404 errors. | [task_03_http_server.py](./task_03_http_server.py) |
| **4. Develop a Simple API using Python with Flask** | Create a RESTful web server using Flask with endpoints for retrieving users, checking status, handling dynamic routes, and adding users via POST requests. | [task_04_flask.py](./task_04_flask.py) |
| **5. API Security and Authentication Techniques** | Secure API endpoints using Basic Authentication (`Flask-HTTPAuth`), JSON Web Tokens (`Flask-JWT-Extended`), custom error handlers, and Role-Based Access Control (RBAC). | [task_05_basic_security.py](./task_05_basic_security.py) |

## Author
* **Luis Gonzalez** - Holberton School
