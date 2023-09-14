import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

movies = pickle.load(open("movies_list.pk1", 'rb'))
similarity = pickle.load(open("similarity.pk1", 'rb'))
movies_list = movies['title'].values

st.header("Movie Recommender System")

import streamlit.components.v1 as components

imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")

imageUrls = [
    fetch_poster(1632),
    fetch_poster(299536),
    fetch_poster(17455),
    fetch_poster(2830),
    fetch_poster(429422),
    fetch_poster(9722),
    fetch_poster(13972),
    fetch_poster(240),
    fetch_poster(155),
    fetch_poster(598),
    fetch_poster(914),
    fetch_poster(255709),
    fetch_poster(572154)
]

imageCarouselComponent(imageUrls=imageUrls, height=200)

select_value = st.selectbox("Select a movie from the dropdown", movies_list)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommend_movie = []
    recommend_poster = []
    for i in distance[1:6]:
        movie_id = movies.iloc[i[0]]['id']
        recommend_movie.append(movies.iloc[i[0]]['title'])
        recommend_poster.append(fetch_poster(movie_id))
    return recommend_movie, recommend_poster

if st.button("Show Recommendations"):
    movie_names, movie_posters = recommend(select_value)
    cols = st.columns(5)
    for i, col in enumerate(cols):
        col.text(movie_names[i])
        col.image(movie_posters[i])
