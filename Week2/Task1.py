def FindPerfSquare(Int):
    
    StartPos = int(round(Int/2)) #Halves the input number in order to decrease number of comparisons
    
    for i in range (2 , StartPos): #Since 0 or 1 wouldnt produce any perfect squares
        Square = i*i
        if (Square < Int+1):
            MyNum = Square
        else:
            break
    print(MyNum)
    
#FindPerfSquare(Check)               

