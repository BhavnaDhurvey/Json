# n=[{"meth":2,"scince":4},{"meth":3,"scince":8},{"meth":5,"scince":6}]
# p=[]
# s=input("enter the meth....")
# for x in n:
#     for k in x:
#         if k in s:
#             # m=n[1].get(s)
  
#             p.append(s)
          
# print(p)

n=[{"meth":2,"scince":4},{"meth":3,"scince":8},{"meth":5,"scince":6}]
z=[]
s=input("enter the meth....")
for x in n:
    for key,value in x.items():
        if key in s:
           z.append(value)
print(z)


# output=[2,3,5]