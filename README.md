# 🎬 BingeBuddy — Movie Recommendation System

BingeBuddy is a content-based movie recommendation web application that suggests movies similar to your favorites instantly. Built using **Python**, **Machine Learning**, **Streamlit**, and the **TMDB API**, the app provides intelligent movie recommendations along with movie posters for a better user experience.

## 🚀 Live Demo

Add your deployed Streamlit link here:

```txt
https://your-streamlit-link.streamlit.app
```

---

## 📌 Features

✅ Movie recommendation based on content similarity  
✅ Interactive and modern UI using Streamlit  
✅ Search and select movies easily  
✅ Displays similar movie recommendations instantly  
✅ Movie posters fetched dynamically using TMDB API  
✅ Fast and lightweight recommendation system  

---

## 🛠️ Tech Stack

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-Learn**
- **Streamlit**
- **Pickle**
- **OMDB API**

---

## 🧠 How It Works

This project uses a **Content-Based Recommendation System**.

Movies are recommended based on similarities between:

- Genres
- Keywords
- Cast
- Crew
- Overview / tags

### Recommendation Process

1. Movie datasets are cleaned and preprocessed.
2. Important movie metadata is combined into tags.
3. Text vectorization is performed.
4. Cosine similarity is calculated between movies.
5. The system recommends movies with the highest similarity scores.

---

## 📂 Project Structure

```txt
movie-recommendation-system/
│── app.py
│── first.py
│── similarity.pkl
│── movies_dict.pkl
│── tmdb_5000_movies.csv
│── tmdb_5000_credits.csv
│── requirement.txt
│── setup.sh
│── .gitignore
│── README.md
```

---

## 📸 Preview

Add screenshots of your application here.

Example:

```txt
Home Page UI
Movie Recommendations
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/movie-recommendation-system.git
```

### 2. Navigate to project folder

```bash
cd movie-recommendation-system
```

### 3. Create virtual environment (optional)

```bash
python -m venv venv
```

### 4. Activate environment

#### Mac/Linux

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirement.txt
```

### 6. Run the application

```bash
streamlit run app.py
```

---

## 📊 Dataset

This project uses the **TMDB 5000 Movie Dataset**.

Files used:

- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

---

## 🎯 Future Improvements

- Genre-based filtering
- Personalized recommendations
- Search by actor/director
- Trending & popular movies section
- Better UI animations
- Dark/Light theme toggle

---

## 👩‍💻 Author

**Mishika Bagrecha**

GitHub:  
https://github.com/mishikabagrecha

---

## ⭐ Support

If you liked this project, consider giving it a **star ⭐** on GitHub.
