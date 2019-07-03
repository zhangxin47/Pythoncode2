import csv
import os
stockfn = "C:\\Users\\b1013\\Desktop\\Pythoncode2\\stockdata.txt"   #開啟檔案文字檔
file1 = open(stockfn, "r", encoding = "cp950", newline = "")      # 因下載下來為big5
cheader = file1.readline()  #把第一行讀出來即丟棄
file1_rows = csv.reader(file1, delimiter = "\t")  #每一列為tab 
stockfn_in = "C:\\Users\\b1013\\Desktop\\Pythoncode2\\stock_tmp3.csv"
file_in = open(stockfn_in, "w", encoding = "utf-8", newline = "")  #輸入檔案
writer_in = csv.writer(file_in)

for i in file1_rows:   #利用for去寫入 將個股空白去除
	i = map( lambda x: x.strip(), i)
	writer_in.writerow(i)

import csvsorter
wd = "C:\\Users\\b1013\\Desktop\\Pythoncode2"
os.chdir(wd)
stockfn_tmp3 = "C:\\Users\\b1013\\Desktop\\Pythoncode2\\stock_tmp3.csv"
stocksorted = "C:\\Users\\b1013\\Desktop\\Pythoncode2\\stocksorted.csv"
csvsorter.csvsort( stockfn_tmp3, [0,2], output_filename = stocksorted , has_header = True) # 來源檔, 排序方式, 目的檔, 是否有標題

#匯入market大盤資料
marketfn = "C:\\Users\\b1013\\Desktop\\Pythoncode2\\bigmarket.txt"
filebigmarket = open(marketfn, "r", encoding = "cp950" ,newline = "")
cheader1 = filebigmarket.readline()  #把第一行讀出來即丟棄
file_big_rows = csv.reader( filebigmarket, delimiter = "\t") 
bigmarket_in = "C:\\Users\\b1013\\Desktop\\Pythoncode2\\bigmarket_in.csv"
file_bigmarket_in = open(bigmarket_in, "w", encoding = "utf-8", newline ="") 
writer_big_in = csv.writer(file_bigmarket_in)

for i in file_big_rows:   #作空白去除
	i = map( lambda x: x.strip(), i)
	writer_big_in.writerow(i)

bigmarket = "C:\\Users\\b1013\\Desktop\\Pythoncode2\\bigmarket_in.csv"
file_bigmarket2 = open(bigmarket, "r", encoding ="utf-8", newline ="")  
reader1 = csv.DictReader(file_bigmarket2)
mktret = dict()

# def compute_model(ylist, sdate, mktret):
	# """
		# ylist: list of stock return
		# sdate: list of return dates
		# mktret: market return dict
	# """
	# xlist = []
	# for i in range(0, len(sdate)):
		# xlist.append(mktret[sdate[i]])
	# if (xlist

# def simple_reg(xlist, ylist):
	# return [alpha, beta, s, r2]


for arow in reader1:   #使大盤日期對應相對ROI
	mktret[arow['MDATE']] = float(arow['ROI']) #少了12月的19筆 不知原因 索性弄到20161202
	print(arow['MDATE'])
print("Read %d market return data " % len(mktret)) #少了12月的19筆 不知原因 索性弄到20161202

sret= []  #存放個股報酬
sdate= [] #存個股日期
last_coid = ""  #前一筆股票代碼
last_name = ""  #前一筆股票名稱
this_coid = ""  #這一筆股票代碼
this_name = ""  #這一筆股票名稱
minlen = 50

sorted_stock = "C:\\Users\\b1013\\Desktop\\Pythoncode2\\stocksorted.csv"
sorted_stockdata = open( sorted_stock, "r", encoding ="utf-8", newline ="")
sortedreader = csv.DictReader(sorted_stockdata, delimiter = ',')

for arow in sortedreader: #要以dict 去存放資料比對
	this_coid = arow["COID"].strip()
	this_name = arow["Name"].strip()
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
		sdate.append(arow['MDATE'].strip()) #紀錄20160104後到20161202
	last_coid = this_coid
	last_name = this_name
#測試整合market return list
# print(sdate)
sdate = ['20160118', '20160119', '20160120', '20160121', '20160122']
xlist = []
for i in range(0,len(sdate)): #蒐集日期內的大盤market return
	xlist.append(mktret[sdate[i]])

print(xlist)#顯示xlist 所有return
print(mktret['20161202'])


file_bigmarket2.close()
file_in.close()
filebigmarket.close()
file_bigmarket_in.close()
sorted_stockdata.close()