e = ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n',
     'O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z']
n = int(input())
while n:
    ss = input().split()
    print(len(ss))
    d = {}
    save = ''
    for s in ss:
        for c in s:
            if d.get(c):
                d[c] += 1
            else:
                d[c] = 1
    l = len(d)
    L = 0
    for c in e:
        if d.get(c):
            if L < l:
                print(f"{c} : {d[c]}")
                L += 1
            else:
                print(f"{c} : {d[c]}", end="")
    n -= 1

