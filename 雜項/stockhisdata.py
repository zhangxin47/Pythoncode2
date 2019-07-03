import csv
with open("C:\\Users\\b1013\\Desktop\\Pythoncode2\\stockdata.csv", "r", newline="") as csvfile: #可不用寫檔名.close
	fh1 = csv.reader(csvfile)
	reader1 = csv.reader( fh1, delimiter = ",")
	with open("C:\\Users\\b1013\\Desktop\\Pythoncode2\\stock_tmp.csv", "w", newline="") as csvfilewriter:
		writer3 = csv.writer(csvfilewriter)
		for arow in reader1:
			arow = map( lambda x: x.strip(), arow)
			writer3.writerow(arow)
		# for arow in reader1:
			# arow = map( lambda x: x.strip(), arow)
			# writer3.writerow(arow)
	
# #建立可寫入檔案
# stock_temp = "C:\\Users\\b1013\\Desktop\\Pythoncode2\\stock_temp.csv"
# fh3 = open(stock_temp, "w" , encoding = "utf-8" , newline= "") #建立新檔案空白可寫入
# writer3 = csv.writer(fh3)
# for arrow in reader1:
	# arrow = map(lambda x: x.strip(), arrow)
	# writer3.writerow(arrow)
# fh3.close()
# fh1.close()

