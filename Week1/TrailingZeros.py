     
def ZeroCalc(Number):
    
    FiveFactors = [] #initialise list for storage of factors of 5
    
    for Num in range (Number , 0 , -1):
        if Num%5 == 0:
            FiveFactors.append(Num)

    count = 0
    for num in FiveFactors:
        #accomodates all the factors of five and breaks them down to just 5's
        while num%5 == 0:
            num = num / 5
            count = count + 1 #count of number of 5's in that specific factor, ultimately all 5's
    print(count)
    
    TensCount = 0
    for s in FiveFactors:
        if s%10 == 0:
            TensCount = TensCount + 1 
