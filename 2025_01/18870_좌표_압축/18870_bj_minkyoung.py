import sys
input = sys.stdin.readline

N = int(input())
coords = list(map(int, input().split()))
sorted_coords = sorted(set(coords))

dict = {sorted_coords[i]:i for i in range(len(sorted_coords))}

for i in range(N):
    coords[i] = dict[coords[i]]

print(*coords)