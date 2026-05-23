import streamlit as st
import pickle
import pandas as pd
import requests

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="BingeBuddy",
    page_icon="🎬",
    layout="wide"
)

# ---------------- BACKGROUND IMAGE ----------------

st.markdown("""
<style>

.stApp {
    background-image: linear-gradient(
        rgba(0,0,0,0.8),
        rgba(0,0,0,0.8)
    ),
    url('https://wallpapercave.com/wp/wp1945897.jpg');

    background-size: cover;
    background-attachment: fixed;
}

/* title */

h1 {
    text-align: center;
    color: white;
    font-size: 55px;
}

/* movie cards */

.movie-card {
    background-color: #1e1e1e;
    padding: 15px;
    border-radius: 18px;
    text-align: center;
    transition: 0.3s;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.5);
}

.movie-card:hover {
    transform: scale(1.05);
}

.movie-card img {
    border-radius: 12px;
}

/* buttons */

.stButton > button {
    width: 100%;
    border-radius: 12px;
    height: 3em;
    background-color: #E50914;
    color: white;
    font-size: 18px;
    border: none;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #ff4b4b;
    transition: 0.3s;
}

/* selectbox */

div[data-baseweb="select"] > div {
    background-color: #1e1e1e;
    color: white;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOAD DATA ----------------

movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open("similarity.pkl", "rb"))

# ---------------- FETCH POSTER ----------------

def fetch_poster(movie_name):

    url = f"http://www.omdbapi.com/?t={movie_name}&apikey=36e856e5"

    data = requests.get(url).json()

    if data["Response"] == "True":
        return data["Poster"]

    else:
        return "https://via.placeholder.com/300x450?text=No+Image"

# ---------------- RECOMMEND FUNCTION ----------------

def recommend(movie):

    movie_index = movies[movies["title"] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:

        movie_title = movies.iloc[i[0]].title

        recommended_movies.append(movie_title)

        recommended_posters.append(fetch_poster(movie_title))

    return recommended_movies, recommended_posters

# ---------------- MOVIE CARD ----------------

def show_card(title, poster_url, rating="⭐ 8.5"):

    st.markdown(f"""
    <div class="movie-card">
        <img src="{poster_url}" width="100%">
        <h4 style="color:white;">{title}</h4>
        <p style="color:gold;">{rating}</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- TITLE ----------------

st.title("🎬 BingeBuddy")

st.markdown(
    "<h3 style='text-align:center; color:white;'>"
    "Find movies similar to your favorites instantly 🍿"
    "</h3>",
    unsafe_allow_html=True
)

st.write("")

# ---------------- SEARCH BAR ----------------

selected_movie_name = st.selectbox(
    "🔍 Search Your Favorite Movie",
    movies["title"].values
)

# ---------------- BUTTON ----------------

if st.button("Recommend Movies"):

    names, posters = recommend(selected_movie_name)

    st.subheader("✨ Recommended Movies")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        show_card(names[0], posters[0])

    with col2:
        show_card(names[1], posters[1])

    with col3:
        show_card(names[2], posters[2])

    with col4:
        show_card(names[3], posters[3])

    with col5:
        show_card(names[4], posters[4])