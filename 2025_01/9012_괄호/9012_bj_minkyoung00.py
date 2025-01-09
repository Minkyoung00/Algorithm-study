T =int(input())
for i in range(T):
	text = input()
	cnt = 0
	for t in text:
		if t == '(':
			cnt += 1
		else:
			if cnt > 0:
				cnt -= 1
			else:
				cnt = -1
				break
	
	if cnt == 0:
		print('YES')
	else:
		print('NO')
