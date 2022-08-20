import sys

sys.setrecursionlimit(10 ** 6) # 재귀 최대 깊이 설정(대부분의 파이썬 재귀 최대 깊이의 기본 설정이 1,000회 이기 때문에 런타임 에러가 발생)
input = sys.stdin.readline
N, M = map(int, input().split())
adj = [[0] * N for _ in range(N)] # 인접행렬
for _ in range(M):
  a, b = map(lambda x: x -1, map(int, input().split())) # 람다 이용하여 a와 b -1씩
  adj[a][b] = adj[b][a] = 1

ans = 0
chk = [False] * N

def dfs(now):
  for next in range(N):
    if adj[now][next] and not chk[next]:
      chk[next] = True
      dfs(next)

for i in range(N):
  if not chk[i]:
    ans += 1 # 비어있는 곳 만나면 연결 요소 갯수 더한 후 True로 변경
    chk[i] = True
    dfs(i)

print(ans)
