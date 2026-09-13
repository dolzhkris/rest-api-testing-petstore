# rest-api-testing-petstore
Python REST API testing for user operations using the Swagger Petstore API.

## About

The following HTTP methods are used:
* POST - create a user;
* GET - retrieve user information;
* PUT - update user information;
* DELETE - delete a user.
The project uses the Python requests library to send HTTP requests and process API responses.

The project was developed as part of university work during the third year of university.

## Key Variables

* BASE_URL - base URL of the Swagger Petstore API;
* USERNAME - username of the test user;
* user_data - data used to create the user;
* updated_data - updated user information;
* response - API response returned by the server;
* id - user identifier;
* firstName - user's first name;
* lastName - user's last name;
* email - user's email address;
* password - user's password;
* phone - user's phone number;
* userStatus - user status value.

## How to Run

1. Clone the repository

```bash
git clone https://github.com/dolzhkris/rest-api-testing-petstore.git
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the Python script

```bash
python main.py
```

The responses returned by the API are displayed in the console.
