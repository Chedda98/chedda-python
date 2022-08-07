d = dict()
for _ in range(int(input())):
  book = input()
  if book in d: # d 안에 book이 있는지 중복체크
    d[book] += 1
  else:
    d[book] = 1

m = max(d.values())
celeb = []
for k, v in d.items():
  if v == m:
    celeb.append(k)

celeb.sort()
print(celeb[0])
