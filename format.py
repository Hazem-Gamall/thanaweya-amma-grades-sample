
lineLs = []
s = ''

with open('natega.txt','r') as f, open('test.txt','w') as w:
    s = f.readlines()
    for i in s:
        if i != '\n':
            lineLs.append(i)
    w.writelines(lineLs)
    # s=s.split('\n')
    # print (s)

