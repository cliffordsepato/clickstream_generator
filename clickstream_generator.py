#Script to generate clickstream data.
import json
import random
from datetime import datetime
import sys
import time
import hashlib

RECORDS = int(sys.argv[1])
MAX_SECONDS_BETWEEN_EVENTS= int(sys.argv[2])

def get_event_id():
    hashed = hashlib.md5(datetime.now().strftime("%m/%d/%YT%H:%M:%S.%f").encode())
    
    return hashed.hexdigest()

def get_event():
    events = [
        "purchased_item", "liked_item", "reviewed_item", "entered_payment_method",
        "clicked_review", "clicked_item_description"
    ]

    return random.choice(events)

def get_user_id():
    MAX_USER_ID = 100

    return random.randint(1, MAX_USER_ID)

def get_event_time():
    return datetime.now().strftime("%m/%d/%YT%H:%M:%S.%f")

def get_os():
    os = ["ios", "android", "web"]

    return random.choice(os)

def get_page():
    pages = ["apparal/", "/food/", "/electronics/", "/home/", "/books/"]

    return random.choice(pages)

for _ in range(RECORDS):
    delay = random.randint(0, MAX_SECONDS_BETWEEN_EVENTS)
    time.sleep(delay)

    event = {
        "event_id": get_event_id(),
        "event": get_event(),
        "user_id": get_user_id(),
        "event_time": get_event_time(),
        "os": get_os(),
        "properties": {
            "page": get_page(),
            "url": "www.fakesite.com"
        }
    }

    print(json.dumps(event))


