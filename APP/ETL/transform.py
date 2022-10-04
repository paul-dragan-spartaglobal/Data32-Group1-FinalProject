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

def table_students(raw_json_path = "All_JSON_Data.csv", raw_csv_path = "All_CSV_Data.csv"):
    df_json = pd.read_csv(raw_json_path)
    df_csv = pd.read_csv(raw_csv_path)
    students = pd.DataFrame()
    students_name = df_json[["name", "result"]].loc[df_json["result"]=='Pass']
    students['student_name'] = pd.concat([students_name['name'], df_csv['name']])
    students = students.drop_duplicates(subset = ['student_name'],keep='first')
    students.reset_index(inplace=True,drop=True)
    students.insert(0, 'student_id', range(100, 100+len(students)))
    students['student_id']= 'S' + students['student_id'].astype(str)
    students.to_csv('students.csv')
    return students

def table_scores(raw_csv_path = "All_CSV_Data.csv"):
    df_csv = pd.read_csv(raw_csv_path)
    students = table_students()
    df_csv['student_id'] = df_csv['name'].map(students.set_index('student_name')['student_id'])
    df_csv.drop(df_csv.columns[[0]],axis=1, inplace=True)
    df_csv.drop(['trainer', 'course'],axis=1, inplace=True)
    new_df = (pd.wide_to_long(df_csv, ['Analytic', 'Independent', 'Determined', 'Professional', 'Studious', 'Imaginative'],
                         i=['student_id'],
                         j='Week', 
                         sep='_', 
                         suffix='\w+')).reset_index()
    new_df["Week"] = new_df["Week"].map(lambda x: int(x.lstrip("W")))
    return new_df.sort_values(by=['student_id','Week']).reset_index(drop=True)

def applicants_table(csv_path = "All_JSON_Data.csv"):
    df_json = pd.read_csv(csv_path)
    # applicants = pd.DataFrame()
    applicants = df_json[['name', 'date', 'self_development', 'geo_flex',
                           'financial_support_self', 'result', 'course_interest']].copy()
    applicants.insert(0, 'applicant_id', range(1, 1 + len(applicants)))
    applicants['applicant_id'] = 'A' + applicants['applicant_id'].astype(str)
    return applicants

def create_trainers_table(raw_csv_path = "All_CSV_Data.csv"):
    df_csv = pd.read_csv(raw_csv_path)
    trainers = pd.DataFrame()
    trainers['trainer_name'] = df_csv['trainer']
    trainers = trainers.drop_duplicates(subset=['trainer_name'], keep='first')
    trainers.reset_index(inplace=True)
    trainers.insert(0, 'trainer_id', range(100, 100+len(trainers)))
    trainers['trainer_id']='T' + trainers['trainer_id'].astype(str)
    del trainers['index']
    print(trainers)

def course_name_table(csv_path = "All_JSON_Data.csv"):
    df_json = pd.read_csv(csv_path)
    course = pd.DataFrame()
    course['course_interest'] = df_json['course_interest']
    course = course.drop_duplicates(subset=['course_interest'], keep='first')
    course.reset_index(inplace=True)
    course.insert(0, 'course_id', range(100, 100+len(course)))
    course['course_id'] = 'C' + course['course_id'].astype(str)
    del course['index']
    print(course)

def language_table(csv_path = "All_JSON_Data.csv"):
    data = pd.read_csv(csv_path)
    tech_data = data.filter(regex='tech_self_score')
    languages_list = []
    for col in tech_data.columns:
        col = col.split('.')[1]
        languages_list.append(col)
    language = pd.DataFrame(languages_list, columns=['language_name'])
    language.insert(0, 'language_id', range(1, 1 + len(language)))
    print(language)

if __name__ == '__main__':
    print(language_table())