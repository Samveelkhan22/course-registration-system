import random
# Define course_names and enroll as global variables
course_names = ['Programming', 'Biology', 'Art']
enroll = [0, 0, 0]

def read_enrollment():
    # a function to open a file, registration.txt, name the file object to "file_registration",
    # and display the list of the courses
    with open("registration.txt", 'r') as file_registration:
        courses = file_registration.readlines()
        print("Here are the course lists:")
        for course in courses:
            print(course.strip())

def enrollment_update(enrollment):
    with open("registration.txt", 'r') as file_registration:
        lines = file_registration.readlines()
        for line in lines:
            parts = line.strip().split()
            if parts and parts[0].isdigit():
                course_number = int(parts[0])
                if 1 <= course_number <= len(enrollment):
                    enrollment[course_number - 1] += 1

    print(f"The enrollment list is {enrollment} {sum(enrollment)}")

def add_enrollment():
    # a function to add 5 randomly generated enrollments
    for _ in range(5):
        random_course = random.choice(course_names)
        print(f"Adding enrollment in {random_course}")
        enrollment_update(enroll)

def reg_summary():
    total_students = sum(enroll)

    if total_students == 0:
        print("\nREGISTRATION SUMMARY\nNo students enrolled.")
        return

    print("\nREGISTRATION SUMMARY")
    for i, course in enumerate(course_names):
        enrolled_students = enroll[i]
        waitlist = max(0, enrolled_students - 25)
        print(f"{enrolled_students} students enrolled in {course}. There are {waitlist} people on the waitlist.")

    most_popular_index = enroll.index(max(enroll))
    most_popular_course = course_names[most_popular_index]
    most_popular_percentage = (enroll[most_popular_index] / total_students) * 100
    print(f"\nThe most popular course in Winter is {most_popular_course}, {most_popular_percentage:.2f}%!")
