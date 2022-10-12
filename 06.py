poly1 = {9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0}
poly2 = {9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0}
poly3 = {9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0}
poly4 = {21: 0, 20: 0, 19: 0, 18: 0, 17: 0, 16: 0, 15: 0, 14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0}
s = 1
while True:
    a = input().split()
    if len(a) == 1:
        s += 1
        if s == 3:
            break
        else:
            continue
    n = int(a[0])
    c = int(a[1])
    print(f"poly{s} =", end="")
    if s == 1:
        first = 0
        poly1[c] += n
        for one, two in poly1.items():
            if two == 0:
                continue
            if first:
                print(" +", end="")
            else:
                print(" ", end="")
            first = 1
            if one != 0:
                print(f"{two}x^{one}", end="")
            else:
                print(f"{two}", end="")
    if s == 2:
        first = 0
        poly2[c] += n
        for one, two in poly2.items():
            if two == 0:
                continue
            if first:
                print(" +", end="")
            else:
                print(" ", end="")
            first = 1
            if one != 0:
                print(f"{two}x^{one}", end="")
            else:
                print(f"{two}", end="")
    print()
print(f"poly{1} =", end="")
first = 0
for one, two in poly1.items():
    if two == 0:
        continue
    if first:
        print(" +", end="")
    else:
        print(" ", end="")
    first = 1
    if one != 0:
        print(f"{two}x^{one}", end="")
    else:
        print(f"{two}", end="")
first = 0
print(f"\npoly{2} =", end="")
for one, two in poly2.items():
    if two == 0:
        continue
    if first:
        print(" +", end="")
    else:
        print(" ", end="")
    first = 1
    if one != 0:
        print(f"{two}x^{one}", end="")
    else:
        print(f"{two}", end="")



print("\npoly3(add) =", end="")
for i in range(10):
    poly3[i] = poly2[i] + poly1[i]
first = 0
for one, two in poly3.items():
    if two == 0:
        continue
    if first:
        print(" +", end="")
    else:
        print(" ", end="")
    first = 1
    if one != 0:
        print(f"{two}x^{one}", end="")
    else:
        print(f"{two}", end="")
print()
print("poly4(mult) =", end="")
for p1n, p1c in poly1.items():
    for p2n, p2c in poly2.items():
        poly4[p1n+p2n] += p1c * p2c
        # print(poly4)
first = 0
for one, two in poly4.items():
    if two == 0:
        continue
    if first:
        print(" +", end="")
    else:
        print(" ", end="")
    first = 1
    if one != 0:
        print(f"{two}x^{one}", end="")
    else:
        print(f"{two}", end="")
print()
