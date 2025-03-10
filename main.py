import tkinter

screen = tkinter.Tk()
screen.title("Mile to Km Converter")
screen.minsize(500,500)
screen.config(padx=50,pady=50)

user_input = tkinter.Entry(width=20)
user_input.grid(row=0,column=1,padx=10,pady=10)

miles =  tkinter.Label(text="Miles",font=('Arial',24,'bold'))
miles.grid(row=0,column=2)

equal = tkinter.Label(text="is equal to ",font=("Arial", 24) )
equal.grid(row=1,column=0)
equal.config(padx=10,pady=10)

km_value = 0
km_label = tkinter.Label(text=f"{km_value}",font=("Arial",24))
km_label.grid(row=1,column=1)

km = tkinter.Label(text="Km", font=("Arial",24))
km.grid(row=1,column=2)

def calculate_button():
    miles_value = float(user_input.get())
    km_value = round(miles_value*1.6,2)
    km_label.config(text=f"{km_value}")

button = tkinter.Button(text="Calculate",command=calculate_button,font=("Arial",18))
button.grid(row=2,column=1)


screen.mainloop()