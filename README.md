# Course Registration System  

A Python-based program that manages and summarizes student course registrations. This project demonstrates fundamental file handling, global variable management, and the use of functions for handling course enrollments in a simple registration system.

---

## Features  

- Reads course registration data from a file (`registration.txt`).  
- Updates the enrollment numbers for available courses.  
- Simulates random student enrollments.  
- Displays a summary of the total enrollment and identifies the most popular course.  

---

## Files  

1. **`Main.py`**  
   - The main script to execute all functionalities, including reading, updating, and summarizing course enrollments.  
   - Includes integration with `registration.py`.  

2. **`registration.py`**  
   - Contains core functions:  
     - `read_enrollment()` - Reads and displays the list of available courses from `registration.txt`.  
     - `enrollment_update(enrollment)` - Updates enrollment data from the file.  
     - `add_enrollment()` - Adds random enrollments to courses.  
     - `reg_summary()` - Generates and displays an enrollment summary, including waitlist and most popular course statistics.  

---

## Example Output

Here are the course lists:
Programming
Biology
Art

Adding enrollment in Biology
Adding enrollment in Art

REGISTRATION SUMMARY
10 students enrolled in Programming. There are 0 people on the waitlist.
12 students enrolled in Biology. There are 0 people on the waitlist.
15 students enrolled in Art. There are 0 people on the waitlist.

The most popular course in Winter is Art, 37.50%!

---

## Dependencies

Python 3.6+
No external libraries required.

