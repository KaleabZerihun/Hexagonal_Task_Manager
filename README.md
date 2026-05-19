# Hexagonal Architecture To-Do App

This project is a simple To-Do application built with Django using Hexagonal Architecture, also known as Ports and Adapters Architecture. The main goal of this app was to organize the code in a clean way by separating the business logic from the database, web framework, and user interface.

The app allows users to create, view, update, complete, and delete tasks. It also includes logic for handling overdue tasks, so users can easily see which tasks need attention.

We built this project to better understand how software architecture can make an application easier to maintain, test, and expand. Instead of putting all the logic directly inside Django views or models, the project separates responsibilities into different layers. This makes the app more flexible because the core task logic can work independently from Django or the database.

## Features

- Create new tasks
- View all tasks
- Mark tasks as completed
- Edit existing tasks
- Delete tasks
- Track overdue tasks
- Organized using Hexagonal Architecture
- Built with Django and SQLite

## Why We Built This App

We built this app to demonstrate how Hexagonal Architecture works in a real project. A normal Django project can become hard to manage when the business logic, database code, and web logic are all mixed together.

Using Hexagonal Architecture helped us separate the main task logic from the outside tools. This made the project cleaner, easier to understand, and easier to test. It also showed how a small app can still use strong software architecture principles.

## Technologies Used

- Python
- Django
- SQLite
- HTML/CSS
- Hexagonal Architecture

## How to Run

To run this project run the following in the command line after you clone the project:

- `cd hex_todo`
- `python -m venv venv`
- `venv\Scripts\activate`
- `pip install django`
- `python manage.py runserver`
