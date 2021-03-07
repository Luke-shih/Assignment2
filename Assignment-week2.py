# 要求一：函式與流程控制
# 完成以下函式，在函式中 使用迴圈 計算最小值到最大值之間，所有整數的總和。
def calculate(min,max):
    sum=0
    for n in range(min,max+1):
        sum=sum+n
    print(sum)
calculate(1, 3)       
calculate(4, 8)

# 要求二：Python 字典與列表、JavaScript 物件與陣列
# 完成以下函式，正確計算出員工的平均薪資，請考慮員工數量會變動的情況。
def avg(data):
    sum = 0
    value_list = list(data.values())
    for x in value_list[1]:
        a = list(x.values())
        sum += a[1]
    print(sum/value_list[0])
avg({
  "count":3,
    "employees":[
        {
            "name":"John",
            "salary":30000
        },
        {
            "name":"Bob",
            "salary":60000
        },
        {
            "name":"Jenny",
            "salary":50000
        }
    ]
}) # 呼叫 avg 函式

# 要求三：演算法
# 找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。
def maxProduct(nums):
    a = nums[0]
    b = nums[1]
    n = len(nums)
    for i in range(0, n):
        for j in range(i + 1, n):
            if (nums[i] * nums[j] > a * b):
                a = nums[i]
                b = nums[j]
    print(a * b)
maxProduct([5, 20, 2, 6]) # 得到 120 因為 20 和 6 相乘得到最大值
maxProduct([10, -20, 0, 3]) # 得到 30 因為 10 和 3 相乘得到最大值

# 要求四 ( 請閱讀英文 )：演算法
# Given an array of integers, show indices of the two numbers such that they add up to a
# specific target. You can assume that each input would have exactly one solution, and you
# can not use the same element twice.
def twoSum(nums, target):
    for i in range(len(nums)):
        b = nums[i+1:]
        for j in range(len(b)):
            if (nums[i] + b[j]) == target:
                return i, j+i+1
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9