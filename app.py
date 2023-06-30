import streamlit as st
import pickle
import pandas as pd
import bz2


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

ifile = bz2.BZ2File("similarity11",'rb')
similarity = pickle.load(ifile)
ifile.close()

st.title('Movie Recommendation System')

movie_name = st.selectbox('Select Movie', movies['title'].values)

if st.button('Recommend Movies'):
    recommendations = recommend(movie_name)
    for i in recommendations:
        st.write(i)
