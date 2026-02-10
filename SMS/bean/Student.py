class Student:
    def __init__(self,rollNo,name,address,subject,marks):
        self.rollNo = rollNo
        self.name = name
        self.address = address
        self.subject = subject
        self.marks = marks
    def getRollNo(self):
        return self.rollNo
    def getName(self):
        return self.name
    def getAddress(self):
        return self.address
    def getSubject(self):
        return self.subject
    def getMarks(self):
        return self.marks
    def __str__(self):
        return (str(self.rollNo) + '\t' +self.name + '\t' +self.address + '\t' +self.subject + '\t' +
            str(self.marks))
