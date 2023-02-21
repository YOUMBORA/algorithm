def solution(nums):
    n = len(nums)//2
    u = len(set(nums))
    return min(n,u)