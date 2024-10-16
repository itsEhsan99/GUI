from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from tkcalendar import DateEntry
import pandas as pd
import numpy as np
from joblib import dump, load
# from KnnForObesity import myKNN



class ObesityFormClass:
    def ObesityFormLoad(self):
        ObesityFormObject = Tk()
        ObesityFormObject.title('Obesity Prediction Form')
        ObesityFormObject.geometry('700x680')
        ObesityFormObject.iconbitmap('Image/Scale.ico')
        ObesityFormObject.resizable(0, 0)
        X = int(ObesityFormObject.winfo_screenwidth() / 2 - 700 / 2)
        Y = int(ObesityFormObject.winfo_screenheight() / 2 - 680 / 2)
        ObesityFormObject.geometry('+{}+{}'.format(X, Y))


        def PredictKNN():
            params=[float(intsex.get()), float(textage.get()) , float(textHeight.get()) ,
                    float(textWeight.get()) , float(intFamily.get()) ,
                    float(intFAVC.get()) , float(valuesFCVC[textFCVC.get()]) , float(valuesNCP[textNCP.get()]) ,
                    float(valuesCAEC[textCAEC.get()]) , float(intSmoke.get()) , float(valuesCH2O[textCH2O.get()]) ,
                    float(intSCC.get()) , float(textFAF.get()) , float(textTUE.get()) ,
                    float(valuesCALC[textCALC.get()]) , float(valuesMTRANS[textMTRANS.get()])]

            model_knn = load("Obesity_Package/KNNforObesity.joblib")
            mypredict=model_knn.predict([params])
            msg.showinfo("our Prediction ", f" based on your info , \n this is your situation{ mypredict}")



        # def backToMainForm():
        #     ObesityFormObject.destroy()
        #     # from Menu.menu import mainClass
        #     MainFormObject = MainFormClass()
        #     MainFormObject.MainFormLoad()

        def ResetForm():
            for widget in ObesityFormObject.winfo_children():
                if type(widget) == ttk.Entry:
                    widget.delete(0,END)

        def backToMainForm():
            from UserInterFace_Layer.MainFormModule import MainFormClass
            ObesityFormObject.destroy()
            MainFormObject = MainFormClass()
            MainFormObject.MainFormLoad(" again dear ")

        # region age
        lblage = Label(ObesityFormObject, background="light blue", text="age: ")
        lblage.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        textage = StringVar()

        def focus_in(*args):
            if enterage.get() == "Enter age of patient":
                enterage.delete(0, "end")
                enterage.insert(0, "")
                enterage.config(foreground="black")

        def focus_out(*args):
            if enterage.get() == "":
                textage.set("")
                enterage.insert(0, "Enter age of patient")
                enterage.config(foreground="grey")

        enterage = ttk.Entry(ObesityFormObject, textvariable=textage, width=50)
        enterage.insert(0, "Enter age of patient")
        enterage.config(foreground="grey")
        enterage.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        enterage.bind("<FocusIn>", focus_in)
        enterage.bind("<FocusOut>", focus_out)
        # endregion

        # region sex
        lblsex = Label(ObesityFormObject, background="light blue", text="sex: ")
        lblsex.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        intsex = IntVar()
        rdZero = ttk.Radiobutton(ObesityFormObject, text="female", variable=intsex, value=0) # 2
        rdZero.grid(row=1, column=1, padx=40, pady=10, sticky="w")
        rdOne = ttk.Radiobutton(ObesityFormObject, text="male", variable=intsex, value=1)
        rdOne.grid(row=1, column=1, padx=10, pady=10, sticky="e")
        intsex.set(0)
        # endregion

        # region Height
        lblHeight = Label(ObesityFormObject, background="light blue", text="Height: ")
        lblHeight.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        textHeight = StringVar()

        def focus_in(*args):
            if enterHeight.get() == "Enter Height of patient":
                enterHeight.delete(0, "end")
                enterHeight.insert(0, "")
                enterHeight.config(foreground="black")

        def focus_out(*args):
            if enterHeight.get() == "":
                textHeight.set("")
                enterHeight.insert(0, "Enter Height of patient")
                enterHeight.config(foreground="grey")

        enterHeight = ttk.Entry(ObesityFormObject, textvariable=textHeight, width=50)
        enterHeight.insert(0, "Enter Height of patient")
        enterHeight.config(foreground="grey")
        enterHeight.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        enterHeight.bind("<FocusIn>", focus_in)
        enterHeight.bind("<FocusOut>", focus_out)
        # endregion


        # region Weight
        lblWeight = Label(ObesityFormObject, background="light blue", text="Weight: ")
        lblWeight.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        textWeight = StringVar()

        def focus_in(*args):
            if enterWeight.get() == "Enter Weight of patient":
                enterWeight.delete(0, "end")
                enterWeight.insert(0, "")
                enterWeight.config(foreground="black")

        def focus_out(*args):
            if enterWeight.get() == "":
                textWeight.set("")
                enterWeight.insert(0, "Enter Weight of patient")
                enterWeight.config(foreground="grey")

        enterWeight = ttk.Entry(ObesityFormObject, textvariable=textWeight, width=50)
        enterWeight.insert(0, "Enter Weight of patient")
        enterWeight.config(foreground="grey")
        enterWeight.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        enterWeight.bind("<FocusIn>", focus_in)
        enterWeight.bind("<FocusOut>", focus_out)

        # region family_history_with_overweight
        lblFamily = Label(ObesityFormObject, background="light blue", text="family history with overweight: ")
        lblFamily.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        intFamily = IntVar()
        rdZero = ttk.Radiobutton(ObesityFormObject, text="no", variable=intFamily, value=0)  # 2
        rdZero.grid(row=4, column=1, padx=40, pady=10, sticky="w")
        rdOne = ttk.Radiobutton(ObesityFormObject, text="yes", variable=intFamily, value=1)
        rdOne.grid(row=4, column=1, padx=10, pady=10, sticky="e")
        intFamily.set(0)
        # endregion

        # region FAVC
        lblFAVC = Label(ObesityFormObject, background="light blue", text="Do you eat high caloric food frequency? ")
        lblFAVC.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        intFAVC = IntVar()
        rdZero = ttk.Radiobutton(ObesityFormObject, text="no", variable=intFAVC, value=0)  # 2
        rdZero.grid(row=5, column=1, padx=40, pady=10, sticky="w")
        rdOne = ttk.Radiobutton(ObesityFormObject, text="yes", variable=intFAVC, value=1)
        rdOne.grid(row=5, column=1, padx=10, pady=10, sticky="e")
        intFAVC.set(0)
        # endregion

        # region FCVC
        lblFCVC = Label(ObesityFormObject, background="light blue", text="Do you usually eat vegetables in your meals(how many) ?  ")
        lblFCVC.grid(row=6, column=0, padx=10, pady=10, sticky="w")
        textFCVC = StringVar()
        valuesFCVC = {"one": 1, "two": 2, "three": 3, "four": 4}
        cmbFCVC = ttk.Combobox(ObesityFormObject, values=[key for key in valuesFCVC.keys()], textvariable=textFCVC,
                               state="readonly", width=47)
        cmbFCVC.grid(row=6, column=1, padx=10, pady=10, sticky="w")
        cmbFCVC.current(0)
        # endregion

        # region NCP
        lblNCP = Label(ObesityFormObject, background="light blue", text="How many main meals do you have daily?   ")
        lblNCP.grid(row=7, column=0, padx=10, pady=10, sticky="w")
        textNCP = StringVar()
        valuesNCP = {"one": 1, "two": 2, "three": 3}
        cmbNCP = ttk.Combobox(ObesityFormObject, values=[key for key in valuesNCP.keys()], textvariable=textNCP,
                              state="readonly", width=47)
        cmbNCP.grid(row=7, column=1, padx=10, pady=10, sticky="w")
        cmbNCP.current(0)
        # endregion

        # region CAEC
        lblCAEC = Label(ObesityFormObject, background="light blue", text="Do you eat any food between meals?    ")
        lblCAEC.grid(row=8, column=0, padx=10, pady=10, sticky="w")
        textCAEC = StringVar()
        valuesCAEC = {"no": 1, "sometimes": 2, "Frequently": 3 , "Always" : 4 }
        cmbCAEC = ttk.Combobox(ObesityFormObject, values=[key for key in valuesCAEC.keys()], textvariable=textCAEC,
                               state="readonly", width=47)
        cmbCAEC.grid(row=8, column=1, padx=10, pady=10, sticky="w")
        cmbCAEC.current(0)
        # endregion

        # region Smoke
        lblSmoke = Label(ObesityFormObject, background="light blue", text="Do you Smoke ? ")
        lblSmoke.grid(row=9, column=0, padx=10, pady=10, sticky="w")
        intSmoke = IntVar()
        rdZero = ttk.Radiobutton(ObesityFormObject, text="no", variable=intSmoke, value=0)  # 2
        rdZero.grid(row=9, column=1, padx=40, pady=10, sticky="w")
        rdOne = ttk.Radiobutton(ObesityFormObject, text="yes", variable=intSmoke, value=1)
        rdOne.grid(row=9, column=1, padx=10, pady=10, sticky="e")
        intSmoke.set(0)
        # endregion

        # region CH2O
        lblCH2O = Label(ObesityFormObject, background="light blue", text="How much water do you drink daily?  ")
        lblCH2O.grid(row=10, column=0, padx=10, pady=10, sticky="w")
        textCH2O = StringVar()
        valuesCH2O = {"low": 1, "Moderate": 2, "high": 3  }
        cmbCH2O = ttk.Combobox(ObesityFormObject, values=[key for key in valuesCH2O.keys()], textvariable=textCH2O,
                               state="readonly", width=47)
        cmbCH2O.grid(row=10, column=1, padx=10, pady=10, sticky="w")
        cmbCH2O.current(0)
        # endregion

        # region monitoring
        lblSCC = Label(ObesityFormObject, background="light blue", text="Do you monitor the calories you eat daily ? ")
        lblSCC.grid(row=11, column=0, padx=10, pady=10, sticky="w")
        intSCC = IntVar()
        rdZero = ttk.Radiobutton(ObesityFormObject, text="no", variable=intSCC, value=0)  # 2
        rdZero.grid(row=11, column=1, padx=40, pady=10, sticky="w")
        rdOne = ttk.Radiobutton(ObesityFormObject, text="yes", variable=intSCC, value=1)
        rdOne.grid(row=11, column=1, padx=10, pady=10, sticky="e")
        intSCC.set(0)
        # endregion

        # region FAF
        lblFAF = Label(ObesityFormObject, background="light blue", text="How often do you have physical activity? ")
        lblFAF.grid(row=12, column=0, padx=10, pady=5, sticky="w")
        textFAF = StringVar()

        def focus_in(*args):
            if enterFAF.get() == "float number between 0 to 3":
                enterFAF.delete(0, "end")
                enterFAF.insert(0, "")
                enterFAF.config(foreground="black")

        def focus_out(*args):
            if enterFAF.get() == "":
                textFAF.set("")
                enterFAF.insert(0, "float number between 0 to 3")
                enterFAF.config(foreground="grey")

        enterFAF = ttk.Entry(ObesityFormObject, textvariable=textFAF, width=50)
        enterFAF.insert(0, "float number between 0 to 3")
        enterFAF.config(foreground="grey")
        enterFAF.grid(row=12, column=1, padx=10, pady=5, sticky="w")
        enterFAF.bind("<FocusIn>", focus_in)
        enterFAF.bind("<FocusOut>", focus_out)
        # endregion

        # region TUE
        lblTUE = Label(ObesityFormObject, background="light blue", text="How much time do you use technological devices ? ")
        lblTUE.grid(row=13, column=0, padx=10, pady=5, sticky="w")
        textTUE = StringVar()

        def focus_in(*args):
            if enterTUE.get() == "float number between 0 to 2":
                enterTUE.delete(0, "end")
                enterTUE.insert(0, "")
                enterTUE.config(foreground="black")

        def focus_out(*args):
            if enterTUE.get() == "":
                textTUE.set("")
                enterTUE.insert(0, "float number between 0 to 2")
                enterTUE.config(foreground="grey")

        enterTUE = ttk.Entry(ObesityFormObject, textvariable=textTUE, width=50)
        enterTUE.insert(0, "float number between 0 to 2")
        enterTUE.config(foreground="grey")
        enterTUE.grid(row=13, column=1, padx=10, pady=5, sticky="w")
        enterTUE.bind("<FocusIn>", focus_in)
        enterTUE.bind("<FocusOut>", focus_out)
        # endregion

        # region CALC
        lblCALC = Label(ObesityFormObject, background="light blue", text="How often do you drink alcohol?  ")
        lblCALC.grid(row=14, column=0, padx=10, pady=10, sticky="w")
        textCALC = StringVar()
        valuesCALC = {"no": 1, "sometimes": 2, "Frequently": 3 , "Always" : 4 }
        cmbCALC = ttk.Combobox(ObesityFormObject, values=[key for key in valuesCALC.keys()], textvariable=textCALC,
                               state="readonly", width=47)
        cmbCALC.grid(row=14, column=1, padx=10, pady=10, sticky="w")
        cmbCALC.current(0)
        # endregion

        # region MTRANS
        lblMTRANS = Label(ObesityFormObject, background="light blue", text="Which transportation do you usually use?  ")
        lblMTRANS.grid(row=15, column=0, padx=10, pady=10, sticky="w")
        textMTRANS = StringVar()
        valuesMTRANS = {"Automobile": 1, "Motorbike": 2, "Public_Transportation": 3 , "Walking" : 4 ,"Bike" : 5}
        cmbMTRANS = ttk.Combobox(ObesityFormObject, values=[key for key in valuesMTRANS.keys()], textvariable=textMTRANS,
                                 state="readonly", width=47)
        cmbMTRANS.grid(row=15, column=1, padx=10, pady=10, sticky="w")
        cmbMTRANS.current(0)
        # endregion



        btnPredictKNN = ttk.Button(ObesityFormObject, text="KNN", width=20, command=PredictKNN)
        btnPredictKNN.grid(row=16, column=0, padx=5, pady=10)
        #

        BtnReset = ttk.Button(ObesityFormObject, width=20,text='Reset Form ',  command=ResetForm)
        BtnReset.grid(row=16, column=1, padx=10, pady=20,sticky="w")

        btnPredictbackToMainForm = ttk.Button(ObesityFormObject, text="MainForm", width=20, command=backToMainForm)
        btnPredictbackToMainForm.grid(row=16, column=1, padx=10, pady=10,sticky="e")

        ObesityFormObject.mainloop()