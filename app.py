# Import Libraries

import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from newsapi.newsapi_client import NewsApiClient
import os

# Load environment variables
load_dotenv()

# Retrieve API keys
groq_api_key = os.getenv("GROQ_API_KEY")
newsapi_key = os.getenv("NEWSAPI_KEY")

# Initialize Chat Groq LLM
groq_llm = ChatGroq(
    temperature=0,
    model = 'mixtral-8x7b-32768',
    groq_api_key = groq_api_key
    )

# Initialize NewsAPI
newsapi = NewsApiClient(api_key=newsapi_key)

# Define the prompt template
template = """
You are an AI assistant helping an equity research analyst. Given 
the following query and the provided news article summaries, provide 
an overall summary.

Query: {query}
Summaries: {summaries}
"""


# Create the prompt
prompt = PromptTemplate.from_template(template)
pipeline = prompt | groq_llm

# Helper Functions
def get_news_articles(query):
    articles = newsapi.get_everything(q=query, language="en", sort_by="relevancy")
    return articles["articles"]

def summarize_articles(articles):
    summaries = []
    for article in articles[:5]:  # Limit to top 5 articles
        summaries.append(article["description"] or "No description available")
    return " ".join(summaries)

def get_summary(query):
    articles = get_news_articles(query)
    article_summaries = summarize_articles(articles)
    pipeline = prompt | groq_llm
    response = pipeline.invoke({"query": query, "summaries": article_summaries})
    return response

# Streamlit App
st.title("Equity Research News Tool")
st.write("Enter your query to get the latest news articles summarized")

# Query Input
query = st.text_input("Query", placeholder="e.g., Impact of inflation on stock markets")

if st.button("Get News"):
    if query:
        st.write("### Fetching Articles and Generating Summary...")
        try:
            summary = get_summary(query)
            st.write("### Summary:")
            st.write(summary)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a query before clicking the button.")

# Footer
st.write("---")
st.write("Powered by [Groq LLM](https://groq.com), [NewsAPI](https://newsapi.org), and [Streamlit](https://streamlit.io)")