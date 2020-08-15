import requests
from bs4 import BeautifulSoup

def items_parser(items):
    fetched_items = []

    for item in items:
        title = item.find("a", {
            "class": "post-title"
        }).get_text()
        
        url = item.find("a", {
            "class": "post-title"
        })["href"]

        img = item.find("a", {
            "class": "img-holder"
        })["style"].replace("background-image: url(", "").replace(");", "")

        category = item.find("span", {
            "class": "term-badge"
        }).find("a").get_text()

        date = item.find("time", {
            "class": "post-published"
        }).get_text()

        obj = {
            "title": title,
            "url": url,
            "img": img,
            "category": category,
            "date": date
        }

        fetched_items.append(obj)

    return fetched_items


def process(search: str, pages=1):
    fetched_items = []

    for p in range(int(pages)):
        r = requests.get("https://freecoursesite.com/page/" + str(p) + "/?s=" + str(search))
        items = BeautifulSoup(r.content.decode(), "html.parser").find_all("div", {
            "class": "item-inner"
        })
        fetched_items = fetched_items + items_parser(items)

    return fetched_items