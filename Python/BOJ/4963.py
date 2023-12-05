def dfs(x, y): # 높이, 너비 순
    if x<= -1 or y >=w or y <=-1 or x>=h:
        return False

    if graph[x][y]==1:
        graph[x][y] = 0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        dfs(x-1,y-1)
        dfs(x+1,y-1)
        dfs(x-1,y+1)
        dfs(x+1,y+1)
        return True
    return False

while True:
    w, h = map(int,input().split())

    if w ==0 & h ==0:
        break

    graph=[]
    for i in range(h):
        graph.append(list(map(int,input().split())))

    result = 0
    for i in range(h):
        for j in range(w):
            if dfs(i,j) == True:
                 result +=1
    print(result)