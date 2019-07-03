
#ord 將英文字轉成數字 chr 將數字轉成對應英文字
#checksum 將數字乘銓重去計算其是否符合
#因身分證字號有權重 [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
# C220565187=> C121529754=>
def check_ID(ID):
	if (len(ID)!=10): #確認是否為 10 個
		print("ID不為10")
		return False
	if (ord(ID[0]) < 65 or ord(ID[0]) > 90 ): #確認第一碼英文字母是否正確
		print("ID 第一碼錯")
		return False
	if ( (ID[1]!= '1') and (ID[1]!= '2') ): #確認第二碼數字是否為1或2
		print("ID 第二碼錯")
		return False
	codenumber = ID[2:]
	
	for i in codenumber:
		if ( ord(i) < 48 or ord(i) > 57): #確認後續數字是否正確
			print("ID 數字碼錯誤")
			return False
	
	cmap=[10, 11, 12, 13, 14, 15, 16, 17, \
	  34, 18, 19, 20, 21, 22, 35, 23, 24, \
	  25, 26, 27, 28, 29, 32, 30, 31, 33]
	transcode0 = cmap [ord(ID[0]) - 65] #把第一碼轉成對照
	newID = str(transcode0) + ID[1:] #新 ID 產生
	checksum = 0
	weight=[1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1] 
	eachpair = map( lambda cpair: int( cpair[0]) * cpair[1] , zip( newID, weight))
	checksum = sum(eachpair)
	if (checksum % 10 != 0):
		print("ID 數字邏輯權重錯誤")
		return False
	else:
		return True

ID = input("input your ID number:")
print(check_ID(ID))

