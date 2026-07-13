print("Hello World") 
print("黃郁捷")
print("不要低頭\n雙下巴會出來")
"""
這是多行註解
"""

#這是單行註解
print("Hello World!") #print是在終端機顯示文字的指令
#ctrl + ? 可以快速註解/取消註解

#基本型態
print (1) #int這是整數, -1,0,1,2,3,4,5,6,7,8,9
print (1.0) #float這是浮點數
print (1.234) #float這是浮點數
print ("apple") #str這是字串 "sadas123125557", '1'
print (True) #bool這是布林值 True/False
print (False) #bool這是布林值 True/False

#變數
a = 10 #新增一個儲存空間並取名為a, "="的功能是將右邊的值10存入左邊的a
print(a) #在終端機上顯示a所存的值
a = "apple" #將a的值改為"apple"
print(a) #在終端機上顯示a所存的值

#運算子
print(1+1) #加法
print(1-1) #減法
print(1*1) #乘法
print(1/1) #除法
print(1//1) #取商
print(1%1) #取餘數
print(2**3) #次方

#優先順序
# 1.() 括號
# 2.** 次方
# 3./ // % 乘 除 取商 取餘數
# 4.+ - 加 減  



#字串運算 ，+ ` *
print("apple" + "pen") #字串相加
print("apple" * 3) #字串乘法

#字串格式化
name = "apple"
age = 18
print(f"Hello, my name is {name}, I'm {age} years old.")  # f-string