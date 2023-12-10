nums = input("Введите числа через запятую:")
nums = list(map(lambda x: int(x), nums.split(",")))


print(nums)
# list.sort(reverse = True)
# result = 0
# for i in range(0,len(list)-1):
#     result += list[i]-list[i+1]
# print(result)