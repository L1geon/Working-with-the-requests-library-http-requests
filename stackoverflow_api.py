import requests
from pprint import pprint


def get_questions(tag: str):
    s_tag = tag
    url = fr"https://api.stackexchange.com/2.3/search?page=25&pagesize=40&fromdate=1655596800&todate=1655683200&order=desc&sort=activity&tagged=%22{s_tag}%22&site=stackoverflow"
    r = requests.get(url)
    pprint(r.json())
    data = r.json()
    print("Всего таких вопросов", len(data["items"]))

