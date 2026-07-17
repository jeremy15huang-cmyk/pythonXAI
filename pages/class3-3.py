#算術指定運算子
a = 1
a += 1 #a = a + 1
print(a) #2
a -= 1 #a = a - 1
print(a) #1
a *= 2 #a = a * 2
print(a) #2
a /= 2 #a = a / 2
print(a) #1.0
a //= 2 #a = a // 2
print(a) #0
a %= 2 #a = a % 2
print(a) #0.0
a **= 2 #a = a ** 2
print(a) #0.0

# 優先順序
# 1. () 括號
# 2. ** 次方
# 3. * / // % 乘 除 取商 取餘數
# 4. + - 加 減
# 5. == != > < >= <= 比較運算子
# 6. not
# 7. and
# 8. or
# 9. = += -= *= /= //= %= **= 算數指定運算子

#while 迴圈
#while 會搭配一個條件式來使用
#條件式為 True 時會一直執行迴圈
#條件式為 False 時會跳出迴圈
#每次回圈執行完都會心檢查條件有沒有變成False
i = 0
while i < 5:
    print(i)
    i += 1 #i = i + 1

#break 可以跳出迴圈
#先判斷break屬於哪個迴圈，然後跳出迴圈
i = 0
while i < 5:
    if i < 5:
        print(i)

        for j in range(5):
            print(j)
            if i == 3:
                break #跳出迴圈, 屬於while迴圈
        i += 1

for i in range(5):
            print(i)
            if i == 3:
                break #跳出迴圈

import random #匯入random模組

#random.randrange()設定抽籤範圍的方式跟range()一樣
print(random.randrage(7)) #0~6
print(random.randrange(1, 6)) #1~6
print(random.randrange(1, 6, 2)) #1~6, 間隔2

