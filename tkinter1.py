import tkinter as tk1
site=tk1.Tk()
site.title("Window I")
site.geometry("600x400")
labeler=tk1.Label(site, text="this is the first window")
labeler.pack(pady=15)
def on_button_click():
        labeler.config(text="button has beeen clicked")
button=tk1.buttton(site, text="click here",command=on_button_click,bg="lightblue",font=("Arial",12))
button.pack(pady=10)
site.mainloop()