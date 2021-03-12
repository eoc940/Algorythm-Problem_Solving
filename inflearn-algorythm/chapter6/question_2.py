# 이진트리 순회(DFS-깊이우선탐색)
'''
부모, 왼쪽, 오른쪽 노드가 있다고 할 때
전위순회 -> 부 - 왼 - 오
중위순회 -> 왼 - 부 - 오
후위순회 -> 왼 - 오 - 부
'''
def DFS(v) :
    if v > 7 : # 노드가 7까지 있음
        return
    else :
        #print(v, end=" ") # 함수 호출되기 전에 자기 일을 먼저 함 -> 전위순회
        DFS(v*2)
        #print(v, end=" ")  # 왼쪽과 오른쪽 사이에서 자기 일을 함 -> 중위순회
        DFS(v*2+1)
        print(v, end=" ")  # 함수가 호출되고 나서 자기 일을 함 -> 후위순회
if __name__ == "__main__" :
    DFS(1)
