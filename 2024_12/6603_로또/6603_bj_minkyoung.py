nums = []

while True:
    temp = input()
    if temp != '0':
        nums.append(list(map(int, temp.split())))
    else: break

print(nums)
     