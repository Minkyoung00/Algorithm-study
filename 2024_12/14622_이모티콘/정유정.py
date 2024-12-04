# recursion error

import sys

sys.setrecursionlimit(1000000)

emoticon_num = int(sys.stdin.readline())
result = copy = paste = 0


def emoji_cal(time: int, emoji: int):
    global emoticon_num, result, copy, paste

    if emoticon_num == emoji:
        result = min(result, time)
        return

    # copy
    copy = emoji
    emoji_cal(time + 1, emoji)

    # paste
    paste = copy
    emoji_cal(time + 1, emoji + paste)

    # subtraction
    emoji_cal(time + 1, emoji - 1)


emoji_cal(0, 1)
print(result)
