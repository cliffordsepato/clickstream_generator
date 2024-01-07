#Script to generate clickstream data.
import json
import random
from datetime import datetime
import sys
import time
import hashlib
import boto3

# Get the number of records and the maximum delay between events from the command line arguments
RECORDS = int(sys.argv[1])
MAX_SECONDS_BETWEEN_EVENTS= int(sys.argv[2])

# Function to generate a unique event ID[^1^][1]
def get_event_id():
    hashed = hashlib.md5(datetime.now().strftime("%m/%d/%YT%H:%M:%S.%f").encode())
    
    return hashed.hexdigest()

# Function to get a random event type
def get_event():
    events = [
        "purchased_item", "liked_item", "reviewed_item", "entered_payment_method",
        "clicked_review", "clicked_item_description"
    ]

    return random.choice(events)

# Function to get a random user ID
def get_user_id():
    MAX_USER_ID = 100

    return random.randint(1, MAX_USER_ID)

# Function to get the current event time
def get_event_time():
    return datetime.now().strftime("%m/%d/%YT%H:%M:%S.%f")

# Function to get a random operating system
def get_os():
    os = ["ios", "android", "web"]

    return random.choice(os)

# Function to get a random page
def get_page():
    pages = ["apparal/", "/food/", "/electronics/", "/home/", "/books/"]

    return random.choice(pages)

# Create an S3 client
s3 = boto3.client('s3')

for _ in range(RECORDS):
    # Generate a random delay between events
    delay = random.randint(0, MAX_SECONDS_BETWEEN_EVENTS)
    time.sleep(delay)

    # Generate a random event
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

    # Convert the event to JSON
    event_json = json.dumps(event)

    # Upload the event to S3
    object_name = f"{get_event_id()}.json"
    s3.put_object(Bucket='my-clickstream-bucket', Key=object_name, Body=event_json)

    # Print a message to indicate that the event was uploaded to S3
    print(f"Uploaded event {object_name} to S3 bucket my-clickstream-bucket")


