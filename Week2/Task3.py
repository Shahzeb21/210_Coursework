def MatrixCalc(B,C,N,Operation):
    
    Result = []
    for i in range(0 , N):
        Result.append([])
        for s in range(0 , N):
            Result[i].append(0)
            
    if Operation == "+":
    #For Addition:
        for row in range (0 , N):
            for col in range (0 , N):
                (Result[row])[col] = (B[row])[col] + (C[row])[col]
        print(Result)
        
    elif Operation == "-":
    #For Subtraction:
        for row in range (0 , N):
            for col in range (0 , N):
                (Result[row])[col] = (B[row])[col] - (C[row])[col]
        print(Result)
        
    elif Operation == "*":
    #For Multiplication:
        for row in range (0 , N):
            for col in range (0 , N):
                Sum = 0
                for k in range (0 , N):
                    Sum += B[row][k] * C[k][col]
                    Result[row][col] = Sum
        print(Result)

r1 = MatrixCalc([(1,2),(3,4)],[(2,4),(6,8)], 2, "*")
r2 = MatrixCalc([(1,2),(3,4)],[(2,4),(6,8)], 2, "+")
r3 = 2*r2
R = r1 + r3


        

#MatrixCalc([(1,2),(3,4)],[(1,2),(3,4)],2,"*")
                   
