# Armstrong number in a given range at high speed 

rang = int(input("Enter the range : "))

for i in range(1, rang):
    add = 0 
    length = len(str(i))
    temp = i 
    while (temp != 0):
        reminder = temp % 10 
        add = add + (reminder**length)
        temp = temp // 10 
    
    if (i==add):
        print(i)
    