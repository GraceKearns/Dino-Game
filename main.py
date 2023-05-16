import tkinter as tk
from PIL import ImageTk, Image
Image.MAX_IMAGE_PIXELS = None

class Game:
   
    
    def __init__(self):
        self.window = tk.Tk(className="Tah")
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
        self.window.mainloop()
    def loadImageLibrary(self):
        self.imageList = []
        self.imageList.append(ImageTk.PhotoImage(Image.open("assets\ground\ground.png")))
        print(self.imageList)
    def placeImage(self,imageData,width,height,x,y,panel):
        panel.create_image(0,0, anchor=tk.NW,image=imageData)
        panel.place(x=x,y=y)


# ground = tk.Canvas(window, image = img2)
# ground.place(x=0,y=0)
def main():
    game = Game()
if __name__ == "__main__":
    main()