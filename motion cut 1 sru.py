import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.google.com/search?q=weather+report+bangalore")

soup = BeautifulSoup(req.content, "html.parser")

res = soup.title

print(soup.get_text())