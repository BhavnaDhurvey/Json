import json


f=open("love.txt","r")
d=f.read()
print(d)
with open("you","w") as f:
    json.dump(d,f)