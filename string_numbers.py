def count_digits_letters(sentence):
    #start writing your code here
  result_list=[0,0]
  c = sentence.split()
  for x in c:
      for i in x:
            if ord(i) in range(65, 91) or ord(i) in range(97,123):
              result_list[0]+=1
            elif ord(i) in range(48,58): 
              result_list[1]+=1
  return result_list

sentence="Infosys 123"
print(count_digits_letters(sentence))
