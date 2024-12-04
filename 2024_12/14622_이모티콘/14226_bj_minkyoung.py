S = int(input())
unit = 1
sum = 1

def copy(lst):
    global unit, sum
    unit = sum

def paste(lst):
    global unit, sum
    sum += unit

def delete(lst):
    global sum
    sum -= 1