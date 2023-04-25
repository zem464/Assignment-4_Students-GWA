# Zemerelin Iris M. Membrere
# BSCPE 1-4
# Assignment 4

# Problem 2 - The one with the highest GWA among 20 students

# Create and open the file with students and gwa
with open("students_gwa.txt") as student_file:
    # Initialize lowest possible gwa and student name
    gwa_equivalent = 5.0
    gwa_student = ""
    # Read the file line by line
    for line in student_file:
        # Split the name and gwa
        name, gwa_str = line.strip().split(" : ")
        # if gwa is lower than the initialized gwa, get the highest gwa and name
        gwa = float(gwa_str)
        if gwa < gwa_equivalent:
            gwa_equivalent = gwa
            gwa_student = name
# Print the name with highest gwa
print("\033[31m\033[1mHighest GWA awardee: \033[35m\033[0m", gwa_student)
print("\033[31m\033[1mGWA: \033[35m\033[0m", gwa_equivalent)