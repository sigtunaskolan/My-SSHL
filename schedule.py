import requests
import json

url = "https://web.skola24.se/api/get/timetable/render/key"
url_2 = "https://web.skola24.se/api/render/timetable"

payload = "null"
headers = {
    "Content-Type": "application/json",
    "X-Scope": "8a22163c-8662-4535-9050-bc5e1923df48",
}

r = requests.post(url, headers=headers, data=payload).json()
k = r["data"]["key"]


p_2 = {
    "renderKey": f"{k}",
    "host": "boras.skola24.se",
    "unitGuid": "M2E2ZjI4Y2UtNDFhYS1mNWFhLWE4NTQtMTI2YWYyYzk1MWU2",
    "startDate": None,
    "endDate": None,
    "scheduleDay": 0,
    "blackAndWhite": False,
    "width": 1280,
    "height": 720,
    "selectionType": 0,
    "selection": "MGM0ZDc2MmQtYTZkZi1mMDcyLTg0ZDgtYzFkM2Q1ZDBiZDEy",
    "showHeader": False,
    "periodText": "",
    "week": 33,
    "year": 2022,
    "privateFreeTextMode": None,
    "privateSelectionMode": False,
    "customerKey": "",
}

s = requests.post(url_2, headers=headers, json=p_2).json()

print(s["data"]["lessonInfo"])
