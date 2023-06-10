def sms_encoding(data):
    output=""
    vowel=["a",'e','i','o','u',"I"]
    for x in data.split():
        if len(x)==1:
           output=output+x
        else :
           for t in x: 
            if t in vowel :
               x.replace(t,"")
            else:
                output=output+t

        output=output+" "
    output=output.rstrip()
    return output
                
               
data="I love Python"
print(sms_encoding(data))
