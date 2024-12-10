import itertools

while True:
    temp = input()
    if temp == '0': break
    else:
        temp = list(map(int, temp.split()))
        k = temp.pop(0)
        nCr = itertools.combinations(temp, 6)
        for i in list(nCr):
            print(*i)
        print()

     