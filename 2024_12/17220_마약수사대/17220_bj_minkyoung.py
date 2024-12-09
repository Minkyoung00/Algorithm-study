def chr_to_ord(x):
    return ord(x)-64

def ord_to_chr(x):
    return chr(x + 64)

N, M = map(int,input().split())
# edge = [ map(chr_to_ord, input().split()) for i in range(M) ]

edge = []
node_give = [[] for i in range(N+1)]
node_given = [[] for i in range(N+1)]

for i in range(M):
    from_p, to_p = map(chr_to_ord, input().split())
    edge.append((from_p, to_p))
    node_give[from_p].append(to_p)
    node_given[to_p].append(from_p)

known_list = input().split()
known_n = int(known_list.pop(0))
known_list = map(chr_to_ord, known_list)

queue = list(known_list)

while queue:
    i = queue.pop(0)
    node_given[i] = []
    for j in node_give[i]:
        node_given[j].remove(i)
        if not len(node_given[j]):
            queue.append(j)

print(edge)
print(node_give)
print(node_given)
print(known_list)
print(known_n)





