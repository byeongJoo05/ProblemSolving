n = int(input())
storeData = list(map(int,input().split()))

m = int(input())
memData = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2

        if array[mid] == target:
            return mid

        elif array[mid] > target:
            end = mid-1
        else :
            start = mid +1
    return None


for i in memData:
    result = binary_search(storeData, i, 0, n-1)
    if result != None:
        print('yes', end= ' ')
    else:
        print('no', end=' ')