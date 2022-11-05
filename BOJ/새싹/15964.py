def function(a,b):
    ans = (a + b) * (a - b)
    return ans

a, b = map(int,input().split())
print(function(a,b))