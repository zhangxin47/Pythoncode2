#最小公倍數
import math
a=int(input("請輸入第一個數:"))
b=int(input("請輸入第二個數:"))
tep=0
fac=0
minimal=min(a,b)
for i in range(1,minimal+1):
	if ( (a % i ==0) and ( b % i ==0)):
		fac = i
print("最大公因數%i" %fac)

if ( a % fac ==0):
	pua = int(a / fac)
if ( b % fac ==0):
	pub = int(b / fac)
max=0
max = fac * pua * pub
print("最大公倍數 %i" %max)

	