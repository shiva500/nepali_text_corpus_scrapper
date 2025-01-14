from bs4 import BeautifulSoup
import requests

url = 'https://www.onlinekhabar.com/sports'

response = requests.get(url)
#response.encoding = 'utf-8'


if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    articles = soup.find_all('h2')
    nepali_texts = [article.get_text(strip=True) for article in articles]
    
    for idx, text in enumerate(nepali_texts):
        print(f'{idx + 1}: {text}')
        
else:
    print(f"Faled to fetch url. Status code {response.status_code}")

