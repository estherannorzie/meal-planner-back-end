# Meal Planner iOS: Back-end

Meal Planner iOS is a capstone project created during Ada Developers Academy, cohort 17. Users can create a meal plan for the current day or for a future day.

## Features
- Create an account
- Delete an account
- Update account password or email address
- Create a meal plan
- Delete a meal plan
- Update a meal plan
- View all meal plans

## API Design
![Entity relationship diagram](/assets/meal-planner-diagram-back-end-erd.png)

## Technologies
- Python3
- Flask
- SQLAlchemy
- PostgreSQL

## Prerequisites
- [Python3](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)
- An API Testing client such as [Postman](https://www.postman.com/downloads/)


## Usage
1. Clone the repository to a folder on your local machine. 
2. In your terminal, move into your project directory and run the following commands to create your virtual environment.
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
3. Create a configuration text file at the root of the project directory.
```
$ touch .env
```
4. Run PostgresSQL from your terminal and create a database for development and testing.
```
CREATE DATABASE db_name;
CREATE DATABASE db_test_name;
```

5. Navigate to the project directory’s ```.env``` file and configure the development and test databases .
```
SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://postgres:postgres@localhost:5432/db_name
SQLALCHEMY_TEST_DATABASE_URI=postgresql+psycopg2://postgres:postgres@localhost:5432/db_test_name
```
6. Use an API testing client to make requests.
