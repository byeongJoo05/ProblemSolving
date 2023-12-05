s = input()

def palindrome(s):
    for i in range(len(s)):
        if s[i] != s[-1-i]:
            return False
        return True

print(str(s))
if palindrome(s):
    print("입력하신 단어는 회문(Palindrome)입니다.")
else:
    print("입력하신 단어는 회문(Palindrome)이 아닙니다.")

