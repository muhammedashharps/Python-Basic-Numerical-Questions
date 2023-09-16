# Print the nth abundant numbers 

rang = int(input("Enter the range: "))

for i in range(1, rang):
    add = 0
    for j in range(1, i):
        if (i%j == 0):
            add = add + j 
    if (i<add):
        print(i)
    