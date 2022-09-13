import  json      
b={"A":5,"B":10}
with open("hello.json","w")as json_file:
    json.dump(b,json_file)
