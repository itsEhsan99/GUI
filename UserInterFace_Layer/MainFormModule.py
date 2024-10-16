from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from Obesity_Package.ObesityFormModule import ObesityFormClass
from Abalone_Package.AbaloneModuleform import AbaloneFormClass
from Rice_Package.RiceFormMOdule import RiceFormClass


class MainFormClass:
    def MainFormLoad(self, name):
        MainFormObject = Tk()
        MainFormObject.title('Main Form')
        MainFormObject.geometry('700x300')
        MainFormObject.iconbitmap('Image/Main.ico')
        MainFormObject.resizable(0, 0)
        x = int(MainFormObject.winfo_screenwidth() / 2 - 700 / 2)
        y = int(MainFormObject.winfo_screenheight() / 2 - 300 / 2)
        MainFormObject.geometry('+{}+{}'.format(x, y))

        def ObesityFormLoad():
            MainFormObject.destroy()
            ObesityFormObject=ObesityFormClass()
            ObesityFormObject.ObesityFormLoad()
        #
        def AbaloneFormLoad():
            MainFormObject.destroy()
            AbaloneFormObject=AbaloneFormClass()
            AbaloneFormObject.AbaloneFormLoad()
        #
        def RiceFormLoad():
            MainFormObject.destroy()
            RiceFormObject=RiceFormClass()
            RiceFormObject.RiceFormLoad()


        lblWelcomeMessage = Label(MainFormObject, text=f'Welcome  {name} , let start prediction : ' )
        lblWelcomeMessage.grid(row=0, column=0, padx=10, pady=10)

        ObesityImage = PhotoImage(file='Image/Scale.png')
        BtnObesity = Button(MainFormObject,compound=TOP,image = ObesityImage,text='Obesity Level',command=ObesityFormLoad)
        BtnObesity.grid(row=1,column=0,padx=20,pady=20)


        AbaloneImage = PhotoImage(file='Image/AbaloneClassification.png')
        BtnAbalone = Button(MainFormObject,compound=TOP, image = AbaloneImage,text='Years of Abalone',command=AbaloneFormLoad)
        BtnAbalone.grid(row=1,column=1,padx=20,pady=20)
        #

        RiceImage = PhotoImage(file='Image/RiceClassification.png')
        BtnRice = Button(MainFormObject,compound=TOP,image=RiceImage,text='type of Rice ',command=RiceFormLoad)
        BtnRice.grid(row=1,column=2,padx=20,pady=20)

        MainFormObject.mainloop()