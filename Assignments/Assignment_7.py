import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/Art_Deco"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

paragraphs = soup.find_all('p')
headings = soup.find_all(['h1', 'h2', 'h3'])

paragraph_texts = [para.get_text() for para in paragraphs]
heading_texts = [heading.get_text() for heading in headings]

len_headings = len(heading_texts)
len_paragraphs = len(paragraph_texts)

if len_headings < len_paragraphs:
    heading_texts.extend([''] * (len_paragraphs - len_headings))

if len_paragraphs < len_headings:
    paragraph_texts.extend([''] * (len_headings - len_paragraphs))

data = {
    'Heading': heading_texts,
    'Paragraph': paragraph_texts
}


df = pd.DataFrame(data)
df.to_csv('art_deco_paragraphs_headings.csv', index=False)

print("Scraping complete. CSV saved as 'art_deco_paragraphs_headings.csv'.")
