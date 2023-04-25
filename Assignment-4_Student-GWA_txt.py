# Zemerelin Iris M. Membrere
# BSCPE 1-4
# Assignment 4

# Problem 2 - The one with the highest GWA among 20 students

# Create and open the file with students and gwa
with open("students_gwa.txt") as student_file:
    # Initialize lowest possible gwa and student name
    gwa_equivalent = 5.0
    gwa_student = ""