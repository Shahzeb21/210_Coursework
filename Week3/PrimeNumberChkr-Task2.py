def prime(n,m):

    if n < 2: #Base Case
        
        print("not a prime number")
        return False

    else: #Terminating Cases
     
        if n % m == 0:
            print("not a prime number")
            return False
        
        elif n % m != 0 and m != 2:
            prime(n,m-1)           

        elif n % m != 0 and m == 2:
            print("prime number")
            return True



        
        
