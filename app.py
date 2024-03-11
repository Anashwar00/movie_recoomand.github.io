import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?language=en-US&api_key=1d5be8e1523e05cb5048d8d2810e6c5e'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/original/"+data['poster_path']

movies=pickle.load(open('movie.pkl','rb'))
movie_list=movies['title'].values

similar=pickle.load(open('similar.pkl','rb'))
#making recommend function
def recommend(movie):    
    index_movie=movies[movies['title']==movie].index[0]
    distance=sorted(enumerate(similar[index_movie]),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movie=[]
    recommended_poster=[]
    for i in distance:

        movie_id=movies.iloc[i[0]]['movie_id']
        recommended_poster.append(fetch_poster(movie_id))

        recommended_movie.append(movies.iloc[i[0]]['title'])
    return recommended_movie,recommended_poster



st.title("Movie Recommender System")
selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    (movie_list))

#button
# st.button("Recommend", type="primary")


if st.button('Recommend'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

