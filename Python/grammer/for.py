result = 0

# i는 1부터 9까지의 모든 값을 순회
for i in range(1, 10):
  result += i

print(result)

scores = [90,85, 77, 65, 97]

for i in range(5):
  if scores[i] >= 80:
    print(i+1,"번 학생은 합격입니다.")


scores = [90,85, 77, 65, 97]
cheating_list = {2,4}

for i in range(5):
  if i+1 in cheating_list:
    continue
  if scores[i] >= 80:
    print(i+1, "번 학생은 합격입니다.")

for i in range(2,10):
  for j in range(1,10):
    print(i, "X", j, "=", i*j)
    print()