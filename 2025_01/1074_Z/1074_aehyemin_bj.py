n, r, c = map(int, input().split())
#r행 c열을 몇번째로 방문하는지?
#배열은 2의 n-1승 으로 4등분 한 후에 방문

def mol(n, row, col):
    if n == 0:
        return 0
    num = 2*(row%2) + col%2 
    return 4 * mol(n-1, row//2, col //2) + num
#행과열이 2로 나누어질 때와 나누어지지 않을때
print(mol(n,r,c))