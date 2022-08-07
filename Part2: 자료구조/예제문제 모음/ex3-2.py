# 해당 문제는 백준 11286. 절댓값 힙 문제입니다
# 우선순위 큐를 두 개 만드는 방법으로 구현
import heapq as hq
import sys

input = sys.stdin.readline
min_heap = [] # 양수
max_heap = [] # 음수
for _ in range(int(input())):
  x = int(input())
  if x:
    if x > 0:
      hq.heappush(min_heap, x)
    else:
      hq.heappush(max_heap, -x) # 파이썬은 최소값이 루트에 위치하기 때문에 부호를 바꾸는 처리가 필요함
  else:
    if min_heap:
      if max_heap:
        if min_heap[0] < abs(-max_heap[0]): # 반환할 때도 부호를 바꿔줘야 함
          print(hq.heappop(min_heap[0]))
        else:
          print(-hq.heappop(max_heap[0]))
      else:
        print(hq.heappop(min_heap[0]))
    else:
      if max_heap:
        print(-hq.heappop(max_heap[0]))
      else:
        print(0)
