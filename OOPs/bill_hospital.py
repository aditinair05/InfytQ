class Bill:
        
        def __init__(self,bill_id,patient_name):
            self.__bill_id= bill_id
            self.__patient_name= patient_name
            self.__bill_amount = 0
           
            
        def get_bill_id(self):
            return self.__bill_id 
        def get_patient_name(self):
            return self.__patient_name
        def get_bill_amount(self):
            return self.__bill_amount
        def calculate_bill_amount(self,consultation_fees, quantity_list, price_list):
            ba = 0
            for i, j in zip(quantity_list, price_list):
                    ba+=i*j
            self.__bill_amount= (consultation_fees+ba)
                
             
    
p1 = Bill(1 ,"Kirti")
p1.calculate_bill_amount(300, [3,5,6],[60,70,50])
print(p1.get_bill_amount())
p2 = Bill(2 ,"Kruti")
p2.calculate_bill_amount(300, [5,8,6],[90,40,20])
print(p2.get_bill_amount())
