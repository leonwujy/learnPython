temp=input().split()
M=int(temp[0])
N=int(temp[1])
index=0
result=[]

i=2
while(1):
    Flag=1
    for j in range(2,int(i**0.5) + 1):
        if i % j == 0:
            Flag = 0
            break
    if Flag == 1:
        index += 1
        if index > N:
            break
        if index >= M:
            result.append(i)
    i+=1

for i in range(0,len(result)):
    if i==0:
        print(result[0],end='')

    elif i%10==0:
        print('')
        print(result[i],end='')
    else:
        print(' '+ str(result[i]),end='')

# print("\n".join([i + 10 > len(primes) and " ".join(primes[i:]) or " ".join(primes[i:i+10]) for i in range(len(primes)) if i % 10 == 0]))
