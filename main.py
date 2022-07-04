from tkinter import *
app = Tk()
app.title("Miles to Kilometer Converter")
app.geometry("400x300")
app.resizable(False,False)
app.config(padx=20,pady=20)
app.iconbitmap("exchange.ico")


def miles_to_km():

    miles = float(miles_input.get())
    km = round(miles * 1.609)
    km_result.config(text=f"{km} km")
    is_equal_label.config(text=f"{miles} miles is equal to")

label = Label(app, text="Mile to Km Converter 🔁", font=("Arial", 20), fg="black",borderwidth=0)
label.place(x=30, y=10)

label2 = Label(app, text="Enter Miles:", font=("Arial", 15), fg="Black",borderwidth=0)
label2.place(x=30, y=60,height=30)

miles_input = Entry(app, font=("Arial", 20), bg="silver", borderwidth=0)
miles_input.place(x=160, y=60, width=180,height=30)


calc_button = Button(app,text="Calculate",font=("Arial", 20), bg="#FFC300",borderwidth=0,border=2,command=miles_to_km)
calc_button.place(x=100 ,y=100,height=60,width=150)

is_equal_label = Label(app, font=("Arial", 15), fg="black",text="")
is_equal_label.place(x= 35,y=180,height=30,width=200)

km_result = Label(app, font=("Arial", 18),borderwidth=0,fg="#C84E4E")
km_result.place(x=240, y=181, width=80,height=30)


app.mainloop()