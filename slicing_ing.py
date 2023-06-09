
def add_string(str1):
  #start writing your code here
  if len(str1)>=3 and str1[-3:]!="ing":
      str1=str1+"ing"
  elif srt1[-3:]=="ing":
      str1=str1+"ly"
  elif len(str1<3):
      str1=str1
  
  return str1

str1="com"
print(add_string(str1))
