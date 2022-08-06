from queue import Queue
# 큐 모듈은 멀티쓰레드로 구성할 수 있도록 thread-safe 환경으로 갖춰져 있어 느림
# 알고리즘 문제에선 멀티쓰레드 구성은 따로 다루지 않기 때문에 비효율적

q = Queue()
q.put(123)
q.put(456)
q.put(789)
while q:
  print(q.get())
