import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

def Plus(source):
	total = 0
	for i in range(len(source) - 1):
		total += abs(source[i] - source[i+1])
	return total

perms = []
temp = []
def Permute(source, temp):
	if not source:
		perms.append(temp)
		return temp[:-1]
    
	for i in range(len(source)):
		temp.append(source[i])
		temp = Permute(source[:i]+source[i+1:], temp)
    
	return temp[:-1]

Permute(A, temp)
result = 0
for p in perms:
	ret = Plus(p)
	if ret > result:
		result = ret
	
print(result)
