def binary_search_range(Sorted, NumberFrom, NumberTill):
    #Sorted is the sorted sequence of numbers
    #NumberFrom is the lower limit of the interval
    #NumberTill is the upper limit of the interval
    
    StartPos = 0
    EndPos = len(Sorted)-1
    MidVal = (StartPos + EndPos) // 2

    ShouldBreak = False

    while StartPos <= EndPos:
            MidVal = (StartPos + EndPos) // 2

            #print( "Found at position = {}, The value = {}".format(MidVal,Sorted[MidVal]) )
            #print( NumberFrom, NumberTill ) Was using this for debugging
        
            if (Sorted[MidVal] >= NumberFrom) and  (Sorted[MidVal] <= NumberTill):
                return True
                
            elif Sorted[MidVal] > NumberTill: #if specific value is greater than upper limit then ignore second half of list
                #print("gt") Debugging
                EndPos = MidVal - 1 
            
            elif Sorted[MidVal] < NumberFrom: #if specific value is greater than the lower limit then ignore first half half of list
                #print("lt") Debugging
                StartPos = MidVal + 1
                
    return False

# I really wanted to use Manual entry for some reason.
First = input("Please enter the sequence?: ")
NumberFrom = int(input("Please enter the number your interval starts from: "))
NumberTill = int(input("Please enter the number your interval ends at: "))

List = First.split(" ")

for i in range (0 , len(List)):
    List[i] = int(List[i])  

print(List)

Sorted = sorted(List)

print( "found {}".format( binary_search_range( Sorted, NumberFrom, NumberTill ) ) )

