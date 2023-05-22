import threading
import time
import tkinter as tk
from PIL import ImageTk, Image
import keyboard
Image.MAX_IMAGE_PIXELS = None

import random

class Game:
   
    class movingObject:
        x = 0
        title="undefined"
        def __init__(self,x,title):
            self.xValue = x
            self.title = title
    def __init__(self):
        self.letDrop = False
        self.firstInit = True
        self.yValue = 0;
        self.window = tk.Tk(className="Dino Game 1.0")
        window_width = 640
        window_height= 480
        self.loadImageLibrary()
        self.window.geometry(f"{window_width}x{window_height}")
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        self.window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        self.panel = tk.Canvas(self.window, width=640,height=480,background="bisque")
        self.placeImage(imageData=self.imageList[0],width=0,height=0,x=0,y=0,panel=self.panel)
        self.placeImage(imageData=self.imageList[1],width=0,height=0,x=50,y=360,panel=self.panel,tags="dino")
     
        
        self.properties()
        self.panel.place(x=0,y=0)
        self.update()

        self.window.mainloop()
    def properties(self):
        self.currentItems = []
        
        
        
    def setYValue(self,value):
        if self.panel.bbox("dino")[1] > 270 and self.panel.bbox("dino")[1] < 360:
            self.yValue = 10
            return
        if self.panel.bbox("dino")[1] == 270:
            self.letDrop = True
            self.yValue = 10
            return
        if self.panel.bbox("dino")[1] >= 360:
            self.letDrop = False
            self.yValue = value
            self.panel.moveto("dino",50,360)
            return
        if self.letDrop == True:
            self.yValue = 10
            
            return
        
        self.yValue = value
    def update(self):
        if self.firstInit:
            self.firstInit = False
            self.placeImage(imageData=self.imageList[2],width=0,height=0,x=560,y=369,panel=self.panel,tags="asset1")
            self.placeImage(imageData=self.imageList[2],width=0,height=0,x=500,y=369,panel=self.panel,tags="asset2")
            self.placeImage(imageData=self.imageList[3],width=0,height=0,x=640,y=369,panel=self.panel,tags="bomb")
        max_frames = 125 # 25*5
        current_frame = 1
        while current_frame <= max_frames:
            current_frame += 1
        self.panel.move("asset1",-10,0)
        self.panel.move("asset2",-10,0)
        self.panel.move("bomb",-10,0)
        keyboard.on_press_key("space", lambda _:self.setYValue(-10),True)
        keyboard.on_release_key("space", lambda _:self.setYValue(10),True)
        print(self.panel.bbox("dino")[1])

        if self.panel.bbox("dino")[1] <= 360:
            self.panel.move("dino",0,self.yValue)
           
        else:
            
            self.setYValue(0)
            self.panel.moveto("dino",50,360)
        if self.panel.bbox("dino")[1] >= 270:
          
            self.panel.move("dino",0,self.yValue)
         
        else:
            self.setYValue(0)
           
            self.panel.moveto("dino",50,270)

            
        

        if self.panel.bbox("bomb")[0] + 20 > self.panel.bbox("dino")[0] and self.panel.bbox("bomb")[0] - 20 < self.panel.bbox("dino")[0] and self.panel.bbox("bomb")[1] - 10 < self.panel.bbox("dino")[1] and self.panel.bbox("bomb")[1] + 10 > self.panel.bbox("dino")[1]:
            exit()
        if self.panel.bbox("asset1")[0] < 0:
            self.panel.move("asset1",random.randint(650,800),0) 
        if self.panel.bbox("asset2")[0] < 0:
            self.panel.move("asset2",random.randint(650,800),0) 
        if self.panel.bbox("bomb")[0] < 0:
            self.panel.move("bomb",random.randint(650,740),0) 
        self.window.after(50,self.update)
    def loadImageLibrary(self):
        self.imageList = []
        self.imageList.append(ImageTk.PhotoImage(Image.open("assets\ground\ground.png")))
        self.imageList.append(ImageTk.PhotoImage(Image.open("assets\dino\dino-1.png")))
        self.imageList.append(ImageTk.PhotoImage(Image.open("assets/FriendlyBush/bush.png")))
        self.imageList.append(ImageTk.PhotoImage(Image.open("assets/mine/mine.png")))
       
    def placeImage(self,imageData,width,height,x,y,panel,tags="nil"):
        f = panel.create_image(x,y, anchor=tk.NW,image=imageData,tags=tags)



# ground = tk.Canvas(window, image = img2)
# ground.place(x=0,y=0)
def main():
    game = Game()
if __name__ == "__main__":
    main()