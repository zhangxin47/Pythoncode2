import csv
bigmarket = "C:\\Users\\b1013\\Desktop\\Pythoncode2\\bigmarket_in.csv"
file_bigmarket2 = open(bigmarket, "r", encoding ="utf-8", newline ="")
reader1 = csv.DictReader(file_bigmarket2, delimiter=',')
mktret = dict()

for arow in reader1:
	mktret[arow['MDATE']] = float(arow['ROI'])

file_bigmarket2.close()