from recommender import recommend_jobs

results = recommend_jobs(
    "python, machine learning, data analysis",
    "new york",
    "entry"
)

print("\nTop 5 Recommended Jobs:\n")

for i, job in enumerate(results, 1):
    print(f"Recommendation {i}")
    print("Job Title:", job["job_title"])
    print("Company:", job["company"])
    print("Location:", job["job_location"])
    print("Link:", job["job_link"])
    print("-" * 40)