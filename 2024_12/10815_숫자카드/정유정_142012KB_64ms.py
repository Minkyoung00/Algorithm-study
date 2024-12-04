import sys

card_num = int(sys.stdin.readline())
cards = set(map(int, sys.stdin.readline().strip().split()))

num = int(sys.stdin.readline())
check_nums = list(map(int, sys.stdin.readline().strip().split()))

result = []

for c in check_nums:
    cards.add(c)
    if card_num != len(cards):
        card_num = len(cards)
        result.append(0)
    else:
        result.append(1)

print(' '.join(map(str, result)))
