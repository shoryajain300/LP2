
graph1 = {
    0:[1,2,3],
    1:[2,3],
    2:[3,4],
    3:[4],
    4:[5,6],
    5:[],
    6:[]
}

visited=[]
explore=[]
def bfs(graph1,start):
    visited.append(start)
    explore.append(start)

    while explore:
        front=explore[0]
        
        for i in graph1[front]:
            if i not in visited:
                visited.append(i)
                explore.append(i)

        explore.pop(0)

    for i in visited:
        print(i,end=" ")


def dfs(graph1,start):
    if start in visited:
        return
    
    visited.append(start)
    
    for neighbour in graph1[start]:
        dfs(graph1,neighbour)

bfs(graph1,0)

for i in visited:
    print(i)
