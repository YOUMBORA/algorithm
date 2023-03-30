N = int(input())

sum_ = [0 for _ in range(N)]

for i in range(N):
  if i == 0:
    first = int(input())
    sum_[0] = first
  
  elif i == 1:
    A, B = map(int, input().split())
    sum_[0] = first + A
    sum_[1] = first + B

  else:
    list_ = list(map(int, input().split()))
    cnt = 0
    cal_ = list(sum_)

    for x in range(len(list_)):
      if x == 0:
        sum_[x] = cal_[0] + list_[0]
      elif x == len(list_)-1:
        sum_[x] = cal_[x-1] + list_[x]
      
      else:
        sum_[x] = max((cal_[x-1] + list_[x]) , (cal_[x] + list_[x]))

print(max(sum_))
