i=0
while i< 10:
    print(i)
    i=i+1
    print()
    for i in range(10): #the whole thing is with range
        print(i)

    for i in range(0,100,7): #multiples of 7 less than 100
        print(i)

    for i in range(15):
        #add code here to print multiples of 7
         print(7*i)

    for i in range(1,11):
        for j in range(i,11): #this can use variables
            print(f"{i} x {j} = {i*j}")
            print()


