import sys

string = list(map(str, sys.stdin.readline().strip()))
repeat = int(sys.stdin.readline().strip())
cursor = len(string)

for i in range(repeat):
    command = list(map(str, sys.stdin.readline().strip().split()))
    if command[0] == 'P':
        if cursor == len(string):
            string.append(command[1])
        else:
            string.insert(cursor - 1, command[1])
        cursor += 1

    elif command[0] == 'L':
        if cursor == 0:
            continue
        cursor -= 1

    elif command[0] == 'D':
        if cursor == len(string):
            continue
        cursor += 1

    else:
        if cursor == 0:
            continue
        del string[cursor - 1]
        cursor -= 1

print(''.join(string))
