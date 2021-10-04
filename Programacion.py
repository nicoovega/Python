from tkinter import *
ventana = Tk()
ventana.title("Bienvenido a Doctops")
ventana.geometry("700x600")
selected=IntVar()
def clicked():
    numero1= int(num1.get())
    numero2= int(num2.get())
    op=int(selected.get())
    res=""
    if op==1:
        res =  numero1+numero2 
    elif op==2:
        res =  numero1-numero2 
    elif op==3:
        res =  numero1*numero2 
    elif op==4:
        res =  numero1/numero2 
    lbl.configure(text=res)
lbl= Label(ventana, text="Que operacion desea realizar", font=("Arial bold",20))
lbl.grid(column=0,row=0)
num1= Entry(ventana,width=10)
num1.grid(column=0,row=2)
num2= Entry(ventana,width=10)
num2.grid(column=0,row=3)
rad1 = Radiobutton(ventana,text='Suma', value=1, variable=selected)
rad2 = Radiobutton(ventana,text='Resta', value=2,variable=selected)
rad3 = Radiobutton(ventana,text='Multiplicacion', value=3,variable=selected)
rad4 = Radiobutton(ventana,text='Division', value=4, variable=selected)



boton = Button(ventana, text="Calcular",bg="red",fg="white", command=clicked)
boton.grid(column=1,row=0)

rad1.grid(column=0, row=1)
rad2.grid(column=1, row=1)
rad3.grid(column=2, row=1)
rad4.grid(column=3, row=1)
ventana.mainloop()