def printnumber(n):
    iteration=0
    print ("total number entered by user",n)
    iteration+=1
    print ("total iteration done by computer",iteration)
    
printnumber(10)
printnumber(200)

#actiity 2
def Ontime(n):
    iteration=0
    for i in range(1,n+1):
        iteration+=1
    print("when n is",n,"iteration=", iteration)
Ontime(50)
Ontime(60)
Ontime(70)
#activity 3
def Test(n):
    iteration=0
    for i in range(0,n):
        for j in range(0,n):
            print("*",end="")
            iteration+=1
        print("")
    print(n,"iteration n=",iteration)
Test(5)
Test(10)
Test(200)

     