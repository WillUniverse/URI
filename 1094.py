N = int(input())
r = 0
s = 0
c = 0

for i in range (1, N+1):
    x = input().split()
    a , b = x
    if b == 'R':
        r += int(a)
    elif b == 'S':
        s += int(a)
    elif b == 'C':
        c += int(a)
        
tot = r + s + c 
pr = (100*r)/tot
ps = (100*s)/tot
pc = (100*c)/tot

print('Total: {} cobaias'.format(tot))
print('Total de coelhos: {}'.format(c))
print('Total de ratos: {}'.format(r))
print('Total de sapos: {}'.format(s))
print('Percentual de coelhos: {:.2f} %'.format(pc))
print('Percentual de ratos: {:.2f} %'.format(pr))
print('Percentual de sapos: {:.2f} %'.format(ps))