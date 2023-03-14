class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {} # 딕셔너리로 올리기
        max_length = start = 0 # start와 문자열 길이를 0으로 초기화
        for index, char in enumerate(s):
            if char in used and start <= used[char]: # 만약 문자가 사용되고 있으며 시작이 사용된 문자보다 작거나 같다면
                start = used[char] + 1 # 문자 점프하기
            else: # 만일 문자가 사용되지 않고 있거나 사용된 문자보다 크다면
                max_length = max(max_length, index - start + 1) # 최대 문자열 길이는 최대 문자열 길이와 현재 인덱스에서 스타트를 뺀 길이 +1
            used[char] = index # 문자를 사용했다고 딕셔너리에 위치시켜놓기

        return max_length
