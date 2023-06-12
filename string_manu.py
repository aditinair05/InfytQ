def reverse(str):
    return str[::-1]
def rearrange(str):
    vowel=['a','e','i','o','u']
    m=''
    n=''
    for i in str:
        if i in vowel:
            m+=i
        else:
            n+=i
    return n+m
def encrypt_sentence(sentence):
    words = sentence.split()
    for i in range(len(words)):
        if i % 2 ==0:
            words[i] = reverse(words[i])
        else:
            words[i] = rearrange(words[i])
    output=" ".join(words)
    return output
        
sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)
