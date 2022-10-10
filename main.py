from multiprocessing import freeze_support
from tkinter import *
from tkinter import ttk
from pose_identifier.pose_identify import pose_identifier
from screen_recorder.screen_recorder import *
# from audio_recorder.audio_recorder import  *
# from audio_recorder.audio_recorder import RecAUD
from multiprocessing import Process

import cv2
import numpy as np
import tkinter as tk
import threading
import moviepy.editor as mpe
import screen_recorder.screen_recorder

root = Tk()
root.title("white board")
root.geometry("1500x870+150+50")
root.configure(bg="#f2f3f5")
root.resizable(False, False)

current_x = 0
current_y = 0
color = 'black'

def locate_xy(work):
    global current_x,current_y

    current_x = work.x
    current_y = work.y

def addLine(work):
    global current_x, current_y

    canvas.create_line((current_x, current_y, work.x, work.y), width=get_current_value(), fill=color, capstyle=ROUND, smooth=TRUE)
    current_x, current_y = work.x, work.y

def show_color(new_color):
    global color
    color = new_color

def new_canvas():
    canvas.delete('all')
    display_pallete()


#icon
image_icon = PhotoImage(file="assets/logo.png")
root.iconphoto(False,image_icon)

eraser=PhotoImage(file="assets/eraser.png")
Button(root, image=eraser, bg="#f2f3f5", height=20, width=20, command=new_canvas).place(x=47,y=340)

colors = Canvas(root, bg="#ffffff", width=37, height=310, bd=0)
colors.place(x=40, y=10)


def display_pallete():
    id = colors.create_rectangle((10,10,30,30), fill="black")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('black'))

    id = colors.create_rectangle((10,40,30,60), fill="gray")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('gray'))

    id = colors.create_rectangle((10,70,30,90), fill="brown4")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('brown4'))

    id = colors.create_rectangle((10,100,30,120), fill="yellow")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('yellow'))

    id = colors.create_rectangle((10,130,30,150), fill="blue")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('blue'))

    id = colors.create_rectangle((10,160,30,180), fill="orange")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('orange'))

    id = colors.create_rectangle((10,190,30,210), fill="pink")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('pink'))

    id = colors.create_rectangle((10,220,30,240), fill="brown4")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('brown4'))

    id = colors.create_rectangle((10,250,30,270), fill="purple")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('purple'))

    id = colors.create_rectangle((10,280,30,300), fill="red")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('red'))


display_pallete()

canvas = Canvas(root, width=1350, height=700, background="white", cursor="hand2")
canvas.place(x=120,y=10)

canvas.bind('<Button-1>', locate_xy)
canvas.bind('<B1-Motion>', addLine)

############SLIDER##############

current_value = tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    value_label.configure(text=get_current_value())

slider = ttk.Scale(root, from_=0, to=100, orient='horizontal', command=slider_changed, variable=current_value)
slider.place(x=10,y=380)

#value label
value_label = ttk.Label(root, text=get_current_value())
value_label.place(x=10, y=410)


# rec_aud = RecAUD()

############WEB CAMERA##############
def start_web_cam():
    # process_one = Process(target=start_pose_identifier)
    # process_one.start()


    th = threading.Thread(target=pose_identifier)
    th.start()


web_cam_start = Button(text ="Start Web Camera", command=start_web_cam).place(x=10,y=450)


def combine_audio(vidname="temp_vid.mp4", audname="test_recording.wav", outname="output.mp4", fps=10):

    my_clip = mpe.VideoFileClip(vidname)
    audio_background = mpe.AudioFileClip(audname)
    print(str(audio_background.duration))
    print(str(my_clip.duration))
    print(str(my_clip.duration - audio_background.duration))
    clip = my_clip.subclip(my_clip.duration - audio_background.duration, my_clip.duration)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(outname,fps=fps)

############MERGE AUDIO AND VIDEO##############
merge_things = Button(text ="Merge", command=combine_audio).place(x=10,y=480)




############SCREEN RECORDER & AUDIO RECORDER##############
start_cap = Button(root, text='Start Recording', width=30, command=start_screen_capturing)
start_cap.place(x=285, y=760)

stop_cap = Button(root, text='Stop Recording', width=30, command=stop_screen_capturing)
stop_cap.place(x=535,y=760)

start_cap = Button(root, text='Pause Recording', width=30, command=pause_screen_capturing)
start_cap.place(x=785, y=760)

stop_cap = Button(root, text='Resume Recording', width=30, command=resume_screen_capturing)
stop_cap.place(x=1035,y=760)



if __name__ == '__main__':
    freeze_support()
    root.mainloop()