class Maxheap:
    def __init__(self):
        self.heap = []
        self.heap.append(0)        # 1부터 시작
    def size(self):
        return len(self.heap)-1    # 1부터 시작이니까 삭제
    def isEmpty(self):
        return self.size()==0
    def Parent(self,i):            # 해당 i의 부모 노드를 반환
        return self.heap[i//2]
    def Left(self,i):              # 왼쪽 자식 노드를 반환
        return self.heap[i*2]
    def Right(self,i):             # 오른쪽 자식 노드를 반환
        return self.heap[i*2+1]
    def display(self,msg = '힙트리 : '):
        print(msg, self.heap[1:])
    def insert(self,n):
        self.heap.append(n)                 # 맨 마지막에 노드로 일단 삽입
        i = self.size()                     # 노드 n의 위치 맨 마지막(삽입한 노드의 위치)
        while (i!=1 and n> self.Parent(i)): # 부모보다 큰 동안 계속 업힙
            self.heap[i] = self.Parent(i)   # 부모와 위치 변경
            i //= 2                         # 변경된 인덱스 업데이트
        self.heap[i] = n                    # 올라간 마지막 위치에 n삽입
    
    def delete(self):
        parent = 1
        child = 2
        if not self.isEmpty():
            hroot = self.heap[1]           # 나중에 삭제할 루트
            last = self.heap[self.size()]  # 마지막 노드
            while (child <= self.size()):  # 마지막 노드 이전까지
								# 만약 오른쪽 노드가 더 크면 child 1증가 (기본은 왼쪽 노드
                if child <self.size() and self.Left(parent) <self.Right(parent):
                    child +=1
                if last >= self.heap[child]:         # 더 큰 자식이 더 작으면
                    break;                           # 삽입 위치를 찾음. 종료
                self.heap[parent] = self.heap[child] # downheap 계속
                parent = child
                child *=2
            self.heap[parent] = last                 # 맨 마지막 노드를 parent로 복사
            self.heap.pop(-1)                        # 맨 마지막 노드 삭제
            return hroot                             # 저장해두었던 루트를 반환
        
if __name__=='__main__':
    heap = Maxheap()
    data = [2,5,4,8,9,3,7,3]
    print('삽입한 데이터', data)
    for e in data:
        heap.insert(e)
    heap.display('삽입후 : ')
    heap.delete()
    heap.display('삭제 후 : ')
    heap.delete()
    heap.display('삭제 후 : ')
