a=['name','Designation','age','salary']
b=['neelam','programer','24','2400']
c=['komal','trainer','24','20000']
d=['anuradha','HR','25','40000']
e=['Abhishek','manager','29','63000']
p={}
t={}
u={}
v={}
k={}
l="emp1"
n="emp2"
r="emp3"
g="emp4"
i=0
while i < len(a):
    s=a[i]
    p[s]=b[i]
    t[s]=c[i]
    u[s]=d[i]
    v[s]=e[i]
    k[l]=p
    k[n]=t
    k[r]=u
    k[g]=v
    i=i+1

print(k)



# Output:-

# { 
#      "emp1":{ "name":"nilam",
#        "Designation":"programmer",
#        "Age":"34",
#        "salary":"24000",
#          }

#     "emp2":
#       { "name":"komal",
#         "Designation":"Trainee",
#         "Age":"24",
#         "salary":"20000" ,
#         }

 
#     "emp3":
#        { "name":"anuradha",
#          "Designation":"HR",
#          "Age":"25",
#          "salary":"40000",
#          }


#     "emp4":
#        { "name":"Abhishek",
#          "Designation":"Manager",
#          "Age":"29",
#        }
# }
