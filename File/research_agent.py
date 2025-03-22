#Fetches Trending HR Topics
import requests
from bs4 import BeautifulSoup

def fetch_trending_topics():
    """
    Fetches trending HR topics using web scraping or APIs.
    """
    url = "https://www.shrm.org/resourcesandtools/hr-topics/Pages/default.aspx"  # SHRM website
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract trending topics (example logic)
        topics = []
        for item in soup.find_all('h3', class_='title'):  # Adjust class based on website structure
            topics.append(item.text.strip())

        # If no topics are found, use default topics
        if not topics:
            print("No topics found. Using default topics.")
            topics = ["Remote Work Trends in 2024", "Employee Well-being Strategies", "AI in HR"]

        return topics[:3]  # Return top 3 trending topics
    except requests.exceptions.RequestException as e:
        print(f"Error fetching trending topics: {e}")
        return ["Remote Work Trends in 2024", "Employee Well-being Strategies", "AI in HR"]
