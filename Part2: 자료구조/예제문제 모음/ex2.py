from collections import deque

N = int(input())
dq = deque()
for i in range(1, N + 1):
  dq.append(i)
# 위 코드는 아래와 같이 한줄로도 짤 수 있음
# dq = deque(range(1, N + 1))
while len(dq) > 1:
  dq.popleft()
  dq.append(dq.popleft()) # 최상단 값을 빼서 맨 뒤로 append() 시킴

print(dq.pop())
