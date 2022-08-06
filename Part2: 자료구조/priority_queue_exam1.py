from queue import PriorityQueue
# 우선순위 큐 모듈 역시 멀티쓰레드로 구성할 수 있도록 thread-safe 환경으로 갖춰져 있어 느림

pq = PriorityQueue()
pq.put(6)
pq.put(10)
pq.put(-5)
pq.put(0)
pq.put(8)
while not pq.empty():
  print(pq.get()) # pop
