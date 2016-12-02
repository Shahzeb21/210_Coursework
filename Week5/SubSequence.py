def AscSubSeq(Sequence):

    TempList = [] #Primarily holds asscending sequence
    FinalList = [] #Ultimately stores largest asscending sequence

    for i in range (0 , len(Sequence)):
        TempList.append(Sequence[i])
        #print(TempList)
        if len(TempList) >= len(FinalList):
            FinalList = TempList

        if i!=len(Sequence)-1:
            if Sequence[i+1] < Sequence[i]: # if the next element in sequence is less than the one before, list descending, so empty
                TempList=[]                  # TempList and start again.
            
                
                
    print("Maximum Length Sub-Sequence: " + str(FinalList))
AscSubSeq([1,26,5,4,8,9,7])
    
