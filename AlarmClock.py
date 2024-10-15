import pyttsx3
from tkinter import *
import datetime
import time




def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        print(now)
        if now == set_alarm_timer:
            #print("Time to Wake up")
            #playsound.PlaySound("sound.mp3", playsound.SND_ASYNC)

            if set_alarm_timer<"12:00:00":
                print("Time is " + set_alarm_timer + " a.m. Please Wake up from the sleep")
                engine = pyttsx3.init()
                engine.say("Hey Redwan, it is " + (str)(set_alarm_timer)+"a.m. Please, wake up from the sleep")
                engine.runAndWait()
                engine.stop()
            else:
                print("Time is " + set_alarm_timer + " p.m. Please Wake up from the sleep")
                engine = pyttsx3.init()
                engine.say("Hey Redwan, it is " + (str)(set_alarm_timer)+"p.m.. Please, wake up from the sleep")
                engine.runAndWait()
                engine.stop()
            break


def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)


alarm_clock = Tk()
alarm_clock.title("Digital Alarm Clock")
alarm_clock.geometry("400x400")
time_format = Label(alarm_clock, text="", fg="black", bg="red", font="Arial").place(x=60, y=120)
addTime = Label(alarm_clock, text="Hour  Min   Sec", font=60).place(x=110)
setYourAlarm = Label(alarm_clock, text="", fg="blue", relief="solid",
                     font=("Helevetica", 7, "bold")).place(x=0, y=29)


hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime = Entry(alarm_clock, textvariable=hour, bg="green", width=15).place(x=110, y=30)
minTime = Entry(alarm_clock, textvariable=min, bg="green", width=15).place(x=150, y=30)
secTime = Entry(alarm_clock, textvariable=sec, bg="green", width=15).place(x=200, y=30)

submit = Button(alarm_clock, text="Set Alarm", fg="blue", width=10, command=actual_time).place(x=110, y=70)

alarm_clock.mainloop()
