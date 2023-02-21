def solution(nums):
    a = int(len(nums) / 2)

    num = set(nums)
    print(num)

    if a < len(num):
        return a
    else:
        return len(num)
