from collections import deque
# 덱은 앞뒤로 모두 삽입 가능
# 멀티쓰레드 환경이 아니기 때문에 빠름
# Double-Ended QUEue 라는 의미

dq = deque()
dq.append(123) # 그냥 append는 뒤로 삽입
dq.appendleft(456)
dq.appendleft(789) # 왼쪽에 삽입
print(dq)

print(dq.pop())
print(dq.popleft())
