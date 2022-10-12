n = int(input())
name = input()
women = {}
for i in range(1, n+1):
    women[i] = name[i-1]
while True:
    man = input().split()
    if man[0] == '0':
        break
    arr = []
    if man[0] == '1':
        for woman, english_name in women.items():
            if english_name == man[1] or english_name == man[2]:
                arr.append(woman)
    elif man[0] == '2':
        for i in range(int(man[1]), int(man[2])+1):
            arr.append(i)
    else:
        for i in range(int(man[1]), int(man[2])+1):
            arr.append(i)
        for woman, english_name in women.items():
            if english_name == man[3]:
                y = 1
                for k in arr:
                    if k == woman:
                        y = 0
                        break
                if y:
                    arr.append(woman)
    arr.sort()
    if len(arr) == 0:
        print()
    else:
        for i in range(len(arr)-1):
            print(arr[i], end=" ")
        print(arr[len(arr)-1])
