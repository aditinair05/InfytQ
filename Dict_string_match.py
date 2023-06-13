#lex_auth_01269444890062848087

def find_correct(word_dict):
    output=[0,0,0]
    for k,v in word_dict.items():
        if k==v:
            output[0]+=1
        elif len(k)!= len(v):
             output[2]+=1
        
        else:
            a=0
            for i in range(len(k)):
                if k[i]!=v[i] :
                     a+=1
            if a<=2:
                output[1]+=1
            else :
               output[2]+=1
        
    return output 
        

word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))
