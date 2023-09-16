#Print N number of Automorophic numbers in a given range

range = int(input('Enter the given range : '))

for i in range(1, rang):
    sqr = i**2
    mod = 10 ** len(str(i))
    if (sqr%mod == i):
        print(i)

