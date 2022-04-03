# rest_api_market_place
The marketplace allows employers to post jobs, while prospective self-employed can bid for projects.

Steps for using the application:
1. Clone(fork) the project.
2. Using the terminal on the main folder run "pip install -r requirements.txt".
3. Using the terminal on the main folder, "python app.py" run the application on "http://localhost:5000/".
4. Using Postman a new project can be created sending a post request to "http://localhost:5000/projects". Providing the following attributes on a JSON format: "description": "string", "requirements": "string", "max_budget": number, "bids_deadline": "AAAA-MM-DD HH:MM:SS", and "owner": "string".
5. Using Postman a new offer can be created sending a post request to "http://localhost:5000/offer". Providing the following attributes on a JSON format: "project_id": "string", "price": number, "seller": "string".

Application notes:
1. Once an user submits a bid it automatically calculates the best offer and display it on the "lowest_bid_amount" field.
2. No bids can be submitted after the deadline expires.
3. The Buyer with the lowest bid automatically wins the bid when the deadline is reached. 
4. About the autobid feature, an offer is considered auto_bid if it has a min_price to accept otherwise it is a manual offer.
5. For running the tests open the terminal on the "tests" folder and run "pytest test_api.py".

The following tests can be run:
1. Test for getting all listed projects.
2. Test for creating a new project.
3. Test for posting an offer. 

The application was tested using:
1. python 3.8.9
2. flask 1.0.2
3. marshmallow 3.14.1
4. requests 2.27.1
5. pytest 7.1.1
