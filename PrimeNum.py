# a=int(input("Enter the number"))
# for a in range(2,a+1):
#     count=0
#     for i in range(1,a+1):
#         if a%i==0:
#             count+=1
#     if count==2:
#         print(a,end=" ")

num=int(input("Enter the number"))
for i in range(0,num+1):
    if (i>1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i)
