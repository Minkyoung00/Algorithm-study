import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
coords = list(map(int, input().split()))
sorted_coords = sorted(list(set(coords)))

result = [bisect_left(sorted_coords, coord) for coord in coords]

print(*result)
