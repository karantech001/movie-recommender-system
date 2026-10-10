
import streamlit as st
import pandas as pd
import pickle
import requests
from pathlib import Path

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Movie Recommender System")
st.write("Choose a movie and get 5 similar movie recommendations!")

# Project folder
folder = Path(__file__).resolve().parent


# Load movie data and reconstruct similarity matrix
@st.cache_resource
def load_data():
    # Load movie dictionary
    with open(folder / "movie_dict.pkl", "rb") as file:
        movies_data = pickle.load(file)

    # Find all split similarity files
    parts = sorted(folder.glob("similarity.part*"))

    if parts:
        # Join all parts into one file
        combined_file = folder / "similarity_combined.pkl"

        with open(combined_file, "wb") as output:
            for part in parts:
                with open(part, "rb") as chunk:
                    while True:
                        data = chunk.read(1024 * 1024)

                        if not data:
                            break

                        output.write(data)

        # Load reconstructed similarity matrix
        with open(combined_file, "rb") as file:
            similarity_data = pickle.load(file)

    else:
        # Fallback to original similarity file
        original_file = folder / "similarity.pkl"

        if not original_file.exists():
            raise FileNotFoundError(
                "Similarity files not found. "
                "Please add similarity.part files or similarity.pkl."
            )

        with open(original_file, "rb") as file:
            similarity_data = pickle.load(file)

    return pd.DataFrame(movies_data), similarity_data


try:
    movies, similarity = load_data()

except Exception as error:
    st.error(f"Could not load movie files: {error}")
    st.stop()


# Read TMDB API key securely
try:
    api_key = st.secrets["TMDB_API_KEY"]
except (KeyError, FileNotFoundError):
    api_key = None


# Fetch movie poster
@st.cache_data(ttl=3600)
def fetch_poster(movie_id):
    if not api_key:
        return None

    url = f"https://api.themoviedb.org/3/movie/{movie_id}"

    try:
        response = requests.get(
            url,
            params={
                "api_key": api_key,
                "language": "en-US"
            },
            timeout=15
        )

        if response.status_code != 200:
            return None

        poster_path = response.json().get("poster_path")

        if poster_path:
            return (
                "https://image.tmdb.org/t/p/w500/"
                + poster_path
            )

    except (requests.RequestException, ValueError):
        return None

    return None


# Recommend similar movies
def recommend(movie_title):
    matching = movies.index[
        movies["title"] == movie_title
    ].tolist()

    if not matching:
        return []

    movie_index = matching[0]
    distances = similarity[movie_index]

    similar_movies = sorted(
        enumerate(distances),
        key=lambda item: item[1],
        reverse=True
    )

    results = []

    for index, score in similar_movies:
        if index == movie_index:
            continue

        movie = movies.iloc[index]

        results.append({
            "title": movie["title"],
            "movie_id": movie["movie_id"]
        })

        if len(results) == 5:
            break

    return results


# Movie selection
selected_movie = st.selectbox(
    "Select a movie",
    movies["title"].dropna().astype(str).tolist()
)


# Display recommendations
if st.button("Recommend Movies", type="primary"):

    if not api_key:
        st.error(
            "TMDB API key not found. Add TMDB_API_KEY "
            "in .streamlit/secrets.toml for local use "
            "or in Streamlit Cloud Settings > Secrets."
        )
        st.stop()

    with st.spinner("Finding similar movies..."):
        recommendations = recommend(selected_movie)

    if not recommendations:
        st.warning("No recommendations found.")

    else:
        st.subheader("Your Recommended Movies")
        columns = st.columns(5)

        for column, movie in zip(columns, recommendations):
            with column:
                st.markdown(f"**{movie['title']}**")

                poster = fetch_poster(movie["movie_id"])

                if poster:
                    st.image(
                        poster,
                        use_container_width=True
                    )
                else:
                    st.caption("Poster not available")


st.divider()
st.caption(
    "Movie Recommender System | "
    "Movie data and posters powered by TMDB"
)
