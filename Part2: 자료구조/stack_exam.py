s = []
s.append(123)
s.append(456)
s.append(789)
print("size:", len(s))
while len(s) > 0:
  print(s[-1])
  s.pop(-1) # pop()은 pop(-1)과 같은 의미
