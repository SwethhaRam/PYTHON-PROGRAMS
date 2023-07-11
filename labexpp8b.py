d1="sample.txt"
d2="sample2.txt"
start=open(d1,'a')
end=open(d2,'r')
content=end.read()
start.write(content)
start=open(d1,'r')
print(start.read())
