acc=open('acc_data.csv')
x,y,z=[],[],[]
count=0
vx,vy,vz=0,0,0

for i in acc:
    i=i.strip()
    l=i.split(',')
    if l[1]!='x':
        x,y,z=x+[float(l[1])],y+[float(l[2])],z+[float(l[3])]

for a in x:
       vx=vx+a
       count=count+1    
for b in y:
       vy=vy+b
for a in z:
       vz=vz+a
       
print(vx/count,vy/count,vz/count)
