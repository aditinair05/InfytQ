class Parrot:
        __counter = 7000
        def __init__(self,name,color):
            self.__name= name
            self.__color= color
            Parrot.__counter+=1
            self.__unique_number =  Parrot.__counter
            
            
        def get_name(self):
            return self.__name 
        def get_color(self):
            return self.__color
        def get_unique_number(self):
            return self.__unique_number
    
p1 = Parrot("A","Yellow")
p2 = Parrot("B","Green")
p3 = Parrot("C","Red")
p4 = Parrot("D","Blue")

print(p1.get_name() ,"  " , p1.get_color() , "  " , p1.get_unique_number())
print(p2.get_name() ,"  " , p2.get_color() , "  " , p2.get_unique_number())
print(p3.get_name() ,"  " , p3.get_color() , "  " , p3.get_unique_number())
print(p4.get_name() ,"  " , p4.get_color() , "  " , p4.get_unique_number())
