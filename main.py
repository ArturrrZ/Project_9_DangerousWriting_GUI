import tkinter as tk
from tkinter import messagebox
import time
timer=None
def get():
    global timer
    if timer is not None:
        window.after_cancel(timer)
        timer_label.config(text='Timer',fg='black')
    typed_text=text.get(1.0,"end")
    text.delete(1.0, "end")
    print(typed_text)
    with open('typed_text.txt','a' ) as doc:
        doc.write(f"{typed_text}\n---------------------\n")
def clear():
    global timer
    if timer is not None:
        window.after_cancel(timer)
        timer_label.config(text='Timer',fg='black')
    text.delete(1.0,"end")

def on_key_press(event):
    global timer
    if timer is not None:
        window.after_cancel(timer)
        timer_label.config(fg='black')
    start_timer(5)
    # print("You started typing")
    # print(symbol_in_text)

def start_timer(count):
    counted_sec=count % 6
    if counted_sec < 10:
        counted_sec=f"0{counted_sec}"
    if count <=2:
        timer_label.config(text=f'HURRY\n\nUP:\n\n'
                                f'{counted_sec}',fg='red')
    else:
        timer_label.config(text=f'Timer:\n\n'
                                f'{counted_sec}')

    if count > 0:
        global timer
        timer=window.after(1000,start_timer, count-1)
        # print(timer)
        # print(type(timer))
    if count == 0:
        clear()
        messagebox.showerror(title='FAILED',message='You did not type for 5 seconds \nYou LOST your text')

window=tk.Tk()
window.config(width=1024, height=720, padx=50, pady=50)
window.title('The Most Dangerous Writing App')
#Frames
top_frame=tk.Frame(window, height=100,width=500,bg='grey',)
top_frame.grid(row=0,column=1,pady=20,sticky="nsew")

middle_frame=tk.Frame(window,height=500,width=500,bg='grey')
middle_frame.grid(row=1,column=1,sticky="nsew")

left_frame=tk.Frame(window,height=500, width=100,bg='grey',)
left_frame.grid(row=1,column=0,padx=20,sticky="nsew")

#Labels

top_label=tk.Label(top_frame,text='Write whatever you want!✨',bg='grey',justify='center', anchor='center',font=('Courier',14,'bold'))
top_label.grid(row=0,column=0,sticky="nsew", padx=250,pady=20)

timer_label=tk.Label(left_frame,text='',bg='grey')
timer_label.grid(row=0,column=0,sticky="nsew",pady=100,padx=10)

#Text

text=tk.Text(middle_frame,height=30,width=100)
text.grid(row=0,column=0,pady=10,padx=10)

#Buttons
get_button=tk.Button(middle_frame,text='Save',command=get,width=20)
get_button.grid(row=1,column=0)

clear_button=tk.Button(middle_frame,text='Clear',command=clear)
clear_button.grid(row=2,column=0,pady=10)

text.bind("<KeyPress>", on_key_press)

# Configure row and column weights to make frames expand
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1, weight=1)
window.mainloop()
