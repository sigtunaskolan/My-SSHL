# get finish time for each day

import requests
import json

headers = {
    "Content-Type": "application/json",
    "X-Scope": "8a22163c-8662-4535-9050-bc5e1923df48",
}


def key():
    url_key = "https://web.skola24.se/api/get/timetable/render/key"
    payload_key = "null"
    r_k = requests.post(url_key, headers=headers, data=payload_key)
    js = r_k.json()

    if r_k.ok:
        try:
            key = js["data"]["key"]
            return key
        except KeyError:
            return "Key not found"
    else:
        return "Error"


def ttable():
    url_ttable = "https://web.skola24.se/api/render/timetable"
    payload_ttable = {
        "renderKey": f"{key()}",
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

    r_t = requests.post(url_ttable, headers=headers, json=payload_ttable)
    js_t = r_t.json()

    if r_t.ok:
        try:
            return js_t["data"]["lessonInfo"]
        except KeyError:
            return "Error_ttable"


def times(day):
    for x in ttable():
        if x["dayOfWeekNumber"] == day:
            yield x["timeEnd"]


def finish(day):
    return max(list(times(day)))
