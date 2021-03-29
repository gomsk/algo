# 상하좌우
# 입력 : 1.맵크기, 2.계획
# 출력 : 계획에 따라 이동한 현재 위치 (이동 불가능한 계획은 포함되지 않음)

n = int(input())
x,y = 1,1
plans = input().split()

#L, R, U, D
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]

  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue

  x,y = nx, ny  

print(x,y)
