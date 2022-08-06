s = set()
s.add(10)
s.add(10)
s.add(20)
s.add(50)
s.add(50)
s.add(30)
print("size:", len(s))
for i in s:
  print(i)

# set에선 pop()할 때 어떤 값이 빠질지 몰라서 잘 안씀
# 특정값 빼고 싶으면 remove() 사용
