# coding=utf-8
# Python3
# Proyecto
#
# DESCRIPCION: La vieja tridimensional en un tablero NxNxN.

# Autores: 
#	Gregory Muñoz (Carnet: 16-11313) && Ka Shing Fung Ng (Carnet: 16-10388)

# Ultima modificacion: 24/05/2019

# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.messagebox
import sys
import os

# La funciones fueron clasificadas en tres archivos para mejorar la visualización del código.
from HayLineas import HayAlineaVertical, HayAlineaHorizontal, HayAlineaDiag, HayAlineaTableros
from Fichas import Quedan_fichas
from Jugada import EsValida, CambiarJugador, ReflejarJugada, SumarLinea

import random

class Application (Tk):
        # args (variables), wargs (keyboard arguments)      

        def __init__ (self, *args, **wargs):
                Tk.__init__ (self, *args, **wargs)                          

                ventana = Frame(self)
                ventana.pack (side = 'right', fill = BOTH, expand = "True")
                ventana.grid_rowconfigure(0, weight = 1)
                ventana.grid_columnconfigure(0, weight = 1)

                self.frames = {}

                for page in (Principal, Reglas, User, Tablero):
                        frame = page (ventana, self)
                        self.frames[page] = frame
                        frame.grid (row = 0, column = 0, sticky = "nsew")

                self.mostrar_ventana (Principal)

        def mostrar_ventana (self, cont):
            frame = self.frames[cont]
            frame.tkraise()      

class Principal (Frame):
        def __init__ (self, parent, controller):
                Frame.__init__ (self, parent)
                self.controller=controller                                             

                self.config (bg = "midnight blue")

                # Frame 1 (Principal)
                Frame_1 = Frame(self)
                Frame_1.pack()
                Frame_1.place (x = 300, y = 60)
                Frame_1.config(width="380", height="430", bg = "blue4")

                # Frame 2 (Principal)
                Frame_2 = Frame(Frame_1)
                Frame_2.pack()
                Frame_2.place (x = 5, y = 5)
                Frame_2.config(width="370", height="420", bg = "navy")

                # Frame 3 (Principal)
                Frame_3 = Frame(Frame_2)
                Frame_3.pack()
                Frame_3.place (x = 5, y = 5)
                Frame_3.config(width="360", height="410", bg = "RoyalBlue4")

                # Frame 4 (Principal)
                Frame_4 = Frame(Frame_3)
                Frame_4.pack()
                Frame_4.place (x = 5, y = 5)
                Frame_4.config(width="350", height="400", bg = "slate blue")              

                label = Label (Frame_4, text = u'TicTacToe\u207F', font = "Arial 32 bold", bg = "slate blue", fg = 'white')
                label.place(x = 60, y = 60)    

                # Botones (Principal)
                jugar = Button(Frame_4, text='Jugar', font = "Arial 16 bold", width = 10, height = 1, bg = "light steel blue", fg = 'gray10', relief = RAISED, command = lambda : controller.mostrar_ventana(User))
                jugar.place(x = 105, y =150)

                regla = Button(Frame_4, text='Reglas', font = "Arial 16 bold", width = 10, height = 1, bg = "light steel blue", fg = 'gray10', relief = RAISED, command = lambda : controller.mostrar_ventana(Reglas))
                regla.place(x = 105, y =220)                 

                salir = Button(Frame_4, text='Salir', font = "Arial 16 bold", width = 10, height = 1, bg = "light steel blue", fg = 'gray10', relief = RAISED, command = quit)
                salir.place(x = 105, y = 285)


class User (Frame):
        def __init__ (self, parent, controller):
                Frame.__init__ (self, parent)
                self.controller=controller                                             
                
                self.config (bg = "midnight blue")

                # Frame 1 (User)
                Frame_1 = Frame(self)
                Frame_1.pack()
                Frame_1.place (x = 300, y = 60)
                Frame_1.config(width="380", height="430", bg = "blue4")

                # Frame 2 (User)
                Frame_2 = Frame(Frame_1)
                Frame_2.pack()
                Frame_2.place (x = 5, y = 5)
                Frame_2.config(width="370", height="420", bg = "navy")

                # Frame 3 (User)
                Frame_3 = Frame(Frame_2)
                Frame_3.pack()
                Frame_3.place (x = 5, y = 5)
                Frame_3.config(width="360", height="410", bg = "RoyalBlue4")

                # Frame 4 (User)
                Frame_4 = Frame(Frame_3)
                Frame_4.pack()
                Frame_4.place (x = 5, y = 5)
                Frame_4.config(width="350", height="400", bg = "slate blue")

                # Frame 5 (User)
                Frame_5 = Frame(Frame_4)
                Frame_5.pack()
                Frame_5.place (x = 0, y = 30)
                Frame_5.config(width="350", height="60", bg = "gray25")              

                label = Label (Frame_5, text = u'TicTacToe\u207F', font = "Arial 32 bold", bg = "gray25", fg = 'white')
                label.place(x = 60, y = 5)

                # Datos del usuario
                Label1 = Label(Frame_4, text="Jugador 1:", bg = "slate blue", font = "Arial 10 bold")
                Label1.place (x=100, y=180)
                Label2 = Label(Frame_4, text="Jugador 2:", bg = "slate blue", font = "Arial 10 bold")
                Label2.place (x=100, y=210)
                Label3 = Label(Frame_4, text="Tamaño del tablero:", bg = "slate blue", font = "Arial 10 bold")
                Label3.place (x=40, y=240)
                Label4 = Label(Frame_4, text="Datos de la partida", bg = "slate blue", font = "Arial 13 bold")
                Label4.place (x=100, y=140)
                
                self.user1 = StringVar()        
                self.user2 = StringVar()                
                self.N = StringVar()

                user1_entry = Entry(Frame_4)
                user1_entry.place (x=190, y=180)

                user2_entry = Entry(Frame_4)
                user2_entry.place (x=190, y=210)

                N_entry = Entry(Frame_4)
                N_entry.place (x=190, y=240)

                
                def entero():
                        self.N = int(N_entry.get())
                        self.user1 = user1_entry.get()
                        self.user2 = user2_entry.get()

                        def savefile(text1, text2, text3):                     
                                save_text = open("save.txt", 'a+')
                                save_text.write(text1)
                                save_text.write("\n")
                                save_text.write(text2)
                                save_text.write("\n")
                                save_text.write(text3)
                                save_text.close()                                           
                        
                        if (self.N > 1 and len(self.user1) > 0 and len(self.user1) > 0):                                
                                tkinter.messagebox.showinfo("Validación", "Los datos han sido validados.")                                
                                self.after(1, controller.mostrar_ventana(Tablero))                                
                                savefile(N_entry.get(), user1_entry.get(), user2_entry.get())
                                return True
                        else:
                                tkinter.messagebox.showwarning("Datos erróneos", "El tamaño del tablero debe ser mayor a 1 y los nombres deben contener al menos un caracter.")
                                user1_entry.delete(0,END)
                                user2_entry.delete(0,END)
                                N_entry.delete(0,END)
                                return False
    
                def Salir ():
                        ok = tkinter.messagebox.askokcancel("Salir", "¿Desea salir del juego? Nota: No se guardará la partida.")
                        if (ok == True):                                                      
                                self.quit()

                # Botones (User)                                       
                Validar = Button(Frame_4, text='Validar', font = "Arial 14 bold", width = 7, height = 1, bg = "light steel blue", fg = 'gray10', relief = RAISED, command = entero)
                Validar.place(x = 15, y =305)            
 
                Volver = Button(Frame_4, text='Volver', font = "Arial 14 bold", width = 7, height = 1, bg = "light steel blue", fg = 'gray10', relief = RAISED, command = lambda : controller.mostrar_ventana(Principal))
                Volver.place(x = 127, y =305)               

                salir = Button(Frame_4, text='Salir', font = "Arial 14 bold", width = 7, height = 1, bg = "light steel blue", fg = 'gray10', relief = RAISED, command = Salir)
                salir.place(x = 237, y = 305)


class Reglas (Frame):
        def __init__ (self, parent, controller):
                Frame.__init__ (self, parent)
                self.controller=controller                                             

                self.config (bg = "midnight blue")

                # Frame 1 (Reglas)
                Frame_1 = Frame(self)
                Frame_1.pack()
                Frame_1.place (x = 300, y = 60)
                Frame_1.config(width="380", height="430", bg = "blue4")

                # Frame 2 (Reglas)
                Frame_2 = Frame(Frame_1)
                Frame_2.pack()
                Frame_2.place (x = 5, y = 5)
                Frame_2.config(width="370", height="420", bg = "navy")

                # Frame 3 (Reglas)
                Frame_3 = Frame(Frame_2)
                Frame_3.pack()
                Frame_3.place (x = 5, y = 5)
                Frame_3.config(width="360", height="410", bg = "RoyalBlue4")

                # Frame 4 (Reglas)
                Frame_4 = Frame(Frame_3)
                Frame_4.pack()
                Frame_4.place (x = 5, y = 5)
                Frame_4.config(width="350", height="400", bg = "black")              

                label = Label (Frame_4, text = "Reglas", font = "Arial 30 bold", bg = "black", fg = 'white')
                label.place(x = 110, y = 40)

                # Texto (Reglas)
                text1 = Text(Frame_4)
                text1.pack()
                text1.place(x = 5, y = 110)
                text1.config (bg = "black", fg = 'white', font = "Arial 9 bold", height = "30", width = "48", relief = FLAT)
                text1.insert(INSERT, "  1. Los puntos se obtienen marcando lineas con" )
                text1.insert(INSERT, " fichas de un mismo usuario;  en un tablero,")
                text1.insert(INSERT, "  esto se logra con lineas   verticales,  horizontales y diagonales,")
                text1.insert(INSERT, "  mientras que entre    tableros, con pilares.")
                text1.insert(INSERT, "                                                                                                                                                                                          " )
                text1.insert(INSERT, "  2. El mínimo y máximo de jugadores por partida son dos.")
                text1.insert(INSERT, "                                                                                                                    ")
                text1.insert(INSERT, "  3. Gana quien tenga más puntos.")            

                # Botones (Reglas)
                Volver = Button(Frame_4, text='Volver', font = "Arial 14 bold", width = 7, height = 1, bg = "light steel blue", fg = 'gray10', relief = RAISED, command = lambda : controller.mostrar_ventana(Principal))
                Volver.place(x = 130, y =305)

 
class Tablero (Frame):
        def __init__ (self, parent, controller):
                Frame.__init__ (self, parent)
                self.controller=controller
                                                          

                self.config (bg = "black")
                
                # Frame 0 (Tablero)
                Frame_0 = Frame(self)
                Frame_0.pack()
                Frame_0.place (x = 0, y = 0)
                Frame_0.config(width="1000", height="600", bg = "DodgerBlue4")

                # Frame_text (Tablero)
                Frame_text = Frame(Frame_0)
                Frame_text.pack()
                Frame_text.place (x = 300, y = 60)
                Frame_text.config(width="380", height="430", bg = "slate blue")

                # Frame 5 (Tablero)
                Frame_text2 = Frame(Frame_text)
                Frame_text2.pack()
                Frame_text2.place (x = 0, y = 30)
                Frame_text2.config(width="380", height="60", bg = "gray25")              

                label = Label (Frame_text2, text =  u'TicTacToe\u207F', font = "Arial 32 bold", bg = "gray25", fg = 'white')
                label.place(x = 65, y = 10)                
                
                text2 = Text(Frame_text)
                text2.pack()
                text2.place(x = 5, y = 130)
                text2.config (bg = "slate blue", fg = 'gray17', font = "Arial 12 bold", height = "30", width = "48", relief = FLAT)                
                text2.insert(INSERT, "            Ahora que los datos han sido validados, \n")
                text2.insert(INSERT, "  ¡Es hora de decidir al ganador! , si están listos \n")
                text2.insert(INSERT, "  presionen EMPEZAR. \n")
                text2.insert(INSERT, "  \n  WARNING: Una pieza mal colocada y podrías  \n")
                text2.insert(INSERT, "  perder. Piensa bien antes de jugar. \n")                  

                # Métodos

                def Empezar ():                                                                     

                        # Abrir archivo que contiene los datos de los usuarios y mostrarlos en pantalla
                        with open ("save.txt", "r") as data:
                                lines = data.readlines()                                                                         
                        data.close()

                        # Data
                        N = int (lines[0])                                              
                        T = [[[0 for col in range(0,N)] for row in range(0,N)] for tab in range (0,N)]

                        # Eliminar 
                        Frame_0.destroy()
                        Empezar.destroy()

                        # Frame 1 (Tablero)
                        Frame_1 = Frame(self)
                        Frame_1.pack()
                        Frame_1.place (x = 0, y = 0)
                        Frame_1.config(width="280", height="600", bg = "medium purple")

                        # Frame 2 (Tablero)
                        Frame_2 = Frame(self)
                        Frame_2.pack()
                        Frame_2.place (x = 280, y = 0)
                        Frame_2.config(width="720", height= "600", bg = "white")

                        # Frame 3 (Tablero)                        
                        Frame_3 = Frame(self)
                        Frame_3.pack()
                        Frame_3.place (x = 0, y = 0)
                        Frame_3.config(width="280", height="60", bg = "black")

                        # Frame 4 (Tablero)
                        Frame_4 = Frame(self)
                        Frame_4.pack()
                        Frame_4.place (x = 0, y = 120)
                        Frame_4.config(width="280", height="40", bg = "gray20")

                        # Frame 5 (Tablero)
                        Frame_5 = Frame(self)
                        Frame_5.pack()
                        Frame_5.place (x = 0, y = 200)
                        Frame_5.config(width="280", height="40", bg = "gray20")                        

                        Usuario1 = Label (Frame_4, text = lines[1], font = "Arial 13 bold", bg = "gray20", fg = 'white')
                        Usuario1.place(x = 0, y = 10)

                        Usuario2 = Label (Frame_5, text = lines[2], font = "Arial 13 bold", bg = "gray20", fg = 'white')
                        Usuario2.place(x = 0, y = 10)

                        # Labels/output 
                        label1 = Label (Frame_3, text = "Datos de la partida", font = "Arial 15 bold", bg = "black", fg = 'white')
                        label1.place(x = 30, y = 15)                                                   

                        label2 = Label (Frame_1, text = "Puntos:", font = "Arial 12 bold", bg = "medium purple", fg = 'black')
                        label2.place(x = 50, y = 170)                               

                        label3 = Label (Frame_1, text = "Puntos:", font = "Arial 12 bold", bg = "medium purple", fg = 'black')
                        label3.place(x = 50, y = 250)

                        label4 = Label (Frame_1, text = "Turno:", font = "Arial 14 bold", bg = "medium purple", fg = 'black')
                        label4.place(x = 20, y = 300)                                               

                        # Scrollbar                                                
                        canvas1 = Canvas(Frame_2, bg ='Skyblue3', width = "700", height = "600")                        
                        vbar = Scrollbar(Frame_2, orient = VERTICAL)
                        vbar.pack(side = RIGHT, expand = False, fill = Y)
                        vbar.config(command = canvas1.yview)                        
                        canvas1.config(width = "700", height = "600", yscrollcommand = vbar.set, scrollregion = (0,0,0, 455*N))                        
                        canvas1.pack(side=LEFT, expand=True, fill=BOTH)                                                

                        # Crear tablero
                        for k in range (0, N):
                                canvas1.create_text(350, 30 + (450*k), text = "Tablero " + str(k), font = "Arial 12 bold", fill= 'black')
                                canvas1.create_rectangle(150, 50 + (450*k), 550, 450 + (450*k), fill='LightGoldenrod3')

                        #-----------------Crear N-1 lineas *N Casillas ----------------#
                                
                        for k in range (0, N):                            
                            xo, x, yo, y = 150, 550, (50 + (450*k)), 450 + (450*k)
                            for i in range(0,N+1):
                                canvas1.create_line(xo, (y-yo)*(i)//N + (50 + 450*k), x, (y-yo)*(i)//N +(50+450*k), width=2, fill='black')
                                canvas1.create_line((x-xo)*i//N + 150, yo, (x-xo)*i//N + 150, y, width=2, fill='black')

                        
                        # Mostrar turno inicial
                        if turno == 1:
                                name = lines[1]                                            
                                Turno = Label (Frame_1, text = name, font = "Arial 13 bold", bg = "medium purple", fg = 'black')
                                Turno.place(x = 40, y = 330)
                        elif turno == 2:
                                name = lines[2]                                            
                                Turno = Label (Frame_1, text = name, font = "Arial 13 bold", bg = "medium purple", fg = 'black')
                                Turno.place(x = 40, y = 330)


                        # Action por click                                              
                        
                        def getorigin(evt):                                
                                global turno
                                global jugadas, Puntos1, Puntos2
            
                                clicky, clickx = canvas1.canvasx(evt.x), canvas1.canvasy(evt.y)                                 
                                        
                                dentro_tablero = False
                                m, n, l = 0, 0, 0                               


                                while m < N and (dentro_tablero == False):
                                        if 150 < clicky < 550 and (50 + (450*m)) < clickx < (450 + 450 *m):
                                                dentro_tablero = True
                                                tablero = m                                                
                                        m = m + 1                               

                                if dentro_tablero:                                                
                                        while n < N:
                                                if (150 + (n*(400//N))) < clicky <= (150 + ((n+1)*(400//N))):                                                        
                                                        while l < N:
                                                                if (50 +  (450*tablero) + (400//N)*l) < clickx <= (50 +  (450*tablero) + (400//N)*(l+1)):
                                                                        x, y, z = l, n, tablero

                                                                        if EsValida (T, x, y, z, N):
                                                                                T[x][y][z] = turno                                                                        

                                                                                if turno == 1:
                                                                                        posx1 = 150 + (n*(400//N)) + (0.35 *n)
                                                                                        posx2 = 150 + ((n+1)*(400//N)) + (0.35 *n)
                                                                                        posy1 = 50 + (450*tablero) + (400//N)*(l) 
                                                                                        posy2 = 50 + (450*tablero) + (400//N)*(l+1)                                                                        
                                                                                        canvas1.create_oval(posx1, posy1, posx2, posy2, width = (N//2), fill='blue')
                                                                                elif turno == 2:
                                                                                        posx1 = 150 + (n*(400//N)) + (0.35 *n)
                                                                                        posx2 = 150 + ((n+1)*(400//N)) + (0.35 *n)
                                                                                        posy1 = 50 + (450*tablero) + (400//N)*(l) 
                                                                                        posy2 = 50 + (450*tablero) + (400//N)*(l+1)                                                                        
                                                                                        canvas1.create_oval(posx1, posy1, posx2, posy2, width = (N//2), fill='red')

                                                                                # Buscar lineas y sumar puntos.
                                                                                
                                                                                if HayAlineaHorizontal (T, x, z, N):
                                                                                        Puntos1, Puntos2 = SumarLinea (turno, Puntos1, Puntos2)
                                                                                        canvas1.create_line(150 + (400//(2*N)), 50 +  (450*tablero) + (400//(2*N)) + (l*(400//N)), 550 - (400//(2*N)), 50 +  (450*tablero) + (400//(2*N)) + (l*(400//N)), width=2, fill='black')
                                                                                        
    
                                                                                if HayAlineaVertical (T, y, z, N):
                                                                                        Puntos1, Puntos2 = SumarLinea (turno, Puntos1, Puntos2)
                                                                                        canvas1.create_line(150 + (400//(2*N)) + (n*(400//N)), 50 +  (450*tablero) + (400//(2*N)), 150 + (400//(2*N)) + (n*(400//N)), 450 +  (450*tablero) - (400//(2*N)), width=2, fill='black')                                                                                     

                                                                                HayDiagonalP, HayDiagonalS = HayAlineaDiag (T, x, y, z, N)
                                                                                                
                                                                                if HayDiagonalP:
                                                                                        Puntos1, Puntos2 = SumarLinea (turno, Puntos1, Puntos2)
                                                                                        canvas1.create_line(150 + (400//(2*N)), 50 +  (450*tablero) + (400//(2*N)), 550 - (400//(2*N)), 450 +  (450*tablero) - (400//(2*N)), width=2, fill='black')

                                                                                if HayDiagonalS:
                                                                                        Puntos1, Puntos2 = SumarLinea (turno, Puntos1, Puntos2)
                                                                                        canvas1.create_line(550 - (400//(2*N)), 50 +  (450*tablero) + (400//(2*N)), 150 + (400//(2*N)), 450 +  (450*tablero) - (400//(2*N)), width=2, fill='black')
                                                                                                
                                                                                if HayAlineaTableros (T, x, y, N):
                                                                                        Puntos1, Puntos2 = SumarLinea (turno, Puntos1, Puntos2)                                                                                
                                                                                
                                                                                # Cambiar de jugador 
                                                                                turno = CambiarJugador (turno)                                                                                

                                                                                # Abrir archivo que contiene los datos de los usuarios y mostrarlos en pantalla
                                                                                with open ("save.txt", "r") as data:
                                                                                        liness = data.readlines()                                                                         
                                                                                data.close()

                                                                                if turno == 1:
                                                                                        Frame_aux = Frame(self)
                                                                                        Frame_aux.pack()
                                                                                        Frame_aux.place (x = 0, y = 330)
                                                                                        Frame_aux.config(width="280", height="50", bg = "medium purple")

                                                                                        name = liness[1]                                                                                
                                                                                        Turno = Label (Frame_aux, text = name, font = "Arial 13 bold", bg = "medium purple", fg = 'black')
                                                                                        Turno.place(x = 40, y = 0)
                                                                                elif turno == 2:
                                                                                        Frame_aux = Frame(self)
                                                                                        Frame_aux.pack()
                                                                                        Frame_aux.place (x = 0, y = 330)
                                                                                        Frame_aux.config(width="280", height="50", bg = "medium purple")

                                                                                        name = liness[2]                                                                                
                                                                                        Turno = Label (Frame_aux, text = name, font = "Arial 13 bold", bg = "medium purple", fg = 'black')
                                                                                        Turno.place(x = 40, y = 0)
                                                                                
                                                                                # Mostrar Puntos
                                                                                Frame_aux2 = Frame(Frame_1)
                                                                                Frame_aux2.pack()
                                                                                Frame_aux2.place (x = 120, y = 170)
                                                                                Frame_aux2.config(width="280", height="50", bg = "medium purple")
                                                                                Punto1 = Label (Frame_aux2, text = str(Puntos1), font = "Arial 13 bold", bg = "medium purple", fg = 'black')
                                                                                Punto1.place(x = 0, y = 0)

                                                                                Frame_aux3 = Frame(Frame_1)
                                                                                Frame_aux3.pack()
                                                                                Frame_aux3.place (x = 120, y = 250)
                                                                                Frame_aux3.config(width="280", height="50", bg = "medium purple")                           
                                                                                Punto2 = Label (Frame_aux3, text = str(Puntos2), font = "Arial 13 bold", bg = "medium purple", fg = 'black')
                                                                                Punto2.place(x = 0, y = 0)

                                                                                jugadas = jugadas + 1
                                                                        else:
                                                                                tkinter.messagebox.showinfo("Inválido", "La jugada no es válida")
                                                                        
                                                                        if Quedan_fichas (N, jugadas) == 0:
                                                                                if Puntos1 > Puntos2:
                                                                                        tkinter.messagebox.showinfo("Fin de la partida", lines[1] + " has ganado. " + lines[2] + " claramente eres el perdedor.")                                                                                        
                                                                                elif Puntos1 < Puntos2:
                                                                                        tkinter.messagebox.showinfo("Fin de la partida", lines[2] + " has ganado. " + lines[1] +  " claramente eres el perdedor.")                                                                                        
                                                                                else:
                                                                                        tkinter.messagebox.showinfo("Fin de la partida", " Han empatado, que aburridos son.")
                                                                                        
                                                                                
                                                                                Puntos1, Puntos2 = 0, 0
                                                                                os.remove("save.txt")                                                                                                                                                                                                                                                                      
                                                                                python = sys.executable
                                                                                os.execl(python, python, *sys.argv)
                                                                                

                                                                l = l + 1

                                                n = n + 1                                       
                        
                        
                        canvas1.bind("<Button-1>", getorigin)                                               
                

                # Acciones (Frame 3)                               

                Empezar = Button(Frame_0, text='Empezar', font = "Arial 14 bold", width = 7, height = 1, bg = "light steel blue", fg = 'gray10', relief = RAISED, command = Empezar)            
                Empezar.place(x = 445, y = 400)                            


# Métodos (main)
def on_closing():
        if tkinter.messagebox.askokcancel("Salir", "¿Desea salir?" + "\n" + "No se guardará la partida"):
                if os.path.exists('save.txt'):                        
                        os.remove("save.txt")                                              
                main.destroy()


#--------------------------------------Variables iniciales a cualquier partida-------------------------------------------#
turno = random.randrange(1,3)
jugadas, Puntos1, Puntos2 = 0, 0, 0

#-----------------------------------------------Ventana Principal---------------------------------------------------------#
main = Application()

# Título de las ventanas
main.title(u'TicTacToe\u207F')

# Tamaño
main.geometry("1000x600")
main.resizable(0,0)

# Icono
main.iconbitmap("tic_tac_toe.ico")

# Protocolo de cierre
main.protocol("WM_DELETE_WINDOW", on_closing)

main.mainloop()