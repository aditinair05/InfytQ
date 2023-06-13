class Student:
    def __init__(self):
        self.__student_id=None
        self.__marks=None 
        self.__age=None
        
    def	set_student_id(self,student_id):
        self.__student_id = student_id
    def	get_student_id(self):
        return self.__student_id
    def	set_marks(self,marks):
        self.__marks = marks
    def	get_marks(self):
        return self.__marks
    def	set_age(self,age):
        self.__age = age
    def	get_age(self):
        return self.__age

    def validate_marks(self):
        if self.__marks >=0 and self.__marks <=100:
            return True
        else:
            return False
    
    def validate_age(self):
        if self.__age >20:
            return True
        else:
            return False
    def check_qualification(self):
        if self.validate_marks() ==True and self.validate_age()==True :
            if self.__marks >=65:
                return True
            else:
                return False
        else:
            return False
