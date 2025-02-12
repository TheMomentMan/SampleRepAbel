import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the New York Times homepage
url = "https://www.nytimes.com/"

# Headers to mimic a real browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Fetch the page content
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract headlines (refining the selection for actual news headlines)
    headlines = []
    for item in soup.find_all("h2"):
        text = item.get_text(strip=True)
        if len(text) > 10:  # Filter out short or irrelevant texts
            headlines.append(text)

    # Remove duplicates and non-news items
    headlines = list(dict.fromkeys(headlines))

    # Create a DataFrame for a clean table
    df = pd.DataFrame({"NYT Headlines": headlines})

    # Display the table
    print(df)

else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
