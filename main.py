import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'English']


# task 1
def students_with_failed_courses(grades: pd.DataFrame) -> pd.DataFrame:
    filtered_students = grades.loc[grades[subjects].lt(50).any(axis=1)]
    unique_students = filtered_students.drop_duplicates(subset=['Student'], keep='first').loc[:, ['Student']]
    return unique_students


# task 2
def average_grade_per_subject(grades: pd.DataFrame) -> pd.DataFrame:
    return grades.groupby('Semester')[subjects].mean()


# task 4
def hardest_subject(grades: pd.DataFrame) -> tuple:
    subject_averages = grades[subjects].mean()
    result_subject = subject_averages.idxmin()
    result_average = subject_averages.min()
    return result_subject, result_average


# task 3
def highest_average_student(grades: pd.DataFrame):
    grades['Average'] = grades[subjects].mean(axis=1)
    overall_average = grades.groupby('Student')['Average'].mean()
    top_student = overall_average.idxmax()
    highest_average = overall_average.max()
    return top_student, highest_average


# task 5
def write_average_grades(average_grades: pd.DataFrame):
    average_grades.to_excel('average_grades.xlsx')


# task 6 (visualisation)
def visualise_average_grade_per_semester(average_grades: pd.DataFrame):
    index = []
    for i in range(1, 8):
        index.append(f"Semester {i}")

    average_grades = pd.DataFrame(average_grades, index=index)
    average_grades.reset_index(inplace=True)
    average_grades.rename(columns={'index': 'Semester'}, inplace=True)
    grades_melted = pd.melt(average_grades, id_vars='Semester', var_name='Subject', value_name='Average Grade')
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Semester', y='Average Grade', hue='Subject', data=grades_melted)
    plt.title('Average Grades per Subject in Each Semester', fontsize=16)
    plt.xlabel('Semester', fontsize=12)
    plt.ylabel('Average Grade', fontsize=12)
    plt.show()


def average_grade_per_semester(grades: pd.DataFrame):
    grades_without_student = grades.drop('Student', axis=1)
    semester_avg = grades_without_student.groupby('Semester').mean()
    semester_avg['Overall Average'] = semester_avg.mean(axis=1)
    plt.figure(figsize=(10, 6))
    plt.plot(semester_avg.index, semester_avg['Overall Average'], marker='o')
    plt.title('Overall Average Grade per Semester', fontsize=16)
    plt.xlabel('Semester', fontsize=12)
    plt.ylabel('Overall Average Grade', fontsize=12)
    plt.show()


if __name__ == '__main__':
    subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'English']
    # pd.set_option('display.max_rows', None)
    # pd.set_option('display.max_columns', None)
    grades = pd.read_csv('student_scores_random_names.csv')

    # task 1
    failed_students = students_with_failed_courses(grades)
    print("|||||||||||||||||||||||||||||||||||||||||||students who failed||||||||||||||||||||||||||||||||||")
    print(failed_students)
    # task 2
    print("|||||||||||||||||||||||||||||||||||||||||||average grades per semester||||||||||||||||||||||||||")
    average_grades_per_semester = average_grade_per_subject(grades)
    print(average_grades_per_semester)
    # task 3
    print("|||||||||||||||||||||||||||||||||||||||||||student with highest average|||||||||||||||||||||||||")
    student, grade = highest_average_student(grades)
    print(student, grade)

    # task 4
    print("||||||||||||||||||||||||||||||||||||||||||hardest subject|||||||||||||||||||||||||||||||||||||||")
    hardest_subject, lowest_average = hardest_subject(grades)
    print(hardest_subject, lowest_average)

    # task 5
    write_average_grades(average_grades_per_semester)

    # task 6 (visualisation 1)
    visualise_average_grade_per_semester(average_grades_per_semester)

    # task 7
    average_grade_per_semester(grades)
