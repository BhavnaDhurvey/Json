import json


dict={"a":1,"b":2,"c":3}
# print(dict)
# print(type(dict))


json_s=json.dumps(dict)
# print(json_s)
# print(type(json_s))

some=json.loads(json_s)
# print(some)
# print(type(some))

list=["hello","bye"]
# print(list)
# print(type(list))

another=json.dumps(list)
# print(another)
# print(type(another))

json='{"a":1,"b":2,"c":3}'
print(json)
print(type(json))

json={'a':1,'b':2,'c':3}
js_obj=json.parse(json)
print(js_obj)