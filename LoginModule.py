from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from tkcalendar.dateentry import DateEntry
from babel import dates
from babel import numbers



import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from joblib import dump, load
from tkinter import filedialog

def ChekckLogin():
    Name = txtName.get()
    from UserInterFace_Layer.MainFormModule import MainFormClass
    LoginFormObject.destroy()
    MainFormObject = MainFormClass()
    MainFormObject.MainFormLoad(Name)
LoginFormObject =Tk()

LoginFormObject.title('Login Form')
LoginFormObject.geometry('300x150')
LoginFormObject.iconbitmap('Image/Login.ico')
LoginFormObject.resizable(0,0)
X=int(LoginFormObject.winfo_screenwidth()/2 - 300/2)
Y=int(LoginFormObject.winfo_screenheight()/2 - 150/2)
LoginFormObject.geometry('+{}+{}'.format(X,Y))

lblName =Label(LoginFormObject,text='your Name :')
lblName.grid(row=0,column=0,padx=10,pady=10)

txtName=StringVar()
entName =ttk.Entry(LoginFormObject,width=30,textvariable=txtName)
entName.grid(row=0,column=1,padx=10,pady=10)

# lblPassword=Label(LoginFormObject,text='Password :')
# lblPassword.grid(row=1,column=0,padx=10,pady=10)

# txtPassword=StringVar()
# entPassword=ttk.Entry(LoginFormObject,width=30,textvariable=txtPassword,show='*')
# entPassword.grid(row=1,column=1,padx=10,pady=10)

BtnLoginCheck = Button(LoginFormObject,text='Login ',fg='red',font='Bold',command=ChekckLogin)
BtnLoginCheck.grid(row=2,column=1,padx=10,pady=10,sticky='e')

LoginFormObject.mainloop()