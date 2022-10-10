from PIL import ImageGrab
from audio_recorder.audio_recorder import RecAUD
from audio_recorder.audio_recorder import *
from multiprocessing import Process

import cv2
import numpy as np
import tkinter as tk
import threading
from time import sleep


rec_aud = RecAUD()

p = ImageGrab.grab()
a, b = p.size
filename=('temp_vid.mp4')
fourcc = cv2.VideoWriter_fourcc(*'avc1')
frame_rate = 16
out = cv2.VideoWriter()

def screen_capturing():

    global capturing
    capturing = True

    th = threading.Thread(target=rec_aud.start_record)
    th.start()

    while capturing:

        img = ImageGrab.grab()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        out.write(frame)

def start_screen_capturing():

    if not out.isOpened():
        out.open(filename, fourcc, frame_rate, (a, b))

    print(' rec started')
    t1 = threading.Thread(target=screen_capturing)
    # t2 = threading.Thread(target=rec_aud.start_record)

    t1.start()
    # t2.start()


    # process_one = Process(target=screen_capturing)
    # process_two = Process(target=rec_aud.start_record)
    #
    # process_one.start()
    # process_one.join()
    #
    # process_two.start()
    # process_two.join()

def stop_screen_capturing():
    global capturing

    rec_aud.stop()

    capturing = False
    out.release()
    print('complete')



def pause_screen_capturing():
    global capturing
    capturing = False
    print("Paused")

def resume_screen_capturing():
    global capturing
    capturing = True
    if not out.isOpened():
        out.open(filename,fourcc, frame_rate,(a,b))
    t1=threading.Thread(target=screen_capturing, daemon=True)
    t1.start()
    print("Resumed")