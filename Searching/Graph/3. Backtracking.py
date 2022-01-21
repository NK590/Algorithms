### Backtracking (백트래킹)

# 특정 조건을 만족하는 해답을 찾기위한 일련의 탐색 과정
# 주어진 조건에 맞게 탐색을 하다 해답이 아니면 도중에 되돌아가서 다른 경로를 탐색하는 방식으로,
# 그 특성상 DFS가 주로 사용되나, 제한적으로 BFS가 사용될 수도 있음
# 전수조사를 하게 되면 탐색해야 되는 경우의 수가 일반적으로 매우 커지므로,
# 문제에서 주어지는 각종 제약 조건을 잘 활용하여 탐색하는 가지수를 줄여나가는 게 중요

### 예제 1
'''
1부터 n까지의 자연수 중에서 중복 없이 m개를 고른 수열을 모두 출력하시오.
단, 수열은 사전 순으로 증가하는 순서로 출력해야 한다.
'''

import sys

n, m = map(int, sys.stdin.readline().split())
li = [x for x in range(1, n+1)]
visited = []

def DFS():
    if len(visited) == m:
        print(' '.join(map(str, visited)))
        return
    for num in li:
        if num not in visited:
            visited.append(num)
            DFS()
            visited.pop()

DFS()

### 예제 2
'''
N이 주어졌을 때, 크기가 N * N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 배치하는 경우의 수를 구하시오.
(N-Queen 문제)
'''

n = int(sys.stdin.readline())

ans = 0
v = [0 for _ in range(n)]

def backtracking(row):
    global ans
    
    if row == n:
        ans += 1
        return
    
    for c in range(n):
        chk = True
        for r in range(row):
            if v[r] == c or row - r == abs(v[r] - c):
                chk = False
                break
        
        if chk:
            v[row] = c
            backtracking(row + 1)

backtracking(0)

print(ans)