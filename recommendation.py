import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy
import pickle
import seaborn as sns

df=pd.read_csv(r'C:\AIML\Projects\Intelligent Book Recomendation System\clean.csv')
df = df.reset_index(drop=True)
with open("books.pkl","rb") as f:
    similarity=pickle.load(f)   

with open("model.pkl","rb") as f:
    model=pickle.load(f)  
with open("books_df.pkl", "rb") as f:
    df = pickle.load(f)
     
st.set_page_config(
    page_title="Audible Insights",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

def recommend(book_name):

    idx = df[df["Book Name"] == book_name].index[0]

    distances = list(enumerate(similarity[idx]))

    similar_books = sorted(
        distances,
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    recommendations = []

    for i in similar_books:

        recommendations.append(
            {
                "Book Name": df.iloc[i[0]]["Book Name"],
                "Author": df.iloc[i[0]]["Author"],
                "Rating": df.iloc[i[0]]["Rating"]
            }
        )

    return pd.DataFrame(recommendations)

st.sidebar.title("Navigation")

with st.sidebar:

    st.title("📚 Audible Insights")

    st.caption("Intelligent Book Recommendation System")

    page = st.radio(
        "Navigation",
        [
            "📘 Project Introduction",
            "🔍 Book Recommendations",
            "📊 Analytics Dashboard",
            "👩‍💻 Creator Info"
        ]
    )

if page == "📘 Project Introduction":

    st.title("📚 Audible Insights")
    st.caption("Intelligent Book Recommendation System")

    st.info("""
    Discover books tailored to your interests using Natural Language Processing,
    Content-Based Filtering, Clustering Techniques, and Hybrid Recommendation Models.
    """)

    st.divider()

    # =====================================================
    # PROJECT SNAPSHOT
    # =====================================================

    st.subheader("📊 Project Snapshot")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📚 Datasets", "2")

    with col2:
        st.metric("🧠 Models", "2")

    with col3:
        st.metric("🔍 NLP", "TF-IDF")

    with col4:
        st.metric("⚡ Framework", "Streamlit")

    st.divider()

    # =====================================================
    # ABOUT PROJECT
    # =====================================================

    with st.container(border=True):

        st.subheader("🎯 About the Project")

        st.write("""
        Audible Insights is an intelligent recommendation system designed
        to help readers discover books based on their interests and reading preferences.

        The system processes audiobook and book datasets, performs extensive
        data cleaning and exploratory data analysis, extracts text features
        using Natural Language Processing, and generates recommendations
        through machine learning techniques.

        The recommendation engine combines content similarity,
        clustering-based grouping, and hybrid recommendation approaches
        to provide personalized book suggestions.
        """)

    st.write("")

    # =====================================================
    # PROJECT MODULES
    # =====================================================

    st.subheader("🚀 Core Modules")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.success("""
        ### 📖 Recommendation Engine

        • Content-Based Filtering

        • Similar Book Discovery

        • Personalized Suggestions

        • Hybrid Recommendations
        """)

    with col2:

        st.info("""
        ### 🧠 NLP Processing

        • Text Cleaning

        • TF-IDF Vectorization

        • Feature Extraction

        • Similarity Analysis
        """)

    with col3:

        st.warning("""
        ### 📊 Analytics

        • Genre Analysis

        • Rating Trends

        • Author Insights

        • Hidden Gems Detection
        """)

    st.divider()

    # =====================================================
    # WORKFLOW
    # =====================================================
    st.subheader("⚙️ Project Workflow")

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.markdown("""
            ### 📂 Data Collection

            - Audible Catalog Dataset
            - Advanced Features Dataset
            - Data Integration
            """)

    with col2:
        with st.container(border=True):
            st.markdown("""
            ### 🧹 Data Cleaning

            - Missing Value Handling
            - Duplicate Removal
            - Data Standardization
            """)

    with col3:
        with st.container(border=True):
            st.markdown("""
            ### 📊 Exploratory Analysis

            - Genre Analysis
            - Rating Trends
            - Author Insights
            """)

    st.write("")

    col4, col5, col6 = st.columns(3)

    with col4:
        with st.container(border=True):
            st.markdown("""
            ### 🧠 NLP Processing

            - Text Preprocessing
            - TF-IDF Vectorization
            - Feature Extraction
            """)

    with col5:
        with st.container(border=True):
            st.markdown("""
            ### 🤖 Recommendation Engine

            - Content-Based Filtering
            - Clustering Approach
            - Hybrid Model
            """)

    with col6:
        with st.container(border=True):
            st.markdown("""
            ### 🚀 Deployment

            - Streamlit Application
            - Interactive Dashboard
            - Recommendation Interface
            """)

    # =====================================================
    # BUSINESS IMPACT
    # =====================================================

    st.subheader("💼 Business Impact")

    col1, col2 = st.columns(2)

    with col1:

        st.success("""
        ### 🎯 Reader Benefits

        • Personalized Recommendations

        • Faster Book Discovery

        • Genre Exploration

        • Hidden Gems Suggestions
        """)

    with col2:

        st.info("""
        ### 📈 Industry Benefits

        • Improved User Engagement

        • Better Book Sales

        • Author Popularity Insights

        • Data-Driven Decisions
        """)

    st.divider()

    # =====================================================
    # TECHNOLOGY STACK
    # =====================================================

    st.subheader("🛠 Technology Stack")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        with st.container(border=True):
            st.markdown("""
            ### 💻 Programming

            • Python

            • Pandas

            • NumPy
            """)

    with col2:
        with st.container(border=True):
            st.markdown("""
            ### 🤖 Machine Learning

            • Scikit-Learn

            • Recommendation Systems

            • Clustering
            """)

    with col3:
        with st.container(border=True):
            st.markdown("""
            ### 🧠 NLP

            • TF-IDF Vectorization

            • Text Processing

            • Cosine Similarity
            """)

    with col4:
        with st.container(border=True):
            st.markdown("""
            ### 🚀 Deployment

            • Streamlit

            • Pickle

            • Interactive Dashboard
            """)

        st.divider()

    # =====================================================
    # DATASET INFO
    # =====================================================

    with st.expander("📂 Dataset Information"):

        st.markdown("""
        ### Dataset 1: Audible Catalog

        - Book Name
        - Author
        - Genre
        - Rating
        - Reviews
        - Price
        - Description
        - Listening Time

        ---

        ### Dataset 2: Audible Advanced Features

        - Book Name
        - Author
        - Rating
        - Reviews
        - Price

        ---

        These datasets are merged and processed to create
        a recommendation-ready database for analytics
        and personalized book recommendations.
        """)
elif page == "🔍 Book Recommendations":

    st.title("📚 Book Recommendation System")

    books = sorted(df["Book Name"].dropna().unique())

    selected_book = st.selectbox(
        "📖 Select a Book",
        books
    )

    selected_info = df[df["Book Name"] == selected_book].iloc[0]

    st.success(f"Selected Book: {selected_book}")

    st.write(f"✍️ Author: {selected_info['Author']}")
    st.write(f"⭐ Rating: {selected_info['Rating']}")

    if st.button("🚀 Recommend Similar Books"):

        recommendations = recommend(selected_book)

        st.subheader("📚 Top 5 Similar Books")

        st.dataframe(
            recommendations,
            use_container_width=True,
            hide_index=True
        )

elif page == "📊 Analytics Dashboard":

    st.title("📊 Analytics Dashboard")

    questions=st.selectbox(
        "Select Analysis Question",
        [
            "1. What are the most popular genres in the dataset?",
            "2. Which authors have the highest-rated books?",
            "3. What is the average rating distribution across books?",
            "4. Are there trends in publication years for popular books?",
            "5. How do ratings vary between books with different review counts?",
            "6. What is the effect of author popularity on book ratings?"
        ]
    )

    if questions == "1. What are the most popular genres in the dataset?":

        genre_counts = df['Genre'].value_counts().head(10)
        genre_counts.plot(kind='bar')

        plt.title("Top 10 Genres")
        plt.xlabel("Genre")
        plt.ylabel("Count")

        st.pyplot(plt.gcf())
        plt.clf()

    elif questions == "2. Which authors have the highest-rated books?":
        author_rating=(
            df.groupby('Author')['Rating']
            .mean()
            .sort_values()
            .head())
        author_rating.plot(kind='bar')
        plt.title("Top 10 Highest Rated Authors")
        plt.xlabel("Author")
        plt.ylabel("Rating")
        st.pyplot(plt.gcf())
        plt.clf()

    elif questions ==  "3. What is the average rating distribution across books?":
        df['Rating'].describe()

        sns.histplot(df['Rating'],kde=True,bins=20)
        plt.title("Rating Distribution")
        st.pyplot(plt.gcf())
        plt.clf()

    elif questions == "4. Are there trends in publication years for popular books?":
        df[['Rating','Number of Reviews']].corr()

        sns.scatterplot(data=df)
        plt.xlabel("Number of Reviews")
        plt.ylabel("Rating")
        st.pyplot(plt.gcf())
        plt.clf()

    elif questions == "5. How do ratings vary between books with different review counts?":
        numeric=[
            'Rating',
            'Price',
            'Rank',
            'Number of Reviews'
            ]

        corr=df[numeric].corr()

        sns.heatmap(corr,annot=True,cmap='coolwarm')
        plt.title("Correlation Heatmap")
        st.pyplot(plt.gcf())
        plt.clf()
          
    elif questions ==  "6. What is the effect of author popularity on book ratings?":
        authors=df.groupby('Author').agg({
    'Number of Reviews':'sum',
    'Rating':'mean'
    })

        authors.head()

        plt.figure(figsize=(10,6))
        sns.scatterplot(
            data=authors,
            x="Number of Reviews",
            y="Rating")
        plt.title("Effect of Author Popularity on Ratings")
        st.pyplot(plt.gcf())
        plt.clf()
elif page == "👩‍💻 Creator Info":

    st.title("👩‍💻 Creator")

    st.markdown("## Vasantha Leela M")

    st.caption("B.E Computer Science and Engineering | Karpagam Academy of Higher Education")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### 💻 Skills

        • Python

        • Machine Learning

        • NLP

        • Streamlit

        • Scikit-Learn
        """)

    with col2:
        st.markdown("""
        ### 🎯 Specialization

        • Recommendation Systems

        • Content-Based Filtering

        • Hybrid Models

        • Data Analytics

        • AI Applications
        """)

    st.divider()

    st.caption(
        "Passionate about building intelligent recommendation systems using Machine Learning and Natural Language Processing."
    )
