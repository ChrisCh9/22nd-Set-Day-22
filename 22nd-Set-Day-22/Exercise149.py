#Create a program that will display the following screen: When the user enters a number in the first box and clicks on the “View Times Table” button it should show the times table in the list area. For instance, if the user entered 99 they would see the list as shown in the example on the right. The “Clear” button should clear both boxes. 

from tkinter import *

def show_table():
    num = num_box.get()
    num = int(num)
    value = 1
    for i in range(1,13):
        answer = i * num
        num_list.insert(END,(i,"x",num,'=',answer))
        value += 1
    num_box.delete(0,END)
    num_box.focus()
        
def clear_list():
    num_box.delete(0,END)
    num_list.delete(0,END)
    num_box.focus()


window = Tk()

window.title("Times Table")

window.geometry("500x250")

label1 = Label(text = "Enter a number: ")

label1.place(x = 30,y = 20)

num_box = Entry(text = 0)
    
num_box.place(x = 150,y = 20,height = 25,width = 200)

num_box.focus()

button1 = Button(text = "View Times Table",command = show_table)
    
button1.place(x = 30,y = 75,height = 25,width = 110)

num_list = Listbox()
    
num_list.place(x = 150,y = 50,height = 50,width = 200)

button2 = Button(text = "Clear",command = clear_list)
    
button2.place(x = 30,y = 50,height = 25,width = 110)

window.mainloop()