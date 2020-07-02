N = int(input())

if N>2 and N<1000:
    for i in range (1,11):
      x = N*i
      print("%d x %d = %d" % (i, N, x))
        