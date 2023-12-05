n, m = map(int, input().split())
dict = {}

for _ in range(n):
    url, password = input().split()
    dict[url] = password

for _ in range(m):
    url = input()
    print(dict.get(url))