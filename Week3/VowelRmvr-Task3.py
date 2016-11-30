def VowelRmvr(word):
    
    Vowels = ('a','e','i','o','u')

    if len(word) == 0:
        return word
    
    else:
        if word[0] in Vowels:
            return VowelRmvr(word[1:])
        else:
            return word[0] + VowelRmvr(word[1:])

print(VowelRmvr("beautiful"))


                                 
                
