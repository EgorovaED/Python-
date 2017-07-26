import tkinter
from tkinter import *
import numpy as np
import math as mt
import random
import timeit
from time import clock

class fig:
    def __init__(self, x, y, N, S, Xrec, Yrec):
        self.x = x
        self.y = y
        self.N = N
        self.S = S
        self.Xrec = Xrec
        self.Yrec = Yrec
class rec:
#     x
#     y
#     flag
#     center
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.centerX = x + r/2*np.sqrt(2) - r
        self.centerY = y + r/2*np.sqrt(2) - r
        self.flag = True
        self.G = 0
        self.H = 0
        self.rod = 0
    def close(self):
        self.flag = False        


def close_line(i, j, k, Fig, rasb):
    ch_x = Fig[i].x[j]//rasb
    ch_y = Fig[i].y[j]//rasb
    per_x = ch_x*rasb + rasb
    per_y = ch_y*rasb + rasb
    if (Fig[i].x[k] > Fig[i].x[j]):
        while (Fig[i].x[k] > per_x):
            y = (per_x - Fig[i].x[j])*(Fig[i].y[k] - Fig[i].y[j])/(Fig[i].x[k] - Fig[i].x[j]) + Fig[i].y[j]
            y = y//rasb
            x = per_x//rasb
#             print( '1 ', i, j,  int((abs(y))*100 + (x)))
            if (x*rasb>Fig[i].Xrec[0])and(x*rasb<Fig[i].Xrec[1])and(y*rasb>Fig[i].Yrec[0]-5)and(y*rasb<Fig[i].Yrec[1]):
    
                c[int((y)*100 + (x))].close()
            if ((x+1)*rasb>Fig[i].Xrec[0])and((x+1)*rasb<Fig[i].Xrec[1])and(y*rasb>Fig[i].Yrec[0])and(y*rasb<Fig[i].Yrec[1]):
                c[int((y)*100 + (x)+1)].close()
            per_x += rasb
    if (Fig[i].x[k] < Fig[i].x[j]):
        while (Fig[i].x[k] < per_x):
            y = (per_x - Fig[i].x[j])*(Fig[i].y[k] - Fig[i].y[j])/(Fig[i].x[k] - Fig[i].x[j]) + Fig[i].y[j]
            y = y//rasb
            x = per_x//rasb
#             print( '2 ', i, j,  int((abs(y))*100 + (x)))
            
            if (x*rasb>Fig[i].Xrec[0])and(x*rasb<Fig[i].Xrec[1])and(y*rasb>Fig[i].Yrec[0])and(y*rasb<Fig[i].Yrec[1]):
                c[int((y)*100 + (x))].close()
            if ((x-1)*rasb>Fig[i].Xrec[0])and((x-1)*rasb<Fig[i].Xrec[1])and(y*rasb>Fig[i].Yrec[0])and(y*rasb<Fig[i].Yrec[1]):
                c[int((y)*100 + (x)-1)].close()
            per_x -= rasb
    if (Fig[i].y[k] > Fig[i].y[j]):
        while (Fig[i].y[k] > per_y):
            x = (per_y - Fig[i].y[j])*(Fig[i].x[k] - Fig[i].x[j])/(Fig[i].y[k] - Fig[i].y[j]) + Fig[i].x[j]
            x = x//rasb
            y = per_y//rasb
#             print( '3 ', i, j,  int((abs(y))*100 + (x)))
            if (x*rasb>Fig[i].Xrec[0]-5)and(x*rasb<Fig[i].Xrec[1])and(y*rasb>Fig[i].Yrec[0])and(y*rasb<Fig[i].Yrec[1]):
                c[int(((y))*100 + (x))].close()
            if (x*rasb>Fig[i].Xrec[0])and(x*rasb<Fig[i].Xrec[1])and((y+1)*rasb>Fig[i].Yrec[0])and((y+1)*rasb<Fig[i].Yrec[1]):
                c[int((abs(y+1))*100 + (x))].close()
            per_y += rasb
    if (Fig[i].y[k] < Fig[i].y[j]):
        while (Fig[i].y[k] < per_y):
            x = (per_y - Fig[i].y[j])*(Fig[i].x[k] - Fig[i].x[j])/(Fig[i].y[k] - Fig[i].y[j]) + Fig[i].x[j]
            x = x//rasb
            y = per_y//rasb
#             print( '4 ', i, j,  int((abs(y))*100 + (x)))
            if (x*rasb>Fig[i].Xrec[0]-5)and(x*rasb<Fig[i].Xrec[1])and(y*rasb>Fig[i].Yrec[0])and(y*rasb<Fig[i].Yrec[1]):
                c[int(((y))*100 + (x))].close()
            if (x*rasb>Fig[i].Xrec[0])and(x*rasb<Fig[i].Xrec[1])and((y-1)*rasb>Fig[i].Yrec[0])and((y-1)*rasb<Fig[i].Yrec[1]):
                c[int((abs(y-1))*100 + (x))].close()
            per_y -= rasb




#     N=0
#     x=np.zeros(30)
#     y=np.zeros(30)
def square(x1, x2, y1, y2, f1, f2):
    r1=mt.sqrt(y1**2+x1**2)
    r2=mt.sqrt(y2**2+x2**2)
    s=0
    if (mt.sin(abs(f2-f1)) >0):
        s=1/2*r1*r2*mt.sin(abs(f2-f1))
    else:
        s=1/2*r1*r2
        s=s+1/2*r1*r2*mt.sin(abs(f2-f1)-mt.pi*10/2)
    return s
def generate():
    Fig.clear()
    c.clear()
    for i in range(k):
        s = 0
        fi = np.zeros((20))
        kolvo_ver = 0
        x=np.zeros((20))
        y=np.zeros((20))
        x_rec=np.zeros((2))
        y_rec=np.zeros((2))
        smesh_x = 0
        smesh_y = 0 
        x[0]=60
        y[0]=60
        f0=0
        j=1
        yg=0
        while(s<3600):
            r = np.random.randint(25, 40)
            if j==1:
                f = np.random.randint(1, int(mt.pi*10/2))
                f0=f
                fi[j]=f
            else:
                if(yg < 48+f0):
                    f = np.random.randint(1, int(mt.pi*10/4))
                else:
                    if (int(mt.pi*10)-yg<7):
                        j=1
                        s=0
                    else:
                        f = np.random.randint(1, int(mt.pi*10)-yg)
                yg+=f
                fi[j]=yg

            x[j]=x0+r*mt.cos((f0+yg)/10)
            y[j]=y0+r*mt.sin((f0+yg)/10)

            if(j>1):
                s += square(x[j-1]-x0, x[j]-x0, y[j-1]-y0, y[j]-y0, fi[j-1], fi[j])
    #             print('s: ', i, ':', j, ' ', s[i])
            if(s<4200):
                #print(x[i][j])
                # print(y[i][j])
                j+=1

            else:
                s=s-square(x[j-1]-x0, x[j]-x0, y[j-1]-y0, y[j]-y0, fi[j-1], fi[j])

        kolvo_ver=j+1

        x_rec[0]=x[0]
        x_rec[1]=x[0]
        y_rec[1]=y[0]
        y_rec[0]=y[0]

        for p in range(1,int(kolvo_ver-1)):
            if(x[p]<x_rec[0]):
                x_rec[0]=x[p]-10
            if(x[p]>x_rec[1]):
                x_rec[1]=x[p]+10
            if(y[p]<y_rec[0]):
                y_rec[0]=y[p]-10
            if(y[p]>y_rec[1]):
                y_rec[1]=y[p]+10
        Fig.append(fig(x, y, kolvo_ver, s, x_rec, y_rec))


    # print('a',mt.acos(0))
    for i in range(k):
        flag=False
        while(flag is False):
            d = np.random.randint(1, 398)
            h = np.random.randint(1, 395)
            r=0
            t=0
            for p in range (i):
                r=0
                if(Fig[i].Xrec[1]+d < Fig[p].Xrec[0]):
                    r=1
                if(Fig[i].Xrec[0]+d > Fig[p].Xrec[1]):
                    r=1
                if(Fig[i].Yrec[0]+h > Fig[p].Yrec[1]):
                    r=1
                if (Fig[i].Yrec[1]+h < Fig[p].Yrec[0]):
                    r=1
                if(r!=1):
                    t=1
                    p=i

            if (t==0):
                Fig[i].x=Fig[i].x + d
                Fig[i].y=Fig[i].y + h
                #print(Fig[i].x, Fig[i].y)
                Fig[i].Xrec[0] = Fig[i].Xrec[0] + d
                Fig[i].Xrec[1] = Fig[i].Xrec[1] + d
                Fig[i].Yrec[0] = Fig[i].Yrec[0] + h
                Fig[i].Yrec[1] = Fig[i].Yrec[1] + h
    #              print(d, h)
                flag=True
        num = 0
    for i in range ((int)(500/rasb)):
        for j in range ((int)(500/rasb)):
            c.append(rec(j*rasb+rasb, i*rasb+rasb, rasb))
    #         print(num, c[num].centerX,c[num].centerY )
            num += 1
    for i in range (k):
        for j in range (Fig[i].N - 1):
            ch_x = Fig[i].x[j]//rasb
    #         print(Fig[i].x[j], ch_x)
            ch_y = Fig[i].y[j]//rasb
    #         print(int((ch_y)*100 + (ch_x)))
            c[int((ch_y)*100 + (ch_x))].close()

    for i in range (k):
        for j in range (Fig[i].N - 1):
    #         print(j, Fig[i].N - 1)
            if j<(Fig[i].N - 2):
                close_line(i, j, j+1, Fig, rasb)
            else:
                close_line(i, j, 0, Fig, rasb)
    #             print(Fig[i].N - 1, j,  'vf')
            
        
        
   
def cost_mar(x1, y1, x2, y2):
    s = (abs(x2-x1)/rasb + abs(y2-y1)/rasb)*35
    #s = (mt.sqrt(((x2-x1)/rasb)**2 + ((y2-y1)/rasb)**2))*35
    
#     print('H: ', s)
    return s

def prinadl(i):
    flag = False
    for j in range (len(open_list)):
        if i == open_list[j]:
            flag = True
    for j in range (len(close_list)):
        if i == close_list[j]:
#             print(i, 'in close_list')
            flag = True
    if c[i].flag == False:
        flag = True
    return flag
def prinadl_open(i):
    flag = False
    for j in range (len(open_list)):
        if i == j:
            flag = True
    return flag

def addOpen(i, rod_i, x2, y2):
    if (prinadl(i) == False):
        open_list.append(i)
        if (abs(rod_i - i) == 101)or(abs(rod_i-i) == 99):
            c[i].G= c[rod_i].G + 14
        if (abs(rod_i - i) == 1)or(abs(rod_i-i) == 100):
            c[i].G= c[rod_i].G + 10
        y1 = i//100
        x1 = i%100
        c[i].H = cost_mar(x1, y1, x2, y2)
        c[i].rod = rod_i
#         print( 'addOpen: ', c[i].rod, c[i].H)
    else:
        if (prinadl_open(i) == True):
            k=0
            if (abs(rod_i - i) == 101)or(abs(rod_i-i) == 99):
                k = c[rod_i].G + 14
            if (abs(rod_i - i) == 1)or(abs(rod_i-i) == 100):
                k = c[rod_i].G + 10
        
            if (c[i].G > k):
                c[i].G = k
                c[i].rod = rod_i
                
        
def delOpen(i):
    j = 0
    while (open_list[j] != i) :
        j+=1
    for k in range (j, len(open_list)-1):
        open_list[k] = open_list[k+1]
    open_list.pop()
def minim():
    m = open_list[0]
    for j in range (1, len(open_list)):
        if (c[open_list[j]].H + c[open_list[j]].G) < (c[m].H + c[m].G):
            m = open_list[j]
    return m
def smesh(x, y):
    print('smesh called')
    for i in range(k):
        if (Fig[i].Xrec[0] < x) and (Fig[i].Xrec[1] > x) and (Fig[i].Yrec[0] < y) and (Fig[i].Yrec[1] > y):
            xl = x - Fig[i].Xrec[0]
            xr = Fig[i].Xrec[1] - x
            yu = y - Fig[i].Yrec[0]
            yd = Fig[i].Yrec[1] - y
            if (xl < xr)and(xl < yu)and(xl<yd):
                x = Fig[i].Xrec[0] - 5
            else:
                if (xr<xl)and(xr < yu)and(xr<yd):
                    x = Fig[i].Xrec[1] +5
                else:
                    if (yu<yd)and(yu<xl)and(yu<xr):
                        y = Fig[i].Yrec[0] - 5
                    else:
                        if (yd<yu)and(yd<xl)and(yd<xr):
                            y = Fig[i].Yrec[1] + 5
    return (int(((y//rasb))*100 + (x//rasb)))
def route(x1, y1, x2, y2):
    open_list.clear()
    close_list.clear()
    pyt.clear()
#    print('route')
    canv.create_rectangle(x1 - 1,y1- 1,x1 + 1 ,y1 +1, fill="yellow")
    canv.create_rectangle(x2 - 1,y2- 1,x2 + 1 ,y2 +1, fill="yellow")

    ch_x = x1//rasb
    ch_y = y1//rasb
    x_kon = x2//rasb
    y_kon = y2// rasb
    up = -100   #upper
    un = 100   #under
    lf = -1   #left 
    rt = 1   #rite
    up_rt = - 99   #upper rite
    up_lf = -101   #upper left
    un_rt = 101    #under rite
    un_lf = 99     #unger left
    i = int(((ch_y))*100 + (ch_x))
#     if (c[i].flag == False):
        #print('smesh')
    i = smesh(x1, y1)
    
    z = i
    j = int(((y_kon))*100 + (x_kon))
    j = smesh(x2, y2)
#    print(i, j, prinadl(j))
    n = 0
    while (prinadl(j)==False):
        n+=1
#         if n>1000:
#             break
        close_list.append(i)
#         print('close_list: ', close_list)
#         print('open_list: ', open_list)
        if (i%100 != 99):
            addOpen(i+rt, i, x_kon, y_kon)
        if (i%100 != 0):
            addOpen(i+lf, i, x_kon, y_kon)
        if (i//100 != 99):
            addOpen(i+un, i, x_kon, y_kon)
        if (i//100 != 0):
            addOpen(i+up, i, x_kon, y_kon)
        if (i%100 != 0)and(i//100 != 0):
            addOpen(i+up_lf, i, x_kon, y_kon)
        if (i%100 != 0)and(i//100 != 99):
            addOpen(i+un_lf, i, x_kon, y_kon)
        if (i%100 != 99)and(i//100 != 99):
            addOpen(i+un_rt, i, x_kon, y_kon)
        if (i%100 != 99)and(i//100 != 0):
            addOpen(i+up_rt, i, x_kon, y_kon)
#         print('open_list: ', open_list)
        i = minim()
#         if (len(close_list)>1):
        delOpen(i)
#         print('open_list: ', open_list)
#         canv.create_line(c[close_list[n-1]].x,c[close_list[n-1]].y,c[i].x ,c[i].y, fill="green")

#         print('min', i)
#         canv.create_rectangle(c[i].x - 1,c[i].y - 1,c[i].x + 1 ,c[i].y +1, fill="green")

        
    pyt.append(j)
    n = 0
    canv.create_line(x2,y2,c[pyt[0]].centerX,c[pyt[0]].centerY, fill="green")

    while (pyt[n]!=z):
        pyt.append(c[j].rod)
        j = c[j].rod
        if(n>0):
            canv.create_line(c[pyt[n]].centerX,c[pyt[n]].centerY,c[pyt[n-1]].centerX,c[pyt[n-1]].centerY, fill="green")

#         print(j)
        n+=1  
    canv.create_line(x1,y1,c[pyt[n-1]].centerX,c[pyt[n-1]].centerY, fill="green")

#         if n>1000 :
#             break
#    print(pyt)


def prov_point(x1, y1):
    flag = True
    for i in range(k):
        if (Fig[i].Xrec[0] < x1) and (Fig[i].Xrec[1] > x1) and (Fig[i].Yrec[0] < y1) and (Fig[i].Yrec[1] > y1):
            flag = False
            break
    return flag
    



from tkinter import *
root = Tk()
root.geometry('500x540')
def getXY(event):
#    print ('started'   )            
 
    getx=event.x        
    gety=event.y        
       
    #print('x',getx)               
    #print('y',gety)
    my_file = open("buff.txt", "a")
    my_file.write(str(getx) +' '+ str(gety) + '\n')
    my_file.close()

    canv.create_rectangle(getx - 1,gety - 1,getx + 1 ,gety +1, fill="green")

def handle_button():
#     try:
#     except:
    f = open('buff.txt', 'r')
    str = []
    for line in f:
        str.append(line)
    f.close()
    f = open('buff.txt', 'w')
    f.close()
    koord1 = str[0].split()
    koord2 = str[1].split()
#    print( koord1, koord2)
    x1 = int(koord1[0])
    y1 = int(koord1[1])
    x2 = int(koord2[0])
    y2 = int(koord2[1])
#    print (x1, y1, x2, y2)
    route(x1, y1, x2, y2)
def handle_button2():
    #Sum=0
    canv.delete("all")
    #np.random.seed(1)
    generate()

    for i in range(k):
    #    Sum+=Fig[i].S
    #     if(i>0):
    #         print(s[i]/s[i-1])
        for j in range(int(Fig[i].N-1)):
    #         print('x', x[i][j], 'y', y[i][j])
            if (j<Fig[i].N-2):
                canv.create_line(Fig[i].x[j],Fig[i].y[j],Fig[i].x[j+1],Fig[i].y[j+1], width = 3, fill="blue")
            else:
                canv.create_line(Fig[i].x[j],Fig[i].y[j],Fig[i].x[0],Fig[i].y[0], width = 3, fill="blue")
#     for i in range (10000):
#         if c[i].flag == False:
#             canv.create_rectangle(c[i].x - rasb,c[i].y-rasb,c[i].x ,c[i].y, fill="green")
def handle_button3():
    start1 = clock()
  
    for z in range(5):
        flag = False
        while (flag == False):
            flag1 = False
            while (flag1 == False):
                x1 = np.random.randint(5, 495)
                y1 = np.random.randint(5, 495)
                flag1 = prov_point(x1, y1)
            

            flag2 = False
            while (flag2 == False):
                x2 = np.random.randint(5, 495)
                y2 = np.random.randint(5, 495)
                flag2 = prov_point(x2, y2)
            if (np.sqrt((x1-x2)**2 + (y1-y2)**2)>300):
                flag = True
        canv.create_rectangle(x1 - 1,y1 - 1,x1 + 1 ,y1 +1, fill="green")
        canv.create_rectangle(x2 - 1,y2 - 1,x2 + 1 ,y2 +1, fill="green")

        route(x1, y1, x2, y2)
    end1 = clock()
    print(end1 - start1)
        
    
Fig = []
k=25
x0=60
y0=60
c = []
rasb = 5
open_list= []
close_list = []
pyt = []
canv = Canvas(root,width=500,height=500,bg="lightblue", cursor="pencil")
# for i in range(k):
#     c=rec()
#     d = np.random.randint(5, 420)
#     h = np.random.randint(1, 420)


# print(Sum/(500*500))
#for j in range (len(pyt)-1):
#    canv.create_line(c[j].x,c[j].y,c[j+1].x ,c[j+1].y, fill="green")

fr = Frame(root)
Button(fr, command=handle_button, text='Find route').pack(side=RIGHT)
Button(fr, command=handle_button2, text='Create map').pack(side=RIGHT)
Button(fr, command=handle_button3, text='Atomatic test').pack(side=RIGHT)
root.bind('<Button-3>', getXY)

fr.pack()
canv.pack()
root.mainloop()
