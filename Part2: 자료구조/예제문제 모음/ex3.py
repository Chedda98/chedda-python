# 해당 문제는 백준 11286. 절댓값 힙 문제입니다
# 튜플로 묶어서 반환하는 방법으로 구현
import heapq as hq
import sys

input = sys.stdin.readline # input으로 대체해서 쓸 때는 readline을 함수처리하면 안됨
pq = []
for _ in range(int(input())):
  x = int(input())
  if x:
    hq.heappush(pq, (abs(x), x))
  else:
    print(hq.heappop(pq)[1] if pq else 0) # 우리가 튜플값 중 궁금한 것은 원값이기 때문에 인덱스 1번째
    """
    if pq:
      print(hq.heappop(pq)[1])
    else:
      print(0)
    """
