# Task 3: Append new student and create log file
with open("students.txt", "a") as file:  # 'a' mode appends data
    file.write("Eve,88\n")
with open("activity.log", "w") as log_file:
    log_file.write("Added new student: Eve\n")
print("New student added and activity logged.")
