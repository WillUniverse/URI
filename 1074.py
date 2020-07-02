N = int(input())

v = []
if N<10000:
    for i in range (0, N):
        X = int(input())
        v.append(X)
    for n in range (0, len(v)):
        
        if v[n]%2==0 and v[n]>0:
            print("EVEN POSITIVE")
        
        elif v[n]%2==0 and v[n]<0:
            print("EVEN NEGATIVE")
        
        elif v[n]%2!=0 and v[n]>0:
            print("ODD POSITIVE")
        
        elif v[n]%2!=0 and v[n]<0:
            print("ODD NEGATIVE")
       
        else:
            print('NULL')
      