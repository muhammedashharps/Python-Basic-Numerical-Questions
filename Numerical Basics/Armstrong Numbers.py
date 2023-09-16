# Armstrong Number - The Tough Number 

num = int(input("Enter the number You Want: "))

add = 0 
n = len(str(num))
temp = num 


while (temp!=0):
    reminder = temp % 10
    add = add + (reminder**n)
    temp = temp // 10

if num == add:
    print("Palindrome")
else:
    print("Not Palindrome")