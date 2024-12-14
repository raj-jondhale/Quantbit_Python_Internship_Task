import requests

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")

api_url = "https://jsonplaceholder.typicode.com/posts/1"
fetch_data(api_url)
