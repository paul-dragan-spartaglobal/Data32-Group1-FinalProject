USE master;
DROP DATABASE IF EXISTS Data32ETL;
CREATE DATABASE Data32ETL;
USE Data32ETL;

CREATE TABLE Courses (
   course_id VARCHAR NOT NULL PRIMARY KEY,
   course_name VARCHAR(20) NOT NULL
);

CREATE TABLE Trainer (
   trainer_id VARCHAR NOT NULL PRIMARY KEY,
   trainer_name VARCHAR(20) NOT NULL
);

CREATE TABLE Students (
   student_id VARCHAR NOT NULL PRIMARY KEY,
   student_name VARCHAR(20) NOT NULL,
   trainer_id VARCHAR FOREIGN KEY REFERENCES Trainer(trainer_id),
   course_id VARCHAR FOREIGN KEY REFERENCES Courses(course_id)
);

CREATE TABLE Languages (
   language_id int NOT NULL PRIMARY KEY,
   language_name VARCHAR(10) NOT NULL
);

CREATE TABLE Scores (
    week_id INT NOT NULL,
    student_id VARCHAR FOREIGN KEY REFERENCES Students(student_id),
    imaginative_score FLOAT,
    analytics_score FLOAT,
    determined_score FLOAT,
    independent_score FLOAT,
    studious_score FLOAT,
    professional_score FLOAT,
    PRIMARY KEY (week_id, student_id)
);



CREATE TABLE Attributes(
	attribute_id VARCHAR NOT NULL PRIMARY KEY,
	attributes VARCHAR,
    weaknesses BIT,
	strengths BIT
	
);


CREATE TABLE Applicants (
    applicant_id VARCHAR PRIMARY KEY,
    applicant_name VARCHAR,
    dates DATETIME,
    self_development VARCHAR,
    geo_flex VARCHAR,
    financial_support VARCHAR,
    result VARCHAR,
    course_interest VARCHAR
);

CREATE TABLE Junction_table1(
	student_id VARCHAR FOREIGN KEY REFERENCES Students(student_id),
	applicant_id VARCHAR FOREIGN KEY REFERENCES Applicants(applicant_id),
	PRIMARY KEY(student_id, applicant_id)
);

CREATE TABLE Tech_self_score(
    applicant_id VARCHAR FOREIGN KEY REFERENCES Applicants(applicant_id),
    language_id INT FOREIGN KEY REFERENCES Languages(language_id),
    score INT,
    PRIMARY KEY(applicant_id, language_id)
);


CREATE TABLE Junction_table2 (
    applicant_id VARCHAR FOREIGN KEY REFERENCES Applicants(applicant_id),
    attributes_id VARCHAR FOREIGN KEY REFERENCES Attributes(attribute_id),
    PRIMARY KEY(applicant_id, attributes_id)
);