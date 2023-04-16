import sys
input = sys.stdin.readline

k, n = map(int, input().split())
line = [int(input()) for _ in range(k)]

start = 1
end = max(line)

while start <= end:
    mid = (start + end) // 2
    
    sum_ = 0
    for i in range(len(line)):
        sum_ += (line[i] // mid)
    
    if sum_ < n:
        end = mid - 1
    else:
        start = mid + 1

print(end)