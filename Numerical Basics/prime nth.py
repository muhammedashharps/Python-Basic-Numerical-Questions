# Prime Number in a Given Rnage 

rang = int(input("Enter the range you want: "))

for i in range(2, rang):
    flag = 0 #Used To Assume a number is prime , on every new outerloop , the value is resetted to 0 
    for j in range(2, i):
        if (i%j==0):
            flag  = 1
            break;
    if (flag ==0):
        print(i)
            