data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 #透過計數來看讀去狀況
		if count % 1000 == 0: #％只是拿來求餘數，count是1000的倍數
			print(len(data))
print(len(data))
print(data[0])
print('-------------------------------------------')
print(data[1])