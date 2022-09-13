import json     
with open('list.json','r') as f:
    p=json.load(f)
print(p)

# list.json file inside outpu
# output={"A":1,"B":2,"C":3,"D":4}