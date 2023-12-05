import sys
from math import ceil, log
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        segment_tree[node] = nums[start-1]
        return segment_tree[node]
    mid = (start+end) // 2
    segment_tree[node] = max(init(node*2, start, mid), init(node*2+1, mid+1, end))
    return segment_tree[node]

def find_max(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return segment_tree[node]
    mid = (start+end) // 2
    return max(find_max(node*2, start, mid, left, right), find_max(node*2+1, mid+1, end, left, right))

n , m = map(int, input().split())
nums = list(map(int, input().split()))
segment_tree = [0] * (pow(2, ceil(log(len(nums), 2) + 1)) - 1)

init(1, 1, n)

for i in range(n-(m*2-1)+1): # m*2-1 -> 시야범위
    print(find_max(1, 1, n, 1+i, i+(m*2-1)), end=' ')
