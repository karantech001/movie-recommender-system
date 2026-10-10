 <div align="center">

<img src="assets/movies-recommender-system.jpeg" alt="Movie Recommendation System Banner" width="100%" />

# 🎬 Movie Recommendation System

### Discover Movies You'll Love with Content-Based Recommendations

An interactive movie recommendation web application built with Python and Streamlit. Select a movie, explore similar titles, and view movie posters powered by the TMDB API.

[![Live Demo](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://movie-recommender-system-karankr.streamlit.app/)

[🚀 **Launch Live Demo**](https://movie-recommender-system-karankr.streamlit.app/) · [💻 **GitHub Repository**](https://github.com/karantech001/movie-recommender-system)

**Python** · **Pandas** · **Machine Learning** · **Streamlit** · **TMDB API**

</div>

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Live Demo](#-live-demo)
- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [How It Works](#-how-it-works)
- [Project Workflow](#-project-workflow)
- [Repository Structure](#-repository-structure)
- [Installation and Setup](#-installation-and-setup)
- [TMDB API Configuration](#-tmdb-api-configuration)
- [Deployment](#-deployment)
- [Testing](#-testing)
- [Challenges and Considerations](#-challenges-and-considerations)
- [Future Improvements](#-future-improvements)
- [Skills Demonstrated](#-skills-demonstrated)
- [Author](#-author)
- [Acknowledgements](#-acknowledgements)

## 🎯 Project Overview

The **Movie Recommendation System** is a machine learning project that helps users discover movies similar to a title they already enjoy.

The application uses a content-based recommendation approach and loads precomputed movie and similarity data. Its interactive Streamlit interface allows users to select a movie and explore recommended titles. The TMDB API is integrated to retrieve movie poster images.

This project demonstrates how Python, data preparation, recommendation logic, API integration, and web application development can be combined to build a practical machine learning application.

### Project Objectives

- Build an interactive movie recommendation application.
- Recommend related movie titles based on content similarity.
- Integrate an external API to retrieve movie posters.
- Use saved recommendation data to avoid rebuilding the model whenever the app launches.
- Deploy the application online so users can access it through a web browser.
- Practice end-to-end machine learning application development.

## 🚀 Live Demo

**Try the deployed application:**

### [🎬 Open Movie Recommendation System](https://movie-recommender-system-karankr.streamlit.app/)

**Source code:** [View the project on GitHub](https://github.com/karantech001/movie-recommender-system)

The demo URL is the application link supplied for this project. Its availability and functionality may depend on the hosting service and API connectivity.

## ✨ Features

- **🎥 Movie Selection:** Select a title from the movie collection available in the application.
- **🎯 Content-Based Recommendations:** Discover titles related to the selected movie.
- **🖼️ Movie Posters:** Retrieve movie poster images using the TMDB API.
- **⚡ Precomputed Data:** Load saved movie and similarity data rather than calculating all similarities at application startup.
- **🌐 Interactive Interface:** Access the recommendation system through a Streamlit web application.
- **🔗 API Integration:** Connect the application to an external movie metadata service.
- **☁️ Online Access:** Access the deployed application through its public URL, subject to service availability.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application programming |
| Pandas | Data loading and preparation |
| Jupyter Notebook | Dataset exploration and experimentation |
| Content-Based Filtering | Recommend movies using content similarity |
| Streamlit | Interactive web interface |
| Requests | HTTP requests to the TMDB API |
| TMDB API | Retrieve movie poster images |
| Pickle | Load saved movie data |
| Git | Version control |
| GitHub | Source-code hosting |
| Streamlit Community Cloud | Application hosting |

*The exact feature extraction method, similarity metric, and preprocessing implementation should be documented according to the code that generated the saved model data.*

## ⚙️ How It Works

The application follows this high-level flow:

1. The user opens the Streamlit application.
2. The application loads the saved movie and similarity data.
3. The user selects a movie from the available collection.
4. The recommendation logic identifies related titles using the precomputed similarity data.
5. The application displays the recommended movie titles.
6. TMDB API requests retrieve poster images for display.
7. The user explores the recommendations in the web interface.

**Important:** The application uses precomputed recommendation data. The precise similarity algorithm and feature-generation steps should be verified from the original model-generation code rather than assumed.

## 🔄 Project Workflow

### 1. Dataset Collection

The model-development workflow can use the following public datasets:

- TMDB 5000 Movies Dataset
- TMDB 5000 Credits Dataset

**Dataset source:** [TMDB 5000 Movie Metadata — Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

These datasets contain movie metadata and credits information, including fields such as genres, cast, crew, keywords, and overviews where available.

### 2. Data Understanding

Use Pandas and Jupyter Notebook to explore the data structure.

Typical activities include:

- Inspecting rows, columns, and data types.
- Checking missing values and duplicate records.
- Identifying relevant movie attributes.
- Understanding the relationship between movie metadata and credits.

### 3. Data Preprocessing

Prepare the data required by the recommendation model. Depending on the original implementation, preprocessing may involve selecting useful columns, merging datasets, processing text fields, handling missing values, and removing duplicates.

### 4. Exploratory Data Analysis (EDA)

Explore the dataset to understand movie characteristics and identify useful patterns.

Potential analyses include genre distribution, release-year trends, missing-value summaries, and popularity distributions where the relevant fields are available.

### 5. Feature Engineering

Prepare the movie attributes used by the recommendation model. The feature representation and text-processing approach must match the implementation used to create the saved similarity data.

### 6. Recommendation Model

The project uses a **content-based recommendation approach** to identify movies related to the user's selected title.

The application loads precomputed movie and similarity data. The specific feature extraction technique and similarity metric should be confirmed from the model-generation code.

### 7. Saving and Loading Data

The repository includes saved data files used by the application:

- `movie_dict.pkl`
- `similarity.part000` through `similarity.part008`

These files must remain compatible with the loading logic in `app.py`.

### 8. Web Application Development

Streamlit provides the user interface for movie selection and recommendations. The application also uses TMDB API requests to retrieve poster images.

### 9. API Integration

The TMDB API provides movie poster images. The API key must be configured securely and should never be hard-coded into public source code.

### 10. Deployment

The application is hosted at the Live Demo URL listed above. Deployment configuration and secrets should be maintained securely.

## 📁 Repository Structure

```text
movie-recommender-system/
│
├── app.py
├── movie_dict.pkl
├── requirements.txt
├── split_similarity.py
│
├── similarity.part000
├── similarity.part001
├── similarity.part002
├── similarity.part003
├── similarity.part004
├── similarity.part005
├── similarity.part006
├── similarity.part007
├── similarity.part008
│
├── assets/
│   └── movies recommender system.jpeg
│
├── .gitattributes
├── .gitignore
└── README.md
```

This structure reflects the project files discussed for this repository. Ensure that the filenames and folders match the files actually committed to GitHub.

## 💻 Installation and Setup

Follow these steps to run the project locally.

### Prerequisites

- Python installed on your computer.
- Git installed on your computer.
- A TMDB API key for poster retrieval.
- All required application and saved-data files.

### Step 1: Clone the Repository

Open PowerShell or a terminal and run:

```bash
git clone https://github.com/karantech001/movie-recommender-system.git
cd movie-recommender-system
```

### Step 2: Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Alternatively, from Command Prompt:

```bat
.venv\Scripts\activate.bat
```

### Step 3: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Configure the TMDB API Key

Create a `.streamlit` folder in the project directory. Inside it, create a file named `secrets.toml`.

Add the following configuration:

```toml
TMDB_API_KEY = "YOUR_TMDB_API_KEY"
```

Replace the placeholder with your own API key.

### Step 5: Run the Application

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal.

If the application cannot load the saved recommendation data, check that all required similarity files exist and that their format matches the loader in `app.py`.

## 🔑 TMDB API Configuration and Security

The TMDB API is used to retrieve movie poster images.

For local development, store the API key in `.streamlit/secrets.toml`. For the deployed app, configure the secret in the hosting platform's app settings.

- Never publish a real API key in source code.
- Never commit `.streamlit/secrets.toml` to a public repository.
- Make sure `.gitignore` excludes local secrets.
- Avoid exposing credentials in screenshots, logs, or documentation.
- If a key is accidentally published, revoke or rotate it.

See the official [Streamlit Secrets Management documentation](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

## ☁️ Deployment

The project uses a Streamlit-hosted application URL.

For future deployments or updates:

1. Push the required application files to GitHub.
2. Open [Streamlit Community Cloud](https://share.streamlit.io/).
3. Connect your GitHub account.
4. Select the repository, branch, and `app.py` entry point.
5. Configure `TMDB_API_KEY` in the application's Secrets settings.
6. Deploy and review the application logs if an error occurs.
7. Test the movie selection, recommendations, and poster retrieval.
8. Update the README if the public application URL changes.

See the official [Streamlit deployment guide](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app).

## 🧪 Testing Checklist

Use this checklist to verify the application:

- [ ] The application starts without errors.
- [ ] The movie selection control loads.
- [ ] Selecting a valid movie returns recommendations.
- [ ] All required saved-data files load correctly.
- [ ] Movie posters appear when the TMDB API is accessible.
- [ ] Missing posters and API failures do not unexpectedly crash the application.
- [ ] The deployed application opens in a browser.
- [ ] The README Live Demo link points to the correct URL.
- [ ] No API keys or private credentials are exposed in GitHub.

## ⚠️ Challenges and Considerations

### Saved Similarity Data

The similarity data is divided into multiple files. Every required part must be present and compatible with the application's loading logic.

### External API Availability

Poster retrieval depends on the TMDB API and network connectivity. A poster request can fail even when the recommendation logic is working.

### Deployment and File Size

Large saved-data files can create repository and hosting constraints. Verify the current limits of the selected platform and use an appropriate storage strategy if needed.

### Model Documentation

The exact preprocessing steps, feature representation, and similarity metric should be documented only after verifying the code used to generate the saved data.

## 🔮 Future Improvements

Potential enhancements include:

- Add movie search functionality.
- Filter movies by genre or release year.
- Display movie overviews, release dates, and ratings.
- Improve the interface and responsive design.
- Add automated tests for recommendation and API behavior.
- Evaluate recommendation quality with suitable offline metrics.
- Optimize saved-data loading and memory usage.
- Improve error messages and loading indicators.
- Explore hybrid recommendation methods combining content and user-rating information.

## 📚 Skills Demonstrated

This project provides practical experience with:

- Python programming.
- Data handling using Pandas.
- Data preparation and exploratory analysis.
- Content-based recommendation systems.
- External API integration.
- Streamlit web application development.
- Git and GitHub workflows.
- Application configuration and deployment.

## 👨‍💻 Author

**Karan Kumar**

BCA Graduate — Artificial Intelligence & Data Science

- **GitHub Profile:** [karantech001](https://github.com/karantech001)
- **Project Repository:** [Movie Recommendation System](https://github.com/karantech001/movie-recommender-system)
- **Live Application:** [Try the Movie Recommender](https://movie-recommender-system-karankr.streamlit.app/)

## 🙏 Acknowledgements

- [Kaggle](https://www.kaggle.com/) — Dataset hosting.
- [The Movie Database (TMDB)](https://www.themoviedb.org/) — Movie metadata and poster API.
- [Streamlit](https://streamlit.io/) — Web application framework.
- [Python](https://www.python.org/) — Core programming language.

---

<div align="center">

### 🎬 Built with Python, Machine Learning, and Streamlit

**Explore movies. Discover similar titles. Find your next favourite.**

[🚀 Launch Live Demo](https://movie-recommender-system-karankr.streamlit.app/) · [⭐ View on GitHub](https://github.com/karantech001/movie-recommender-system)

</div>
