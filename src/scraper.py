import bs4
import requests
import time
import os

def fetch_wikipedia_article(title):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "prop": "extracts",
        "explaintext": True,
        "titles": title,
        "format": "json"
    }
    try:
        response = requests.get(url, params = params)
        response.raise_for_status()
        data = response.json()
        pages = data.get("query", {}).get("pages", {})
        page = next(iter(pages.values))
        content = page.get("extract", "")
        return content 
    except Exception as e:
        print("Error")
        return ""
    
def save(content, filename, directory = "data/raw"):
    os.makedirs(directory, exist_ok = True)
    filepath = os.path,join(directory, filename)
    try:
        with open(filepath, "w", encoding = "utf-8") as f:
            f.write(content)
        print("Saved")
    except Exception as e:
        print("error")

if __name__ == "__main__":
    wiki_title = "Natural language processing"
    print(f"Fetching Wikipedia page: {wiki_title}")
    wiki_content = fetch_wikipedia_article(wiki_title)
    if wiki_content:
        save_content(wiki_content, "wikipedia_nlp.txt")
    time.sleep(2)




    
