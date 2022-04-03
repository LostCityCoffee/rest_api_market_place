from flask import Flask, jsonify, request
from market_place.model.project import Project, ProjectSchema
from market_place.model.offer import OfferSchema
import datetime as dt

app = Flask(__name__)

all_projects = []


# Route to get projects by id
@app.route("/projects/<string:pk>")
def get_project_by_id(pk):
    for project in all_projects:
        if str(project.id) == pk:
            schema = ProjectSchema(many=False)
            return jsonify(schema.dump(project)), 200
    return "There is no project with id=" + pk, 404


# Route to get all listed projects
@app.route("/projects")
def get_projects():
    schema = ProjectSchema(many=True)
    projects = schema.dump(all_projects)
    return jsonify(projects), 200


# Route to post a new project
@app.route('/projects', methods=['POST'])
def add_project():
    schema = ProjectSchema(many=False)
    project = ProjectSchema().load(request.get_json())
    newProject = Project(project["description"], project["requirements"],
                        project["max_budget"], project["bids_deadline"], project["owner"])
    all_projects.append(newProject)
    return jsonify(schema.dump(newProject)), 200


# Route to post a new offer
@app.route('/offer', methods=['POST'])
def bid_to_project():
    schema = OfferSchema(many=False)
    offer = OfferSchema().load(request.get_json())
    for project in all_projects:
        print(project.id)
        print(offer.project_id)
        if str(project.id) == str(offer.project_id):
            if dt.datetime.now() < project.bids_deadline:
                project.assign_better_offer(offer)
                return jsonify(schema.dump(offer)), 200 
            else:
                return "Deadline ended for submitting a bid.", 200
    return "There is no object with id = " + str(offer.project_id), 404


if __name__ == '__main__':
    app.run(debug=True)

