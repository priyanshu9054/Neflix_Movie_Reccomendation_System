Introduction
This project aims to provide personalized movie recommendations on Netflix using cosine similarities. The recommendation system utilizes the concept of cosine similarity to identify movies that are most similar to a user's preferences.

Dataset: Dataset was downloaded from kaggle

Usage
Run the Recommendation System:

Beegin with extracting all folders and files in a single dictionary/folder and when you try to run it on your studio make sure you have opened up the extactted folder on your studio
open main.py
Copy code
streamlit run main.py
User Input:
Enter the name of a movie you like when prompted. The system will use cosine similarities to recommend movies based on your input.

Algorithm
The recommendation system uses the following steps:

Data Preprocessing:

Load the Netflix movie dataset.
Handle missing values and clean the data.
Feature Extraction:

Utilize natural language processing techniques to convert movie descriptions into numerical vectors.
Cosine Similarity Calculation:

Compute the cosine similarity between the vectorized movie descriptions to identify similar movies.
User Interaction:

Prompt the user to input their favorite movie.
Recommendation Generation:

Based on the user's input, recommend a list of movies with high cosine similarity.
Example
bash
Copy code
Enter the name of a movie you like: Inception
Recommended Movies:

1. The Matrix
2. Interstellar
3. Shutter Island
4. The Dark Knight
5. Blade Runner 2049
