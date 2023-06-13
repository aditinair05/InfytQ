class Instructor:
    def __init__(self):
        self.__instructor_name = None
        self.__technology_skill = []
        self.__avg_feedback = None
        self.__experience = None
        
    def set_instructor_name(self, instructor_name):
        self.__instructor_name = instructor_name
    
    def set_avg_feedback(self, avg_feedback):
        self.__avg_feedback = avg_feedback
    
    def set_technology_skill(self, technology_skill):
        self.__technology_skill = technology_skill
        
    def set_experience(self, experience):
        self.__experience = experience
    
    def get_instructor_name(self):
        return self.__instructor_name
        
    def get_avg_feedback(self):
        return self.__avg_feedback
        
    def get_experience(self):
        return self.__experience
        
    def get_technology_skill(self):
        return self.__technology_skill
        
    def check_eligibility(self):
        if self.__experience >3 and self.__avg_feedback >= 4.5:
            return True
        elif self.__experience <=3 and self.__avg_feedback >= 4:
            return True
        else:
            return False
    
    def allocate_course(self,technology):
        if self.check_eligibility() == True:
            if technology in self.__technology_skill:
                return True
            else:
                return False
        else: 
            return False

h = Instructor()
h.set_instructor_name("ABC")
h.set_technology_skill(["Python","Java","Ruby","C++"])
h.set_avg_feedback(4.7)
h.set_experience(5)
print(h.allocate_course("Java"))
