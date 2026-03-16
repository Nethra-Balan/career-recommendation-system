from flask import Flask, request, jsonify
from flask_cors import CORS
from recommender import recommend_jobs

app = Flask(__name__)
CORS(app)

# HOME ROUTE
@app.route("/")
def home():
    return "Job Recommendation API Running"

# RECOMMENDATION ROUTE
@app.route("/recommend", methods=["POST"])
def recommend():

    data = request.json

    skills = data.get("skills", "")
    location = data.get("location", "")
    level = data.get("level", "")

    jobs = recommend_jobs(skills, location, level)

    return jsonify(jobs)

if __name__ == "__main__":
    app.run(debug=True)