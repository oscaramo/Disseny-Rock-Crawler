from sense_hat import SenseHat
from datetime import datetime
import csv

def dif(a,b):
    d=a-b
    return(d.seconds>=3)

with open('acc_data.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['t','x','y','z'])
    
    sense=SenseHat()
    
    l=[datetime.now(),0,0,0]
    lx=l
    ly=lx
    lz=lx
    t=datetime.now()
    t0=t
    while True:
        tn=datetime.now()
        fin=tn-t0
        acc=sense.get_accelerometer_raw()
        if abs(acc['x'])>lx[1]:
            lx=[datetime.now(),acc['x']-0.0423-0.019,acc['y']-0.0137,acc['z']-0.9654]
        elif abs(acc['y'])>ly[2]:
            ly=[datetime.now(),acc['x'],acc['y'],acc['z']]
        elif abs(acc['z'])>lz[3]:
            lz=[datetime.now(),acc['x'],acc['y'],acc['z']]
            
        elif dif(datetime.now(),t):
            w.writerow(lx)
            w.writerow(ly)
            w.writerow(lz)
            print(lx)
            lx,ly,lz=l,l,l
            t=datetime.now()
        elif fin.seconds>60*2:
            break
    
