import tkinter


def miles_to_km():
    miles = float(entry.get())
    km = miles*1.609
    label2.config(text=f"{km}")


window = tkinter.Tk()
window.title("mile to km converter")
window.config(padx=20, pady=20)

entry = tkinter.Entry(width=10)
entry.grid(row=0, column=1)

label1 = tkinter.Label(text="is equal to")
label1.grid(row=1, column=0)

label2 = tkinter.Label(text="0")
label2.grid(row=1, column=1)

label3 = tkinter.Label(text="miles")
label3.grid(row=0, column=2)

label4 = tkinter.Label(text="km")
label4.grid(row=1, column=2)

button = tkinter.Button(text="calculate", command=miles_to_km)
button.grid(row=2, column=1)

window.mainloop()
