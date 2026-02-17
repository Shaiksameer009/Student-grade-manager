#Task 1: Create and write student data
file = open("students.txt", "w")  # 'w' mode creates/overwrites the file
file.write("Alice,85\n")
file.write("Bob,92\n")
file.write("Charlie,78\n")
file.write("Diana,95\n")
file.close()  
print("Student records written successfully.")
