import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of New York Times homepage
url = "https://www.nytimes.com/"

# Headers to mimic a real browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Fetch the page content
response = requests.get(url, headers=headers)

# Check if request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract headlines (usually inside <h2> tags, adjust if necessary)
    headlines = [h2.get_text(strip=True) for h2 in soup.find_all("h2")]
    
    # Create DataFrame
    df = pd.DataFrame({"Headlines": headlines})
    
    # Display the table
    print(df)
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
