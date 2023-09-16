# Sum of numbers between rabges 

n1 = int(input("Enter The Initial Range : "))
n2 = int(input("Enter the final range : "))

add = 0 

for i in range(n1, n2+1):
    add = add + i 
    
print(add)