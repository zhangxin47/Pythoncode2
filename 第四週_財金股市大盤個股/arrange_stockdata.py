import csv
import os
stockfn = "C:\\Users\\b1013\\Desktop\\Pythoncode2\\stockdata.txt"   #開啟檔案文字檔
file1 = open(stockfn, "r", encoding = "cp950", newline = "")      # 因下載下來為big5
cheader = file1.readline()  #把第一行讀出來即丟棄
file1_rows = csv.reader(file1, delimiter = "\t")  #每一列為tab 
stockfn_in = "C:\\Users\\b1013\\Desktop\\Pythoncode2\\stock_tmp3.csv"
file_in = open(stockfn_in, "w", encoding = "utf-8", newline = "")  # 開啟檔案
writer_in = csv.writer(file_in) #讓其可寫入

for i in file1_rows:   #利用for去寫入 將個股空白去除
	i = map( lambda x: x.strip(), i)  
	writer_in.writerow(i)

import csvsorter   
wd = "C:\\Users\\b1013\\Desktop\\Pythoncode2"
os.chdir(wd)
stockfn_tmp3 = "C:\\Users\\b1013\\Desktop\\Pythoncode2\\stock_tmp3.csv"  #來源檔
stocksorted = "C:\\Users\\b1013\\Desktop\\Pythoncode2\\stocksorted.csv"  #整理後檔
csvsorter.csvsort( stockfn_tmp3, [0,2], output_filename = stocksorted , has_header = True) # 來源檔, 排序方式, 目的檔, 是否有標題

#匯入market大盤資料
marketfn = "C:\\Users\\b1013\\Desktop\\Pythoncode2\\bigmarket.txt"
filebigmarket = open(marketfn, "r", encoding = "cp950" ,newline = "")
cheader1 = filebigmarket.readline()  #把第一行讀出來即丟棄
file_big_rows = csv.reader( filebigmarket, delimiter = "\t") 
bigmarket_in = "C:\\Users\\b1013\\Desktop\\Pythoncode2\\bigmarket_in.csv"
file_bigmarket_in = open(bigmarket_in, "w", encoding = "utf-8", newline ="")  # 開啟檔案
writer_big_in = csv.writer(file_bigmarket_in)  #讓其可寫入

for i in file_big_rows:   #利用for去寫入 將個股空白去除
	i = map( lambda x: x.strip(), i)
	writer_big_in.writerow(i)
#close the file
file_in.close()
file1.close()
filebigmarket.close()
file_bigmarket_in.close()
