import tkinter as tk


window=tk.Tk()
window.config(width=1024, height=720, padx=50, pady=50)
window.title(' The Most Dangerous Writing App')
# window.config(bg='black')

#Frames
top_frame=tk.Frame(window, height=100,width=500,bg='grey')
top_frame.grid(row=0,column=1,pady=20)

middle_frame=tk.Frame(window,height=500,width=500,bg='grey')
middle_frame.grid(row=1,column=1)

left_frame=tk.Frame(window,height=500, width=100,bg='grey',)
left_frame.grid(row=1,column=0,padx=20)

window.mainloop()