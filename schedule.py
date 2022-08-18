# get finish time for each day

import datetime
import requests
import json
from variablesBE import *


def key():
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
    payload_ttable = {
        "renderKey": f"{key()}",
        "host": "sshl.skola24.se",
        "unitGuid": "NGIwYjNiM2UtNzcwNi1mNzc4LTgxZDYtYWY0M2Q4OGM5YzE1",
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
        "week": 34,  # update to this when w34 reached: datetime.date.today().isocalendar()[1]
        "year": datetime.date.today().isocalendar()[0],
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


def finish_today(class_id):
    return finish(datetime.datetime.today().isoweekday(), class_id)[:-3].strip()


# class finish times
dp23 = finish_today(d23)
dp24 = finish_today(d24)
myp5a = finish_today(m5a)
myp5b = finish_today(m5b)

print(dp24)
