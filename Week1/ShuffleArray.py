
def ArrayShuffler(Elements):
    from random import randint
    Array = [] # Users input Array declaration
    NewArray = [] # Array for storage of shuffled elements
    ShuffledIndex = [] # Declaration for shuffled indexes
    
    for i in range (0, Elements):
        Array.append(input("Enter element " + str(i+1) + " of array: "))

    
    for s in range (0 , Elements):
        index = randint(0 , Elements-1)
        while index in ShuffledIndex: # Keeps generating random number until a number not already occoured is generated
            index = randint(0 , Elements-1)
        ShuffledIndex.append(index) # Makes a List of shuffled indexes for use later that are strictly not repeated
    #print(ShuffledIndex)

                
    for index in ShuffledIndex: # Using the shuffled index List simply assigns elements of users array into a new shuffled array and prints
        NewArray.append(Array[index])
                
        

    print (NewArray)

#ArrayShuffler(6)
    # L[2] , L[4] = L[4] , L[2]
        #Think of shuffling without the declaration of a new list
