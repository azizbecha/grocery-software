#Importing Libs

import mysql.connector

import tkinter as tk
from tkinter import * 
import tkinter
from tkinter import messagebox
import tkinter.ttk as ttk

from PIL import ImageTk,Image
from functools import partial

import datetime
from datetime import date
from datetime import datetime

from math import *

root = Tk()

root.geometry("1600x1370")
root.title("Grocery")

screen = StringVar()
screen.set("0")

current = ""
power = ""

firstnum = str()
secondnum = str()
mathsign = str()
defxworking = False
percentt = False

my_connect = mysql.connector.connect(
  host="localhost",
  user="root", 
  passwd="",
  database="grossiste"
)

my_conn = my_connect.cursor()
my_conn.execute("SELECT * FROM produits ORDER BY produit_id DESC")

e=Label(root,width=17,text='ID',borderwidth=1, relief='ridge',anchor='w',bg='#0066ff',fg="white",font=("Arial", 17))
e.grid(row=3,column=0)

e=Label(root,width=17,text='Name',borderwidth=1, relief='ridge',anchor='w',bg='#0066ff',fg="white",font=("Arial", 17))
e.grid(row=3,column=1)

e=Label(root,width=17,text='Description',borderwidth=1, relief='ridge',anchor='w',bg='#0066ff',fg="white",font=("Arial", 17))
e.grid(row=3,column=2)

e=Label(root,width=17,text='Quantity',borderwidth=1, relief='ridge',anchor='w',bg='#0066ff',fg="white",font=("Arial", 17))
e.grid(row=3,column=3)

e=Label(root,width=17,text="Add date",borderwidth=1, relief='ridge',anchor='w',bg='#0066ff',fg="white",font=("Arial", 17))
e.grid(row=3,column=4)

e=Label(root,width=17,text='Price',borderwidth=1, relief='ridge',anchor='w',bg='#0066ff',fg="white",font=("Arial", 17))
e.grid(row=3,column=5)

i=4

now = datetime.now().time()

for product in my_conn: 
    for j in range(len(product)):
        e = Entry(root, width=17,borderwidth=1, fg='black',relief="ridge",font=("Arial", 18)) 
        e.grid(row=i, column=j) 
        e.insert(END, product[j]) 
    i=i+1

def clock():
    time = datetime.now().strftime("%H:%M:%S")
    Label(root, text=date.today(),font=("Arial", 18),fg="black").grid(row=0,column=6)
    lab = Label(root,text=time,font=("Arial", 18),fg="black",pady=0).grid(row=0,column=0) 
    root.after(500, clock)

clock()


input_product_name = tk.StringVar(root) 
input_product_description = tk.StringVar(root)                 
input_product_quantity = tk.StringVar(root)                
input_product_price = tk.StringVar(root) 

#Add product function
def ajouter():
    main=Toplevel(root)
    main.geometry('260x300')
    main.maxsize(width = 260,height = 300)
    main.minsize(width = 260,height = 300)
    main.title("Ajouter Un Produit")
    def ajouterProduit():
        productname = input_product_name.get()
        productdesc = input_product_description.get()
        productquanttity = input_product_quantity.get()
        productprice = input_product_price.get()
        my_conn.execute("INSERT INTO produits (nom, description, quantite, prix) VALUES ('"+productname+"','"+productdesc+"','"+productquanttity+"','"+productprice+"' )")
        main.destroy()

    text=DoubleVar()
    text2=DoubleVar()
    var=StringVar()
    Label(main, text="Nom Du Produit",font=("Arial", 12)).grid(column=0,row=1)
    Entry(main, textvariable=input_product_name,width=40).grid(column=0, row=2,ipady=4)
    Label(main, text="Description Du Produit",font=("Arial", 12)).grid(column=0,row=3,ipady=4)
    Entry(main, textvariable=input_product_description,width=40).grid(column=0, row=4,ipady=4)
    Label(main, text="Quantité",font=("Arial", 12)).grid(column=0,row=5,ipady=4)
    Entry(main, textvariable=input_product_quantity,width=40).grid(column=0, row=6,ipady=4)
    Label(main, text="Prix",font=("Arial", 12)).grid(column=0,row=7,ipady=4)
    Entry(main, textvariable=input_product_price,width=40).grid(column=0, row=8,ipady=4)
    Label(main, textvariable=var).grid(column=2, row=9,ipady=4)
    Button(main, text="Button", command=ajouterProduit,bg="#00b33c",fg="white",width="27",height="2",).grid(column=0, row=10, columnspan=2)

#Search function (missing some improvements)
def rechercher():
    main=Toplevel(root)
    main.geometry('260x300')
    main.title("Search")
    def rechercherProduit():
        productname = input_product_name.get()
        my_conn.execute("SELECT * FROM produits WHERE nom OR description LIKE '%"+productname+"%'")
        main.destroy()
        
    text=DoubleVar()
    text2=DoubleVar()
    var=StringVar()
    Label(main, text="Nom Du Produit",font=("Arial", 12)).grid(column=0,row=1)
    Entry(main, textvariable=input_product_name,width=40).grid(column=0, row=2,ipady=4)
    Button(main, text="Button", command=rechercherProduit,bg="#00b33c",fg="white",width="27",height="2",).grid(column=0, row=3, columnspan=2)

#Delete product function    
def supprimer():
    main=Toplevel(root)
    main.geometry('260x300')
    main.maxsize(width = 260,height = 300)
    main.minsize(width = 260,height = 300)    
    main.title("Delete Product")
    def supprimerProduit():
        productname = input_product_name.get()
        my_conn.execute("DELETE FROM produits WHERE nom = '"+productname+"'")

    text=DoubleVar()
    text2=DoubleVar()
    var=StringVar()
    Label(main, text="Nom Du Produit",font=("Arial", 12)).grid(column=0,row=1)
    Entry(main, textvariable=input_product_name,width=40).grid(column=0, row=2,ipady=4)

    Button(main, text="Button", command=supprimerProduit,bg="#00b33c",fg="white",width="27",height="2",).grid(column=0, row=3, columnspan=2)
    
#Sell product function
def vendre():
    main=Toplevel(root)
    main.geometry('260x300')
    main.maxsize(width = 260,height = 300)
    main.minsize(width = 260,height = 300)    
    main.title("Sell Produit")
    def vendreProduit():
        quantity = input_product_quantity.get()
        name = input_product_name.get()
        my_conn.execute("UPDATE produits SET quantite = quantite - '"+quantity+"' WHERE nom = '"+name+"' ")
        main.destroy()

    text=DoubleVar()
    text2=DoubleVar()
    var=StringVar()
    Label(main, text="Product Name",font=("Arial", 12)).grid(column=0,row=1)
    Entry(main, textvariable=input_product_name,width=40).grid(column=0, row=2,ipady=4)
    Label(main, text="Quantity",font=("Arial", 12)).grid(column=0,row=3)
    Entry(main, textvariable=input_product_quantity,width=40).grid(column=0, row=4,ipady=4)

    Button(main, text="Button", command=vendreProduit,bg="#00b33c",fg="white",width="27",height="2",).grid(column=0, row=5, columnspan=2)

#Calculator
def Calculatrice():
    main=Toplevel(root)
    main.geometry('210x300')
    main.maxsize(width = 210,height = 300)
    main.minsize(width = 210,height = 300)    
    main.title("Calculator")    
    def math_button_pressed():
        if mathsign == '+':
            button_plus.config(relief=SUNKEN)
        if mathsign == '-':
            button_minus.config(relief=SUNKEN)
        if mathsign == '*':
           button_multiply.config(relief=SUNKEN)
        if mathsign == '/':
            button_division.config(relief=SUNKEN)

    def math_button_raised():
        button_plus.config(relief=RAISED)
        button_minus.config(relief=RAISED)
        button_multiply.config(relief=RAISED)
        button_division.config(relief=RAISED)

    def is_int(num):
        if int(num) == float(num):
           return int(num)
        else:
            return float(num)

    def number_pressed(butt):
        global current, power, firstnum, secondnum

        if mathsign == str() and defxworking == False:
            current = current + str(butt)
            screen.set(current)
            firstnum = float(current)

        elif mathsign != str() and defxworking == False:
            math_button_raised()
            current = current + str(butt)
            screen.set(current)
            secondnum = float(current)

        elif mathsign == str() and defxworking == True:
            power = power + str(butt)
            current = current + str(butt)
            screen.set(current)

        elif mathsign != str and defxworking == True:
            power = power + str(butt)
            current = current + str(butt)
            screen.set(current)
            print(power)

    def math_pressed(math):
        global current, power, mathsign, firstnum, secondnum, defxworking, percentt

        if mathsign == str() and defxworking == False and percentt == False and firstnum != str():
            mathsign = str(math)
            math_button_pressed()
            current = ""

        elif mathsign != str() and defxworking == False and percentt == False:
            print(2)
            if mathsign == '+':
                firstnum = round(float(firstnum + secondnum),6)
            if mathsign == '-':
                firstnum = round(float(firstnum - secondnum),6)
            if mathsign == '*':
                firstnum = round(float(firstnum * secondnum),6)
            if mathsign == '/':
                firstnum = round(float(firstnum / secondnum),6)
            screen.set(is_int(firstnum))

            mathsign = str(math)
            math_button_pressed()
            current = ""

        elif mathsign != str() and defxworking == True and percentt == False:
            if mathsign == '+':
                firstnum = round(firstnum + secondnum ** int(power),6)
            if mathsign == '-':
                firstnum = round(firstnum - secondnum ** int(power),6)
            if mathsign == '*':
                firstnum = round(firstnum * (secondnum ** int(power)),6)
            if mathsign == '/':
                firstnum = round(firstnum / (secondnum ** int(power)),6)
            defxworking = False
            screen.set(is_int(firstnum))
            defxworking = False
            mathsign = str(math)
            math_button_pressed()
            power = ""
            current = ""

        elif defxworking and percentt == False:
            firstnum = round(firstnum ** int(power), 6)
            defxworking = False
            screen.set(is_int(firstnum))
            mathsign = str(math)
            math_button_pressed()
            power = ""
            current = ""

        elif percentt:
            if mathsign == '+':
                firstnum = round(float(firstnum + firstnum/100*secondnum),6)
            if mathsign == '-':
                firstnum = round(float(firstnum - firstnum/100*secondnum),6)
            screen.set(is_int(firstnum))
            percentt = False
            mathsign = str(math)
            math_button_pressed()
            current = ""

    def squareroot():
        global firstnum, secondnum, mathsign, current

        if mathsign == str():
            firstnum = round(sqrt(firstnum),6)
            screen.set(is_int(firstnum))

        if mathsign != str():
            if mathsign == '+':
                firstnum = round(sqrt(firstnum + float(secondnum)),6)
            if mathsign == '-':
                firstnum = round(sqrt(firstnum - float(secondnum)),6)
            if mathsign == '*':
                firstnum = round(sqrt(firstnum * float(secondnum)),6)
            if mathsign == '/':
                firstnum = round(sqrt(firstnum / float(secondnum)),6)

            screen.set(is_int(firstnum))
            secondnum = str()
            mathsign = str()
            current = ""

    def x():
        global firstnum, secondnum, mathsign, current, defxworking

        if mathsign == str():
            current = str(is_int(firstnum)) + '^'
            screen.set(current)
            defxworking = True

        elif mathsign != str():

            current = str(is_int(secondnum)) + '^'
            screen.set(current)
            defxworking = True

    def result():
        global firstnum, secondnum, mathsign, current, power, defxworking, percentt
        if defxworking == False and percentt == False:
            if mathsign == '+':
                firstnum = round(float(firstnum + secondnum),6)
            if mathsign == '-':
                firstnum = round(float(firstnum - secondnum),6)
            if mathsign == '*':
                firstnum = round(float(firstnum * secondnum),6)
            if mathsign == '/':
                firstnum = round(float(firstnum / secondnum),6)
            screen.set(is_int(firstnum))

        if mathsign == str() and defxworking == True and percentt == False:
            firstnum = round(firstnum ** int(power),6)
            defxworking = False
            screen.set(is_int(firstnum))

        if mathsign != str() and defxworking == True and percentt == False:
            if mathsign == '+':
                firstnum = round(firstnum + secondnum ** int(power),6)
                defxworking = False
            if mathsign == '-':
                firstnum = round(firstnum - secondnum ** int(power),6)
                defxworking = False
            if mathsign == '*':
                firstnum = round(firstnum * (secondnum ** int(power)),6)
                defxworking = False
            if mathsign == '/':
                firstnum = round(firstnum / (secondnum ** int(power)),6)
                defxworking = False
            screen.set(is_int(firstnum))


        if defxworking == False and percentt == True:
            if mathsign == '+':
                firstnum = round(float(firstnum + firstnum/100*secondnum),6)
                screen.set(is_int(firstnum))
                percentt = False
            if mathsign == '-':
                firstnum = round(float(firstnum - firstnum/100*secondnum),6)
                screen.set(is_int(firstnum))
                percentt = False

        mathsign = str()
        current = ""
        power = ""

        if defxworking == False and mathsign == '*' or '/' and percentt == True:
            clear()

    def clear():
        global current, firstnum, secondnum, mathsign, power, defxworking, percentt

        screen.set(0)
        current = ""
        power = ""
        firstnum = str()
        secondnum = str()
        mathsign = str()
        defxworking = False
        math_button_raised()
        percentt = False

    def percent():
        global firstnum, secondnum, current, percentt

        current = str(is_int(secondnum)) + '%'
        screen.set(current)
        percentt = True

    calculation = Entry(main, textvariable = screen, font=("Verdana", 15, ), bd = 12,
                        insertwidth=4, width=14, justify=RIGHT)
    calculation.grid(columnspan=4)
#   Numbers
    button1 = Button(main, text='1', command=lambda: number_pressed(1), bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
    button1.grid(row=2, column=0, sticky=W)
    button2 = Button(main, text='2', command=lambda: number_pressed(2), bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
    button2.grid(row=2, column=1, sticky=W)
    button3 = Button(main, text='3', command=lambda: number_pressed(3), bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
    button3.grid(row=2, column=2, sticky=W)
    button4 = Button(main, text='4', command=lambda: number_pressed(4), bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
    button4.grid(row=3, column=0, sticky=W)
    button5 = Button(main, text='5', command=lambda: number_pressed(5), bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
    button5.grid(row=3, column=1, sticky=W)
    button6 = Button(main, text='6', command=lambda: number_pressed(6), bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
    button6.grid(row=3, column=2, sticky=W)
    button7 = Button(main, text='7', command=lambda: number_pressed(7), bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
    button7.grid(row=4, column=0, sticky=W)
    button8 = Button(main, text='8', command=lambda: number_pressed(8), bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
    button8.grid(row=4, column=1, sticky=W)
    button9 = Button(main, text='9', command=lambda: number_pressed(9), bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
    button9.grid(row=4, column=2, sticky=W)
    button0 = Button(main, text='0', command=lambda: number_pressed(0), bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
    button0.grid(row=5, column=0, sticky=W)
    button_float = Button(main, text='.', command=lambda: number_pressed('.'), bg="gainsboro",
                      bd=3, padx=15, pady=5, font=("Helvetica", 14, "bold"))
    button_float.grid(row=5, column=1)

#   Math signs
    button_plus = Button(main, text='+', command=lambda: math_pressed('+'), bg="gray70",
                     bd=3, padx=11, pady=5, font=("Helvetica", 14, "bold"))
    button_plus.grid(row=2, column=3, sticky=W)
    button_minus = Button(main, text='-', command=lambda: math_pressed('-'),  bg="gray70",
                      bd=3, padx=11, pady=4, font=("Verdana", 14, "bold"))
    button_minus.grid(row=3, column=3, sticky=W)
    button_multiply = Button(main, text='*', command=lambda: math_pressed('*'), bg="gray70",
                         bd=3, padx=13, pady=5, font=("Helvetica", 14, "bold"))
    button_multiply.grid(row=4, column=3, )
    button_division = Button(main, text='/', command=lambda: math_pressed('/'),  bg="gray70",
                         bd=3, padx=14, pady=5, font=("Helvetica", 14, "bold"))
    button_division.grid(row=5, column=3, )
    button_equal = Button(main, text='=', command=lambda: result(), bg='#00b33c',
                      bd=3, padx=12, pady=5, font=("Arial", 14))
    button_equal.grid(row=5, column=2, )

    button_percent = Button(main, text='%', command=lambda: percent(),  bg="gray70",
                         bd=3, padx=8, pady=5, font=("Helvetica", 14, "bold"))
    button_percent.grid(row=1, column=3, )

    button_clear = Button(main, text='C', command=lambda: clear(), bg='gray70',
                      bd=3, padx=11, pady=5, font=("Helvetica", 14))
    button_clear.grid(row=1, column=0)
    button_sqrt = Button(main, text='√', command=lambda: squareroot(), bg="gray70",
                        bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
    button_sqrt.grid(row=1, column=1, sticky=W)
    button_x = Button(main, text='x^y', command=lambda: x(), bg="gray70",
                  bd=3, padx=6, pady=5, font=("Helvetica", 14))
    button_x.grid(row=1, column=2, sticky=W)


BoutonAjouter = Button(root, text ="Ajouter",bg="#00b33c",fg="white",width="27",height="1",command = ajouter).grid(row=3,column=6,)
BoutonRechercher = Button(root, text ="Rechrecher",bg="#00b33c",fg="white",width="27",height="1", command=rechercher).grid(row=4,column=6)
BoutonSupprimer = Button(root, text ="Supprimer",bg="#00b33c",fg="white",width="27",height="1",command=supprimer).grid(row=5,column=6)
BoutonModifier = Button(root, text ="Modifier",bg="#00b33c",fg="white",width="27",height="1").grid(row=6,column=6)
BoutonVendre = Button(root, text ="Vendre",bg="#00b33c",fg="white",width="27",height="1",padx=1,command=vendre).grid(row=7,column=6)
BoutonCalculatrice = Button(root, text ="Calculatrice",bg="#00b33c",fg="white",width="27",height="1",command=Calculatrice,padx=1).grid(row=8,column=6)
BoutonExit = Button(root, text ="Sortir",bg="#00b33c",fg="white",width="27",height="1",padx=1,command=root.destroy).grid(row=9,column=6)

root.mainloop()
