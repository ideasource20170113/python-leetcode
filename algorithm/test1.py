# 给出任意整数，求得每一位相加之和

def ek(nums):
    nums = str(nums)
    L = [0]
    for num in nums:
        num = int(num)
        L[0] = L[0] + num
    print(L[0])
