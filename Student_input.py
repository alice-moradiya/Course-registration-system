from audioop import add
from optparse import Option



class student1:
    # Student_name, Student_ID, Email_ID, Privious_courses, Grades, current_courses
    def __init__(self, stdinfo):
        self.Student_name = stdinfo[0]
        self.Student_ID = stdinfo[1]
        self.Email_ID = stdinfo[2]
        self.Privious_courses = stdinfo[3].split(",")
        Grades = []
        Grades.append(stdinfo[4])
        self.Grades = Grades
        self.Current_courses = stdinfo[5].split(",")

class course:
    def __init__(self,courseinfo):
        self.course_number = courseinfo[0]
        self.course_name = courseinfo[1]
        self.course_dateday = courseinfo[2]
        self.course_Credits = courseinfo[3]
        self.course_instucter = courseinfo[4]
        self.class_location = courseinfo[5]
        self.course_prereq = courseinfo[6]
        


# reading studentfile
# studentfile = open("services/student.txt", "r")
studentfile = open("student.txt", "r")
temp = []
temp2 = []
for line in studentfile:
    temp.append(line.strip().split(' '))
for i in range(len(temp)):
    temp2.append(temp[i])
studentfile.close()

# reading coursefile
# coursefile = open("services/course.txt", "r")
coursefile = open("course.txt", "r")
tempcourse3 = []
tempcourse4 = []
for line in coursefile:
    tempcourse3.append(line.strip().split(','))
for i in range(len(tempcourse3)):
    tempcourse4.append(tempcourse3[i])
# print(tempcourse4)



           
         
            
            
       
def options_func():
    
    option=1
    while(option!=4):
              print("1. student report \n 2. Register students into a course \n 3. Add new  courses into the student's current course \n 4. exit")
              option = int(input("choose from above iptions"))
              
              if(option>3 or option<0 or type(option)!= int) : 
                        print("please enter a valid option ")
              elif (option==1):
                  student_report()
              elif(option==2):
                  add_multiple_Courses() 
                  
              elif(option ==3):
                    add_multiple_students()
              elif(option ==4):
                     return    
                       
def student_registration():
        z = int(input("enter student number for the student registration:"))
        

        details = ["Name", "id", "Email",
                   "Previous Courses", "Grades", "current courses"]
        print("\n")
        stdobj = student1(temp2[z-1])

        for j in range(len(temp2[z-1])):

            print(details[j] + ": "+temp2[z-1][j])
        print("\n")
        coursesnames=[]
        for i in range(len(tempcourse4)-1):
              coursesnames.append(tempcourse4[i][0]+tempcourse4[i][1])
        for i in range(len(coursesnames)):
            print(str(i+1) + " " + coursesnames[i] )
        addcourse = int(input("enter course number from above options that student want to register:"))
        if(type(addcourse)!= int or addcourse<=0 or addcourse>10):
            print("please enter valid value from 1 to 10")
        else:
            check = False
            
            for i in range(len(stdobj.Privious_courses)):
                # print(tempcourse4[addcourse-1][6])
                if(stdobj.Privious_courses[i] == tempcourse4[addcourse-1][6] ):
                  check=True
                  return
            if(tempcourse4[addcourse-1][6]=="-" or check == True):
              temp[z-1][5] = temp[z-1][5]+","+coursesnames[addcourse-1] 
              stdobj.Current_courses.append(coursesnames[addcourse-1]) 
            else:
                print("you cannot add " , coursesnames[addcourse-1] , " because you didn't took " , tempcourse4[addcourse-1][6] ) 

        
       
        print(details[j] + ": ")
        print(stdobj.Current_courses)
        print("\n")
      


def add_multiple_Courses():
    
        z = int(input("enter student number for the student registration:"))
        

        details = ["Name", "id", "Email",
                   "Previous Courses", "Grades", "current courses"]
        print("\n")
        stdobj = student1(temp2[z-1])

        for j in range(len(temp2[z-1])):

            print(details[j] + ": "+temp2[z-1][j])
        print("\n")
        
       
            
        userinput=1
      
        while userinput ==1:  
          coursesnames=[]
          for i in range(len(tempcourse4)-1):
              coursesnames.append(tempcourse4[i][0]+tempcourse4[i][1])
          for i in range(len(coursesnames)):
            print(str(i+1) + " " + coursesnames[i] )     
          addcourse = int(input("enter course number from above options that student want to register:"))
          if(type(addcourse)!= int or addcourse<=0 or addcourse>10):
            print("please enter valid value from 1 to 10")
          else:
            check = False
            
            for i in range(len(stdobj.Privious_courses)):
                # print(tempcourse4[addcourse-1][6])
                if(stdobj.Privious_courses[i] == tempcourse4[addcourse-1][6] ):
                  check=True
                  return
            if(tempcourse4[addcourse-1][6]=="-" or check == True):
              temp[z-1][5] = temp[z-1][5]+","+coursesnames[addcourse-1] 
              stdobj.Current_courses.append(coursesnames[addcourse-1]) 
            else:
                print("you cannot add " , coursesnames[addcourse-1] , " because you didn't took " , tempcourse4[addcourse-1][6] ) 

        
       
            print(details[j] + ": ")
            print(stdobj.Current_courses)
            print("\n")
            
            userinput=int(input("enter your option \n 1 countinue to add courses \n 2 exit"))
            
            if userinput==2:
               details = ["Name", "id", "Email",
                   "Previous Courses", "Grades", "current courses"]
               print("\n")


               for j in range(len(temp2[z-1])):
  
                 print(details[j] + ": "+temp2[z-1][j])
                 
            return
                
            
      
        

def student_report():

    print("enter 1 for all student report")
    print("enter 2 for singal student information ")
    choise = int(input("enter your choise:"))
  
    if choise == 1:
        details = ["Name", "id", "Email",
                   "Previous Courses", "Grades", "current courses"]
        print("\n")

        for i in range(len(temp)):

            for j in range(len(temp2[i])):

                print(details[j] + ": "+temp2[i][j])
            print("\n")
    elif choise == 2:
        y = int(input("enter student number:"))
        details = ["Name", "id", "Email",
                   "Previous Courses", "Grades", "current courses"]
        print("\n")


        for j in range(len(temp2[y-1])):

            print(details[j] + ": "+temp2[y-1][j])
        print("\n")
    else:
        print("invalid input")


# student_registration()

# student_report()
# add_multiple_Courses()
# print(temp2)

# #"GajeraDrij", 146127, "gajeradrij78@gmail.com", "104PSY", "A", "200MAT,111CMPT,206PSY"
# arrofstdinfo = []
# for i in range(len(temp3)):
#     # print(temp3[i])
#     arrofstdinfo.append(temp3[i])
# nputforstudent=0
# arrofstdinfo = []
# arrofstdinfo.append(temp2[inputforstudent])

# obj_type = student1(arrofstdinfo[0])
# print(obj_type.Current_courses)




def add_multiple_students():
        coursesnames=[]
        details = ["Name", "id", "Email",
                   "Previous Courses", "Grades", "current courses"]
        for i in range(len(tempcourse4)-1):
              coursesnames.append(tempcourse4[i][0]+tempcourse4[i][1])
        for i in range(len(coursesnames)):
            print(str(i+1) + " " + coursesnames[i] ) 
        z = int(input("enter course number to add it into students cureent courses :"))
        

        details = ["number", "name", "time&day",
                   "credits", "location", "pre-requsite"]
        print("\n")
        # print(tempcourse4)
        courseobj = course(tempcourse4[z-1])

        for j in range(len(tempcourse4[z])-1):
           
            print(details[j] + ": "+tempcourse4[z-1][j])
            
        print("\n")
        
       
            
        userinput=1
      
        while userinput ==1:  
          studentnames=[]
          for i in range(len(temp2)-1):
              studentnames.append(temp2[i][0])
          for i in range(len(studentnames)):
            print(str(i+1) + " " + studentnames[i] )     
          addstudents = int(input("enter student number from above options to register course into students current courses:"))
          if(type(addstudents)!= int or addstudents<=0 or addstudents>len(temp2)):
            print("please enter valid value from 1 to "+ len(temp2))
          temp2[addstudents-1][5]=temp2[addstudents-1][5]+","+coursesnames[z-1]
          
          for j in range(len(temp2[z-1])):
  
            print(details[j] + ": "+temp2[z-1][j]) 
          userinput=int(input("enter your option \n 1 countinue to add courses \n 2 exit"))
            
          if userinput==2:
             
               print("\n")
               return


options_func()                
                 
        