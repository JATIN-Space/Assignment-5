student_marks={"Rahul":83,"Keshav":98,"Jaskeerat":87,"Alice":86,"Jatin":99,"Rishad":78}
name=input("Enter the student's name:")
if name in student_marks:
    print(f"{name}'s marks:{student_marks[name]}")
else:
    print("Student not found.")