from customtkinter import *
import face_rcog
import training
import csv
class app(CTk):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.details = "D:\Python files\Hackathon\Face recog 1\details.csv"
        with open(self.details,"a") as f:
            pass
        self.markedroll = "D:\Python files\Hackathon\Face recog 1\markedroll.dat"
        self.attendance = "D:\Python files\Hackathon\Face recog 1\sattendance.csv"
        self.label3 =CTkLabel(self,text="Roll no. already exists",font = ("bold",20))
        self.geometry("600x500")
        self.title("Attendance Manager")
        self.label = CTkLabel(self,text="Attendance Manager",font = ("bold",20))
        self.label.place(relx = 0.36,rely = 0.1)
        self.label2 = CTkLabel(self,text="Press q to exit cam",font = ("bold",20))
        self.label2.place(relx = 0.01,rely = 0.01)
        self.back = CTkButton(self,text = "back",width = 200,height=50,font = ("bold",20),command=lambda:app.page(self))
        self.entry = CTkEntry(self,text_color="white",placeholder_text="Student name",placeholder_text_color="white",height = 30,width = 220,font=("Bold",12))
        self.e2 = CTkEntry(self,text_color="white",placeholder_text="Roll no.",placeholder_text_color="white",height = 30,width = 220,font=("Bold",12))
        self.b1 = CTkButton(self,text = "Create Entry",width = 200,height=50,font = ("bold",20),command=lambda:app.b1f(self))
        self.b1.place(relx = 0.35,rely = 0.2)
        #self.b5 = CTkButton(self,text = "",width = 200,height=50,font = ("bold",20),command=lambda:app.b1f(self))
        self.b4 = CTkButton(self,text = "Reset",width = 200,height=50,font = ("bold",20),command=lambda:app.b4f(self))
        self.b3 = CTkButton(self,text = "Get cam",width = 200,height=50,font = ("bold",20),command=lambda:app.reader(self))
        self.b2 = CTkButton(self,text = "Start Attendance",width = 200,height=50,font = ("bold",20),command=lambda:app.b2f(self))
        self.b2.place(relx = 0.35,rely = 0.4)
        self.b4.place(relx = 0.35,rely = 0.6)
        self.mainloop()
    def b4f(self):
        with open(self.attendance,"w") as f:
            pass
        with open(self.markedroll,"w") as f:
            pass
    def reader(self):
        self.exists = 0
        self.name = self.entry.get()
        self.roll = self.e2.get()
        if self.name != "" and self.roll != "":
            with open(self.details,"r") as f:
                reader = csv.reader(f)
                for i in list(reader):
                    if i[1] == self.roll:
                        self.exists = 1
                        self.label3.place(relx = 0.35,rely= 0.65)
                        break
            if self.exists == 0:
                self.destroy()
                training.train(self.name,self.roll)
                app()

    def page(self):
        for i in self.winfo_children():
            i.place_forget()
        self.label.place(relx = 0.36,rely = 0.1)
        self.label2.place(relx = 0.01,rely = 0.01)
        self.b1.place(relx = 0.35,rely = 0.2)
        self.b2.place(relx = 0.35,rely = 0.4)
        self.b4.place(relx = 0.35,rely = 0.6)
    def b1f(self):
        for i in self.winfo_children():
            i.place_forget()
        self.entry.place(relx = 0.34,rely = 0.3)
        self.e2.place(relx = 0.34,rely= 0.4)
        self.b3.place(relx = 0.35,rely = 0.5)
        self.back.place(relx = 0.355,rely = 0.8)
        
    def b2f(self):
        self.destroy()
        face_rcog.facerecog()
        app()        
app()
