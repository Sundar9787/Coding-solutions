string ="Hello World"

def reverse_word(word):
    reversed_word =''
    for l in range(len(word)-1,-1,-1):
        reversed_word = reversed_word + word[l]
    return reversed_word
    
def reverse_sentence(string):
    ans=[]
    words = string.split()
    for word in words:
        ans.append(reverse_word(word))
    result =' '.join(ans)
    return result
    
print(reverse_sentence(string))
