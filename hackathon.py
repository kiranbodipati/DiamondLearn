from datetime import date
import calendar
import time
from tkinter import *
from backend import *

today = date.today()
day_of_the_week= date.today().weekday()
list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
show_day = list[day_of_the_week]

window= Tk()
window.title("Welcome to study system")
window.geometry("1400x800")
C = Canvas(window, bg="blue", height=400, width=500)
filename = PhotoImage(file ="diamond.png")
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
Label(window, text="Name").place(x=900,y=500)
Label(window,text="Level").place(x=900,y=550)






date_today = Label(window, text= today, font="times 20 bold",bg="black",fg="grey")

date_today.place(x=20,y=60)

weekday_today= Label(window,text=show_day,font="times 20 bold",bg="black",fg="grey")
weekday_today.place(x=20,y=60)


#show exact current time
time1 = ""
clock = Label(window, font=("times", 20, "bold"),fg="grey",bg="black")
clock.place(x=20,y=120)

def tick():
    global time1
    time2 = time.strftime("%H:%M:%S")
    if time2 != time1:
        time1= time2
        clock.config(text=time2)
    clock.after(200,tick)
tick()




add_image=PhotoImage(file= "addtermsbutton.png")
add_image1=add_image.subsample(4,4)
enter_image=PhotoImage(file="enterbutton.png")
enter_image1=enter_image.subsample(4,4)
search_image=PhotoImage(file="searchbutton.png")
search_image1=search_image.subsample(4,4)
searchterm_image=PhotoImage(file="searchtermbutton.png")
searchterm_image1=searchterm_image.subsample(4,4)



def window1_1_1():
    window=Toplevel()
    window.geometry("1400x800")
    window.title("definition")
    c = Canvas(window, bg="blue", height=400, width=500)
    filename1_1_1 = PhotoImage(file="bg.png")
    background_label1_1_1= Label(window, image=filename1_1_1)
    background_label1_1_1.place(x=0, y=0, relwidth=1, relheight=1)
    background_label1_1_1.image = filename1_1_1
    c.pack()








def window1_2_1():
    window=Toplevel()
    window.geometry("1400x800")
    window.title("Search terms")
    c = Canvas(window, bg="blue", height=400, width=500)
    filename1_2_1 = PhotoImage("bg.png")
    background_label1_2_1 = Label(window, image=filename1_2_1)
    background_label1_2_1.place(x=0, y=0, relwidth=1, relheight=1)
    background_label1_2_1.image = filename1_2_1
    c.pack()

def window1_1():
    window=Toplevel()
    window.geometry("1400x800")
    window.title("Add terms")
    c=Canvas(window,bg="blue",height=400, width=500)
    filename1_1 = PhotoImage(file="bg.png")
    background_label1_1 = Label(window, image=filename1_1)
    background_label1_1.place(x=0, y=0, relwidth=1, relheight=1)
    background_label1_1.image=filename1_1
    Label(window,text="Term:",font="50").place(x=500,y=300)
    Label(window, text="Definition/Explanation:",font="50").place(x=800, y=300)

    term=StringVar()
    Entry(window,textvariable= term).place(x=500,y=350,width=120,height=50)
    defi=StringVar()
    Entry(window,textvariable=defi).place(x=800,y=350,width=200,height=250)

    Button(window,text="Add",command=window1_1_1).place(x=800,y=650)
    c.pack()


def window1_2():
    window=Toplevel()
    window.geometry("1400x800")
    window.title("Search terms")
    c=Canvas(window,bg="blue",height=400, width=500)
    filename1_2= PhotoImage(file="bg.png")
    background_label1_2 = Label(window, image=filename1_2)
    background_label1_2.place(x=0, y=0, relwidth=1, relheight=1)
    background_label1_2.image = filename1_2
    term = StringVar()
    Entry(window,textvariable=term).place(x=500,y=350,width=120,height=50)
    Label(window,text="I want to know the meaning of : ").place(x=500, y=300)
    Button(window,text=search_image1,command= window1_2_1).place(x=700,y=350)
    c.pack()





def window1():
    window=Toplevel()
    window.geometry("1400x800")
    window.title("Activity")
    C = Canvas(window, bg="blue", height=400, width=500)
    filename1 = PhotoImage(file="bg.png")
    background_label1 = Label(window, image=filename1)
    background_label1.place(x=0, y=0, relwidth=1, relheight=1)
    background_label1.image = filename1
    add_term= Button(window, text=add_image1,command=window1_1)
    add_term.place(x=500,y=300)
    search_term=Button(window,text=searchterm_image1,command=window1_2)
    search_term.place(x=800,y=300)
    Label(window,text="Hello  " + name.get(),font="50",fg="black").place(x=300,y=200)
    C.pack()

name=StringVar()
nameEntered=Entry(window,width=15,textvariable=name)
nameEntered.place(x=1000,y=500)

level=StringVar()
levelEntered=Entry(window,width=15,textvariable=level)
levelEntered.place(x=1000,y=550)

im_ready_button = Button(window, text=enter_image1,  command=window1)
im_ready_button.place(x=1000, y=600)








mainloop()
