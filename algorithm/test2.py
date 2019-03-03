# 给出一个列表，求最大值

def max(list):
    L = [0]
    for num in list:
        num = int(num)
        if num > L[0]:
            L[0] = num
    print(L[0])

