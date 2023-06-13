class Student:
    def __init__(self):
        self.__student_id=None
        self.__marks=None 
        self.__age=None
        self.__course_id=None
        self.__fees=None
        
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
    def	set_course_id(self,course_id):
        self.__course_id = course_id
    def	get_course_id(self):
        return self.__course_id
    def	set_fees(self,fees):
        self.__fees = fees
    def	get_fees(self):
        return self.__fees

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
    
    def choose_course(course_id):
        if course_id == 1001 or course_id ==1002:
            self.course_id(course_id4)
            if self.__marks >85:
                
        
