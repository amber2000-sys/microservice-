import requests
import json
from bs4 import BeautifulSoup
import re

def get_word_frequency(url):
    # Fetch the HTML content of the webpage
    response = requests.get(url)
    html_content = response.text

    # Use BeautifulSoup to extract the text from the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text()

    # Clean the text by removing unwanted characters
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)

    # Split the text into words and create a dictionary to store the frequency of each word
    words = text.lower().split()
    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    # Convert the dictionary to a JSON format and return it as the output
    output = json.dumps(word_frequency, indent=4)
    return output
url = "https://www.example.com"
word_frequency = get_word_frequency(url)
print(word_frequency)
