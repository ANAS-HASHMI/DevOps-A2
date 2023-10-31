import requests
from bs4 import BeautifulSoup

def scrape_webpage(url):
    try:
        # Fetch the webpage content
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract text from the HTML
        text = soup.get_text()

        # Print clean text
        print(text)

    except requests.RequestException as e:
        print(f"Failed to retrieve the webpage: {e}")
        print("Try Again")

# Replace 'URL_HERE' with the URL of the webpage you want to scrape
webpage_url = 'https://www.waheediqbal.info/courses/devops23'
scrape_webpage(webpage_url)
