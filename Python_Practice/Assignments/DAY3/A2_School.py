print("SCHOOL GRADING SYSTEM")

marks=int(input("enter the Marks : "))
if(marks>90):
    print("extra-curricular activites praticipation")
    extra_activity=input("type y or yes if participated\ntype n or no if not participated\nchoice--> ")
    if(extra_activity=='y' or extra_activity=='yes'):
        print("GRADE = A+")
    else:
        print("GRADE = A")
elif(marks>60 and marks<90):
    print("GRADE = B")
elif(marks<60):
    print("GRADE = C")
else:
    print("ivalid marks")