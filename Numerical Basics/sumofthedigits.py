# Sum of the digits of a number 

num = int(input("Enter a number : "))

# Let us Do This By using modulus

add = 0 

while (num!=0):
    reminder = num % 10
    add = add + reminder 
    num = num // 10
    
print(add) 
    
