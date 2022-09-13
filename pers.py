
# import json

# person_dict = {"name": "Bob",
# "languages": ["English", "French"],
# "married": True,
# "age": 32
# }

# with open('person.txt', 'w') as json_file:
#   json.dump(person_dict, json_file)


# import json      
# pers={"name":"Bhavna","age":18,"from":"MP"}
# with open ('bhavna.txt','w') as json_file :
#     json.dump(pers,json_file)

import json      
a={"A":"Archan","B":"Bhavna"}
with open ("bhavna.txt","w") as json_file:
    json.dump(a,json_file)