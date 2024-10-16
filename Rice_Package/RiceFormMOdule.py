from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from tkcalendar import DateEntry
import pandas as pd
import numpy as np
from joblib import dump, load
# from RiceModel import riceknn


class RiceFormClass:
    def RiceFormLoad(self):
        RiceFormObject = Tk()
        RiceFormObject.title('Rice prediction form ')
        RiceFormObject.geometry('900x300')
        RiceFormObject.iconbitmap('Image/Rice.ico')
        RiceFormObject.resizable(0, 0)
        X = int(RiceFormObject.winfo_screenwidth() / 2 - 900 / 2)
        Y = int(RiceFormObject.winfo_screenheight() / 2 - 300 / 2)
        RiceFormObject.geometry('+{}+{}'.format(X, Y))

        def PredictReg():
            params=[float(textArea.get()), float(textPerimeter.get()) , float(textMajorAL.get()) ,
                    float(textMinorAL.get()) , float(textEccentricity.get()) ,
                    float(textRCA.get()) , float(textExtent.get())]

            model_knn = load("Rice_Package/KNNforRice.joblib")
            mypredict=model_knn.predict_proba([params])
            if mypredict.tolist()[0][0] > mypredict.tolist()[0][1]:
                msg.showinfo("our Prediction",f"berenje shoma  be ehtemale {(mypredict.tolist()[0][0]) * 100}% classe Cammeo hast \n ( accuracy model : 89,7% :) ) ")
            else:
                msg.showinfo("our Prediction",f"berenje shoma  be ehtemale {(mypredict.tolist()[0][1]) * 100}% classe Osmancik hast \n ( accuracy model : 89,7% :))  ")

        def ResetForm():
            for widget in RiceFormObject.winfo_children():
                if type(widget) == ttk.Entry:
                    widget.delete(0,END)

        def backToMainForm():
            from UserInterFace_Layer.MainFormModule import MainFormClass
            RiceFormObject.destroy()
            MainFormObject = MainFormClass()
            MainFormObject.MainFormLoad(" again dear ")

        # region Area
        lblArea = Label(RiceFormObject, background="light blue", text="Area :              ")
        lblArea.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        textArea = StringVar()

        def focus_in(*args):
            if enterArea.get() == "number of pixels within the boundaries of the rice grain":
                enterArea.delete(0, "end")
                enterArea.insert(0, "")
                enterArea.config(foreground="black")

        def focus_out(*args):
            if enterArea.get() == "":
                textArea.set("")
                enterArea.insert(0, "number of pixels within the boundaries of the rice grain")
                enterArea.config(foreground="grey")

        enterArea = ttk.Entry(RiceFormObject, textvariable=textArea, width=85)
        enterArea.insert(0, "number of pixels within the boundaries of the rice grain")
        enterArea.config(foreground="grey")
        enterArea.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        enterArea.bind("<FocusIn>", focus_in)
        enterArea.bind("<FocusOut>", focus_out)
        lblArea2 = Label(RiceFormObject, background="light blue", text="note: average = 12500 ")
        lblArea2.grid(row=0, column=2, padx=10, pady=5, sticky="w")
        # endregion

        # region Perimeter
        lblPerimeter = Label(RiceFormObject, background="light blue", text="Perimeter :         ")
        lblPerimeter.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        textPerimeter = StringVar()

        def focus_in(*args):
            if enterPerimeter.get() == "the distance between pixels around the boundaries of the rice grain":
                enterPerimeter.delete(0, "end")
                enterPerimeter.insert(0, "")
                enterPerimeter.config(foreground="black")

        def focus_out(*args):
            if enterPerimeter.get() == "":
                textPerimeter.set("")
                enterPerimeter.insert(0, "the distance between pixels around the boundaries of the rice grain")
                enterPerimeter.config(foreground="grey")

        enterPerimeter = ttk.Entry(RiceFormObject, textvariable=textPerimeter, width=85)
        enterPerimeter.insert(0, "the distance between pixels around the boundaries of the rice grain")
        enterPerimeter.config(foreground="grey")
        enterPerimeter.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        enterPerimeter.bind("<FocusIn>", focus_in)
        enterPerimeter.bind("<FocusOut>", focus_out)
        lblPerimeter2 = Label(RiceFormObject, background="light blue", text="note: average = 450 ")
        lblPerimeter2.grid(row=1, column=2, padx=10, pady=5, sticky="w")
        # endregion

        # region Major_Axis_Length
        lblMajorAL = Label(RiceFormObject, background="light blue", text="Major Axis Length:  ")
        lblMajorAL.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        textMajorAL = StringVar()

        def focus_in(*args):
            if enterMajorAL.get() == "The longest line that can be drawn on the rice grain":
                enterMajorAL.delete(0, "end")
                enterMajorAL.insert(0, "")
                enterMajorAL.config(foreground="black")

        def focus_out(*args):
            if enterMajorAL.get() == "":
                textMajorAL.set("")
                enterMajorAL.insert(0, "The longest line that can be drawn on the rice grain")
                enterMajorAL.config(foreground="grey")

        enterMajorAL = ttk.Entry(RiceFormObject, textvariable=textMajorAL, width=85)
        enterMajorAL.insert(0, "The longest line that can be drawn on the rice grain")
        enterMajorAL.config(foreground="grey")
        enterMajorAL.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        enterMajorAL.bind("<FocusIn>", focus_in)
        enterMajorAL.bind("<FocusOut>", focus_out)
        lblMajorAL2 = Label(RiceFormObject, background="light blue", text="note: average = 185 ")
        lblMajorAL2.grid(row=2, column=2, padx=10, pady=5, sticky="w")
        # endregion

        # region Major_Axis_Length
        lblMinorAL = Label(RiceFormObject, background="light blue", text="Minor Axis Length:  ")
        lblMinorAL.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        textMinorAL = StringVar()

        def focus_in(*args):
            if enterMinorAL.get() == "The shortest line that can be drawn on the rice grain":
                enterMinorAL.delete(0, "end")
                enterMinorAL.insert(0, "")
                enterMinorAL.config(foreground="black")

        def focus_out(*args):
            if enterMinorAL.get() == "":
                textMinorAL.set("")
                enterMinorAL.insert(0, "The shortest line that can be drawn on the rice grain")
                enterMinorAL.config(foreground="grey")

        enterMinorAL = ttk.Entry(RiceFormObject, textvariable=textMinorAL, width=85)
        enterMinorAL.insert(0, "The shortest line that can be drawn on the rice grain")
        enterMinorAL.config(foreground="grey")
        enterMinorAL.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        enterMinorAL.bind("<FocusIn>", focus_in)
        enterMinorAL.bind("<FocusOut>", focus_out)
        lblMinorAL2 = Label(RiceFormObject, background="light blue", text="note: average = 85 ")
        lblMinorAL2.grid(row=3, column=2, padx=10, pady=5, sticky="w")
        # endregion

        # region Eccentricity
        lblEccentricity = Label(RiceFormObject, background="light blue", text="Eccentricity:       ")
        lblEccentricity.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        textEccentricity = StringVar()

        def focus_in(*args):
            if enterEccentricity.get() == "It measures how round the ellipse, which has the same moments as the rice grain, is":
                enterEccentricity.delete(0, "end")
                enterEccentricity.insert(0, "")
                enterEccentricity.config(foreground="black")

        def focus_out(*args):
            if enterEccentricity.get() == "":
                textEccentricity.set("")
                enterEccentricity.insert(0, "It measures how round the ellipse, which has the same moments as the rice grain, is")
                enterEccentricity.config(foreground="grey")

        enterEccentricity = ttk.Entry(RiceFormObject, textvariable=textEccentricity, width=85)
        enterEccentricity.insert(0, "It measures how round the ellipse, which has the same moments as the rice grain, is")
        enterEccentricity.config(foreground="grey")
        enterEccentricity.grid(row=4, column=1, padx=10, pady=5, sticky="w")
        enterEccentricity.bind("<FocusIn>", focus_in)
        enterEccentricity.bind("<FocusOut>", focus_out)
        lblEccentricity = Label(RiceFormObject, background="light blue", text="note: average = 0.9 ")
        lblEccentricity.grid(row=4, column=2, padx=10, pady=5, sticky="w")
        # endregion

        # region Convex_Area
        lblRCA = Label(RiceFormObject, background="light blue", text="region Convex Area :")
        lblRCA.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        textRCA = StringVar()

        def focus_in(*args):
            if enterRCA.get() == "Returns the pixel count of the smallest convex shell of the region formed by the rice grain":
                enterRCA.delete(0, "end")
                enterRCA.insert(0, "")
                enterRCA.config(foreground="black")

        def focus_out(*args):
            if enterRCA.get() == "":
                textRCA.set("")
                enterRCA.insert(0, "Returns the pixel count of the smallest convex shell of the region formed by the rice grain")
                enterRCA.config(foreground="grey")

        enterRCA = ttk.Entry(RiceFormObject, textvariable=textRCA, width=85)
        enterRCA.insert(0, "Returns the pixel count of the smallest convex shell of the region formed by the rice grain")
        enterRCA.config(foreground="grey")
        enterRCA.grid(row=5, column=1, padx=10, pady=5, sticky="w")
        enterRCA.bind("<FocusIn>", focus_in)
        enterRCA.bind("<FocusOut>", focus_out)
        lblRCA = Label(RiceFormObject, background="light blue", text="note: average = 12952 ")
        lblRCA.grid(row=5, column=2, padx=10, pady=5, sticky="w")
        # endregion

        # Extent
        lblExtent = Label(RiceFormObject, background="light blue", text="Extent :         ")
        lblExtent.grid(row=6, column=0, padx=10, pady=5, sticky="w")
        textExtent = StringVar()

        def focus_in(*args):
            if enterExtent.get() == "Returns the ratio of the region formed by the rice grain to the bounding box":
                enterExtent.delete(0, "end")
                enterExtent.insert(0, "")
                enterExtent.config(foreground="black")

        def focus_out(*args):
            if enterExtent.get() == "":
                textExtent.set("")
                enterExtent.insert(0, "Returns the ratio of the region formed by the rice grain to the bounding box")
                enterExtent.config(foreground="grey")

        enterExtent = ttk.Entry(RiceFormObject, textvariable=textExtent, width=85)
        enterExtent.insert(0, "Returns the ratio of the region formed by the rice grain to the bounding box")
        enterExtent.config(foreground="grey")
        enterExtent.grid(row=6, column=1, padx=10, pady=5, sticky="w")
        enterExtent.bind("<FocusIn>", focus_in)
        enterExtent.bind("<FocusOut>", focus_out)
        lblExtent = Label(RiceFormObject, background="light blue", text="note: average = 0.65 ")
        lblExtent.grid(row=6, column=2, padx=10, pady=5, sticky="w")
        # endregion


        btnPredictReg = ttk.Button(RiceFormObject, text="KNN", width=20, command=PredictReg)
        btnPredictReg.grid(row=7, column=0, columnspan=2, padx=5, pady=10,sticky="w")

        BtnReset = ttk.Button(RiceFormObject, text='Reset Form ',width=20,  command=ResetForm)
        BtnReset.grid(row=7, column=1, padx=10, pady=20,sticky="w")

        btnPredictbackToMainForm = ttk.Button(RiceFormObject, text="MainForm", width=20, command=backToMainForm)
        btnPredictbackToMainForm.grid(row=7, column=1, padx=5, pady=10, sticky="e")