import tkinter
from tkinter import *
import numpy as np
import math as mt
import random

def S(x1, x2, y1, y2, f1, f2):
    r1=mt.sqrt(y1**2+x1**2)
    r2=mt.sqrt(y2**2+x2**2)
    s=0
    if (mt.sin(abs(f2-f1)) >0):
        s=1/2*r1*r2*mt.sin(abs(f2-f1))
    else:
        s=1/2*r1*r2
        s=s+1/2*r1*r2*mt.sin(abs(f2-f1)-mt.pi*10/2)
    return s
def S2(x1, x2, y1, y2):
    r1=mt.sqrt(y1**2+x1**2)
    r2=mt.sqrt(y2**2+x2**2)
    r3=mt.sqrt((y1-y2)**2+(x1-x2)**2)
    p=1/2*(r1+r2+r3)
    s=mt.sqrt(p*(p-r1)*(p-r2)*(p-r3))
    return s

k=25
x=np.zeros((k, 20))
y=np.zeros((k, 20))
x_rec=np.zeros((k, 2))
y_rec=np.zeros((k, 2))
smesh_x=np.zeros((k))
smesh_y=np.zeros((k))
fi=np.zeros((k,20))
s=np.zeros((k))
kolvo_ver=np.zeros((k))
x0=60
y0=60
for i in range(k):
    x[i][0]=60
    y[i][0]=60
    f0=0
    j=1
    yg=0
    while(s[i]<3600):
        r = np.random.randint(25, 40)
        if j==1:
            f = np.random.randint(1, int(mt.pi*10/2))
            f0=f
            fi[i][j]=f
        else:
            if(yg < 48+f0):
                f = np.random.randint(1, int(mt.pi*10/4))
            else:
                if (int(mt.pi*10)-yg<7):
                    j=1
                    s[i]=0
                else:
                    f = np.random.randint(1, int(mt.pi*10)-yg)
            yg+=f
            fi[i][j]=yg
        
        x[i][j]=x0+r*mt.cos((f0+yg)/10)
        y[i][j]=y0+r*mt.sin((f0+yg)/10)
        
        if(j>1):
            s[i]+=S(x[i][j-1]-x0, x[i][j]-x0, y[i][j-1]-y0, y[i][j]-y0, fi[i][j-1], fi[i][j])
#             print('s: ', i, ':', j, ' ', s[i])
        if(s[i]<4200):
            #print(x[i][j])
            # print(y[i][j])
            j+=1
            
        else:
            s[i]=s[i]-S(x[i][j-1]-x0, x[i][j]-x0, y[i][j-1]-y0, y[i][j]-y0, fi[i][j-1], fi[i][j])
        
    kolvo_ver[i]=j+1
    
    x_rec[i][0]=x[i][0]
    x_rec[i][1]=x[i][0]
    y_rec[i][1]=y[i][0]
    y_rec[i][0]=y[i][0]
    
    for p in range(1,int(kolvo_ver[i]-1)):
        if(x[i][p]<x_rec[i][0]):
            x_rec[i][0]=x[i][p]-5
        if(x[i][p]>x_rec[i][1]):
            x_rec[i][1]=x[i][p]+5
        if(y[i][p]<y_rec[i][0]):
            y_rec[i][0]=y[i][p]-5
        if(y[i][p]>y_rec[i][1]):
            y_rec[i][1]=y[i][p]+5
             

# print('a',mt.acos(0))
for i in range(k):
    flag=False
    while(flag is False):
        d = np.random.randint(1, 400)
        h = np.random.randint(1, 400)
        r=0
        t=0
        for p in range (i):
            r=0
            if(x_rec[i][1]+d < x_rec[p][0]+smesh_x[p]):
                r=1
            if(x_rec[i][0]+d > x_rec[p][1]+smesh_x[p]):
                r=1
            if(y_rec[i][0]+h > y_rec[p][1]+smesh_y[p]):
                r=1
            if (y_rec[i][1]+h < y_rec[p][0]+smesh_y[p]):
                r=1
            if(r!=1):
                t=1
                p=i
                
        if (t==0):
            smesh_x[i]=d
            smesh_y[i]=h
#             print(d, h)
            flag=True
        
        

root = Tk()
canv = Canvas(root,width=500,height=500,bg="lightblue", cursor="pencil")
# for i in range(k):
#     c=rec()
#     d = np.random.randint(5, 420)
#     h = np.random.randint(1, 420)
Sum=0
for i in range(k):
    Sum+=s[i]
    if(i>0):
        print(s[i]/s[i-1])
    for j in range(int(kolvo_ver[i]-1)):
#         print('x', x[i][j], 'y', y[i][j])
        if (j<kolvo_ver[i]-2):
            canv.create_line(smesh_x[i]+x[i][j],y[i][j]+smesh_y[i],smesh_x[i]+x[i][j+1], smesh_y[i]+y[i][j+1], width = 3, fill="blue")
        else:
            canv.create_line(smesh_x[i]+x[i][j],smesh_y[i]+y[i][j],smesh_x[i]+x[i][0], smesh_y[i]+y[i][0], width = 3, fill="blue")
print(Sum/(500*500))
canv.pack()
root.mainloop()