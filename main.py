import tkinter as tk

def clear():
    text.delete(1.0,"end")
def get():
    typed_text=text.get(1.0,"end")
    print(typed_text)

window=tk.Tk()
window.config(width=1024, height=720, padx=50, pady=50)
window.title(' The Most Dangerous Writing App')
# window.config(bg='black')

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

#Text

text=tk.Text(middle_frame,height=30,width=100)
text.grid(row=0,column=0,pady=10,padx=10)

#Buttons
get_button=tk.Button(middle_frame,text='Get',command=get,width=20)
get_button.grid(row=1,column=0)

clear_button=tk.Button(middle_frame,text='Clear',command=clear)
clear_button.grid(row=2,column=0,pady=10)


# Configure row and column weights to make frames expand
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1, weight=1)
window.mainloop()