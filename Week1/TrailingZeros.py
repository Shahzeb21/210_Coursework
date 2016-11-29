def ZeroCalc(Number):
    
    FiveFactors = []
    TwoFactors = []
    
    for Num in range (Number , 0 , -1):
        if Num%5 == 0:
            FiveFactors.append(Num)
    #print (FiveFactors)

    #for Num in range (Number , 0 , -1):
        #if Num%2 == 0:
            #TwoFactors.append(Num)
    #print(TwoFactors)

    count = 0
    for num in FiveFactors:
        while num%5 == 0:
            num = num / 5
            count = count + 1
    print(count)
    
    TensCount = 0
    for s in FiveFactors:
        if s%10 == 0:
            TensCount = TensCount + 1

    #ExclusiveFives = (len(FiveFactors)) - (TensCount)
    #print(len(FiveFactors))
    """if TwoFactors != 0:
        TrailingZeros = TensCount + ExclusiveFives
    else:
        TrailingZeros = TensCount"""
            
#ZeroCalc()
