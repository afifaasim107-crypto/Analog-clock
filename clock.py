import tkinter as tk
import time
import math

root = tk.Tk()
root.title("Stylish Clock ⏰")
canvas = tk.Canvas(root, width=400, height=400, bg="black")
canvas.pack()

def draw_clock():
    canvas.delete("all")

    cx, cy = 200, 200

    # clock border
    canvas.create_oval(50,50,350,350, outline="white", width=2)

    # numbers
    for i in range(1,13):
        angle = i * 30
        x = cx + 130 * math.cos(math.radians(angle-90))
        y = cy + 130 * math.sin(math.radians(angle-90))
        canvas.create_text(x, y, text=str(i), fill="white", font=("Arial", 12, "bold"))

    t = time.localtime()

    sec = t.tm_sec
    min = t.tm_min
    hr = t.tm_hour % 12

    # hands
    sec_angle = sec * 6
    min_angle = min * 6 + sec*0.1
    hr_angle = hr * 30 + min*0.5

    def hand(length, angle, color, width):
        x = cx + length * math.cos(math.radians(angle-90))
        y = cy + length * math.sin(math.radians(angle-90))
        canvas.create_line(cx, cy, x, y, fill=color, width=width)

    hand(100, sec_angle, "red", 1)
    hand(80, min_angle, "white", 3)
    hand(60, hr_angle, "cyan", 4)

    canvas.create_oval(195,195,205,205, fill="white")

    root.after(1000, draw_clock)

draw_clock()
root.mainloop()