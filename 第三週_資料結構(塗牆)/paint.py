paintarray = []
paintinfo = []
wall = int(input("input how many walls:"))
times = int(input("how many times you should paint:")) 

for i in range(times):    #先將輸入的條件字串轉成數字
	paintinfo.append(input("start wall & end wall & paintnumber:").split(" "))
	for j in range(3):
		paintinfo[i][j] = int(paintinfo[i][j])

def countpaint(arr):
	d = dict()
	for paint in arr:
		if ( paint not in d):
			d[paint] = 1
		else:
			d[paint] += 1
	return d

for i in range(wall):      #把所有牆都先預設為 1號顏料
	paintarray.append("1")
print(paintarray)
outputpaintarry = countpaint(paintarray)
print(outputpaintarry)

for count in range(times):
	startwall = paintinfo [count][0]
	endwall = paintinfo [count][1]
	paintnumber = str(paintinfo [count][2])
	for changepaint in range(startwall-1, endwall):
		paintarray[changepaint] = paintnumber
print(paintarray)
outputpaintarry = countpaint(paintarray)
print(outputpaintarry)

