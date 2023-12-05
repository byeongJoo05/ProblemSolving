# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]

print(array)

# 1부터 9까지의 수의 제곱 값을 포함하는 리스트
array = [i * i for i in range(1,10)]

print (array)

# N X M 크기의 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)] #언더바는 반복되는 변수의 값을 무시할 때 사용
print(array)

# N X M 크기의 2차원 리스트 초기화(잘못된 방법)
# 2차원 리스트를 초기화할 때는 반드시 리스트 컴프리헨션을 이용해야함
n = 3
m = 4
array = [[0]*m] * n
print (array)

array[1][1] =5
print(array)