import json
a="""{"company":{"employee":{"name":"emma","payble":{"salary":7000,"bomes":800}}}}"""

n=json.loads(a)
print(n)
g=n.get("salary")
print(g)