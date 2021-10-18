from tkinter import *
import random

x, y=15,15
direction=''
posicion_x = 15
posicion_y = 15
posicion_food = (15,15)
posicion_snake = [(75,75)]
nueva_posicion = [(15,15)]

def coordenadas_snake():
    global direccion, posicion_snake, x,y,nueva_posicion

    if direction == 'up':
        y-=30
        nueva_posicion[0:] = [(x,y)]
        if y>=465:
            y=15
        elif y <= 0:
            y=465
    elif direction =='down':
        y += 30
        nueva_posicion[0:] = [(x,y)]
        if y>=465:
            y=15
        elif y <=0:
            y= 15
    elif direction =='left':
        x -= 30
        nueva_posicion[0:] = [(x,y)]
        if x>=465:
            x=0
        elif y <=0:
            y= 465
    elif direction =='right':
        x += 30
        nueva_posicion[0:] = [(x,y)]
        if x>=465:
            x=15
        elif x <=0:
            x= 15
    posicion_snake = nueva_posicion + posicion_snake[:-1]

    for parte, lugar in zip.find_withtag('snake'),posicion_snake:
        canvas.coords(parte,lugar)

def direccion(event):
    global direction

    if event == 'left':
        if direction != 'right':
            direction=event
    elif event =='right':
        if direction != 'left':
            direction=event
    elif event =='up':
        if direction != 'down':
            direction=event
    elif event =='down':
        if direction != 'up':
            direction=event

def movimiento():
    global posicion_food, posicion_snake, nueva_posicion
    posiciones = [15,45,75,105,135,165,195,225,255,285,315,345,375,405,435,465]

    coordenadas_snake()
    
    if posicion_food == posicion_snake[0]:
        n= len(posicion_snake)
        cantidad['text'] = 'Cantidad 🍎: {}'.format(n)

        posicion_food = (random.choice(posiciones),random.choice(posiciones))
        posicion_snake.append(posicion_snake[-1])

        if posicion_food not in posicion_snake:
            canvas.coord(canvas.find_withtag("food"),posicion_food)

        canvas.create_text(*posicion_snake[-1], text='♦',fill='green2', font = ('Arial',20),tag='snake')

    if posicion_snake[-1] == nueva_posicion[0] and len(posicion_snake)>=4:
        cruzar_snake()
    
    for i in posicion_snake:
        if len(posicion_snake)==257:
            maximo_nivel()

    cantidad.after(300, movimiento)

def cruzar_snake():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, text= f"Intentelo\n de Nuevo \n\n 🍎", fill='red', font=('Arial',20,'bold'))

def maximo_nivel():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, text= f"EXCELENTE\n\n °° FIN °°\n\n 🍎🍎🍎", fill='green2', font=('Arial',35,'bold'))

def salir ():
    ventana.destroy()
    ventana.quit()

ventana=Tk()
ventana.config(bg='black')
ventana.title('Juego Snake')
ventana.geometry('485x510')
ventana.resizable(0,0)

frame_1 = Frame(ventana, width=485, height=25, bg='black')
frame_1.grid(column=0,row=0)
frame_2 = Frame(ventana, width=485, height=490, bg='black')
frame_2.grid(column=0,row=1)

ventana.bind("<KeyPress-Up>", lambda event:direccion('up'))
ventana.bind("<KeyPress-Down>", lambda event:direccion('down'))
ventana.bind("<KeyPress-Right>", lambda event:direccion('right'))
ventana.bind("<KeyPress-Left>", lambda event:direccion('left'))

canvas= Canvas(frame_2,bg='black', width=479, height=479)
canvas.pack()

for i in range(0,460,30):
    for j in range(0,460,30):
        canvas.create_rectangle(i,j,i+30,j+30,fill='gray10')

canvas.create_text(75,75, text='🍎', bg='black',fg='red', font=('Arial',12,'bold'))

button1= Button(frame_1, text='Salir', bg='orange', command=salir)
button1.grid(row=0,column=0,padx=20)
button2= Button(frame_1, text='Iniciar', bg='aqua', command=movimiento)
button2.grid(row=0,column=1,padx=20)

cantidad=Label(frame_1, text='Cantidad 🍎 :', bg='black',fg='red', font=('Arial',12,'bold'))
cantidad.grid(row=0,column=2,padx=20)

ventana.mainloop()