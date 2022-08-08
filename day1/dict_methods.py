from cmath import inf


info={'name':'Srikar','age':20,'Gender':'male','country':'India'}
print(info.keys())
print(info.values())
if 'name' in info.keys():
    print(info['name'])
else:
    print("Damnn")
print(info['name'])
print(info.items())
print(info.clear())