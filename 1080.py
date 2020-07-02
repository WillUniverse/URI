i=0
M = 0
p=0
v = {}
while i < 5:
    x = int(input())
    if x > M:
        M = x
        v[x] = p
    i += 1
print(M)
print(p)