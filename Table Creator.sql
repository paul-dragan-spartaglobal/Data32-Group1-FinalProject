DROP DATABASE IF EXISTS academy;
CREATE DATABASE academy;
USE academy;
CREATE TABLE Courses (
   course_id varchar NOT NULL PRIMARY KEY,
   course_name VARCHAR(20) NOT NULL
);

CREATE TABLE Trainer (
   trainer_id varchar NOT NULL PRIMARY KEY,
   trainer_name VARCHAR(20) NOT NULL
);

CREATE TABLE Students (
   student_id varchar NOT NULL PRIMARY KEY,
   student_name VARCHAR(20) NOT NULL,
   trainer_id VARCHAR,
   course_id varchar
);
CREATE TABLE Languages (
   language_id int NOT NULL PRIMARY KEY,
   language_name VARCHAR(10) NOT NULL
);

CREATE TABLE Scores (
    week_id int NOT NULL,
    student_id varchar FOREIGN KEY REFERENCES Students(student_id),
    imaginative_score float,
    analytics_score float,
    determined_score float,
    independent_score float,
    studious_score float,
    professional_score float,
    PRIMARY KEY (week_id, student_id)
);



CREATE TABLE Attributes(
	attribute_id varchar NOT NULL,
	attributes varchar,
    weaknesses Boolean,
	strengths Boolean
	
);


CREATE TABLE Fact_table(
	student_id varchar FOREIGN KEY REFERENCES Students(student_id),
	applicant_id varchar FOREIGN KEY REFERENCES Applicants(applicant_id),
	
);

CREATE TABLE Applicants (
    applicant_id varchar PRIMARY KEY REFERENCES Fact_table(applicant_id),
    applicant_name VARCHAR,
    dates datetime,
    self_development VARCHAR,
    geo_flex varchar,
    financial_support varchar,
    result varchar,
    course_interest VARCHAR
);

CREATE TABLE Tech_self_score(
    applicant_id varchar FOREIGN KEY REFERENCES Applicants(applicant_id),
    language_id INT FOREIGN KEY REFERENCES Languages(language_id),
    score INT,
    PRIMARY KEY(applicant_id, language_id)
);


CREATE TABLE Applicant_attributes (
    applicant_id varchar FOREIGN KEY REFERENCES Applicants(applicant_id),
    attributes_id varchar FOREIGN KEY REFERENCES Attributes(attribute_id),
    PRIMARY KEY(applicant_id, attributes_id)
);