from exception.StudentDoesntExist import StudentDoesntExist;
from utility.StudentMgmtInterface import StudentMgmtInterface;
from bean.Student import Student;
class StudentManagementSystem(StudentMgmtInterface):
    def __init__(self):
         self.s = []
    def addStudent(self,stud):
        if len(self.s) >= 3 :
            return 'Total size of array exceeded'
        for i in self.s:
            if i.rollNo == stud.rollNo :
                return 'Student Exist'
        self.s.append(stud)
        return 'Successfully Added'
    def deleteStudent(self,rollNo):
        k = 0
        for i in self.s:
            if(i.rollNo == rollNo):
                self.s.pop(k)
                return True
            k+=1
        raise StudentDoesntExist('Given Student is not Present in the list')
    def updateStudent(self,rollNo,stud):
        k = 0
        for i in self.s:
            if(i.rollNo == rollNo):
                self.s[k]=stud
                return True
            k+=1
        raise StudentDoesntExist('Given Student is not Present in the list')
    def findTopper(self):
        tot=[]
        for i in self.s:
            tot.append(sum(i.marks))
        return self.s[tot.index(max(tot))]
    def listStudents(self):
        for i in self.s:
            print(i)
                
        
    
