I = []
J = []

for i in range (1, 38, 3):
    I.append(i)

for j in range (60, -1, -5):
    J.append(j)

for a in range (len(I)):
    print("I=%d J=%d" % (I[a], J[a]))
