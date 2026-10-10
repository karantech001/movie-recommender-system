<div align="center">

<img src="assets/movies recommender system.jpeg" alt="Movie Recommendation System banner" width="100%" />

# 🎬 Movie Recommendation System

### Content-Based Movie Recommendations with Python and Streamlit

Discover movies similar to a title you like, with movie posters retrieved through the TMDB API.

[GitHub Repository](https://github.com/karantech001/movie-recommender-system) · Python · Pandas · Streamlit · TMDB API

</div>

---

## 📌 Overview

This project is an end-to-end machine learning application that recommends movies similar to a movie selected by the user. It combines precomputed movie/recommendation data with a Streamlit interface and uses The Movie Database (TMDB) API to retrieve movie poster images.

The project workflow covers dataset collection, data understanding, preprocessing, exploratory data analysis (EDA), feature preparation, recommendation logic, web-app development, API integration, and deployment.

> **Implementation note:** The Streamlit app loads saved movie and similarity data. The exact preprocessing steps, feature representation, and similarity metric should be confirmed from the notebook or code that generated those files.

## ✨ Features

- Select a movie from the available movie list.
- Get recommendations for similar movie titles.
- Display movie posters through the TMDB API.
- Use an interactive Streamlit web interface.
- Load precomputed movie and similarity data instead of rebuilding the model at every app launch.

## 🧰 Tech Stack

| Tool / Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data loading and data preparation |
| Jupyter Notebook | Dataset exploration and experimentation |
| Content-based recommendation | Recommend titles based on movie-content similarity |
| Streamlit | Interactive web application |
| Requests | HTTP requests to the TMDB API |
| TMDB API | Movie poster retrieval |
| Pickle / saved data files | Load precomputed movie and similarity data |
| Git and GitHub | Version control and source-code hosting |
| Streamlit Community Cloud | Potential hosting option for deployment |

## 🔄 End-to-End Project Workflow

### 1. Dataset Collection

For the model-development workflow, the project can use the following public Kaggle datasets:

- **TMDB 5000 Movies Dataset**
- **TMDB 5000 Credits Dataset**

Dataset source: [TMDB 5000 Movie Dataset — Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

The datasets include movie metadata and credits information such as titles, genres, keywords, cast, crew, and overviews where available. Confirm that the datasets used to generate your saved model files match the files you download.

### 2. Load and Understand the Data

Use Pandas in a Jupyter Notebook to load the CSV files and inspect:

- Rows, columns, data types, and column names
- Missing values and duplicate records
- Available movie metadata and credits fields
- The key used to relate the movies and credits tables

### 3. Data Preprocessing

Prepare the data used by the recommender. Depending on the actual notebook, this may include merging the datasets, selecting relevant columns, parsing fields such as genres or cast, handling missing values, removing duplicates, and normalizing text.

### 4. Exploratory Data Analysis (EDA)

Explore the available data to understand movie characteristics. Suitable analyses may include genre distribution, release-year distribution, missing-value summaries, and popularity or vote distributions where those fields exist.

### 5. Feature Engineering

Prepare the movie attributes used by the recommendation model. The selected features and text-processing approach must match the code that generated the saved similarity data; do not assume a specific vectorizer or metric without checking that code.

### 6. Recommendation Model

The project uses a **content-based recommendation approach**: the application returns movies related to the title selected by the user, based on precomputed movie/similarity data. The exact similarity metric and feature-generation details should be documented from the model-generation code.

### 7. Save and Load Model Data

The current application repository uses saved data files, including `movie_dict.pkl` and the split similarity files. These files must remain compatible with the loading logic in `app.py`.

### 8. Streamlit Web Application

The app provides a movie-selection interface and displays recommendations. Poster images are fetched using TMDB API requests.

### 9. TMDB API Integration

Configure your API key through Streamlit Secrets or a local secrets file. Never put a real API key directly in source code or commit it to a public repository.

### 10. Deployment

The repository can be deployed to [Streamlit Community Cloud](https://share.streamlit.io/) if the app and its data files fit the platform's current requirements. After deployment, test the app and add the **actual** public app URL below.

**Live Demo:** `Add your deployed Streamlit URL here`

## 📁 Repository Structure

```text
movie-recommender-system/
├── app.py
├── movie_dict.pkl
├── requirements.txt
├── split_similarity.py
├── similarity.part000
├── similarity.part001
├── similarity.part002
├── similarity.part003
├── similarity.part004
├── similarity.part005
├── similarity.part006
├── similarity.part007
├── similarity.part008
├── assets/
│   └── movies recommender system.jpeg
├── .gitattributes
├── .gitignore
└── README.md
```

This tree reflects the project files discussed for this repository. Keep it synchronized with the files actually committed to GitHub. Add screenshots only after saving the real app screenshots in the repository.

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/karantech001/movie-recommender-system.git
cd movie-recommender-system
```

### 2. Create and activate a virtual environment (recommended)

**Windows PowerShell:**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can run the commands from Command Prompt using `.venv\Scripts\activate.bat` instead.

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the TMDB API key

Create `.streamlit/secrets.toml` in the project directory:

```toml
TMDB_API_KEY = "YOUR_TMDB_API_KEY"
```

Replace the placeholder with your own TMDB API key. Make sure `.streamlit/secrets.toml` is excluded by `.gitignore` and never commit the real key.

### 5. Start the application

```bash
streamlit run app.py
```

Open the local URL shown in the terminal. If the app reports missing similarity data, verify that every required `similarity.part000` through `similarity.part008` file exists and that the loader in `app.py` matches the split-file format.

## ☁️ Streamlit Community Cloud Deployment

1. Push the project to GitHub.
2. Open [Streamlit Community Cloud](https://share.streamlit.io/) and connect your GitHub account.
3. Select this repository, the correct branch, and `app.py` as the entry point.
4. Add `TMDB_API_KEY` in the app's Secrets settings.
5. Deploy and check the logs if startup fails.
6. Test movie selection, recommendation results, poster loading, and API-error handling.
7. Replace the Live Demo placeholder in this README with the real deployment URL.

## 🔐 Security and Notes

- Never publish `TMDB_API_KEY` or `.streamlit/secrets.toml`.
- Do not include private credentials in screenshots, notebooks, or commit history.
- Only list libraries and model techniques as implemented when they are present in the actual code and dependency files.
- Large saved similarity files may require Git LFS or another storage strategy, depending on repository and hosting limits.
- TMDB API access and poster availability depend on the API service and its terms.

## 🧪 Testing Checklist

- [ ] Required movie data files are present.
- [ ] The app starts locally with `streamlit run app.py`.
- [ ] The movie dropdown or selection control loads correctly.
- [ ] Recommendations appear for a valid movie selection.
- [ ] TMDB posters load when API access is available.
- [ ] Missing posters or API errors do not crash the app.
- [ ] The deployed app starts and works from a public browser.
- [ ] No API key or private secret is committed to GitHub.

## 🚀 Future Improvements

- Add genre and release-year filters.
- Display more movie information, such as overview, release date, and ratings.
- Improve search and user-interface accessibility.
- Add automated tests for recommendation and API behavior.
- Evaluate recommendation quality with suitable offline metrics.
- Optimize loading and storage of the precomputed similarity data.
- Add user preference features for more personalized results.

## 👨‍💻 Developer

**Karan Kumar**  
BCA Graduate — Artificial Intelligence & Data Science

- **GitHub:** [karantech001](https://github.com/karantech001)
- **Project Repository:** [movie-recommender-system](https://github.com/karantech001/movie-recommender-system)

## 🙏 Acknowledgements

- [Kaggle](https://www.kaggle.com/) for dataset hosting
- [The Movie Database (TMDB)](https://www.themoviedb.org/) for movie metadata and poster API
- [Streamlit](https://streamlit.io/) for the web application framework

---

<div align="center">

**Built with Python, Machine Learning, and Streamlit** 🎬

</div>
