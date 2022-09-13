# def fun(n,div):
#     sum=0
#     while n<=div:
#         p=n%4
#         sum=sum+p
#         n=n+1
#     return sum

# n=int(input("enter the number"))
# div=int(input("enter the number"))
# s=fun(n,div)
# print(s)


n = int(input())
div = int(input())

def FindSumOfRemainders(n, div):
  #write your code here
   
    sum=0
    while n<=div:
        p=n%4
        sum=sum+p
        n=n+1
    return sum

# n=int(input("enter the number"))
# div=int(input("enter the number"))

result = FindSumOfRemainders(n, div)
print(result)