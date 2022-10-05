CREATE TABLE Courses (
   course_id int NOT NULL PRIMARY KEY,
   course_name VARCHAR(20) NOT NULL
);

CREATE TABLE Trainer (
   trainer_id int NOT NULL PRIMARY KEY,
   trainer_name VARCHAR(20) NOT NULL
);

CREATE TABLE Students (
   student_id int NOT NULL PRIMARY KEY,
   student_name VARCHAR(20) NOT NULL
);
CREATE TABLE Languages (
   language_id int NOT NULL PRIMARY KEY,
   language_name VARCHAR(10) NOT NULL
);

CREATE TABLE Scores (
    week_id int NOT NULL,
    student_id int FOREIGN KEY REFERENCES Students(student_id),
    imaginative_score int,
    analytics_score int,
    determined_score int,
    independent_score int,
    studious_score int,
    professional_score int,
    PRIMARY KEY (week_id, student_id)
);



CREATE TABLE Attributes(
	attribute_id int NOT NULL,
	attribute_name varchar,
	strengths varchar,
	weaknesses varchar
)


CREATE TABLE Fact_table(
	record_id int NOT NULL PRIMARY KEY,
	trainer_id int FOREIGN KEY REFERENCES Trainer(trainer_id) ,
	student_id int FOREIGN KEY REFERENCES Students(student_id),
	applicant_id int FOREIGN KEY REFERENCES Applicants(applicant_id),
	course_id int FOREIGN KEY REFERENCES Courses(course_id)
)

CREATE TABLE Applicants (
    applicant_id INT PRIMARY KEY REFERENCES Fact_table(applicant_id),
    applicant_name VARCHAR,
    dates datetime,
    self_development VARCHAR,
    geo_flex Boolean,
    financial_support Boolean,
    result Boolean,
    course_interest VARCHAR
)

CREATE TABLE Tech_self_score(
    applicant_id INT FOREIGN KEY REFERENCES Applicants(applicant_id),
    language_id INT FOREIGN KEY REFERENCES Languages(language_id),
    score INT,
    PRIMARY KEY(applicant_id, language_id)
)


CREATE TABLE Applicant_attributes (
    applicant_id INT FOREIGN KEY REFERENCES Applicants(applicant_id),
    attributes_id INT FOREIGN KEY REFERENCES Attributes(attribute_id),
    PRIMARY KEY(applicant_id, attributes_id)
)