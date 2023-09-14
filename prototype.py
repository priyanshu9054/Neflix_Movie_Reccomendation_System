import  streamlit as st

import pickle
import pandas as pd
import requests

st.title('Movie Recommender System')


#url = "https://api.themoviedb.org/3/movie/{}?api_key='YOUR API KEY'&language=en-US".format(movie_id)
    #data = requests.get(url)
   # data = data.json()
  #   full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#    return full_path

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    #recommended_movie_posters = []

    for i in movies_list:
        # fetch the movie poster
        movie_name = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
       # recommended_movie_posters.append(fetch_poster(movie_id))

    return recommended_movies,#recommended_movie_posters

movies_dict = pickle.load(open('movies_list.pk1','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pk1','rb'))


selected_movie_name = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values
)
if st.button("Show Recommend"):
    movie_name=recommend(selected_movie_name)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(movie_name[0])
    with col2:
        st.text(movie_name[1])
    with col3:
        st.text(movie_name[2])
    with col4:
        st.text(movie_name[3])
    with col5:
        st.text(movie_name[4])