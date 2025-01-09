T =int(input())
for i in range(T):
	text = input().split()
	cnt = 0
	for t in text:
		if t == '(':
			cnt += 1
		else:
			if cnt > 0:
				cnt -= 1
			else:
				print('NO')
				break
	print('YES')
