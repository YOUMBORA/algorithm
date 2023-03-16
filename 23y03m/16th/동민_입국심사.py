def solution(n, times):
    answer = 0
    start = 0
    end = times[0]*n
    
    while start<end:
        mid = (start+end)//2
        capable_num = sum(map(lambda x: (mid//x),times))
        
        if capable_num >= n:
            end = mid
        elif capable_num < n:
            start = mid+1
            
    answer = start
    return answer
  
  """
  1. end를 최대로 설정해야함.
  2. 처음에는 배수들을 list에 다 넣고 했음. -> 시간초과
  3. 되는 것들 중에 최소를 찾아야하기 때문에, start,end,mid,answer를 설정하는게 꽤 복잡했음. 하지만 찬찬히 생각해보면 좋을 듯 함. 이렇게 여러개의 후보들 중 최소를 찾아야 하는 경우 등호를 껴놓고 mid와의 관계를 잘 생각해야할 듯 함.
  4. 시간복잡도에 되게 민감한 문제였다. 알고리즘을 줄여서 애초에 times를 sum해야하는건 필수같았기에 다른 것에서 줄여야 한다고 생각했는데 그 중 하나가 이분탐색이었다. 시간복잡도는 m=len(times)라고 하였을 때 mlogm이려나?
  """
