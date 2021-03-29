# 1이 될 때까지
# 1.숫자를 1 뺀다  // 2. 나누어 떨어질 때, 나눈다. -> 횟수 합산
# 먼저 나눌수 있을 때 나누고, 나눌수 없으면 숫자를 빼는 규칙을 적용

n, k = map(int, input().split())
result = 0

while n >= k:
  while n%k != 0:
    n -= 1
    result += 1
  n //= k
  result += 1

while n > 1:
  n -= 1
  result += 1

print(result)  

