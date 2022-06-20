n = 10
t1 = 0
t2 = 1
print('Sequência de Fibonacci')
fibo = [t1, t2]
print('-' * 30)
cont = 3
while cont <= n:
    t3 = t1 + t2
    fibo.append(t3)
    t1 = t2
    t2 = t3
    cont += 1
print(fibo)
print('-' * 30)
num = int(input('Informe um núremo: '))

if num in fibo:
    print('Esse número pertence a sequência de Fibonacci')
else:
    print('Esse número não pertence a sequência de Fibonacci')



