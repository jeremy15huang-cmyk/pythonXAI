#字典
#dict是透過key-value的方式來儲存資料，key是唯一的，value可以重複
#dict是無序的，所以無法透過index來取得資料
#dict的key必須是不可變的資料型態，例如: int, float, string
#dict的value可以是任何資料型態，例如: int, float, string
#dict的key-value是透過冒號來連接，key::value
#dict的key-value是透過逗號來分隔，key::value
d = {"a": 1, "b": 2, "c": 3}

#取的dict的key
print(d.keys()) #dict_keys(['a', 'b', 'c'])
for key in d.keys():
    print(key)

#取得dict的key
print(d.keys()) #dict_keys(['1', '2', '3'])
for key in d.keys():
    print(key)

#取得dict的value
print(d.values()) #dict_values([1, 2, 3])
for value in d.values():
    print(value)

#新增/修改dict的key-value
d["d"] = 4 #新增
print(d) #{'a': 1, 'b': 2, 'c': 3, 'd': 4}
d["a"] = 5 #修改
print(d) #{'a': 5, 'b': 2, 'c': 3, 'd': 4}

#刪除dict的key-value, pop (方法)
#如果資料有存在，就會刪除蹦回傳value
print(d.pop("a")) #5
#如果資料不存在，就會回傳預設值
print(d.pop("e", "Not found")) #Not found
#如果資料不存在也沒有預設值，就會報錯

#檢查dict是否有某個key
#in不能檢查value
#跟list比較，in可以檢查的是list的元素與dict的key
print("a" in d) #True
print("e" in d) #False

# 成績登記系統，key是學生名字，value是學生的成績，每個科目有3個成績
grade = {
    "小明": {"國文": [90, 80, 70], "數學": [85, 75, 65], "英文": [95, 85, 75]},
    "小美": {"國文": [88, 78, 68], "數學": [83, 73, 63], "英文": [93, 83, 73]},
    "小華": {"國文": [86, 76, 66], "數學": [81, 71, 61], "英文": [91, 81, 71]},
}

# 取得小明的數學成績
print(grade["小明"]["數學"])  # [85, 75, 65]
# 取得小美的第一次英文成績
print(grade["小美"]["英文"][0])  # 93
# 取得小華的第二次國文成績
print(grade["小華"]["國文"][1])  # 76


# 印出每一位同學的國文段考平均成績
for name, subjects in grade.items():
    # 取得國文成績
    chinese = subjects["國文"]
    # 計算平均成績
    avg = sum(chinese) / len(chinese)
    print(f"{name}的國文段考平均成績是{avg:.2f}")



# 印出每一位同學的總平均成績
for name, subjects in grade.items():
    total = 0
    for scores in subjects.values():
        total += sum(scores)
    avg = total / (len(subjects) * 3)
    print(f"{name}的總平均成績是{avg:.2f}")



# 整理全校各科目的平均成績
# 建立一個dict用來存放各科目的成績
avg_grade = {"國文": [], "數學": [], "英文": []}
# 逐一取得每一位同學的成績
for subjects in grade.values():  # 取得每一位同學的各科成績
    # subject={"國文": [90, 80, 70], "數學": [85, 75, 65], "英文": [95, 85, 75]}
    # 逐一取得每一位同學的各科成績
    for subject, scores in subjects.items():
        # scores=[90, 80, 70]
        # 將各科成績加入avg_grade
        avg_grade[subject] += scores
print(avg_grade)
avg_grade = {
'國文': [90, 80, 70, 88, 78, 68, 86, 76, 66],
'數學': [85, 75, 65, 83, 73, 63, 81, 71, 61],
'英文': [95, 85, 75, 93, 83, 73, 91, 81, 71]
}

# dict取長度, 取得dict的key的數量
print(len(avg_grade))  # 3