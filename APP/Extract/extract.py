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

def get_keys(bucket_name = 'data32-final-project-files'):

    bucket_contents = s3_client.list_objects_v2(Bucket = bucket_name)['Contents']
    csv_keys , json_keys = [],[]
    #loop through the content of a bucket and get the keys
    for object in bucket_contents:
        #save csv key into csv key list
        if object['Key'].endswith('.csv'):
            csv_keys.append(object['Key'])
        #save json key into json list
        else:
            json_keys.append(object['Key'])
    #return a list of keys
    return csv_keys, json_keys



def export_academy(csv_keys):
    # loop through the buckets which are with fish files
    df_all = pd.DataFrame()
    for object in csv_keys:
        # read inside the bucket
        s3_object = s3_client.get_object(Bucket=bucket_name, Key=object)
        # read the body of the fish file with the fish data
        df = pd.read_csv(s3_object["Body"])
        df["course"] =  object.split("/")[1].split("_")[0]
        df_all = pd.concat([df_all, df],ignore_index=True)
    df_all.to_csv("All_CSV_Data.csv")
# export_academy()

def export_talent(json_keys):
    json_all=[]
    df2 = pd.DataFrame()
    for object in json_keys:
        # read inside the bucket
        s3_object = s3_client.get_object(Bucket=bucket_name, Key=object)
        # read the body of all json files
        strbody = s3_object["Body"].read()
        # normalise the jason rows which have data in a list or dictionary
        df3 = pd.json_normalize(json.loads(strbody), max_level=1)
        #concatenate all the files into a data frame
        df2 = pd.concat([df2, df3], ignore_index=True)
    #convert the dataframe with all details into a CSV file
    df2.to_csv("All_JSON_Data.csv")


csv_keys, json_keys = get_keys()
get_keys()
# export_academy(csv_keys)
export_talent(json_keys)