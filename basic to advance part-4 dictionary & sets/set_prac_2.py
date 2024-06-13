#  You are given a list of subjects for students. Assume one classroom is required for 1
#  subject. How many classrooms are needed by all students.
#  ”python”, “java”, “C++”, “python”, “javascript”,
#  “java”, “python”, “java”, “C++”, “C”

subjects = {"python", "java", "c++", "python", "js", "java", "python", "java", "c++", "c"}

print("classrooms are needed by all students : ", subjects.__len__())