# import pyaudio
# import wave
#
# CHUNK = 1024
# FORMAT = pyaudio.paInt16
# CHANNELS = 2
# RATE = 44100
#
#
# def record(trigger):
#     p = pyaudio.PyAudio()
#
#     stream = p.open(format=FORMAT,
#                     channels=CHANNELS,
#                     rate=RATE,
#                     input=True,
#                     frames_per_buffer=CHUNK)
#
#     print("Start recording")
#
#     frames = []
#
#     try:
#         while trigger:
#             data = stream.read(CHUNK)
#             frames.append(data)
#     except KeyboardInterrupt:
#         print("Done recording")
#     except Exception as e:
#         print(str(e))
#
#     sample_width = p.get_sample_size(FORMAT)
#
#     stream.stop_stream()
#     stream.close()
#     p.terminate()
#
#     return sample_width, frames
#
#
# def record_to_file(file_path):
#     wf = wave.open(file_path, 'wb')
#     wf.setnchannels(CHANNELS)
#     sample_width, frames = record()
#     wf.setsampwidth(sample_width)
#     wf.setframerate(RATE)
#     wf.writeframes(b''.join(frames))
#     wf.close()
#
#
# if __name__ == '__main__':
#     print('#' * 80)
#     print("Please speak word(s) into the microphone")
#     print('Press Ctrl+C to stop the recording')
#
#     record_to_file('output.mp3')
#
#     print("Result written to output.wav")
#     print('#' * 80)
#
# import tkinter
# import tkinter as tk
# import tkinter.messagebox
import pyaudio
import wave
import os


class RecAUD:

    def __init__(self, chunk=1024, frmat=pyaudio.paInt16, channels=2, rate=44100, py=pyaudio.PyAudio()):

        # Start Tkinter and set Title
        # self.main = tkinter.Tk()
        self.collections = []
        # self.main.geometry('500x300')
        # self.main.title('Record')
        self.CHUNK = chunk
        self.FORMAT = frmat
        self.CHANNELS = channels
        self.RATE = rate
        self.p = py
        self.frames = []
        self.st = 1
        self.stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)

        # Set Frames
        # self.buttons = tkinter.Frame(self.main, padx=120, pady=20)

        # Pack Frame
        # self.buttons.pack(fill=tk.BOTH)



        # Start and Stop buttons
        # self.strt_rec = tkinter.Button(self.buttons, width=10, padx=10, pady=5, text='Start Recording', command=lambda: self.start_record())
        # self.strt_rec.grid(row=0, column=0, padx=50, pady=5)
        # self.stop_rec = tkinter.Button(self.buttons, width=10, padx=10, pady=5, text='Stop Recording', command=lambda: self.stop())
        # self.stop_rec.grid(row=1, column=0, columnspan=1, padx=50, pady=5)

        # tkinter.mainloop()

    def start_record(self):
        self.st = 1
        self.frames = []
        stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)
        while self.st == 1:
            data = stream.read(self.CHUNK)
            self.frames.append(data)
            print("* recording")
            # self.main.update()

        stream.close()

        wf = wave.open('test_recording.wav', 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()

    def stop(self):
        self.st = 0


# Create an object of the ProgramGUI class to begin the program.
# guiAUD = RecAUD()