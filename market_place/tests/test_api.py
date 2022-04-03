import requests
import json


# Test for getting all listed projects
def test_empty_db():
    response = requests.get('http://127.0.0.1:5000/projects')
    assert 200 == response.status_code

# Test for creating a new project
def test_post_project():
    requests.post('http://127.0.0.1:5000/projects', json={"description": "project_description",
                                                          "requirements": "project_requirements", "max_budget": 10, "bids_deadline": "2022-05-17 20:57:00",
                                                          "owner": "kevin"})
    response = requests.get('http://127.0.0.1:5000/projects')
    data = json.loads(response.content)
    first_project_id = data[0]['id']
    response2 = requests.get('http://127.0.0.1:5000/projects/' + str(first_project_id))
    assert 200 == response2.status_code

# Test for posting an offer 
def test_post_offer():
    response = requests.get('http://127.0.0.1:5000/projects')
    data = json.loads(response.content)
    firstprojectID = data[0]['id']     
    response2 = requests.post('http://127.0.0.1:5000/offer', json={
     "project_id": firstprojectID, "price": 7, "seller": "best_seller"})
    response3 = requests.get('http://127.0.0.1:5000/projects/' + str(firstprojectID))
    data3 = json.loads(response3.content)
    assert data3['lowest_bid_amount'] != 0
    assert 200 == response2.status_code


