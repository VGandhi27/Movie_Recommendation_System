import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=3b7e0952c7c98a2375419c824c6bb797&language=en-US".format(movie_id))
    data = response.json()
    # st.text(data)
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def fetch_homepage(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=3b7e0952c7c98a2375419c824c6bb797&language=en-US".format(movie_id))
    data2 = response.json()
    # st.text(data2)
    return data2['homepage']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]

    recommended_movies = []
    recommended_movies_posters = []
    recommended_movies_homepage = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
        # fetch homepage from API
        recommended_movies_homepage.append(fetch_homepage(movie_id))
    return recommended_movies,recommended_movies_posters,recommended_movies_homepage

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
# movies_list['title'].values

similarity = pickle.load(open('similarity.pkl','rb'))


st.title('Movie Recommender System')


selected_movie_name = st.selectbox(
'Enter the name of the Movie and also see its recommendation',
movies['title'].values)

if st.button('Enter'):
    names,posters,homepage = recommend(selected_movie_name)

    col1, col2   = st.columns(2, gap="small")
    with col1:
        st.text(names[0])
        st.image(posters[0])
        if homepage[0] == "":
            "link of the Homepage: Not Available"
        else:
            st.markdown("link of the Homepage: " + homepage[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
        if homepage[1] == "":
            "link of the Homepage: Not Available"
        else:
            st.markdown("link of the Homepage: " + homepage[1])

    with col1:
        st.text(names[2])
        st.image(posters[2])
        if homepage[2] == "":
            "link of the Homepage: Not Available"
        else:
            st.markdown("link of the Homepage: " + homepage[2])

    with col2:
        st.text(names[3])
        st.image(posters[3])
        if homepage[3] == "":
            "link of the Homepage: Not Available"
        else:
            st.markdown("link of the Homepage: " + homepage[3])

    with col1:
        st.text(names[4])
        st.image(posters[4])
        if homepage[4] == "": "link of the Homepage: Not Available"
        else:
            st.markdown("link of the Homepage: " +homepage[4]  )

    with col2:
        st.text(names[5])
        st.image(posters[5])
        if homepage[5] == "":
            "link of the Homepage: Not Available"
        else:
            st.markdown("link of the Homepage: " + homepage[5])


