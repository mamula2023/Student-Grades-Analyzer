# Overview
This project analyzes student grades across various subjects and semesters, providing insights into student performance, including identifying students who have failed courses, calculating average grades, and visualizing performance trends.

## Features
Identify Students with Failed Courses: Retrieve a list of students who have received grades below 50 in any subject in any semester
Calculate Average Grades: Compute average grades per subject for each semester.
Identify the Student with the Highest Average: Find the student with the highest overall average grade across all subjects and semesters.
Determine the Hardest Subject: Identify which subject has the lowest average grade across all 8 semesters
Export Average Grades to Excel: Write the calculated average grades to an Excel file.
Visualize Average Grades per Semester: Create a bar plot showing average grades per subject for each semester.
Visualize Overall Average Grade per Semester: Generate a line plot for the overall average grade per semester.


## Usage
Prepare the Dataset: Ensure that you have a CSV file named `student_scores_random_names.csv` in the same directory as the script. The CSV should contain the following columns:

- Student: Student names
- Semester: Semester numbers
- Math, Physics, Chemistry, Biology, English: Grades for each subject

### Run the Script
Execute the script to perform the analyses and visualizations.

```
python main.py
```

### Output
The script will print the results of each analysis to the console.
Average grades will be exported to an Excel file named `average_grades.xlsx`.
Visualization plots will be displayed using Matplotlib.

## Requirements
install required Python packages
```
pip install -r requirements.txt
```







