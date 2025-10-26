import requests

url = "http://127.0.0.1:5000/predict"
data = {"text": "Covid 19 vaccine is not causing infertility!"}

response = requests.post(url, json=data)
print(response.json())
