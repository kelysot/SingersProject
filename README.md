#  Favorite Singers Application

This is a backend project designed to allows users to browse and review singers. 

It provides a REST API for submit reviews for various singer, user authentication, and various other essential functionalities. 

This project is built with Python, FastAPI, and SQLite.


## Features

- User AuthN & AuthZ with JWT (JSON Web Tokens)
- REST API architecture for handling HTTP requests
- Database connectivity to SQLite using SQLAlchemy ORM

## Technologies 

- *Flask*: A web framework written in Python for building web applications.
- *SQLAlchemy*: An SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- *HTML/CSS*: For structuring and styling the web application's frontend.


## Prerequisites

Before running the project, ensure you have the following prerequisites installed and set up:

- Python 3
- pip

## Installation

1. Clone the repository:
   ```bash
      git clone https://github.com/kelysot/SingersFlaskProject.git

2. Create a python virtual environment
   ```bash
      python3 -m venv ./venv

3. Open the virtual environment
   - On Windows:
     ```bash
     .\venv\Scripts\activate

   - On Unix or MacOS:
     ```bash
      source ./venv/bin/activate
   
4. Install the required dependencies:
   ```bash
      pip install -r ./requirements.txt
5. Run flask app


## API Endpoints

For all types of users:

- `/register/` - User registration 
- `/login/` - User login 
- `/logout/` - User logout

For singers:
- `/` - Get all singers
- `/singer_details/<singer_id>/` - Get singer details
- `/add_singer/` - Create a new singer

For comments:
- `/singer/<int:singer_id>/add_comment/` - Create a new comment
