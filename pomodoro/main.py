# used libraries
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_mark = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    """Resets timer to zero"""

    global reps, check_mark

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    reps = 0
    check_mark = ""


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    """Sets the timer to 25 mins (work), then to 5 mins (short-break) and after 4 work sessions
     timer is set to 20 mins (long-break)"""

    global reps, WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN

    # duration of intervals
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # count interval repetitions
    reps += 1

    # check if it's time for long break, short break or work
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    """Counts down the time of every interval and shows a new check mark bellow timer
    for every work session completed"""

    count_min = math.floor(count / 60)
    count_sec = count % 60

    # display time in format "00:09" instead of "00:9" if seconds is under 10
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # display time
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    global check_mark, timer

    # check if already counting down
    if count > 0:
        # wait 1000ms and count down by 1
        timer = window.after(1000, count_down, count - 1)
    else:
        # change interval when count gets to zero
        start_timer()
        if reps % 2 == 0:
            # add check mark if work session is completed
            check_mark += "✔"
            check_marks.config(text=check_mark)

# ---------------------------- UI SETUP ------------------------------- #
# set up GUI window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=35, bg=YELLOW)

# design the window
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 132, text="00:00", font=(FONT_NAME, 26, "bold"), fill="white")
canvas.grid(column=1, row=1)

# labels
title_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

# buttons
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

# check marks
check_marks = Label(font=(FONT_NAME, 12), fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

# keep the window open
window.mainloop()
