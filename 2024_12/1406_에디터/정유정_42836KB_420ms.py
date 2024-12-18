import sys

string = list(map(str, sys.stdin.readline().strip()))
repeat = int(sys.stdin.readline().strip())
new = []

for _ in range(repeat):
    command = list(map(str, sys.stdin.readline().strip().split()))
    if command[0] == 'P':
        string.append(command[1])

    elif command[0] == 'L' and string:
        new.append(string.pop())

    elif command[0] == 'D' and new:
        string.append(new.pop())

    elif command[0] == 'B' and string:
        string.pop()

print(''.join(string + new[::-1]))
