s = input()
a = ""
set = set()

for i in range(len(s)):
    for j in range(i, len(s)):
        set.add(s[i:j])

print(len(set))