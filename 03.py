n = int(input())
while n:
    Map = []
    L = int(input())
    for i in range(L):
        Map.append(input().split())
        for j in range(len(Map[i])):
            Map[i][j] = int(Map[i][j])

    # print(Map)
    n -= 1
