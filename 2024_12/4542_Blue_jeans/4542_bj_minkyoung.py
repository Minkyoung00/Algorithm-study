n = int(input())

for i in range(n):
    m = int(input())
    first_sequence = input()
    sequences = [input() for j in range(m-1)]
    result = []

    for length in range(60, 2, -1):
        check = set()
        
        for index in range(61 - length):
            cur = first_sequence[index : index+length]

            if cur in check: continue
            check.add(cur)

            count = 0
            for sequence in sequences:
                p_cur = p_seq = 0
                while p_seq != 60 and p_cur != length:
                    if sequence[p_seq] == cur[p_cur]:
                        p_seq += 1
                        p_cur += 1
                    else:
                        p_seq = p_seq - p_cur + 1
                        p_cur = 0
                    
                if p_cur == length: count += 1

            if count == m-1:
                result.append(cur)

        if result: break

    if result:
        result.sort()
        print(result[0])
    else:
        print('no significant commonalities')