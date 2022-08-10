def addV1(a, b):
  return a+b

def addV2(a, b):
  print('함수의 결과:', a+b)

def addV3(a, b):
  print('함수의 결과:', a+b)
  
print(addV1(3,7))
addV2(3,7)
addV3(b=3,a=7)

a = 0

def func():
  global a
  a+=1

for i in range(10):
  func()

print(a)

# 일반적인 add() 메서드 사용
print(addV1(3,7))

# 람다 표현식으로 구현한 add() 메서드
print((lambda a, b: a+b)(3,7))