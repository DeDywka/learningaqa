import requests

url = "https://playground.learnqa.ru/api/get_text"

response = requests.get(url)
text = response.text

print(text)