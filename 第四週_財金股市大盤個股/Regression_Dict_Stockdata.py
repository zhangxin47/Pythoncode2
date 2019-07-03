import csv
import os
import csvsorter
bigmarket = "C:\\Users\\b1013\\Desktop\\Pythoncode2\\bigmarket_in.csv" 
file_bigmarket2 = open(bigmarket, "r", encoding ="utf-8", newline ="")  #將已整理好的大盤Data再次開啟
reader1 = csv.DictReader(file_bigmarket2) #建立Dict
mktret = dict()

for arow in reader1:   #使大盤日期對應相對ROI
	mktret[arow['MDATE']] = float(arow['ROI'])#少了12月的19筆 不知原因 索性弄到20161202
	print(arow['MDATE'])
print("Read %d market return data " % len(mktret)) #少了12月的19筆 不知原因 索性弄到20161202

sret= []  #存放個股報酬
sdate= [] #存個股日期
stock_each = dict() #股票代碼對應0104~1201所有ROI
stock_each_num = dict() #有幾天的ROI
last_coid = ""  #前一筆股票代碼
last_name = ""  #前一筆股票名稱
this_coid = ""  #這一筆股票代碼
this_name = ""  #這一筆股票名稱
COID = ""
COIDarr = [] #做查詢
coidarr = [] #紀錄股票代碼
namearr = [] #紀錄股票名
alphaarr = [] #alpha存放
betaarr = [] #beta存放
sarr = [] # s 存放
r2arr = [] # r2 存放
minlen = 50
ylist = [] #存放個股 一年度的ROI

sorted_stock = "C:\\Users\\b1013\\Desktop\\Pythoncode2\\stocksorted.csv"
sorted_stockdata = open( sorted_stock, "r", encoding ="utf-8", newline ="") #將已整理好的個股Data再次開啟
sortedreader = csv.DictReader(sorted_stockdata, delimiter = ',')

def compute_model(ylist, sdate, mktret):
	"""
		ylist: list of stock return
		sdate: list of return dates
		mktret: market return dict
	"""
	xlist = [] #大盤的ROI 
	for i in range(0, len(sdate)):    #就講好到1202 共224筆
		xlist.append(mktret[sdate[i]])
	if len(xlist) != len(ylist):
		raise Exception("Data length Error!")
	return simple_reg(xlist, ylist)
	
def simple_reg(xlist, ylist):
	import math
	N = int(len(xlist))
	sum_x = sum_y = avg_x = avg_y = 0.00 
	beta = alpha = ei2 = s =r2 = 0.0 #定義回傳數 
	for i in xlist:
		sum_x = sum_x + float(i)
	avg_x = sum_x / N
	for i in ylist:
		sum_y = sum_y + float(i)
	avg_y = sum_y / N
	denom = nume = 0.0 #定義分母分子
	for i,j in zip(xlist, ylist):     #算beta
		nume += ( float(j) - avg_y) * ( float(i) - avg_x) #分子加總
		denom += pow(( float(i) - avg_x) ,2)  #分母加總
	beta = nume / denom
	alpha = avg_y - beta * avg_x 
	denom2 = 0.0
	for i,j in zip(xlist, ylist):	  #算ei2加總
		ei2 += pow((float(j) - alpha - beta * float(i)) ,2)
		denom2 += pow((float(j) - avg_y) ,2)
	s = pow( ei2/(N-2) , 0.5)
	r2 = 1- (ei2 / denom2)
	return [alpha, beta, s, r2]

for arow in sortedreader: #要以dict 去存放資料比對
	this_coid = arow["COID"].strip()
	this_name = arow["Name"].strip()
	COID = arow["COID"].strip()
	if (COID == "9904"):   #因為9904以後筆數皆為223筆 與大盤224筆不合 因此不作回歸分析
		break
	if (COID not in COIDarr):
		COIDarr.append(COID)
		stock_each[COID] = [arow['ROI']]  #之前卡到，忘記外面加[]
		stock_each_num[COID] = 1
	else:
		stock_each[COID].append(arow['ROI']) #Dict是可以使用append的不要懷疑
		stock_each_num[COID] += 1
	if ( this_coid != last_coid):
		if (len(sret) > minlen):
			print("Run regression for COID:", last_coid)
			ylist = stock_each[last_coid]  #因要作此支回歸分析，將這支股票一整年度的ROI存入 ylist中，其實sret也是跟ylist同意
			out1 = compute_model( ylist, sdate, mktret)
			coidarr.append(last_coid)
			namearr.append(last_name)
			alphaarr.append(out1[0])
			betaarr.append(out1[1])
			sarr.append(out1[2])
			r2arr.append(out1[3])
			#run regression 寫Call regression
		#rset sret & sdate
		sret = [float(arow['ROI'].strip())] 
		sdate = [arow['MDATE'].strip()]	 #永遠紀錄第一筆20160104 print(this_name,"	",sdate,sret)
	else:
		sret.append(float(arow['ROI'].strip()))
		sdate.append(arow['MDATE'].strip()) #紀錄20160104後到20161201
	last_coid = this_coid
	last_name = this_name

#測試整合market return list
#print(COIDarr)
# print(stock_each_num)
# print(len(stock_each['1216']))
#明早用COIDarr去一筆一筆呼叫 ylist內則有20160104至20161201  原先890支，因股票代碼9904以後(共36支)皆是223 因此扣除
# print(len(COIDarr))
# print(COIDarr)
# ylist = stock_each[last_coid]
# print(ylist)
nstock = len(coidarr)  #共幾支股票
sumr2=0.0
avgr2 = 0.0
for i in r2arr:
	if i < 0:
		print("error")
	else:
		sumr2 += i  #計算所有r square 加總
avgr2 = sumr2 / nstock
print( "共%d支股票，平均R Square 配適性為%f" % (nstock,avgr2))
#測試整合market return list

import matplotlib.pyplot as plt  #import matplotlib 的 pyplot
from matplotlib.font_manager import FontProperties  #管理字型模組
ChinesFont2 = FontProperties(fname = "C:\\Windows\\Fonts\\mingliu.ttc")
fig , ax = plt.subplots() #fig = plt.figure() , ax = plt.subplot(111)
ax.scatter(betaarr, alphaarr)

for i, txt in enumerate(namearr): # i為點的位置 txt為股票名稱
	ax.annotate(txt, (betaarr[i], alphaarr[i]), 
	fontproperties = ChinesFont2)
plt.show()


#close the file
file_bigmarket2.close()
sorted_stockdata.close()