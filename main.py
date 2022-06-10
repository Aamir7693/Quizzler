from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK=25
SHORT_BREAK=5
LONG_BREAK=20
TICK=u'\u2713'
reps=0
cnt=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps,cnt
    reps = 0
    cnt = 0
    canvas.after_cancel(timer)
    label_left.config(text="", font=("Arial", 16))
    canvas.itemconfig(timer_text, text="00:00")
    timer_start()

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_start():
    global reps,cnt
    reps+=1
    if reps % 8 ==0:
        timer_countdown(LONG_BREAK)
        label_top.config(text="LONG BREAK", font=("verdana", 16))


    elif  reps % 2 == 0:
        timer_countdown(SHORT_BREAK)
        label_top.config(text="SHORT BREAK", font=("verdana", 16))


    else:
        timer_countdown(WORK)
        cnt += 1
        label_top.config(text="WORK", font=("verdana", 30))
        label_left.config(text=TICK * cnt)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def timer_countdown(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec==0:
        count_sec="00"
    elif count_sec<10:
        count_sec=f"0{count}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")

    if count>0:
        timer=window.after(1000, timer_countdown, count - 1)
    elif count==0:
        timer_start()
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodore Game")
window.config(padx=100,pady=50,bg=YELLOW)
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
image_=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=image_)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=("Arial",30))
label_top=Label(text="Timer",font=("verdana",30))
label_top.config(bg=YELLOW,highlightthickness=0,fg=GREEN)
label_top.grid(row=0,column=3)
label_left=Label(text="",font=("Arial",16))
label_left.config(bg=YELLOW,highlightthickness=0,fg=GREEN)
label_left.grid(row=10,column=3)
button=Button(text="Start",font=("verdana",10),command=timer_start)
button.config(bg="white",highlightthickness=0,fg="black")
button.grid(row=10,column=1)
button1=Button(text="Reset",font=("verdana",10))
button1.config(bg="white",highlightthickness=0,fg="black",command=reset_timer)
button1.grid(row=10,column=5)




canvas.grid(row=2,column=3)






window.mainloop()