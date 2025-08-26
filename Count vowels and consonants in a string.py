string=input('Enter the string: ')
l_string = string.lower()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
vowels='aeiou'
v_count=0
c_count=0
for char in l_string:
    if char in alphabet:
        if char in vowels:
            v_count = v_count + 1 
        else:
            c_count = c_count + 1
        
print(v_count)
print(c_count)
