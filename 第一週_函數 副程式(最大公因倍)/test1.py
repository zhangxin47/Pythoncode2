# def abc(a,b):
	# print("I love you %s times,but you love me %d times" %(a,b))
	# print()
	# c=a+1
	# return c

# for num in range(1,5):
	# """次數
	# 多航
	# 很多"""
	# avalue=abc(num,num+1)
	# print(avalue)
	# # print(c)  因c為區域變數

# def test(f6):
	# f6[0]=5
	# f6[1]=55
	# f6[2]=555
	# f6[3]=5555

# list=[] #放四個數
# for i in range(4):
	# list.append(input("input %d value:" %i))
	# list[i]=int(list[i])
	
# print(list)
# test(list)
# print("change list:", list)

#質數
# list=[]
# for i in range(101):
	# for j in range(2 , i):
		# if ( i % j == 0):
			# break
	# else:
		# list.append(i)
# list.remove(0)
# list.remove(1)
# print(list)

def fac(n):
	space = " " * (4*n)
	print ( space , "fac(%i)" %n)
	if not isinstance( n , int):
		print("error")
		return None
	elif (n < 0):
		print("negative")
		return None
	elif (n == 0 ):
		print(space , "result=1") 
		return 1
	else:
		result= n * fac(n-1)
		print (space,"result=%i" % result)
		return result

n=int(input("input your n:"))
print(fac(n))
# dictionary_tk = {
  # "name": "Lean",
  # "nickname": "Tk",
  # "nationality": "Brazilian"
# }

# dictionary_tk['age'] = 24

# print(dictionary_tk) # {'nationality': 'Brazilian', 'age': 24, 'nickname': 'Tk', 'name': 'Leandro'}
# list=[1,2,3,4,6]
# print( list[0:])
# ID=input("input your ID number:")
# print(type(ID[1]))

# if ( (ID[1]!= '1') or (ID[1]!= '2') ): #確認第二碼數字是否為1或2
	# print("ID 第二碼錯")

# msg="www.yahoo.com"
# print(msg)
# print("www.yahoo.com".strip("ma"))

# list=[21830, 31649, 31243, 24335, 35373, 35336]
# listtra=[]
# print(chr(list[2]))
# for i in list:
	# listtra.append(chr(i))
# print(listtra)

# if ('a' < 'c'):
	# print("True")
	
# for num in range(2 , 100):
	# for i in range(2,num):
		# if(num % i == 0):
			# break
	# else:
		# print(num)
# import math
# list2=[1, 2, 3]
# list1=[2, 3, 5]
# sum2 = 0 
# pair = zip( list2, list1)
# for i in zip( list2, list1):
	# sum2 += int(i[0]) * i[1]
	# print(i)
# print(sum2)
# print(pair)

# ans = lambda c: pow(c,3)
# out = map( ans, list2)
# print(list(out) )
# pow4=lambda e: pow(e,4)
# test = map( pow4 , list2)
# print( list(test))

# def hist(list3):
	# d = dict()
	# for element in list3:
		# if element not in d:
			# d[element] = 1
		# else:
			# d[element]+=1
	# return d
# def print_dict(ans):
	# for i,j in ans.items():
		# print( i, j )
	# ans.items()
	# print(ans.items())
	

# list3="brontosaurus"
# ans = hist(list3)
# print(ans)
# print_dict(ans)

# import datetime
# d1=datetime.datetime(2010, 3, 2, 12 , 15, 0)
# sec= (10*60+3)*60
# d2=datetime.timedelta(days=145, seconds=sec)
# d1 = d1+d2
# print(str(d1))

# dictionary_tk = {"name": "Lean","nickname": "Tk","nationality": "Brazilian"}
# print(dictionary_tk["name"])
	
