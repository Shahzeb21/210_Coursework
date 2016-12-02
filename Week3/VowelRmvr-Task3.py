def VowelRmvr(word):
    
    Vowels = ('a','e','i','o','u')

    if len(word) == 0:
        return word
    
    else:
        if word[0] in Vowels:
            return VowelRmvr(word[1:]) #If first letter of string is a vowel, then calls the function again withouth the first letter
        else:
            return word[0] + VowelRmvr(word[1:])# if first letter isnt a vowel, the non-vowel letter is returned and the function recalled.

print(VowelRmvr("beautiful"))


                                 
                
