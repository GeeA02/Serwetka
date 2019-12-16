import turtle
import io
from PIL import Image
import sys
import os

class Serwetka:
    def __init__(self, m, filename):
        self.name=filename 
        if(m>0):
            self.n=m
        else:
            self.n=m
            if not os.path.exists('..\\output\\' + self.name):
                os.mkdir('..\\output\\' + self.name)
            f=open('..\\output\\' + self.name +'\\'+ str(self.n) +'.txt', "a")
            f.write("Podano niewlasciwy parametr: "+str(m))
            f.close()
        self.przod=5
        self.zakret=90
        self.zakrety=1
        self.zakretywprawo=1
        self.height=2*self.n*self.przod+self.przod
    
    def __zolw__(self):
        self.zolw = turtle.Turtle()
        self.__window__()
        self.zolw.hideturtle()
        self.zolw.speed(0)
        self.zolw._tracer(0,0)
        self.zolw.up()
        self.zolw.setpos(-turtle.window_width()/2+self.height+self.przod,turtle.window_height()/2-2*self.przod)
        self.zolw.down()


    def __window__(self):
        self.window=self.zolw.getscreen()
        self.window.update()
        self.canva=self.window.getcanvas()


    def makeSerwetka(self):
        if(self.n>0):
            self.__zolw__()
            for j in range(self.n,0,-1):
                kreski=(j-1)*16+8
                for i in range(kreski):
                    if(i%2==0):
                        self.zolw.right(self.zakret)
                        self.zolw.forward(self.przod)
                        if(self.zakretywprawo+1==2*j):
                            self.zolw.right(self.zakret)
                            self.zolw.forward(self.przod)
                            self.zakrety+=1
                            self.zakretywprawo=1
                        else:
                            self.zakretywprawo+=1
                            self.zakrety+=1
                    else:
                        self.zakrety+=1
                        self.zolw.left(self.zakret)
                        self.zolw.forward(self.przod)
                self.zolw.up()
                self.zolw.right(self.zakret)
                self.zolw.forward(2*self.przod)
                self.zolw.left(self.zakret)
                self.zolw.down()
            self.canva.update()
            self.save()
            self.window.clear()
    
    def save(self):
        #self.name += '_'+
        ps = self.canva.postscript(width=2*self.height,height=2*self.height)
        im = Image.open(io.BytesIO(ps.encode('utf-8')))
        if not os.path.exists('..\\output\\' + self.name):
            os.makedirs('..\\output\\' + self.name)
        im.save('..\\output\\' + self.name + '\\' + str(self.n) +'.jpg')


class Parametr:
    def __init__(self, file):
        
        self.f=open(file,'r')
        if(self.f.mode=='r'):
            self.name=os.path.basename(self.f.name).replace(".txt","")
        else:
            if not os.path.exists('..\\output\\' + self.name):
                os.makedirs('..\\output\\' + self.name)
            f=open('..\\output\\' + self.name + '\\' + self.name +'_error.txt', 'a')
            f.write("Nie udało się otworzyć pliku "+self.name)
            f.close()

path=str(sys.argv[1])
parametr=Parametr(path)

for line in parametr.f:
    serwetka=Serwetka(int(line),parametr.name)
    serwetka.makeSerwetka()