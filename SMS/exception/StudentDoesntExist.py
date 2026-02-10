class StudentDoesntExist(Exception):
    def __init__(self,message):
        self.msg = message
        super().__init__(self,message)
        
    def __str__(self):
        return self.msg
