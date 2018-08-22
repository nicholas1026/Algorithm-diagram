import random

#####生成指定个数随机数的有序列表#####
def make_list(nCount):
    nList = []
    n = 0
    while n < nCount:
        nList.append(random.randint(0,100))
        n += 1

    nList.sort()
    return nList


#####二分查找函数#####
def binary_search(list,item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None

my_list = make_list(20)

print(my_list)

#print(binary_search(my_list,8))
#print(binary_search(my_list,-1))
#print(binary_search(my_list,16))
