def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    input=[0,0,0]
    for i in patient_medical_speciality_list:
        if i =='P' or i=='p':
            input[0]+=1
        elif i=='O' or i=='o':
            input[1]+=1
        elif i=='E' or i=='e':
            input[2]+=1
    if input[0] > input[1] and input[0]>input[2]:
        speciality=medical_speciality['P']
    elif input[1] > input[2] and input[1]>input[0]:
        speciality=medical_speciality['O']
    elif input[2] > input[1] and input[2]>input[0]:
        speciality=medical_speciality['E']
        

    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'O',302, 'O' ,305, 'E' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)
