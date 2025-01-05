# LLM-Project-Building-a-News-Research-Tool

## Overview

The Enhanced News Summarizer Tool is an AI-powered application designed to help equity research analysts retrieve and summarize the latest news articles. By leveraging NewsAPI and Groq LLM, this tool provides actionable, concise insights, saving time and effort for users.

The project also includes a user-friendly interface built with Streamlit, allowing users to input queries and receive real-time summaries.

## Features

#### Real-Time News Retrieval:
* Fetches the most relevant news articles using NewsAPI.
#### AI-Powered Summarization:
* Combines user queries with news summaries using Groq LLM.
#### Interactive Web App:
* Built with Streamlit for a seamless user experience.
#### Error Handling:
* Provides warnings for invalid inputs or API issues.

## Technologies Used

#### Programming Language: 
* Python
####  APIs:
* Groq LLM API
* NewsAPI
####  Libraries:
* langchain
* groq-cloud
* streamlit
* newsapi-python
* dotenv

## Installation and Setup

### 1. Clone the Repository

git clone https://github.com/your-username/enhanced-news-summarizer.git

cd enhanced-news-summarizer

## 2. Create a Virtual Environment


## 3. Install Dependencies

pip install -r requirements.txt

## 4. Add API Keys

* Create a .env file in the project root directory.
* Add the following keys:
GROQ_API_KEY=your-groq-api-key

NEWSAPI_KEY=your-newsapi-key

## Usage

### Run the Application

streamlit run app.py

### How to Use

1. Open the link displayed in the terminal (e.g., http://localhost:8501).

2. Enter a query in the input box (e.g., "Impact of inflation on stock markets").

3. Click on Get Enhanced Summary.

4. View the summarized output in the app.

## Project Structure

![Uploading image.png…]()
