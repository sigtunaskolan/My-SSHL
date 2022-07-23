# get finish time for each day

import datetime
import requests
import json

class_6a = "MGM0ZDc2MmQtYTZkZi1mMDcyLTg0ZDgtYzFkM2Q1ZDBiZDEy"
class_5b = "YjJjNTkxZTItMDNjNS1mMDIwLTg1NWUtNzRiMzgzYzZlMmY4"
class_4a = "NDIwOTA3ZjQtYWRiZS1mNjI3LWE5NzYtMDNiNjgyZmQ4ODVk"

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


def ttable(class_id):
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
        "selection": f"{class_id}",
        "showHeader": False,
        "periodText": "",
        "week": 33,  # need to update to current week number
        "year": 2022,  # need to update to current year
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


def times(day, class_id):
    for x in ttable(class_id):
        if x["dayOfWeekNumber"] == day:
            yield x["timeEnd"]


def finish(day, class_id):
    return max(list(times(day, class_id)))


# day set to 1 for testing purposes.
def finish_today(class_id):
    return finish(1, class_id)


# end time for each class functiom:
foura = finish_today(class_4a)
fiveb = finish_today(class_5b)
sixa = finish_today(class_6a)
