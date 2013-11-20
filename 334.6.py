# Problem 6
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
        letterGrade = input("Please enter the letter grade earned by the student. ")
        a_student.addLetterGrade(letterGrade, credits)
        keepgoing = input("Type any key to enter another course or type enter to quit. ")
        print ()

    #Print results
    GPA = a_student.gpa()
    print ("The student's GPA is: ", GPA)





if __name__ == '__main__':
    main ()
