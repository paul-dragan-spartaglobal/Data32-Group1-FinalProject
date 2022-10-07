-- USE master;
-- DROP DATABASE IF EXISTS [Data32ETL];
-- CREATE DATABASE [Data32ETL];
USE [Data32ETL];

CREATE TABLE Courses (
   course_id VARCHAR(20) NOT NULL PRIMARY KEY,
   course_name VARCHAR(20) NOT NULL
);

CREATE TABLE Trainers (
   trainer_id VARCHAR(20) NOT NULL PRIMARY KEY,
   trainer_name VARCHAR(20) NOT NULL
);

CREATE TABLE Students (
   student_id VARCHAR(20) NOT NULL PRIMARY KEY,
   student_name VARCHAR(30) NOT NULL,
   trainer_id VARCHAR(20) FOREIGN KEY REFERENCES Trainers(trainer_id),
   course_id VARCHAR(20) FOREIGN KEY REFERENCES Courses(course_id)
);

CREATE TABLE Languages (
   language_id int NOT NULL PRIMARY KEY,
   language_name VARCHAR(20) NOT NULL
);

CREATE TABLE Scores (
    week_id INT NOT NULL,
    student_id VARCHAR(20) FOREIGN KEY REFERENCES Students(student_id),
    imaginative_score INT,
    analytics_score INT,
    determined_score INT,
    independent_score INT,
    studious_score INT,
    professional_score INT,
    PRIMARY KEY (week_id, student_id)
);

CREATE TABLE Attributes(
	attribute_id VARCHAR(20) NOT NULL PRIMARY KEY,
	attributes VARCHAR(20),
    weaknesses BIT,
	strengths BIT
	
);


CREATE TABLE Applicants (
    applicant_id VARCHAR(20) PRIMARY KEY,
    applicant_name VARCHAR(30),
    dates VARCHAR(20),
    self_development VARCHAR(20),
    geo_flex VARCHAR(20),
    financial_support VARCHAR(20),
    result VARCHAR(20),
    course_interest VARCHAR(20)
);

CREATE TABLE Junction_table1(
	student_id VARCHAR(20) FOREIGN KEY REFERENCES Students(student_id),
	applicant_id VARCHAR(20) FOREIGN KEY REFERENCES Applicants(applicant_id),
	PRIMARY KEY(student_id, applicant_id)
);

CREATE TABLE Tech_self_score(
    applicant_id VARCHAR(20) FOREIGN KEY REFERENCES Applicants(applicant_id),
    language_id INT FOREIGN KEY REFERENCES Languages(language_id),
    score INT,
    PRIMARY KEY(applicant_id, language_id)
);


CREATE TABLE Junction_table2 (
    applicant_id VARCHAR(20) FOREIGN KEY REFERENCES Applicants(applicant_id),
    attributes_id VARCHAR(20) FOREIGN KEY REFERENCES Attributes(attribute_id),
    PRIMARY KEY(applicant_id, attributes_id)
);