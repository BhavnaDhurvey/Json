import json
json_obj =  { "Name":"David", "Class":"I", "Age":6 }
python_obj=json.dumps(json_obj)
print(python_obj)
print(type(python_obj))

# output={"Name":"David","Class":"I","Age":6}
# <class 'str'>