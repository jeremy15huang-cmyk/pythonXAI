print([]) #這是一個空的list
print([1,2,3]) #這是一個有三個元素的list
print([1,2,3,"a","b","c"]) #這是一個有六個元素的list
print([1,2,3,["a","b","c"]]) #這是一個有四個元素的list
print([1,True,"a",1.23]) #這是一個有四個元素的list

#list 讀取元素，元素的index從0開始
L= [1,2,3,"a","b","c"]
print(L[0]) #1
print(L[1]) #2
print(L[2]) #3
print(L[3]) #"a"

L = [1,2,3,"a","b","c"]
#就是取index 0到最後，每次取2個元素，所以是[1,3,'b']
print(L[::2])
#就是取index 1到3的元素，不包含index 4，所以是[2,3,'a']
print(L[1:4])
#就是取index 1到3的元素，不包含index 4，並且每次取2個元素，所以是[2,'a']
print(L[1:4:2])
#跟range一樣的用法，只是符號不同

#list的append
L=[1,2,3]
L.append(4) #把4加到L最後面
print(L)

#list的移除元素方式有兩種
#1. 使用remove，可以移除指定的元素
L=["a","b","c","d","a"]
L.remove("a") #移除第一個"a"
#代表remove會從頭開始找，找到第一個符合的元素就會移除
#如果想要移除所有符合的元素，可以使用迴圈
for i in L:
    if i == "a":
        L.remove(i)

#2. 使用pop，可以移除指定的index的元素
L=["a","b","c","d","a"]
L.pop(0) #移除index 0的元素
#代表pop會移除指定的index的元素
#如果不指定index，則會移除最後一 個元素
L.pop() #移除最後一個元素

#sort:將List中的元素進行排序，預設事由小到大 (升序排列)
#注意:這個方法會直接修改原本的List，不會產生新的List
L=[1,3,2,4,5]
L.sort()
print(L)