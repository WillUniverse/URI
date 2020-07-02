N = int(input())

v=[]
for i in range (0, N):
    a, b, c = input().split(" ")
    a = float(a)
    b = float(b)
    c = float(c)
    a = a*2
    b = b*3
    c = c*5
    s = a + b + c
    r = s/10
    v.append(r)

for i in range(len(v)):
    print("%.1f" %v[i])