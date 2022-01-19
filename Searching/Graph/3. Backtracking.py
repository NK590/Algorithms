### Backtracking (백트래킹)

# 특정 조건을 만족하는 해답을 찾기위한 일련의 탐색 과정
# 주어진 조건에 맞게 탐색을 하다 해답이 아니면 되돌아가서 다른 경로를 탐색하는 방식으로,
# 그 특성상 DFS가 주로 사용되나, 제한적으로 BFS가 사용될 수도 있음

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
