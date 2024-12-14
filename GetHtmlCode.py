import requests

def fetchAndSaveToFile(url, path):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        with open(path, "w", encoding='utf-8') as f:
            f.write(r.text)
    else:
        print(f"Failed to retrieve the content. Status code: {r.status_code}")

url = "https://www.imdb.com/chart/top/"
fetchAndSaveToFile(url, "HTMLofIMDB.html")
