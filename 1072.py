N = int(input())
v = []
im = 0
pa = 0 
for i in range (0, N):
    X = int(input())
    v.append(X)
    if v[i] >= 10 and v[i] <= 20:
        pa += 1
    else:
        im += 1

print("%d in" % pa)
print("%d out" % im)