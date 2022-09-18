#
# n=1
# while (n<5):
#     a= '*'
#     print(a*n)
#     n=n+1


n=int(input("enter number of rows"))
p=bool(int(input('select 0 or 1')))

if p==True:
    x = 1
    while (x<=n):
        print("*"*x)
        x=x+1

else :
    x = n
    while (x>=1):

        print("*" * x)
        x = x - 1
