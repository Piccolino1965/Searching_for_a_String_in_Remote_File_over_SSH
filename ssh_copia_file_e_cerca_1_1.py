#! /usr/bin/python3
#:::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::www.aiutocomputerhelp.it::::::::::::::::::::::::::
#:::Cerco Stringa in un file remoto over ssh:::2019:::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::


import string
import os

#===================================
#import tkinter as tk #per finestra 
#===================================

from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import LabelFrame
from tkinter import Label
from tkinter import Button

#===============paramiko=================
import paramiko
#========================================

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
#==========================================

#piccola funzione che legge i record
#nel file e controlla presenza stringa

   

def leggo_valori():

    ssh.connect(Server.get(), username=Username.get(), password=Password.get()) 
    ftp = ssh.open_sftp()
    ftp.get(File_remoto.get(), File_locale.get())
    ftp.close()
        

    R_file= File_locale.get()
    Find1= Stringa.get()
 
    Record_letto = open(str(R_file), "r");  # creiamo il file objec
    Volte = 0
    txt_out.delete('1.0', END)

    for line in Record_letto:
        end=len(line);
        if ( (line.find(Find1)) > 1 ):
            #print (line)
            txt_out.insert(INSERT,line)
            Volte = Volte +1

    voltetotale = (str(Volte) + "________________Volte")
    messagebox.showinfo("Numero Occorrenze", voltetotale)
        
    Record_letto.close()

#FINE==leggo_valori=======================
    

finestra = Tk()
finestra.resizable(True,True)
finestra.title("www.aiutocomputerhelp.it Cerco Stringa in un file remoto over ssh")
finestra.geometry('1000x500')

 
rows = 0
while rows < 40:
    finestra.rowconfigure(rows, weight=1)
    finestra.columnconfigure(rows,weight=1)
    rows += 1



Input_step = LabelFrame(finestra,text="Parametri", font="Arial 12 bold italic")

Input_step.grid(row=1,column=1, columnspan=10 ,rowspan = 10, sticky='W', padx=1, pady=1, ipadx=1, ipady=1)


Label(Input_step, text="Server").grid(row=1, column=1)
Label(Input_step, text="Username").grid(row=2, column=1)
Label(Input_step, text="Password").grid(row=3, column=1)
Label(Input_step, text="File remoto").grid(row=4, column=1)
Label(Input_step, text="Nome file locale").grid(row=5, column=1)
Label(Input_step, text="Stringa da cercare").grid(row=6, column=1)

 
#input File Remoto
Server = Entry(Input_step, width=40)
Server.grid(row=1, column=20)

#imput Username
Username = Entry(Input_step,width=40)
Username.grid(row=2, column=20)

#imput Password
Password = Entry(Input_step,width=40)
Password.grid(row=3, column=20)

#imput File_remoto
File_remoto = Entry(Input_step,width=40)
File_remoto.grid(row=4, column=20)

#imput File_locale
File_locale = Entry(Input_step,width=40)
File_locale.grid(row=5, column=20)

#imput Stringa
Stringa = Entry(Input_step,width=40)
Stringa.grid(row=6, column=20)



#Tasto effettua ricerca
action_button = Button(Input_step)
action_button.configure(text='  Effettuo Trasferimento file / Ricerca valori  ', command=leggo_valori)
action_button.grid(row=10, column=20)




#testo
step = LabelFrame(finestra, text="Occorrenze nel file", font="Arial 10 bold italic")
step.grid(row=11, column = 1 ,columnspan=40, rowspan = 60,sticky='W', padx=1, pady=1, ipadx=10, ipady=5)

txt_out = scrolledtext.ScrolledText(step,width=160,height=13,font="Helvetica 8 bold")
txt_out.grid(row=1, column=1)
Label(step, text="Ed ora potete eseguirlo su Microsoft, Mac , Linux , Smartphone Android .... ").grid(row=2, column=1)

 
finestra.mainloop()
