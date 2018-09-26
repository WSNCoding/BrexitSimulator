
import time
import tkinter as tk
from tkinter import *
import random

#player pos



#end of player pos
class Everything:

    timestart=time.clock()
    Bullets = []
    playerposX = 400
    playerposY = 250
    moveX = 0
    moveY = 0
    moveSpeed = 5
    num = 0
    MaxBullets = 10
    Health = 20
    JeanX = 150
    JeanY = 150 #Y pos for Jean Claude Junkckckckckerrds
    lasttime = 0
    def makewin(self):      
        global root
        global window
        root = tk.Tk()
        window = tk.Canvas(root,width=800,height=600)
        root.geometry("800x600")
        window.pack()


    def __init__(self):
        print("starting")
        self.makewin()
        print("images being created, leo & ori are the best by the way")
        self.i=33

        global bulletimg
        
        global trump
        global Jean
        global Win
        Jean =  PhotoImage(file="BadGuy.gif")
        Win = PhotoImage(file="Win.gif")
        trump =  PhotoImage(file="Theresa.gif")
        bulletimg =  PhotoImage(file="DollarBlast.gif")

        #bindings
        root.bind("<Key>", self.handleKeyPress)
        root.bind("<KeyRelease>", self.handleKeyRelease)

        window.after(0,self.renderandupdate)


        global playerposX
        global playerposY
        window.mainloop()

    def BadGuyMove(self):
        newTime = 0
    
        newtime = time.clock()
        if (newtime-self.lasttime)>0.005:
            if(self.JeanY<90):
                self.JeanY+=5
            elif(self.JeanY>225):
                self.JeanY-=5
            if(self.JeanX<90):
                self.JeanX+=5
            elif(self.JeanX>605):
                self.JeanX-=5
            else:
                self.JeanX+=random.randint(-1,1) *5
                self.JeanY+=random.randint(-1,1) *5
                
            self.lasttime=newtime
            
                
        
    def renderandupdate(self):
        window.delete("all")
        self.i+=1
        #if self.i%33==0:
        #    print ("%.02f FPS"%(self.i/(time.clock()-self.timestart)))

        self.updatewindow()
        window.update()
        window.after(10,self.renderandupdate)
   

    def updatewindow(self):
        if(self.Health<=0):
            window.create_image(400, 300, image=Win)
        self.BadGuyMove()
        window.create_image(self.playerposX, self.playerposY, image=trump)
        if(self.Health>0):
            
            window.create_image(self.JeanX, self.JeanY, image=Jean)
        else:
            window.create_text(350,150,text="YOU WIN",font=("Purisa", 100))
        #bullet logicality

        for singleBullet in self.Bullets:
#
            if(self.Health>0 and singleBullet.xpos <self.JeanX+50 and singleBullet.xpos >self.JeanX-50 and singleBullet.ypos <self.JeanY+70 and singleBullet.ypos >self.JeanY-70):
                self.Health -=1
                self.Bullets.remove(singleBullet)
                
            if (singleBullet.visible):
                window.create_image(singleBullet.xpos,singleBullet.ypos,image=bulletimg)
                singleBullet.moveBullet()
            else:
                self.Bullets.remove(singleBullet)
            
        
        if (self.playerposY > 510) & (self.moveY>0):
            self.moveY=0
            print("going in a direction called up")
        if (self.playerposY < 100) & (self.moveY<0):
            self.moveY=0

        if (self.playerposX > 710) & (self.moveX>0):
            self.moveX=0
            
        if (self.playerposX < 70) & (self.moveX<0):
            self.moveX=0      
    
        self.playerposY+=self.moveY
        self.playerposX+=self.moveX  
        
    def handleKeyPress(self,event):

        if (event.char == "a"):
            self.moveX=-self.moveSpeed
        if (event.char =="d"):
            self.moveX=self.moveSpeed
        if (event.char=="w"):
            self.moveY=-self.moveSpeed
        if (event.char=="s"):
            self.moveY=self.moveSpeed
        if (event.char == "A"):
            self.moveX=-self.moveSpeed
        if (event.char =="D"):
            self.moveX=self.moveSpeed
        if (event.char=="W"):
            self.moveY=-self.moveSpeed
        if (event.char=="S"):
            self.moveY=self.moveSpeed

        if (event.char==" "):
            if(self.Bullets.__len__() < self.MaxBullets):            
                self.Bullets.append(bullet(self.playerposX , self.playerposY))
                print("Fire!"+str(self.Bullets.__len__()))

    def handleKeyRelease(self,event):

        if (event.char == "a"):
            self.moveX=0
        if (event.char =="d"):
            self.moveX=0
        if (event.char=="w"):
            self.moveY=0
        if (event.char=="s"):
            self.moveY=0
        if (event.char == "A"):
            self.moveX=0
        if (event.char =="D"):
            self.moveX=0
        if (event.char=="W"):
            self.moveY=0
        if (event.char=="S"):
            self.moveY=0

        if (event.char==" "):
            print("Fire button released")
        else:
            print(event.char + " Key released")



class makeimage():
    def loadsprite(imagename, image):
        imagename = PhotoImage(file="image")
    def drawimage(imagename,x,y):
        window.create_image(x,y, image = imagename)
    





class bullet:
    xpos=0
    ypos=0
    visible=False
    BulletSpeed = 8
    
    def __init__(self, x,y):
        self.ypos = y
        self.xpos = x
        self.visible = True
        self.lasttime = time.clock()
        self.newtime = 0

    def moveBullet(self):
        self.newtime = time.clock()
        if (self.newtime-self.lasttime)>0.005:
            self.ypos-=self.BulletSpeed
            self.lasttime=self.newtime
            if (self.ypos < 10):
                self.visible=False


















print("Starting...")
Everything()
root.mainloop()
    
