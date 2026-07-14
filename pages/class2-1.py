#比較運算子，只能同樣類型作比較
print(1==1) #True
print(1!=1) #False
print(1>1) #False
print(1<1) #False
print(1>=1) #True
print(1<=1) #True

#邏輯運算子
#and 運算子，只要有一個False，結果就是False
print(True and True) #True
print(True and False) #False
print(False and True) #False
print(False and False) #False

#or 運算子，只要有一個True，結果就是True
print(True or True) #True
print(True or False) #True
print(False or True) #True
print(False or False) #False

# not 運算子
print(not True)  # False
print(not False)  # True

# 優先順序
# 1. () 括號
# 2. ** 次方
# 3. * / // % 乘 除 取商 取餘數
# 4. + - 加 減
# 5. == != > < >= <= 比較運算子
# 6. not
# 7. and
# 8. or

#密碼檢查
password = input("請輸入密碼：")
if password == "1234":
    print("歡迎Jeffery")
elif password == "5678":
    print("歡迎Tim")
elif password == "0000":
    print("歡迎chloe")
else:
    print("密碼錯誤")
#連續使用if跟使用if elif else的差別
#elif可以排除前面有判斷過的條件，所以縮短判斷條件的複雜度，也節省時間
#但是如果使用多個if來獨立判斷，則每個if都會被執行，所以效率降低