def make_sample(zido,col):
    
    return sample
def main():
    # 반복문을 세로로 돌면서
    # 1이면 col을 1로 바꿈
    for i in range(c):
        make_sample(zido)
        rs = i
        j = 1
        if i==0:
            continue
        while j == c:
            if zido[rs][j] == 1:
                rs +=1
            if zido[rs][j] == -1:
                rs -= 1
            j +=1
    return None

if __name__ =='__main__':
    c,r,num = map(int,input().split())
    if r ==0:
        print(0)
        exit()
    # count_sadari
    zido = [[0]*(c+1) for i in range(c+1)]

    for _ in range(r):
        x,y = map(int,input().split())
        zido[x][y] = 1

    for i in zido:
        print(i)