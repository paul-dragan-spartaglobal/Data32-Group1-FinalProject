import boto3
import pyodbc
import pprint as pp
import json
import pandas as pd

#connect to boto and s3 server and the desired bucket
s3_client = boto3.client('s3')
bucket_list = s3_client.list_buckets()
bucket_name = "data32-final-project-files"

s3_resource= boto3.resource("s3")
bucket = s3_resource.Bucket(bucket_name)


#create new json file with the keys and timestamps (only used once)
def original_timestamps():
    bucket_contents = s3_client.list_objects_v2(Bucket = bucket_name)['Contents']
    time_stamps = {}
    for item in bucket_contents:
        time_stamps[item['Key']] = str(item["LastModified"])
    with open("timestamps.json","w") as file:
        file.write(json.dumps(time_stamps))

# original_timestamps()


def current_timestamps():
    try:
        with open("timestamps.json", "r") as file:
            old_timestamps = json.load(file)
    except FileNotFoundError:
        original_timestamps()
        with open("timestamps.json", "r") as file:
            old_timestamps = json.load(file)
    return old_timestamps

def compare():
    bucket_contents = s3_client.list_objects_v2(Bucket = bucket_name)['Contents']
    time_stamps = {}
    for item in bucket_contents:
        time_stamps[item['Key']] = str(item["LastModified"])

    if current_timestamps() == time_stamps:
        print("up to date")
    else:
        original_timestamps()
        print("please run the main file for an update")
current_timestamps()
compare()




