from abc import ABC;
class StudentMgmtInterface(ABC):
    def addStudent(self,s):
        None
    def deleteStudent(self,rollNo):
        None
    def listStudents(self):
        None
    def updateStudent(self,rollNo,s):
        None
    def findTopper(self):
        None
