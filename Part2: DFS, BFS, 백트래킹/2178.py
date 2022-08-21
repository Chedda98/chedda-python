from collections import deque

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

N, M = map(int, input().split())
board = [input() for _ in range(N)]

def is_valid_coord(y, x):
  return 0 <= y < N and 0 <= x < M

def bfs():
  chk = [[False] * M for _ in range(N)] # 무한반복 방지
  chk[0][0] = True
  dq = deque()
  dq.append((0, 0, 1)) # 맨 마지막은 몇 칸 왔는지 세기 위함
  while dq:
    y, x, d = dq.popleft()

    if y == N - 1 and x == M - 1:
      return d 
    
    nd = d + 1
    for k in range(4):
      ny = y + dy[k]
      nx = x + dx[k]
      if is_valid_coord(ny, nx) and board[ny][nx] == '1' and not chk[ny][nx]: # 보드에서 1인 곳만 가야하므로
        chk[ny][nx] = True
        dq.append((ny, nx, nd))

print(bfs())
