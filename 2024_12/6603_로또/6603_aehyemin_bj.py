from itertools import combinations
import sys


while True:
    number = list(sys.stdin.readline().split())
    if number[0] == "0":
        break

    s = number[1:]
    for com in combinations(s, 6):
        print(' '.join(map(str, com)))
    print()