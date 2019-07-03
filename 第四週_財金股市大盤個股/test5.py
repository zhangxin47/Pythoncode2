import csv
import os
# sret= []  #存放個股報酬
# sdate= [] #存個股日期
# last_coid = ""  #前一筆股票代碼
# last_name = ""  #前一筆股票名稱
# this_coid = ""  #這一筆股票代碼
# this_name = ""  #這一筆股票名稱
# minlen = 2

# sorted_stock = "C:\\Users\\b1013\\Desktop\\Pythoncode2\\stocksorted.csv"
# sorted_stockdata = open( sorted_stock, "r", encoding ="utf-8", newline ="")
# sortedreader = csv.DictReader(sorted_stockdata, delimiter = ",")
# for arow in sortedreader: #要以dict 去存放資料比對
	# this_coid = arow["COID"].strip()
	# this_name = arow["Name"].strip()
	# if ( this_coid != last_coid):
		# if (len(sret) > minlen):
			# print("Run regression for COID:", last_coid)
			# #run regression
		# #rset sret & sdate
	# sret = [float(arow['ROI'].strip())]
	# sdate = [arow['MDATE'].strip()]
		# minlen+=1
	# else:
		# sret.append(float(arow['ROI'].strip()))
		# sdate.append(arow['MDATE'].strip())
	# last_coid = this_coid
	# last_name = this_name
# def simple_reg(xlist, ylist):
	# return [alpha, beta, s, r2]

# xlist = [-0.4825,-1.0491, -1.7312, 0.5337, 1.3371, -0.2564, 0.7229, -1.0445, 0.2471]
# ylist = [0.9560, -1.3258, 4.9904, -1.2797, -3.7037, 0.3846, 2.4904, 0.0000, 0.5607]
# simple_reg(xlist, ylist)

import csv
import os
import csvsorter
bigmarket = "C:\\Users\\b1013\\Desktop\\Pythoncode2\\bigmarket_in.csv" 
file_bigmarket2 = open(bigmarket, "r", encoding ="utf-8", newline ="")  #將已整理好的大盤Data再次開啟
reader1 = csv.DictReader(file_bigmarket2) #建立Dict
mktret = dict()

for arow in reader1:   #使大盤日期對應相對ROI
	mktret[arow['MDATE']] = float(arow['ROI']) #少了12月的19筆 不知原因 索性弄到20161202
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
minlen = 50

sorted_stock = "C:\\Users\\b1013\\Desktop\\Pythoncode2\\stocksorted.csv"
sorted_stockdata = open( sorted_stock, "r", encoding ="utf-8", newline ="") #將已整理好的個股Data再次開啟
sortedreader = csv.DictReader(sorted_stockdata, delimiter = ',')

for arow in sortedreader: #要以dict 去存放資料比對
	this_coid = arow["COID"].strip()
	this_name = arow["Name"].strip()
	COID = arow["COID"].strip()
	if (COID not in COIDarr):
		COIDarr.append(COID)
		stock_each[COID] = float(arow['ROI']) 
		stock_each_num[COID] = 1
	else:
		stock_each[COID] = float(arow['ROI']) #卡在無法新增append new ROI在同一支股票
		stock_each_num[COID] += 1
	# stock_each[arow['MDATE']] = float(arow['ROI'])  #問題點卡到相加
	# stock_each_count = len (stock_each)
	if ( this_coid != last_coid):
		if (len(sret) > minlen):
			print("Run regression for COID:", last_coid)
			# out1 = compute_model( sret, sdate, mktret)
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
print(len(stock_each))
print(stock_each)
print(len(stock_each_num))

xlist = [] #大盤的ROI
for i in range(0, len(sdate)):    #就講好到1201 共223筆
	xlist.append(mktret[sdate[i]])
# print("xlist num:",len(xlist), "stock_each num:", len(stock_each),stock_each_count)
# print(stock_each['20161201'])


#到此之前

# if len(xlist) != len(ylist):
	# raise Exception("Data length Error!")
	# return simple_reg(xlist, ylist)
# def simple_reg(xlist, ylist):
sum_alpha = sum_beta = avg_alpha = avg_beta = 0.00 
alpha_num = beta_num = 0
for i in range(0, len(xlist)) :
	sum_alpha =  sum_alpha + xlist[i]
	alpha_num += 1
avg_alpha = sum_alpha / alpha_num
print(alpha_num, sum_alpha, avg_alpha)
	# return [alpha, beta, s, r2]
	
# sdate = ['20160118', '20160119', '20160120', '20160121', '20160122']
# xlist = []
# for i in range(0,len(sdate)): #蒐集日期內的大盤market return
	# xlist.append(mktret[sdate[i]])
# print(xlist)#顯示xlist 所有return
# print(mktret['20161202'])

#close the file
file_bigmarket2.close()
sorted_stockdata.close()