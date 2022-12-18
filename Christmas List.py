from tkinter import *
import pygame
import time

pygame.init()
tk = Tk()
tk.title("Christmas Wish List")

canvas = Canvas(master=tk, width=800, height=600)
canvas.pack()
border_image = PhotoImage(file="christmas-background-with-fir-branches-free-download-81.png")
canvas.create_image(0, 0, image=border_image, anchor=NW)

background_sound = pygame.mixer.Sound(file="Mariah Carey - All I Want For Christmas Is You.mp3")
background_sound.play(loops=10)
items = ['apple', 'computer', 'laptop', 'glass', 'phone']

indent = 150
index = 1
for item in items:
    canvas.create_text(150, indent, text=str(index) + "." + item.capitalize(), font = ('Comic Sans MS', 30), anchor=NW)
    indent = indent + 70
    index = index + 1


pointer_image = PhotoImage(file="pointer.png")
pointer_y = 150

for i in range(len(items) - 1):

    for i in range(70):
        tk.update()
        tk.update_idletasks()
        canvas.delete('pointer')
        canvas.create_image(400, pointer_y, image=pointer_image, anchor=NW, tag="pointer")
        pointer_y = pointer_y + 1
        time.sleep(0.01)
    time.sleep(2)




tk.mainloop()