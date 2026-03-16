import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load datasets
jobs_df = pd.read_csv("data/linkedin_job_postings.csv")
skills_df = pd.read_csv("data/job_skills.csv")

# Merge datasets
merged_df = pd.merge(
    jobs_df,
    skills_df,
    on="job_link",
    how="inner"
)

# Fill missing values
merged_df["company"] = merged_df["company"].fillna("unknown_company")
merged_df["job_location"] = merged_df["job_location"].fillna("unknown_location")
merged_df["job_skills"] = merged_df["job_skills"].fillna("")

# Lowercase
merged_df["job_skills"] = merged_df["job_skills"].str.lower()
merged_df["job_location"] = merged_df["job_location"].str.lower()

# TF-IDF only on skills
vectorizer = TfidfVectorizer(max_features=5000)
vectorizer.fit(merged_df["job_skills"])


def recommend_jobs(user_skills, user_location, user_level, top_n=5):

    user_skills = user_skills.lower().replace(",", " ")
    user_location = user_location.lower()

    # Filter by location
    filtered_jobs = merged_df[
        merged_df["job_location"].str.contains(user_location, na=False)
    ]

    if filtered_jobs.empty:
        return []

    # Transform skills
    user_vector = vectorizer.transform([user_skills])
    job_vectors = vectorizer.transform(filtered_jobs["job_skills"])

    similarity = cosine_similarity(user_vector, job_vectors)

    top_indices = similarity.argsort()[0][-top_n:][::-1]

    results = filtered_jobs.iloc[top_indices][
        ["job_title", "company", "job_location", "job_link"]
    ]

    return results.to_dict(orient="records")