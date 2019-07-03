#read
fn1 = "C:\\Users\\b1013\\Desktop\\Pythoncode2\\reading.txt"
fh1 = open(fn1 , "r", encoding= "utf-8")
linecount = 0
for aline in fh1:
	linecount += 1
	if len(aline) < 75 :
		print("%02d:%s" % (linecount, aline.strip()))
	else:
		print("%02d:%s...(truncated)" % (linecount, aline[0:75]))
fh1.close()

#write
name = input("input your name:")
birth = input("input your birth:")
fn2 = "C:\\Users\\b1013\\Desktop\\Pythoncode2\\trywrite.txt"
fn2 = open(fn2, "w", encoding= "utf-8")
fn2.write( name +"\n")
fn2.write( birth +"\n")
fn2.close()

#exception
while True:
	try:
		x = int(input("input your number:"))
		if(x > 0):
			break
	except ValueError:
		print("輸入非數字或小於0")
print("your number is %i" %x)

#擲硬幣
import random
def throw(prob = 0.5):
	if (prob < 0 or prob > 1):
		raise Exception("Error!!!!")
	if random.random() < prob:
		return "head"
	else:
		return "tail"
print(throw())
