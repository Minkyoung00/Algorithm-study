import sys

sys.stdin.readline()

a_array = list(map(int, sys.stdin.readline().strip().split()))
b_array = list(map(int, sys.stdin.readline().strip().split()))

sort_result = sorted(a_array + b_array)

print(" ".join(map(str, sort_result)))
