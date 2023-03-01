import re
f = open("receipt.txt", "rt")
m = re.sub("[,.! ]", ":", f.read())
print(m)