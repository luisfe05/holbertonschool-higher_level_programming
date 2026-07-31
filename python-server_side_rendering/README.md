# Python - Server-Side Rendering

## Description
This project covers server-side rendering (SSR) in Python using Flask and the Jinja templating engine. It progresses from raw string templating, through reusable Jinja templates with includes, loops and conditionals, to dynamically rendering data pulled from JSON, CSV, and SQLite sources based on query parameters.

## Tasks

| Task | Description | File |
| :--- | :--- | :--- |
| **0. Creating a Simple Templating Program** | Write `generate_invitations(template, attendees)`, which fills a text template's placeholders per attendee and writes numbered `output_X.txt` files, with error handling for invalid/empty inputs and missing data (`N/A`). | `task_00_intro.py` |
| **1. Creating a Basic HTML Template in Flask** | Build a Flask app with `/`, `/about`, and `/contact` routes rendering Jinja templates that share a common `header.html`/`footer.html` via `{% include %}`. | `task_01_jinja.py` |
| **2. Creating a Dynamic Template with Loops and Conditions in Flask** | Add an `/items` route that reads `items.json` and renders the list with a Jinja `{% for %}` loop, showing "No items found" when empty. | `task_02_logic.py` |
| **3. Displaying Data from JSON or CSV Files in Flask** | Add a `/products` route that reads `products.json` or `products.csv` based on a `source` query parameter, optionally filters by `id`, and handles "Wrong source"/"Product not found" errors. | `task_03_files.py` |
| **4. Extending Dynamic Data Display to Include SQLite in Flask** | Extend `/products` to support `source=sql`, reading from a `products.db` SQLite database via the same `product_display.html` template. | `task_04_db.py` |

## Author
* **Luis Gonzalez** - Holberton School
