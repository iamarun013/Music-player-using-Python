from tkinter import *
from PIL import ImageTk, Image
import os
from pygame import mixer


# colours
co1 = "#ffffff"  # white
co2 = "#3C1DC6"  # purple
co3 = "#333333"  # black
co4 = "#CFC7F8"  # light purple

window = Tk()
window.title("AS Music Player")
window.geometry('452x355')
window.configure(background=co1)

# frames
left_frame = Frame(window, width=150, height=250, bg=co1)
left_frame.grid(row=0, column=0, padx=1, pady=1)

right_frame = Frame(window, width=300, height=250, bg=co3)
right_frame.grid(row=0, column=1, padx=0)

down_frame = Frame(window, width=452, height=200, bg=co4)
down_frame.grid(row=1, column=0, columnspan=2, padx=0, pady=1)

# right_frame
Listbox = Listbox(right_frame, selectmode=SINGLE,
                  font="Arial 9 bold", width=32, bg=co3, fg=co1)
Listbox.grid(row=0, column=0)

w = Scrollbar(right_frame)
w.grid(row=0, column=1)

Listbox.config(yscrollcommand=w.set)
w.config(command=Listbox.yview)

running_song = Label(down_frame, height=1, width=244, text="Choose a song", font=(
    "Ivy 10"), padx=10, bg=co1, fg=co3, anchor=NW)
running_song.place(x=0, y=1)


# Events
def play_music():
    running = Listbox.get(ACTIVE)
    running_song['text'] = running
    mixer.music.load(running)
    mixer.music.play()


def pause_music():
    mixer.music.pause()


def continue_music():
    mixer.music.unpause()


def stop_music():
    mixer.music.stop()


def next_music():
    global playing
    index = Listbox.curselection()[0]
    new_index = (index + 1) % len(songs)
    playing = songs[new_index]

    mixer.music.load(playing)
    mixer.music.play()

    Listbox.selection_clear(0, END)
    Listbox.select_set(new_index)

    running_song.config(text=playing)


def previous_music():
    global playing
    index = Listbox.curselection()[0]
    new_index = (index - 1) % len(songs)
    playing = songs[new_index]

    mixer.music.load(playing)
    mixer.music.play()

    Listbox.selection_clear(0, END)
    Listbox.select_set(new_index)

    running_song.config(text=playing)


# Images
img_1 = Image.open('Music.png')
img_1 = img_1.resize((120, 160))
img_1 = ImageTk.PhotoImage(img_1)
app_image = Label(left_frame, height=200, image=img_1, padx=0, bg=co1)
app_image.place(x=12, y=15)

img_2 = Image.open('reverse.png')
img_2 = img_2.resize((50, 60))
img_2 = ImageTk.PhotoImage(img_2)
prev_button = Button(down_frame, height=50, width=50,
                     image=img_2, padx=0, bg=co1, command=previous_music)
prev_button.place(x=12+28, y=35)

img_3 = Image.open('play.png')
img_3 = img_3.resize((50, 60))
img_3 = ImageTk.PhotoImage(img_3)
play_button = Button(down_frame, height=50, width=50,
                     image=img_3, padx=0, bg=co1, command=play_music)
play_button.place(x=12+88, y=35)

img_4 = Image.open('fastforward.png')
img_4 = img_4.resize((50, 60))
img_4 = ImageTk.PhotoImage(img_4)
next_button = Button(down_frame, height=50, width=50,
                     image=img_4, padx=0, bg=co1, command=next_music)
next_button.place(x=12+148, y=35)

img_5 = Image.open('pause.png')
img_5 = img_5.resize((50, 60))
img_5 = ImageTk.PhotoImage(img_5)
pause_button = Button(down_frame, height=50, width=50,
                      image=img_5, padx=0, bg=co1, command=pause_music)
pause_button.place(x=12+208, y=35)

img_6 = Image.open('continue.png')
img_6 = img_6.resize((50, 60))
img_6 = ImageTk.PhotoImage(img_6)
continue_button = Button(down_frame, height=50, width=50,
                         image=img_6, padx=0, bg=co1, command=continue_music)
continue_button.place(x=12+268, y=35)

img_7 = Image.open('stop.png')
img_7 = img_7.resize((50, 60))
img_7 = ImageTk.PhotoImage(img_7)
stop_button = Button(down_frame, height=50, width=50,
                     image=img_7, padx=0, bg=co1, command=stop_music)
stop_button.place(x=12+328, y=35)


line = Label(left_frame, height=1, width=200, padx=0, bg=co3)
line.place(x=0, y=1)

line = Label(left_frame, height=1, width=200, padx=0, bg=co1)
line.place(x=0, y=3)


running_song = Label(down_frame, height=1, width=244, text="Choose a song", font=(
    "Ivy 10"), padx=10, bg=co1, fg=co3, anchor=NW)
running_song.place(x=0, y=1)


os.chdir(r"C:\Users\KIIT\Documents\Codes\Python\music")
songs = os.listdir()


def show():
    for i in songs:
        Listbox.insert(END, i)


show()
mixer.init()
music_state = StringVar()
music_state.set("Choose one!")

window.mainloop()
