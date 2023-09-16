# Check Whether a number is a perfect number or not

num = int(input("Enter a number : "))
add = 0

for i in range(1, num):
    if num % i == 0:
        add = add + i

if (num == add):
    print("Perfect Number")
else:
    print("Not Perfect Number")
        
