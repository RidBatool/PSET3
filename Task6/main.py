def find_repeated(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)

nums = [2, 1, 2, 5, 3, 2]
print(find_repeated(nums))
