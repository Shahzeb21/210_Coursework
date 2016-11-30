def StringReverse(Sentence):
    
    NewList = []
    s = (Sentence.split(" "))   
    
    for i in range (len(s) , 0 , -1):
        NewList.append(s[i-1])
         
    Final = ' '.join(NewList)
    print(Final)
  
StringReverse("This is awesome i cant believe what is happening right now!")
