def nonRepeatingCharacter(string):
    str_list = list(string)
    
    for i in str_list:
        if str_list.count(i) == 1:
            return i
    
    return str_list[0]
    
string=input('Enter the String:: ')
print(nonRepeatingCharacter(string))
