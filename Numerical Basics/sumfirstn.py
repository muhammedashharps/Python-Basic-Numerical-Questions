# Sum Of The First N Natural Numbers 

ranges = int(input("Enter the ranges: "))
add = 0
for  i in range(ranges+1):
     add = add + i 

print(f"The sum of the first {ranges} numbers is {add}")