def prime(n,m):
    # where n is the number we want to check is prime
    # and m is equal to n-1

    if n < 2: #Base Case
        
        print("not a prime number")
        return False
    
    if n == 2:
        print("prime number")
        return True

    else: #Terminating Cases
        
        if n % m == 0:
            print("not a prime number") #this covers the case of 2 and 1. 
            return False
        
        elif n % m != 0 and m != 2:
            prime(n,m-1)           

        elif n % m != 0 and m == 2:
            print("prime number")
            return True



        
        
