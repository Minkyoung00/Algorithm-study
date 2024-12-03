import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

def Plus(source):
	total = 0
	for i in range(len(source) - 1):
		total += abs(source[i] - source[i+1])
	return total

# print(Plus(A))
def Permute(source):
	
	# Plus()
	pass

Permute(A)
