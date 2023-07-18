# Course Management System

# Course details
course = {}

# List of students
students = []

# Step 2: Creating a function to add a course.
def add_course(name, duration, modules, fee):
    course['name'] = name                           #Assigns the value of the name parameter to the 'name' key in the course dictionary.
    course['duration'] = duration                   #Assigns the value of the duration parameter to the 'duration' key in the course dictionary.
    course['modules'] = modules                     #Assigns the value of the modules parameter to the 'modules' key in the course dictionary.
    course['fee'] = fee                             #Assigns the value of the fee parameter to the 'fee' key in the course dictionary.

# Step 3: Creating a function to add students to the course.
def add_student(name, fee):
    students.append({'name': name, 'fee': fee})     #'name': name assigns the value of the name parameter to the 'name' key in the student dictionary.
                                                    #'fee': fee assigns the value of the fee parameter to the 'fee' key in the student dictionary.
# Step 4: Creating a function to display the course details.
def display_course():
    print("Course Name:", course['name'])           #prints the value associated with the 'name' key in the course dictionary. It assumes that the course dictionary is accessible within the scope of the display_course function.
    print("Course Duration:", course['duration'])   #prints the value associated with the 'duration' key in the course dictionary.
    print("Course Modules:", course['modules'])     #prints the value associated with the 'modules' key in the course dictionary.
    print("Course Fee:", course['fee'])             #prints the value associated with the 'fee' key in the course dictionary.

# Step 5: Creating a function to display the students in the course.
def display_students():
    for student in students:
        print("Student Name:", student['name'])     #prints the value associated with the 'name' key in the current student dictionary. It assumes that each student is a dictionary with a 'name' key.
        print("Student Fee:", student['fee'])       #prints the value associated with the 'fee' key in the current student dictionary. It assumes that each student is a dictionary with a 'fee' key.

# Step 6: Test the functions.
add_course('Python Programming', '3 months', ['Introduction', 'Advanced Concepts', 'Project'], 500)
add_student('John Doe', 500)
display_course()
display_students()