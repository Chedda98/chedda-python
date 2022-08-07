from itertools import combinations

heights = [int(input()) for _ in range(9)] # 입력값을 바로 초기화해버림
for i in combinations(heights, 7):
  if sum(i) == 100:
    for j in sorted(i):
      print(j)
      
    break # 합이 100인 케이스를 발견하면 탈출해야함
