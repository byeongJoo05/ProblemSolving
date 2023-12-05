n = int(input())
nList = list(map(int, input().split()))
m = int(input())
mList = list(map(int, input().split()))
nList.sort()

def binarysearch(target):
    start = 0
    end = len(nList)-1

    while start <= end:
        mid = (start+end) //2

        if nList[mid] == target:
            return mid
        elif nList[mid] > target:
            end = mid-1
        else:
            start = mid + 1

    return None


for i in mList:
    ans = binarysearch(i)
    if ans is None:
        print('0')
    else:
        print('1')