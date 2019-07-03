stock_each = dict()
year = [101,102,103,104]
value = [24, 28, 32, 36]
for i in range( 0 , len(year)):
	if year[i] not in stock_each:
		stock_each[year[i]] = [value[i]]
	else:
		stock_each[year[i]].append(value[i])
print(stock_each)
print(year)

sum1 = sum2 = 0
for i, j in zip(year,value):
	sum1 +=i
	sum2 +=j
print(sum1,sum2)

N = int(len(year))
print(N)
alist=[6,7,8,9,10]
blist=[]
print(alist)
for i in map(lambda x: x%5,alist):
	blist.append(i)
print(blist) #blist 顯示為 [1, 2, 3, 4, 0]


sum3 = lambda x: x+5 
print(sum3(3))
