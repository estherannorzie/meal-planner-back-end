# Meal Planner: Back-End
<p>
  <a href="https://www.python.org/">
    <img alt="Python3 badge" src="https://img.shields.io/badge/-Python3-purple"/>
  </a>
  <a href="https://pytest.org">
    <img alt="Pytest badge" src="https://img.shields.io/badge/-Pytest-blue"/>
  </a>
  <a href="https://flask.palletsprojects.com">
    <img alt="Flask badge" src="https://img.shields.io/badge/-Flask-red"/>
  </a>
  <a href="https://www.sqlalchemy.org">
    <img alt="SQLAlchemy badge" src="https://img.shields.io/badge/-SQLAlchemy-green"/>
 </a>
  <a href="https://www.postgresql.org">
    <img alt="PostgreSQL badge" src="https://img.shields.io/badge/-PostgreSQL-pink"/>
 </a>
</p>

<p>
  <details open>
    <summary>Table of Contents</summary>
    <ol>
      <li>
        <a href="#description">Description</a>
        <ul>
          <li>
            <a href="#features">Features</a>
          </li>
        </ul>
      </li>
      <li>
        <a href="#usage">Usage</a>
      </li>
      <li>
        <a href="#api-design">API Design</a>
      </li>
      <li>
        <a href="#example-usage">Example Usage</a>
      </li>
    </ol>
  </details>
</p>

## Description
A text-based, meal planner web server that allows users to create meal plans for the current day or a future day. Development has come to a halt.

## Features
- Create an account
- Delete an account
- Update account password or email address
- Create a meal plan
- Delete a meal plan
- Update a meal plan
- View all meal plans

## API Design
<details>
  <summary>Images</summary>
  <img src="./assets/meal-planner-diagram-back-end-erd.png" alt="Entity relationship diagram" />
  <br>
  <img src="./assets/meal-planner-diagram-endpoints.png" alt="Endpoint chart" />
</details>

## Requirements
- [Python3](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)
- An API platform such as [Postman](https://www.postman.com/downloads/)


## Usage
1. Clone the repository to a folder on your local machine. 

2. In your terminal, move into the root of your project directory and run the following commands to create your virtual environment.
    ```
    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ touch .env
    ```

3. Run PostgresSQL from your terminal and create a database for development and testing.
    ```
    $ CREATE DATABASE db_name;
    $ CREATE DATABASE db_test_name;
    ```

4. Copy and paste the URIs below into your `.env` file.
    ```
    SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://postgres:postgres@localhost:5432/db_name
    SQLALCHEMY_TEST_DATABASE_URI=postgresql+psycopg2://postgres:postgres@localhost:5432/db_test_name
    ```
5. Use an API platform to make requests.

## Example Usage

### Creating an account

#### Request
```json
{
  "username": "janeydoe53",
  "password": "df35f~4g*",
  "first_name": "Jane",
  "last_name": "Doe",
  "email": "therealjanedoe@email.com"
}
```

#### Response
`"User janeydoe53 successfully created."`
<hr>

### Creating a meal plan

#### Request
```json
{
  "title": "Krispy Kreme Doughnuts Original Glazed Doughnut",
  "type": 4,
  "calories": 190,
  "date": "Wed, 15 Mar 2023"
}
```

#### Response
`"Krispy Kreme Doughnuts Original Glazed Doughnut meal plan for user eggpioneer10 successfully created."`