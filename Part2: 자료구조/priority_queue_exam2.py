import heapq as hq
# 매번 heapq 쓰기 귀찮다면 as 이용

pq = []
hq.heappush(pq, 6)
hq.heappush(pq, 12)
hq.heappush(pq, 0)
hq.heappush(pq, -5) # 최상단 노드가 될 것임
hq.heappush(pq, 8)
print(pq)
while pq:
  print(pq[0])
  hq.heappop(pq)
