# Find the factors of a number , there is a difference between factors and factorials 

num = int(input("Enter the number : "))

print("The factor of the numbers are: ")
for i in range(1, num+1):
    if num % i == 0:
        print(i, end=',')