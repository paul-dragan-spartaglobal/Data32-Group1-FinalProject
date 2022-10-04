import pandas as pd
import pyodbc
import csv
import os

#Get the current working directory (cwd)
# cwd=os.getcwd()
# Get all the files in that directory
# files = os.listdir(cwd)
# print("Files in %r: %s" % (cwd, files))

df_csv = pd.read_csv("All_CSV_Data.csv")
df_json = pd.read_csv("All_JSON_Data.csv")

def get_strengths():

    strengths_list=[]
    distinct_strengths=[]
    strengths = df_json["strengths"]
    set_strengths =set()
    for strength in strengths:
        strengths_list.append(strength)
    for element in strengths_list:
        # print(element)
        replaced_element = element.replace("'","")
        stripped_element = replaced_element.strip("[]")
        split_element = stripped_element.split(", ")
        for object in split_element:
            set_strengths.add(object)
    list1=list(set_strengths)
    df_strengths = pd.DataFrame(list1,columns=["attributes"])
    df_strengths["strengths"]=True
    return df_strengths


def get_weakness():

    weaknesses_list=[]
    distinct_strengths=[]
    weaknesses = df_json["weaknesses"]
    set_weaknesses =set()
    for weakness in weaknesses:
        weaknesses_list.append(weakness)
    for element in weaknesses_list:
        # print(element)
        replaced_element = element.replace("'","")
        stripped_element = replaced_element.strip("[]")
        split_element = stripped_element.split(", ")
        for object in split_element:
            set_weaknesses.add(object)
    list2 = list(set_weaknesses)
    df_weakness = pd.DataFrame(list2, columns=["attributes"])
    df_weakness["weakness"] = True
    return df_weakness

def get_all_attributes():
    df_all_attributes = pd.concat([get_weakness(), get_strengths()], ignore_index=True)
    return df_all_attributes

def get_attributes_table():
    attributes = pd.DataFrame()
    attributes = pd.concat([attributes,get_all_attributes()], ignore_index=True)
    attributes.reset_index(inplace=True)
    attributes.insert(0, 'attribute_id', range(100, 100+len(attributes)))
    attributes['attribute_id']= 'ATR' + attributes['attribute_id'].astype(str)
    del attributes['index']
    print(attributes)
    return attributes

get_attributes_table()