import tkinter as tk

window = tk.Tk(className="Tah")
window_width = 640
window_height= 480
window.geometry(f"{window_width}x{window_height}")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
window.mainloop()