import requests
from bs4 import BeautifulSoup


def crawler(max_pages , root):
    page = 1
    while page <= max_pages:
        url = root.replace("<PAGE>" , str(page))
        source = requests.get(url).text
        soup = BeautifulSoup(source , "html.parser")
        for link in soup.findAll("a"):
            title = link.get("title")
            text = str(title)
            if "drone" in text.lower():
                print(text)
        page += 1


root_dir = "https://www.amazon.in/s/ref=sr_pg_<PAGE>?fst=as%3Aon&rh=n%3A1350380031%2Ck%3Adrones&page=<PAGE>&keywords=drones"
crawler(1 , root_dir)