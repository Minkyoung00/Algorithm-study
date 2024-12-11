import sys
input = sys.stdin.readline

while 1:
	get = list(map(int, input().split()))
	if get[0] == 0:
		break
	
	# 실행
	max = min(get) * len(get)
	idx_list = [0]*len(get)

	# 요소 리스트
	ele = set(get)	

	# 반복
	for e in ele:
		# min_idx = []
		idx = -1
		for i, g in enumerate(get):
			if g == e:
				# min_idx.append(i)
				idx_list[i] = 1
				temp = (i - idx - 1) * min(get[idx+1:i])
				idx = i

				if temp > max:
					max = temp
				
				print(max, temp)
		
		# 마지막 연산
		temp = (len(get) - idx - 1) * min(get[idx+1:])

		if temp > max:
			max = temp

		print(max, temp)

		# for x in sorted(min_idx, reverse=True):
		# 	del get[x]
		
		# print(get)
	# -> 최소
	# 1 : n = 1 * 8
	# 2 * 2 / 2 * 4 / 2 * 3 -> 8
	# 7 / 2 * 4 / 2 * 3
