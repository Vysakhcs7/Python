#import tkinter module
import tkinter


root = tkinter.Tk()
root.title("STM32 Auto Reload Value Calculator")
root.iconbitmap('D:\Python\Tkinter\Basics\Images\Timer.ico')
root.geometry('400x400+700+300')
root.resizable(0,0)
root.config(bg = '#123456')

name_label_1 = tkinter.Label(root, text = "STM32 ARR Calculator",font=('Arial', 15), bg ='#E6F2FF')
name_label_1.grid(row = 0, column = 0)

text_box = tkinter.Text(root, height=1, width=20)
text_box.grid(row=1,column=0)

name_button = tkinter.Button(root, text= "Submit",bg="#E6F2FF",activebackground="green")
name_button.grid(row=2,column=2)


root.mainloop()

