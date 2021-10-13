#szorzás
line = ""
i = 1
while i <= 20:
    result = i * 7
    if result % 3 == 0:
        line += (str(result) + " * ")
    else:
        line += (str(result) + " ")
    i = i +1
print (line)

#karifa
csillag = "*"
i = 1
while i <= 7:
    print(csillag)
    csillag = csillag + "*"
    i = i +1