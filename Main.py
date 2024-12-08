# main.py

# TODO 0: import the functions in registration.py module.
from registration import (read_enrollment, enrollment_update, add_enrollment, reg_summary)

course_names = ['Programming', 'Biology', 'Art']
# this list will store the number of enrollment for programming, biology, and art courses in order
enroll = [0, 0, 0]

# TODO 1: display the data from registration.txt file(i.e., list of the courses) in the console
read_enrollment()

# TODO 2: read the lines from registration.txt file and update the enroll[] list
enrollment_update(enroll)

# Adding 5 random enrollments.
add_enrollment()

# Displaying the summary
reg_summary()
