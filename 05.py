n = int(input())
while n:
    Max = 0
    carry = 0
    carr = input().split()
    iarr = []
    for c in carr:
        iarr.append(int(c))
    for i in range(1, len(iarr)):
        if iarr[i] > iarr[i-1]:
            carry += 1
        elif iarr[i] <= iarr[i-1]:
            carry = 0
        Max = max(Max, carry)
    print(Max)
    n -= 1
