data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 #透過計數來看讀去狀況
		if count % 10000 == 0: #％只是拿來求餘數，count是10000的倍數
			print(len(data))
print('檔案讀取完畢，共計', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)
	print(sum_len)

print('留言平均長度是', sum_len/len(data))
