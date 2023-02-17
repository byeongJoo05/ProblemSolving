# def fibonacci(n):
#     if n == 0:
#         print(0)
#         return
#     elif n == 1:
#         print(1)
#         return
#     else:
#         fibonacci(n-1)
#         fibonacci(n-2)
#
# print(fibonacci(5))

T = int(input())
d0 = [0 for _ in range(45)]
d1 = [0 for _ in range(45)]

d0[0], d0[1] = 1, 0
d1[0], d1[1] = 0, 1

for i in range(2,41):
    d0[i] = d0[i-1] + d0[i-2]
    d1[i] = d1[i-1] + d1[i-2]

for i in range(T):
    n = int(input())
    print(d0[n], d1[n])