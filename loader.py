ip=[]
op=[]
mot=["A","ST","L"]
file=open("input.txt","r")
out=open("loader.txt","w+")
for i in file:
    ip.append(i.split())
print(ip)
sa=int(ip[2][0][:-1])
print(sa)
temp=""
for i in ip[3:]:
    if(i[1] in mot):
        out.write(str(sa+int(i[0]))+"  "+str(i[1])+"  "+ str(sa+int(i[2]))+"\n")
    else:
        out.write(str(sa+int(i[0]))+"     "+str(i[1]+"\n")) 