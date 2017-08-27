
str_in=input()
temp=[int(n) for n in str_in.split()]
nums=temp[1:]

A=[0,0,0,0,0]
flag=1
A_num=[0,0,0,0,0]

for num in nums:
    mod=num%5
    if mod==0:
        if num%10==0:
            A[0]+=num
            A_num[0]+=1
    elif mod==1:
        A_num[1] += 1
        if flag:
            A[1]+=num
        else:
            A[1]-=num
        flag=1-flag
    elif mod==2:
        A_num[2] += 1
        A[2]+=1
    elif mod==3:
        A_num[3] += 1
        A[3]+=num
    elif mod==4:
        if num>A[4]:
            A_num[4] += 1
            A[4]=num

# if A_num[3]>1:
#     A[3]=round(A[3]/A_num[3],1)
# else:
#     A_num[3]=0
# if A_num[1]==1:
#     A_num[1]=0

for i in range(5):
    if A_num[i]==0:
        print('N',end=' ')
    else:
        if i==4:
            print(A[i])
        else:
            print(A[i],end=' ')

