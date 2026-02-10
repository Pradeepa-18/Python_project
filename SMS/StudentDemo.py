from bean.Student import Student;
from exception.StudentDoesntExist import StudentDoesntExist;
from service.StudentManagementSystem import StudentManagementSystem;

class StudentDemo:
    if __name__ == '__main__':
        stud = StudentManagementSystem()
        s1 = Student(1,'pradeepa','chennai','CSE',[93,90,98,97,95])
        s2 = Student(2,'varsha','Thanjavur','ECE',[99,100,98,57,95])
        s3 = Student (3,'jay','Thanjavur','IT',[39,100,96,57,95])
        stud.addStudent(s1)
        stud.addStudent(s2)
        stud.addStudent(s3)
        print("list Students")
        stud.listStudents()
        print("Topper: ",stud.findTopper())
        s4 = Student (3,'jay','Vellore','IT',[39,70,96,97,85])
        try:
            print('Student Updated: ',stud.updateStudent(5,s4))
        except StudentDoesntExist as e:
            print(e)
        try:
            print(' Student Deleted: ',stud.deleteStudent(2))
        except StudentDoesntExist as e:
            print(e)
                
        
        stud.listStudents()
        
        stud.listStudents()
        
        
        
        
