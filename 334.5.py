# Problem 5
from student import Student

def main ():

    #Introduction
    print ("This program accepts course information for one student in order to compute GPA. ")
    print ()

    #Create student object
    a_student = Student("student", 0, 0)

    #User enters information for each course
    keepgoing = input("Type any key to enter another course or type enter to quit. ")
    while keepgoing != '':
        credits = eval(input("Please enter the number of credits in the course. "))
        gradePoint = eval(input("Please enter the number grade earned by the student (ex:3.7). "))
        a_student.addGrade(gradePoint, credits)
        keepgoing = input("Type any key to enter another course or type enter to quit. ")

    #Print results
    GPA = round(astudent.gpa(), 1)
    print ("The student's GPA is: ", GPA)





if __name__ == '__main__':
    main ()
