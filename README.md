# rest_api_market_place
The marketplace allows employers to post jobs, while prospective self-employed can bid for projects.

1. Clone(fork) the project.
2. Using the terminal in the main folder run "pip install -r requirements.txt".
3. Use "python app.py" to run the application on "http://localhost:5000/".
4. Using Postman a new project can be created sending a post request to "http://localhost:5000/projects". Providing the following attributes on a JSON format: "description": "string", "requirements": "string", "max_budget": number, "bids_deadline": "AAAA-MM-DD HH:MM:SS", and "owner": "string".
5. Using Postman a new offer can be created sending a post request to "http://localhost:5000/offer". Providing the following attributes on a JSON format: "project_id": "string", "price": number, "seller": "string".

The application was runned using:
-python 3.8.9
-flask 1.0.2
-marshmallow 3.14.1
-requests 2.27.1
-pytest 7.1.1
