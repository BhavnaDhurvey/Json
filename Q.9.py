import json
a={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}

s=input("enter the number.....")
r=int(input("enter the number....."))
p={}
l={}
for i in a:
    if a[i][s]==a[i][s]:
        d=a[i][s]
        e=int(d)
        g=e-r
for key in a:
    for value in a[key]:
        p[value]=a[key][value]
        if value==s:
            p[value]=g   
            l[i]=p
print(l)

with open("soso.json","w")as f:
    json.dump(l,f)


    
# output=
# input=chaco           
# int=10

# soso.json file in side output
# show shopping_list:- 

# {
#     "shopping_list":{ 
#         "chaco":"5",
#         "Biscuits":"50",
#         "Diary_milk":"30",
#         "ice_cream":"20",
#          } 
# }


