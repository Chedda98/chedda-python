T = int(input()) # 이후에 따로 T가 사용되지 않는다면 range(int(input())) 로 작성해도 됨

for _ in range(T):
  stk = []
  isVPS = True
  for ch in input():
    if ch == '(':
      stk.append(ch)
    else:
      if len(stk) > 0:
        stk.pop()
      else:
        isVPS = False
        break

  if len(stk) > 0:
    isVPS = False # 위에서 True로 선언해줬기 때문에 따로 True 반환하는 코드짜지 않아도 됨
  print('YES' if isVPS else 'NO')
