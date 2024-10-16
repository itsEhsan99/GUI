from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as msg
import pandas as pd
import numpy as np
from joblib import dump, load
# from Abalone_Package.

class AbaloneFormClass:
    def AbaloneFormLoad(self):
        AbaloneFormObject = tk.Tk()
        AbaloneFormObject.title('year of Abalone Prediction Form')
        AbaloneFormObject.geometry('700x450')
        AbaloneFormObject.iconbitmap('Image/Abalone.ico')
        AbaloneFormObject.resizable(0, 0)
        X = int(AbaloneFormObject.winfo_screenwidth() / 2 - 700 / 2)
        Y = int(AbaloneFormObject.winfo_screenheight() / 2 - 450 / 2)
        AbaloneFormObject.geometry('+{}+{}'.format(X, Y))
        frame_right = tk.Frame(AbaloneFormObject, bg='#f2f2f2')
        frame_left = tk.Frame(AbaloneFormObject, bg='grey')
        frame_right.grid(row=0, column=1, sticky='WENS')
        frame_left.grid(row=0, column=0, rowspan=3, sticky='WENS')

        #
        def PredictReg():
            params=[float(valuesSex[textSex.get()]),float(txtLength.get()),float(txtDiameter.get())
                    ,float(txtHeight.get()),float(txtWWeight.get()),float(txtSWeight.get()),float(txtVWeight.get()),
                    float(txtShellWeight.get())]


            final_model = load("Abalone_Package/RegForAbandon2.joblib")
            mypredict=final_model.predict([params])
            # msg.showinfo("hello world","hello")
            msg.showinfo("our Prediction ", f" based on your info , \n your Abandon has { int(mypredict)} rings ")

        def ResetForm():
            for widget in AbaloneFormObject.winfo_children():
                if type(widget) == ttk.Entry:
                    widget.delete(0,END)

        def backToMainForm():
            from UserInterFace_Layer.MainFormModule import MainFormClass
            AbaloneFormObject.destroy()
            MainFormObject = MainFormClass()
            MainFormObject.MainFormLoad(" again dear ")
        # ----------------------

        # region Sex
        lblSex = Label(frame_left, background="light blue", text="     Sex     " )
        lblSex.grid(row=0, column=0, padx=2, pady=10, sticky="w")
        textSex = StringVar()
        valuesSex = {"Infant": 1, "Female": 2, "Male": 3}
        cmbSex = ttk.Combobox(frame_left, values=[key for key in valuesSex.keys()], textvariable=textSex,
                               state="readonly", width=15)
        cmbSex.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        cmbSex.current(0)
        lblLength3 = Label(frame_right, text='', fg="black")
        lblLength3.grid(row=0, column=0, padx=10, pady=10)
        # endregion



        # style = ttk.Style()
        # style.configure("TScale", background='grey')
        lblLength = Label(frame_left,background="light blue", text='    Length      ')
        lblLength.grid(row=1, column=0, padx=2, pady=10,sticky="w")
        txtLength = StringVar()
        entLength = ttk.Scale(frame_left, orient='horizontal', from_=0, to=1, length=250, variable=txtLength, style="TScale")
        entLength.set(0.5)
        entLength.grid(row=1, column=2, padx=2, pady=10)
        spLength = Spinbox(frame_left, textvariable=txtLength, width=5, from_=0, to=1)
        spLength.grid(row=1, column=1, padx=0, pady=10)

        lblLength2 = Label(frame_right, text='note: Longest shell measurement', fg="black")
        lblLength2.grid(row=1, column=0, padx=2, pady=10,sticky="w")

        # Diameter
        lblDiameter = Label(frame_left, text='     Dimeter     ',background="light blue")
        lblDiameter.grid(row=2, column=0, padx=2, pady=10,sticky="w")
        txtDiameter = StringVar()
        entDiameter = ttk.Scale(frame_left, orient='horizontal', from_=0, to=1, length=250, variable=txtDiameter,
                              style="TScale")
        entDiameter.set(0.5)
        entDiameter.grid(row=2, column=2, padx=2, pady=10)
        spDiameter = Spinbox(frame_left, textvariable=txtDiameter, width=5, from_=0, to=1)
        spDiameter.grid(row=2, column=1, padx=0, pady=10)

        dolblDiameter = Label(frame_right, text='note: perpendicular to length', fg="black")
        dolblDiameter.grid(row=2, column=0, padx=2, pady=10,sticky="w")


        # Height
        lblHeight = Label(frame_left, text='     Height     ',background="light blue")
        lblHeight.grid(row=3, column=0, padx=2, pady=10,sticky="w")
        txtHeight = StringVar()
        entHeight = ttk.Scale(frame_left, orient='horizontal', from_=0, to=2, length=250, variable=txtHeight,
                              style="TScale")
        entHeight.set(0.75)
        entHeight.grid(row=3, column=2, padx=2, pady=10)
        spHeight = Spinbox(frame_left, textvariable=txtHeight, width=5, from_=0, to=2)
        spHeight.grid(row=3, column=1, padx=0, pady=10)

        dolblHeight = Label(frame_right, text='note: with meat in shell', fg="black")
        dolblHeight.grid(row=3, column=0, padx=2, pady=10,sticky="w")


        # Whole_Weight
        lblWWeight = Label(frame_left, text= ' Whole Weight ', background="light blue")
        lblWWeight.grid(row=4, column=0, padx=2, pady=10,sticky="w")
        txtWWeight = StringVar()
        entWWeight = ttk.Scale(frame_left, orient='horizontal', from_=0, to=4, length=250, variable=txtWWeight,
                              style="TScale")
        entWWeight.set(1.5)
        entWWeight.grid(row=4, column=2, padx=2, pady=10)
        spWWeight = Spinbox(frame_left, textvariable=txtWWeight, width=5, from_=0, to=4)
        spWWeight.grid(row=4, column=1, padx=0, pady=10)

        dolblWWeight = Label(frame_right, text='note: whole abalone')
        dolblWWeight.grid(row=4, column=0, padx=2, pady=10,sticky="w")


        # Shucked_weight
        lblSWeight = Label(frame_left, text='Shucked Weight',background="light blue")
        lblSWeight.grid(row=5, column=0, padx=2, pady=10,sticky="w")
        txtSWeight = StringVar()
        entSWeight = ttk.Scale(frame_left, orient='horizontal', from_=0, to=2, length=250, variable=txtSWeight,
                              style="TScale")
        entSWeight.set(0.75)
        entSWeight.grid(row=5, column=2, padx=2, pady=10)
        spSWeight = Spinbox(frame_left, textvariable=txtSWeight, width=5, from_=0, to=2)
        spSWeight.grid(row=5, column=1, padx=0, pady=10)

        dolblSWeight = Label(frame_right, text="note: weight of meat")
        dolblSWeight.grid(row=5, column=0, padx=2, pady=10,sticky="w")



        # Viscera_weight
        lblVWeight = Label(frame_left, text='Viscera weight', background="light blue")
        lblVWeight.grid(row=6, column=0, padx=2, pady=10,sticky="w")
        txtVWeight = StringVar()
        entVWeight = ttk.Scale(frame_left, orient='horizontal', from_=0, to=2, length=250, variable=txtVWeight,
                              style="TScale")
        entVWeight.set(1)
        entVWeight.grid(row=6, column=2, padx=2, pady=10)
        spVWeight = Spinbox(frame_left, textvariable=txtVWeight, width=5, from_=0, to=2)
        spVWeight.grid(row=6, column=1, padx=0, pady=10)

        dolblVWeight = Label(frame_right, text='note: gut weight (after bleeding)')
        dolblVWeight.grid(row=6, column=0, padx=2, pady=10,sticky="w")



        # Shell_weight
        lblShellWeight = Label(frame_left, text='  Shell Weight ',background="light blue")
        lblShellWeight.grid(row=7, column=0, padx=2, pady=10,sticky="w")
        txtShellWeight = StringVar()
        entShellWeight = ttk.Scale(frame_left, orient='horizontal', from_=0, to=2, length=250, variable=txtShellWeight,
                              style="TScale")
        entShellWeight.set(1)
        entShellWeight.grid(row=7 ,column=2, padx=2, pady=10)
        spShellWeight = Spinbox(frame_left, textvariable=txtShellWeight, width=5, from_=0, to=2)
        spShellWeight.grid(row=7, column=1, padx=0, pady=10)

        dolblShellWeight = Label(frame_right, text='note: after being dried')
        dolblShellWeight.grid(row=7, column=0, padx=2, pady=10,sticky="w")



        btnPredictKNN = ttk.Button(AbaloneFormObject, text="Regression", width=20, command=PredictReg)
        btnPredictKNN.grid(row=8, column=0, columnspan=2, padx=5, pady=10,sticky="w")

        btnPredictbackToMainForm = ttk.Button(AbaloneFormObject, text="MainForm", width=20, command=backToMainForm)
        btnPredictbackToMainForm.grid(row=8, column=1, padx=5, pady=10)





        AbaloneFormObject.mainloop()