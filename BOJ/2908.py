a, b = map(list,input().split())

a.reverse()
a_rev = ''.join(a)
b.reverse()
b_rev = ''.join(b)

if int(a_rev) > int(b_rev):
    print(a_rev)
else:
    print(b_rev)