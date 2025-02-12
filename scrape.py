from bs4 import BeautifulSoup

# Load the HTML file
with open("htmlcontent.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find all <h3> tags that are within <p> tags
headers = [h3.get_text(strip=True) for p in soup.find_all("p") for h3 in p.find_all("h3")]

# Print extracted headers
for header in headers:
    print(header)
