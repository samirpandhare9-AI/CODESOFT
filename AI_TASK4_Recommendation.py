import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# A. Prepare the Data (Creating a small sample dataset)
# 1 = liked/watched, 0 = not liked/watched
data = {
    'User': ['A', 'B', 'C', 'D'],
    'Movie1': [1, 0, 1, 0],
    'Movie2': [0, 1, 1, 0],
    'Movie3': [1, 1, 0, 1],
    'Movie4': [0, 1, 0, 1],
}

# Convert the dictionary into a Pandas DataFrame
df = pd.DataFrame(data)
df = df.set_index('User') # Set 'User' as the row index

# B. Calculate User Similarity
# Use Cosine Similarity to find how similar users are to each other
user_similarity = cosine_similarity(df)
user_similarity_df = pd.DataFrame(user_similarity, index=df.index, columns=df.index)

# C. Define the Recommendation Function
def recommend_movies(user_id, df_similarity, df_data):
    
    # 1. Identify the target user's position
    target_user_index = df_data.index.get_loc(user_id)
    
    # 2. Get similarity scores of the target user with all others
    similar_users = df_similarity.iloc[target_user_index]
    
    # 3. Find movies the target user has NOT watched (where rating is 0)
    unwatched_movies = df_data.loc[user_id][df_data.loc[user_id] == 0].index.tolist()
    
    recommendations = {}
    
    # 4. Calculate a score for each unwatched movie
    for movie in unwatched_movies:
        score = 0
        total_similarity = 0
        
        # Look at other users to see if they liked this unwatched movie
        for user in df_data.index:
            if user != user_id and df_data.loc[user, movie] == 1:
                # Add the similarity score if the other user liked the movie
                score += similar_users[user]
                total_similarity += similar_users[user]
        
        if total_similarity > 0:
            recommendations[movie] = score / total_similarity
            
    # 5. Recommend the movie with the highest calculated score
    if recommendations:
        return max(recommendations, key=recommendations.get)
    else:
        return "No recommendations available at the moment."

# D. Test the Model
user_to_recommend = 'A'
recommended_movie = recommend_movies(user_to_recommend, user_similarity_df, df)

print(f"Data watched by User {user_to_recommend}:\n{df.loc[user_to_recommend]}")
print("\n--- Recommendation Result ---")
print(f"The recommended movie for User {user_to_recommend} is: {recommended_movie}")