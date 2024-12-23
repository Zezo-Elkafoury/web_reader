import requests
from bs4 import BeautifulSoup
import json
from extractor import extract_content

def read_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        content = extract_content(soup)
        return json.dumps(content, indent=4)
    else:
        return json.dumps({"error": "Failed to retrieve the website"}, indent=4)

if __name__ == "__main__":
    url = input("Enter the URL of the website: ")
    print(read_website(url))