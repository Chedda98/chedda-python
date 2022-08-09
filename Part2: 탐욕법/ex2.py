N, L = map(int, input().split())
coord = [False] * 1001 # 좌표계 인덱스 1000번까지 false 처리
for i in map(int, input().split()):
  coord[i] = True # 구멍 있을 때마다 true 표시

ans = 0 # 필요한 테이프 개수
x = 0
while x < 1001:
  if coord[x]:
    ans += 1
    x += L
  else:
    x += 1

print(ans)
