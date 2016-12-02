def StringReverse(Sentence):
    
    NewList = []
    s = (Sentence.split(" ")) # s is a list of all the words in the sentence
    
    for i in range (len(s) , 0 , -1):
        NewList.append(s[i-1]) #simply adds all the words in s form the bottom up to NewList
         
    Final = ' '.join(NewList) #joins the elements of the list to make them a sentence
    print(Final)
  
StringReverse("This is awesome i cant believe what is happening right now!")
