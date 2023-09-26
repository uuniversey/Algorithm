li = input().upper()

c_li = list(set(li))

tool = []
for i in c_li:
    tool.append(li.count(i))

if tool.count(max(tool)) > 1:
    print('?')
else:
    print(c_li[tool.index(max(tool))])