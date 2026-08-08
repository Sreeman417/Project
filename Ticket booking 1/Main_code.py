from tkinter import *
from tkinter import messagebox
import customtkinter as ct
import pickle
root = ct.CTk()
ct.set_appearance_mode("dark")
ct.set_default_color_theme("dark-blue")
root.geometry("1000x600")
l={}
with open("newfile3.dat","ab") as f:
   pass
with open("newfile3.dat","rb+") as f:
   while True:
      try:
         s = pickle.load(f)
         break
      except EOFError:
         pickle.dump({"rrr":350,"vada chennai":350,"leo":350},f)
         break
with open("newfile3.dat","rb") as f:
   while True:
      try:
         s = pickle.load(f)
         l = s
      except:
         break

def face3():
    gk_root = ct.CTkToplevel(root)
    gk_root.geometry("1060x350")
    new_root = ct.CTkScrollableFrame(gk_root,width = 1060,height=350,orientation="horizontal")
    new_root.pack(padx=40)
    ct.set_appearance_mode("dark")
    ct.set_default_color_theme("dark-blue")
    l=[]
    def seat_checker_off(s,r,c,n):
        s = ct.CTkButton(new_root,text=n,fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(s,r,c,n))
        s.grid(row = r,column=c)
        l.remove(n)
    def ticket_checker():
        done.configure(state="disabled")
        if len(l)<int(ticket):
            messagebox.showinfo("Not yet","Only {} booked".format(len(l)))
            done.configure(state="normal")
        if len(l) == int(ticket):
            ans = messagebox.askyesno("Sure?","Are You Sure?")

            if ans:
                done.configure(state="disabled")
               
                st = ""
                for i in l:
                    st+=i+","
                messagebox.showinfo("Thank You","You booked {} \n Thank you".format(st))
                with open("newfile2.dat","ab") as file:
                    pickle.dump({movie_pack:l},file)
                with open("newfile3.dat","rb+") as file:
                  while True:
                     try:
                        s = pickle.load(file)
                        for k in s:
                           if k == movie_pack:
                              s[movie_pack] -= int(ticket)
                              file.seek(0)
                              pickle.dump(s,file)
                     except EOFError:
                        break
                root.destroy()
            else:
                done.configure(state="normal")
               
                    
    

    def seat_checker_on(s,r,c,n):
       if len(l)<int(ticket):
        l.append(n)
        s= ct.CTkButton(new_root,text=n,fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,bg_color="green",command=lambda:seat_checker_off(s,r,c,n))
        s.grid(row=r,column=c)       
       if len(l)==int(ticket):
        global done
        done = ct.CTkButton(new_root,text="DONE",fg_color="transparent",border_color="red",hover_color="green",border_width = 1,command=ticket_checker)
        done.grid(row=22,column=22)
            

    j1 = ct.CTkButton(new_root,text="j1",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(j1,0,1,"j1"))
    j1.grid(row=0,column=1)
    j2 = ct.CTkButton(new_root,text="j2",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(j2,0,2,"j2"))
    j2.grid(row=0,column=2)
    j3 = ct.CTkButton(new_root,text="j3",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(j3,0,3,"j3"))
    j3.grid(row=0,column=3)
    j4 = ct.CTkButton(new_root,text="j4",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(j4,0,4,"j4"))
    j4.grid(row=0,column=4)
    j5 = ct.CTkButton(new_root,text="j5",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(j5,0,5,"j5"))
    j5.grid(row=0,column=5)
    j6 = ct.CTkButton(new_root,text="j6",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(j6,0,6,"j6"))
    j6.grid(row=0,column=6)
    j7 = ct.CTkButton(new_root,text="j7",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(j7,0,7,"j7"))
    j7.grid(row=0,column=7)
    j8 = ct.CTkButton(new_root,text="j8",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(j8,0,8,"j8"))
    j8.grid(row=0,column=8)
    j9 = ct.CTkButton(new_root,text="j9",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(j9,0,9,"j9"))
    j9.grid(row=0,column=9)
    j10 = ct.CTkButton(new_root,text="j10",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(j10,0,10,"j10"))
    j10.grid(row=0,column=10)
    j11 = ct.CTkButton(new_root,text="j11",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(j11,0,11,"j11"))
    j11.grid(row=0,column=11)
    j12 = ct.CTkButton(new_root,text="j12",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(j12,0,12,"j12"))
    j12.grid(row=0,column=12)
    j13 = ct.CTkButton(new_root,text="j13",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(j13,0,13,"j13"))
    j13.grid(row=0,column=13)
    j14 = ct.CTkButton(new_root,text="j14",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(j14,0,14,"j14"))
    j14.grid(row=0,column=14)
    j15 = ct.CTkButton(new_root,text="j15",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(j15,0,15,"j15"))
    j15.grid(row=0,column=15)
    j16 = ct.CTkButton(new_root,text="j16",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(j16,0,16,"j16"))
    j16.grid(row=0,column=16)
    j17 = ct.CTkButton(new_root,text="j17",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(j17,0,17,"j17"))
    j17.grid(row=0,column=17)
    j18 = ct.CTkButton(new_root,text="j18",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(j18,0,18,"j18"))
    j18.grid(row=0,column=18)
    j19 = ct.CTkButton(new_root,text="j19",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(j19,0,19,"j19"))
    j19.grid(row=0,column=19)
    j20 = ct.CTkButton(new_root,text="j20",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(j20,0,20,"j20"))
    j20.grid(row=0,column=20)
    j21 = ct.CTkButton(new_root,text="j21",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(j21,0,21,"j21"))
    j21.grid(row=0,column=21)
    j22 = ct.CTkButton(new_root,text="j22",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(j22,0,22,"j22"))
    j22.grid(row=0,column=22)
    j23 = ct.CTkButton(new_root,text="j23",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(j23,0,23,"j23"))
    j23.grid(row=0,column=23)
    j24 = ct.CTkButton(new_root,text="j24",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(j24,0,24,"j24"))
    j24.grid(row=0,column=24)
    j25 = ct.CTkButton(new_root,text="j25",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(j25,0,25,"j25"))
    j25.grid(row=0,column=25)
    j26 = ct.CTkButton(new_root,text="j26",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(j26,0,26,"j26"))
    j26.grid(row=0,column=26)
    j27 = ct.CTkButton(new_root,text="j27",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(j27,0,27,"j27"))
    j27.grid(row=0,column=27)
    j28 = ct.CTkButton(new_root,text="j28",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(j28,0,28,"j28"))
    j28.grid(row=0,column=28)
    j29 = ct.CTkButton(new_root,text="j29",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(j29,0,29,"j29"))
    j29.grid(row=0,column=29)
    j30 = ct.CTkButton(new_root,text="j30",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(j30,0,30,"j30"))
    j30.grid(row=0,column=30)
    j31 = ct.CTkButton(new_root,text="j31",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(j31,0,31,"j31"))
    j31.grid(row=0,column=31)
    j32 = ct.CTkButton(new_root,text="j32",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(j32,0,32,"j32"))
    j32.grid(row=0,column=32)
    j33 = ct.CTkButton(new_root,text="j33",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(j33,0,33,"j33"))
    j33.grid(row=0,column=33)
    j34 = ct.CTkButton(new_root,text="j34",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(j34,0,34,"j34"))
    j34.grid(row=0,column=34)
    j35 = ct.CTkButton(new_root,text="j35",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(j35,0,35,"j35"))
    j35.grid(row=0,column=35)
    i1 = ct.CTkButton(new_root,text="i1",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(i1,1,1,"i1"))
    i1.grid(row=1,column=1)
    i2 = ct.CTkButton(new_root,text="i2",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(i2,1,2,"i2"))
    i2.grid(row=1,column=2)
    i3 = ct.CTkButton(new_root,text="i3",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(i3,1,3,"i3"))
    i3.grid(row=1,column=3)
    i4 = ct.CTkButton(new_root,text="i4",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(i4,1,4,"i4"))
    i4.grid(row=1,column=4)
    i5 = ct.CTkButton(new_root,text="i5",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(i5,1,5,"i5"))
    i5.grid(row=1,column=5)
    i6 = ct.CTkButton(new_root,text="i6",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(i6,1,6,"i6"))
    i6.grid(row=1,column=6)
    i7 = ct.CTkButton(new_root,text="i7",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(i7,1,7,"i7"))
    i7.grid(row=1,column=7)
    i8 = ct.CTkButton(new_root,text="i8",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(i8,1,8,"i8"))
    i8.grid(row=1,column=8)
    i9 = ct.CTkButton(new_root,text="i9",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(i9,1,9,"i9"))
    i9.grid(row=1,column=9)
    i10 = ct.CTkButton(new_root,text="i10",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(i10,1,10,"i10"))
    i10.grid(row=1,column=10)
    i11 = ct.CTkButton(new_root,text="i11",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(i11,1,11,"i11"))
    i11.grid(row=1,column=11)
    i12 = ct.CTkButton(new_root,text="i12",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(i12,1,12,"i12"))
    i12.grid(row=1,column=12)
    i13 = ct.CTkButton(new_root,text="i13",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(i13,1,13,"i13"))
    i13.grid(row=1,column=13)
    i14 = ct.CTkButton(new_root,text="i14",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(i14,1,14,"i14"))
    i14.grid(row=1,column=14)
    i15 = ct.CTkButton(new_root,text="i15",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(i15,1,15,"i15"))
    i15.grid(row=1,column=15)
    i16 = ct.CTkButton(new_root,text="i16",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(i16,1,16,"i16"))
    i16.grid(row=1,column=16)
    i17 = ct.CTkButton(new_root,text="i17",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(i17,1,17,"i17"))
    i17.grid(row=1,column=17)
    i18 = ct.CTkButton(new_root,text="i18",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(i18,1,18,"i18"))
    i18.grid(row=1,column=18)
    i19 = ct.CTkButton(new_root,text="i19",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(i19,1,19,"i19"))
    i19.grid(row=1,column=19)
    i20 = ct.CTkButton(new_root,text="i20",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(i20,1,20,"i20"))
    i20.grid(row=1,column=20)
    i21 = ct.CTkButton(new_root,text="i21",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(i21,1,21,"i21"))
    i21.grid(row=1,column=21)
    i22 = ct.CTkButton(new_root,text="i22",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(i22,1,22,"i22"))
    i22.grid(row=1,column=22)
    i23 = ct.CTkButton(new_root,text="i23",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(i23,1,23,"i23"))
    i23.grid(row=1,column=23)
    i24 = ct.CTkButton(new_root,text="i24",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(i24,1,24,"i24"))
    i24.grid(row=1,column=24)
    i25 = ct.CTkButton(new_root,text="i25",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(i25,1,25,"i25"))
    i25.grid(row=1,column=25)
    i26 = ct.CTkButton(new_root,text="i26",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(i26,1,26,"i26"))
    i26.grid(row=1,column=26)
    i27 = ct.CTkButton(new_root,text="i27",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(i27,1,27,"i27"))
    i27.grid(row=1,column=27)
    i28 = ct.CTkButton(new_root,text="i28",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(i28,1,28,"i28"))
    i28.grid(row=1,column=28)
    i29 = ct.CTkButton(new_root,text="i29",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(i29,1,29,"i29"))
    i29.grid(row=1,column=29)
    i30 = ct.CTkButton(new_root,text="i30",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(i30,1,30,"i30"))
    i30.grid(row=1,column=30)
    i31 = ct.CTkButton(new_root,text="i31",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(i31,1,31,"i31"))
    i31.grid(row=1,column=31)
    i32 = ct.CTkButton(new_root,text="i32",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(i32,1,32,"i32"))
    i32.grid(row=1,column=32)
    i33 = ct.CTkButton(new_root,text="i33",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(i33,1,33,"i33"))
    i33.grid(row=1,column=33)
    i34 = ct.CTkButton(new_root,text="i34",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(i34,1,34,"i34"))
    i34.grid(row=1,column=34)
    i35 = ct.CTkButton(new_root,text="i35",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(i35,1,35,"i35"))
    i35.grid(row=1,column=35)
    h1 = ct.CTkButton(new_root,text="h1",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(h1,2,1,"h1"))
    h1.grid(row=2,column=1)
    h2 = ct.CTkButton(new_root,text="h2",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(h2,2,2,"h2"))
    h2.grid(row=2,column=2)
    h3 = ct.CTkButton(new_root,text="h3",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(h3,2,3,"h3"))
    h3.grid(row=2,column=3)
    h4 = ct.CTkButton(new_root,text="h4",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(h4,2,4,"h4"))
    h4.grid(row=2,column=4)
    h5 = ct.CTkButton(new_root,text="h5",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(h5,2,5,"h5"))
    h5.grid(row=2,column=5)
    h6 = ct.CTkButton(new_root,text="h6",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(h6,2,6,"h6"))
    h6.grid(row=2,column=6)
    h7 = ct.CTkButton(new_root,text="h7",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(h7,2,7,"h7"))
    h7.grid(row=2,column=7)
    h8 = ct.CTkButton(new_root,text="h8",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(h8,2,8,"h8"))
    h8.grid(row=2,column=8)
    h9 = ct.CTkButton(new_root,text="h9",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(h9,2,9,"h9"))
    h9.grid(row=2,column=9)
    h10 = ct.CTkButton(new_root,text="h10",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(h10,2,10,"h10"))
    h10.grid(row=2,column=10)
    h11 = ct.CTkButton(new_root,text="h11",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(h11,2,11,"h11"))
    h11.grid(row=2,column=11)
    h12 = ct.CTkButton(new_root,text="h12",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(h12,2,12,"h12"))
    h12.grid(row=2,column=12)
    h13 = ct.CTkButton(new_root,text="h13",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(h13,2,13,"h13"))
    h13.grid(row=2,column=13)
    h14 = ct.CTkButton(new_root,text="h14",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(h14,2,14,"h14"))
    h14.grid(row=2,column=14)
    h15 = ct.CTkButton(new_root,text="h15",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(h15,2,15,"h15"))
    h15.grid(row=2,column=15)
    h16 = ct.CTkButton(new_root,text="h16",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(h16,2,16,"h16"))
    h16.grid(row=2,column=16)
    h17 = ct.CTkButton(new_root,text="h17",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(h17,2,17,"h17"))
    h17.grid(row=2,column=17)
    h18 = ct.CTkButton(new_root,text="h18",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(h18,2,18,"h18"))
    h18.grid(row=2,column=18)
    h19 = ct.CTkButton(new_root,text="h19",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(h19,2,19,"h19"))
    h19.grid(row=2,column=19)
    h20 = ct.CTkButton(new_root,text="h20",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(h20,2,20,"h20"))
    h20.grid(row=2,column=20)
    h21 = ct.CTkButton(new_root,text="h21",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(h21,2,21,"h21"))
    h21.grid(row=2,column=21)
    h22 = ct.CTkButton(new_root,text="h22",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(h22,2,22,"h22"))
    h22.grid(row=2,column=22)
    h23 = ct.CTkButton(new_root,text="h23",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(h23,2,23,"h23"))
    h23.grid(row=2,column=23)
    h24 = ct.CTkButton(new_root,text="h24",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(h24,2,24,"h24"))
    h24.grid(row=2,column=24)
    h25 = ct.CTkButton(new_root,text="h25",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(h25,2,25,"h25"))
    h25.grid(row=2,column=25)
    h26 = ct.CTkButton(new_root,text="h26",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(h26,2,26,"h26"))
    h26.grid(row=2,column=26)
    h27 = ct.CTkButton(new_root,text="h27",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(h27,2,27,"h27"))
    h27.grid(row=2,column=27)
    h28 = ct.CTkButton(new_root,text="h28",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(h28,2,28,"h28"))
    h28.grid(row=2,column=28)
    h29 = ct.CTkButton(new_root,text="h29",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(h29,2,29,"h29"))
    h29.grid(row=2,column=29)
    h30 = ct.CTkButton(new_root,text="h30",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(h30,2,30,"h30"))
    h30.grid(row=2,column=30)
    h31 = ct.CTkButton(new_root,text="h31",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(h31,2,31,"h31"))
    h31.grid(row=2,column=31)
    h32 = ct.CTkButton(new_root,text="h32",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(h32,2,32,"h32"))
    h32.grid(row=2,column=32)
    h33 = ct.CTkButton(new_root,text="h33",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(h33,2,33,"h33"))
    h33.grid(row=2,column=33)
    h34 = ct.CTkButton(new_root,text="h34",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(h34,2,34,"h34"))
    h34.grid(row=2,column=34)
    h35 = ct.CTkButton(new_root,text="h35",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(h35,2,35,"h35"))
    h35.grid(row=2,column=35)
    g1 = ct.CTkButton(new_root,text="g1",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(g1,3,1,"g1"))
    g1.grid(row=3,column=1)
    g2 = ct.CTkButton(new_root,text="g2",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(g2,3,2,"g2"))
    g2.grid(row=3,column=2)
    g3 = ct.CTkButton(new_root,text="g3",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(g3,3,3,"g3"))
    g3.grid(row=3,column=3)
    g4 = ct.CTkButton(new_root,text="g4",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(g4,3,4,"g4"))
    g4.grid(row=3,column=4)
    g5 = ct.CTkButton(new_root,text="g5",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(g5,3,5,"g5"))
    g5.grid(row=3,column=5)
    g6 = ct.CTkButton(new_root,text="g6",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(g6,3,6,"g6"))
    g6.grid(row=3,column=6)
    g7 = ct.CTkButton(new_root,text="g7",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(g7,3,7,"g7"))
    g7.grid(row=3,column=7)
    g8 = ct.CTkButton(new_root,text="g8",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(g8,3,8,"g8"))
    g8.grid(row=3,column=8)
    g9 = ct.CTkButton(new_root,text="g9",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(g9,3,9,"g9"))
    g9.grid(row=3,column=9)
    g10 = ct.CTkButton(new_root,text="g10",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(g10,3,10,"g10"))
    g10.grid(row=3,column=10)
    g11 = ct.CTkButton(new_root,text="g11",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(g11,3,11,"g11"))
    g11.grid(row=3,column=11)
    g12 = ct.CTkButton(new_root,text="g12",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(g12,3,12,"g12"))
    g12.grid(row=3,column=12)
    g13 = ct.CTkButton(new_root,text="g13",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(g13,3,13,"g13"))
    g13.grid(row=3,column=13)
    g14 = ct.CTkButton(new_root,text="g14",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(g14,3,14,"g14"))
    g14.grid(row=3,column=14)
    g15 = ct.CTkButton(new_root,text="g15",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(g15,3,15,"g15"))
    g15.grid(row=3,column=15)
    g16 = ct.CTkButton(new_root,text="g16",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(g16,3,16,"g16"))
    g16.grid(row=3,column=16)
    g17 = ct.CTkButton(new_root,text="g17",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(g17,3,17,"g17"))
    g17.grid(row=3,column=17)
    g18 = ct.CTkButton(new_root,text="g18",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(g18,3,18,"g18"))
    g18.grid(row=3,column=18)
    g19 = ct.CTkButton(new_root,text="g19",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(g19,3,19,"g19"))
    g19.grid(row=3,column=19)
    g20 = ct.CTkButton(new_root,text="g20",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(g20,3,20,"g20"))
    g20.grid(row=3,column=20)
    g21 = ct.CTkButton(new_root,text="g21",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(g21,3,21,"g21"))
    g21.grid(row=3,column=21)
    g22 = ct.CTkButton(new_root,text="g22",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(g22,3,22,"g22"))
    g22.grid(row=3,column=22)
    g23 = ct.CTkButton(new_root,text="g23",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(g23,3,23,"g23"))
    g23.grid(row=3,column=23)
    g24 = ct.CTkButton(new_root,text="g24",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(g24,3,24,"g24"))
    g24.grid(row=3,column=24)
    g25 = ct.CTkButton(new_root,text="g25",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(g25,3,25,"g25"))
    g25.grid(row=3,column=25)
    g26 = ct.CTkButton(new_root,text="g26",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(g26,3,26,"g26"))
    g26.grid(row=3,column=26)
    g27 = ct.CTkButton(new_root,text="g27",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(g27,3,27,"g27"))
    g27.grid(row=3,column=27)
    g28 = ct.CTkButton(new_root,text="g28",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(g28,3,28,"g28"))
    g28.grid(row=3,column=28)
    g29 = ct.CTkButton(new_root,text="g29",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(g29,3,29,"g29"))
    g29.grid(row=3,column=29)
    g30 = ct.CTkButton(new_root,text="g30",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(g30,3,30,"g30"))
    g30.grid(row=3,column=30)
    g31 = ct.CTkButton(new_root,text="g31",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(g31,3,31,"g31"))
    g31.grid(row=3,column=31)
    g32 = ct.CTkButton(new_root,text="g32",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(g32,3,32,"g32"))
    g32.grid(row=3,column=32)
    g33 = ct.CTkButton(new_root,text="g33",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(g33,3,33,"g33"))
    g33.grid(row=3,column=33)
    g34 = ct.CTkButton(new_root,text="g34",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(g34,3,34,"g34"))
    g34.grid(row=3,column=34)
    g35 = ct.CTkButton(new_root,text="g35",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(g35,3,35,"g35"))
    g35.grid(row=3,column=35)
    f1 = ct.CTkButton(new_root,text="f1",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(f1,4,1,"f1"))
    f1.grid(row=4,column=1)
    f2 = ct.CTkButton(new_root,text="f2",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(f2,4,2,"f2"))
    f2.grid(row=4,column=2)
    f3 = ct.CTkButton(new_root,text="f3",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(f3,4,3,"f3"))
    f3.grid(row=4,column=3)
    f4 = ct.CTkButton(new_root,text="f4",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(f4,4,4,"f4"))
    f4.grid(row=4,column=4)
    f5 = ct.CTkButton(new_root,text="f5",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(f5,4,5,"f5"))
    f5.grid(row=4,column=5)
    f6 = ct.CTkButton(new_root,text="f6",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(f6,4,6,"f6"))
    f6.grid(row=4,column=6)
    f7 = ct.CTkButton(new_root,text="f7",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(f7,4,7,"f7"))
    f7.grid(row=4,column=7)
    f8 = ct.CTkButton(new_root,text="f8",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(f8,4,8,"f8"))
    f8.grid(row=4,column=8)
    f9 = ct.CTkButton(new_root,text="f9",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(f9,4,9,"f9"))
    f9.grid(row=4,column=9)
    f10 = ct.CTkButton(new_root,text="f10",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(f10,4,10,"f10"))
    f10.grid(row=4,column=10)
    f11 = ct.CTkButton(new_root,text="f11",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(f11,4,11,"f11"))
    f11.grid(row=4,column=11)
    f12 = ct.CTkButton(new_root,text="f12",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(f12,4,12,"f12"))
    f12.grid(row=4,column=12)
    f13 = ct.CTkButton(new_root,text="f13",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(f13,4,13,"f13"))
    f13.grid(row=4,column=13)
    f14 = ct.CTkButton(new_root,text="f14",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(f14,4,14,"f14"))
    f14.grid(row=4,column=14)
    f15 = ct.CTkButton(new_root,text="f15",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(f15,4,15,"f15"))
    f15.grid(row=4,column=15)
    f16 = ct.CTkButton(new_root,text="f16",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(f16,4,16,"f16"))
    f16.grid(row=4,column=16)
    f17 = ct.CTkButton(new_root,text="f17",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(f17,4,17,"f17"))
    f17.grid(row=4,column=17)
    f18 = ct.CTkButton(new_root,text="f18",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(f18,4,18,"f18"))
    f18.grid(row=4,column=18)
    f19 = ct.CTkButton(new_root,text="f19",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(f19,4,19,"f19"))
    f19.grid(row=4,column=19)
    f20 = ct.CTkButton(new_root,text="f20",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(f20,4,20,"f20"))
    f20.grid(row=4,column=20)
    f21 = ct.CTkButton(new_root,text="f21",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(f21,4,21,"f21"))
    f21.grid(row=4,column=21)
    f22 = ct.CTkButton(new_root,text="f22",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(f22,4,22,"f22"))
    f22.grid(row=4,column=22)
    f23 = ct.CTkButton(new_root,text="f23",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(f23,4,23,"f23"))
    f23.grid(row=4,column=23)
    f24 = ct.CTkButton(new_root,text="f24",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(f24,4,24,"f24"))
    f24.grid(row=4,column=24)
    f25 = ct.CTkButton(new_root,text="f25",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(f25,4,25,"f25"))
    f25.grid(row=4,column=25)
    f26 = ct.CTkButton(new_root,text="f26",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(f26,4,26,"f26"))
    f26.grid(row=4,column=26)
    f27 = ct.CTkButton(new_root,text="f27",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(f27,4,27,"f27"))
    f27.grid(row=4,column=27)
    f28 = ct.CTkButton(new_root,text="f28",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(f28,4,28,"f28"))
    f28.grid(row=4,column=28)
    f29 = ct.CTkButton(new_root,text="f29",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(f29,4,29,"f29"))
    f29.grid(row=4,column=29)
    f30 = ct.CTkButton(new_root,text="f30",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(f30,4,30,"f30"))
    f30.grid(row=4,column=30)
    f31 = ct.CTkButton(new_root,text="f31",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(f31,4,31,"f31"))
    f31.grid(row=4,column=31)
    f32 = ct.CTkButton(new_root,text="f32",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(f32,4,32,"f32"))
    f32.grid(row=4,column=32)
    f33 = ct.CTkButton(new_root,text="f33",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(f33,4,33,"f33"))
    f33.grid(row=4,column=33)
    f34 = ct.CTkButton(new_root,text="f34",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(f34,4,34,"f34"))
    f34.grid(row=4,column=34)
    f35 = ct.CTkButton(new_root,text="f35",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(f35,4,35,"f35"))
    f35.grid(row=4,column=35)
    e1 = ct.CTkButton(new_root,text="e1",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(e1,5,1,"e1"))
    e1.grid(row=5,column=1)
    e2 = ct.CTkButton(new_root,text="e2",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(e2,5,2,"e2"))
    e2.grid(row=5,column=2)
    e3 = ct.CTkButton(new_root,text="e3",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(e3,5,3,"e3"))
    e3.grid(row=5,column=3)
    e4 = ct.CTkButton(new_root,text="e4",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(e4,5,4,"e4"))
    e4.grid(row=5,column=4)
    e5 = ct.CTkButton(new_root,text="e5",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(e5,5,5,"e5"))
    e5.grid(row=5,column=5)
    e6 = ct.CTkButton(new_root,text="e6",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(e6,5,6,"e6"))
    e6.grid(row=5,column=6)
    e7 = ct.CTkButton(new_root,text="e7",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(e7,5,7,"e7"))
    e7.grid(row=5,column=7)
    e8 = ct.CTkButton(new_root,text="e8",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(e8,5,8,"e8"))
    e8.grid(row=5,column=8)
    e9 = ct.CTkButton(new_root,text="e9",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(e9,5,9,"e9"))
    e9.grid(row=5,column=9)
    e10 = ct.CTkButton(new_root,text="e10",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(e10,5,10,"e10"))
    e10.grid(row=5,column=10)
    e11 = ct.CTkButton(new_root,text="e11",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(e11,5,11,"e11"))
    e11.grid(row=5,column=11)
    e12 = ct.CTkButton(new_root,text="e12",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(e12,5,12,"e12"))
    e12.grid(row=5,column=12)
    e13 = ct.CTkButton(new_root,text="e13",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(e13,5,13,"e13"))
    e13.grid(row=5,column=13)
    e14 = ct.CTkButton(new_root,text="e14",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(e14,5,14,"e14"))
    e14.grid(row=5,column=14)
    e15 = ct.CTkButton(new_root,text="e15",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(e15,5,15,"e15"))
    e15.grid(row=5,column=15)
    e16 = ct.CTkButton(new_root,text="e16",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(e16,5,16,"e16"))
    e16.grid(row=5,column=16)
    e17 = ct.CTkButton(new_root,text="e17",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(e17,5,17,"e17"))
    e17.grid(row=5,column=17)
    e18 = ct.CTkButton(new_root,text="e18",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(e18,5,18,"e18"))
    e18.grid(row=5,column=18)
    e19 = ct.CTkButton(new_root,text="e19",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(e19,5,19,"e19"))
    e19.grid(row=5,column=19)
    e20 = ct.CTkButton(new_root,text="e20",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(e20,5,20,"e20"))
    e20.grid(row=5,column=20)
    e21 = ct.CTkButton(new_root,text="e21",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(e21,5,21,"e21"))
    e21.grid(row=5,column=21)
    e22 = ct.CTkButton(new_root,text="e22",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(e22,5,22,"e22"))
    e22.grid(row=5,column=22)
    e23 = ct.CTkButton(new_root,text="e23",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(e23,5,23,"e23"))
    e23.grid(row=5,column=23)
    e24 = ct.CTkButton(new_root,text="e24",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(e24,5,24,"e24"))
    e24.grid(row=5,column=24)
    e25 = ct.CTkButton(new_root,text="e25",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(e25,5,25,"e25"))
    e25.grid(row=5,column=25)
    e26 = ct.CTkButton(new_root,text="e26",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(e26,5,26,"e26"))
    e26.grid(row=5,column=26)
    e27 = ct.CTkButton(new_root,text="e27",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(e27,5,27,"e27"))
    e27.grid(row=5,column=27)
    e28 = ct.CTkButton(new_root,text="e28",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(e28,5,28,"e28"))
    e28.grid(row=5,column=28)
    e29 = ct.CTkButton(new_root,text="e29",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(e29,5,29,"e29"))
    e29.grid(row=5,column=29)
    e30 = ct.CTkButton(new_root,text="e30",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(e30,5,30,"e30"))
    e30.grid(row=5,column=30)
    e31 = ct.CTkButton(new_root,text="e31",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(e31,5,31,"e31"))
    e31.grid(row=5,column=31)
    e32 = ct.CTkButton(new_root,text="e32",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(e32,5,32,"e32"))
    e32.grid(row=5,column=32)
    e33 = ct.CTkButton(new_root,text="e33",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(e33,5,33,"e33"))
    e33.grid(row=5,column=33)
    e34 = ct.CTkButton(new_root,text="e34",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(e34,5,34,"e34"))
    e34.grid(row=5,column=34)
    e35 = ct.CTkButton(new_root,text="e35",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(e35,5,35,"e35"))
    e35.grid(row=5,column=35)
    d1 = ct.CTkButton(new_root,text="d1",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(d1,6,1,"d1"))
    d1.grid(row=6,column=1)
    d2 = ct.CTkButton(new_root,text="d2",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(d2,6,2,"d2"))
    d2.grid(row=6,column=2)
    d3 = ct.CTkButton(new_root,text="d3",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(d3,6,3,"d3"))
    d3.grid(row=6,column=3)
    d4 = ct.CTkButton(new_root,text="d4",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(d4,6,4,"d4"))
    d4.grid(row=6,column=4)
    d5 = ct.CTkButton(new_root,text="d5",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(d5,6,5,"d5"))
    d5.grid(row=6,column=5)
    d6 = ct.CTkButton(new_root,text="d6",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(d6,6,6,"d6"))
    d6.grid(row=6,column=6)
    d7 = ct.CTkButton(new_root,text="d7",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(d7,6,7,"d7"))
    d7.grid(row=6,column=7)
    d8 = ct.CTkButton(new_root,text="d8",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(d8,6,8,"d8"))
    d8.grid(row=6,column=8)
    d9 = ct.CTkButton(new_root,text="d9",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(d9,6,9,"d9"))
    d9.grid(row=6,column=9)
    d10 = ct.CTkButton(new_root,text="d10",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(d10,6,10,"d10"))
    d10.grid(row=6,column=10)
    d11 = ct.CTkButton(new_root,text="d11",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(d11,6,11,"d11"))
    d11.grid(row=6,column=11)
    d12 = ct.CTkButton(new_root,text="d12",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(d12,6,12,"d12"))
    d12.grid(row=6,column=12)
    d13 = ct.CTkButton(new_root,text="d13",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(d13,6,13,"d13"))
    d13.grid(row=6,column=13)
    d14 = ct.CTkButton(new_root,text="d14",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(d14,6,14,"d14"))
    d14.grid(row=6,column=14)
    d15 = ct.CTkButton(new_root,text="d15",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(d15,6,15,"d15"))
    d15.grid(row=6,column=15)
    d16 = ct.CTkButton(new_root,text="d16",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(d16,6,16,"d16"))
    d16.grid(row=6,column=16)
    d17 = ct.CTkButton(new_root,text="d17",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(d17,6,17,"d17"))
    d17.grid(row=6,column=17)
    d18 = ct.CTkButton(new_root,text="d18",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(d18,6,18,"d18"))
    d18.grid(row=6,column=18)
    d19 = ct.CTkButton(new_root,text="d19",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(d19,6,19,"d19"))
    d19.grid(row=6,column=19)
    d20 = ct.CTkButton(new_root,text="d20",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(d20,6,20,"d20"))
    d20.grid(row=6,column=20)
    d21 = ct.CTkButton(new_root,text="d21",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(d21,6,21,"d21"))
    d21.grid(row=6,column=21)
    d22 = ct.CTkButton(new_root,text="d22",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(d22,6,22,"d22"))
    d22.grid(row=6,column=22)
    d23 = ct.CTkButton(new_root,text="d23",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(d23,6,23,"d23"))
    d23.grid(row=6,column=23)
    d24 = ct.CTkButton(new_root,text="d24",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(d24,6,24,"d24"))
    d24.grid(row=6,column=24)
    d25 = ct.CTkButton(new_root,text="d25",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(d25,6,25,"d25"))
    d25.grid(row=6,column=25)
    d26 = ct.CTkButton(new_root,text="d26",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(d26,6,26,"d26"))
    d26.grid(row=6,column=26)
    d27 = ct.CTkButton(new_root,text="d27",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(d27,6,27,"d27"))
    d27.grid(row=6,column=27)
    d28 = ct.CTkButton(new_root,text="d28",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(d28,6,28,"d28"))
    d28.grid(row=6,column=28)
    d29 = ct.CTkButton(new_root,text="d29",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(d29,6,29,"d29"))
    d29.grid(row=6,column=29)
    d30 = ct.CTkButton(new_root,text="d30",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(d30,6,30,"d30"))
    d30.grid(row=6,column=30)
    d31 = ct.CTkButton(new_root,text="d31",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(d31,6,31,"d31"))
    d31.grid(row=6,column=31)
    d32 = ct.CTkButton(new_root,text="d32",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(d32,6,32,"d32"))
    d32.grid(row=6,column=32)
    d33 = ct.CTkButton(new_root,text="d33",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(d33,6,33,"d33"))
    d33.grid(row=6,column=33)
    d34 = ct.CTkButton(new_root,text="d34",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(d34,6,34,"d34"))
    d34.grid(row=6,column=34)
    d35 = ct.CTkButton(new_root,text="d35",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(d35,6,35,"d35"))
    d35.grid(row=6,column=35)
    c1 = ct.CTkButton(new_root,text="c1",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(c1,7,1,"c1"))
    c1.grid(row=7,column=1)
    c2 = ct.CTkButton(new_root,text="c2",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(c2,7,2,"c2"))
    c2.grid(row=7,column=2)
    c3 = ct.CTkButton(new_root,text="c3",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(c3,7,3,"c3"))
    c3.grid(row=7,column=3)
    c4 = ct.CTkButton(new_root,text="c4",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(c4,7,4,"c4"))
    c4.grid(row=7,column=4)
    c5 = ct.CTkButton(new_root,text="c5",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(c5,7,5,"c5"))
    c5.grid(row=7,column=5)
    c6 = ct.CTkButton(new_root,text="c6",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(c6,7,6,"c6"))
    c6.grid(row=7,column=6)
    c7 = ct.CTkButton(new_root,text="c7",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(c7,7,7,"c7"))
    c7.grid(row=7,column=7)
    c8 = ct.CTkButton(new_root,text="c8",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(c8,7,8,"c8"))
    c8.grid(row=7,column=8)
    c9 = ct.CTkButton(new_root,text="c9",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(c9,7,9,"c9"))
    c9.grid(row=7,column=9)
    c10 = ct.CTkButton(new_root,text="c10",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(c10,7,10,"c10"))
    c10.grid(row=7,column=10)
    c11 = ct.CTkButton(new_root,text="c11",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(c11,7,11,"c11"))
    c11.grid(row=7,column=11)
    c12 = ct.CTkButton(new_root,text="c12",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(c12,7,12,"c12"))
    c12.grid(row=7,column=12)
    c13 = ct.CTkButton(new_root,text="c13",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(c13,7,13,"c13"))
    c13.grid(row=7,column=13)
    c14 = ct.CTkButton(new_root,text="c14",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(c14,7,14,"c14"))
    c14.grid(row=7,column=14)
    c15 = ct.CTkButton(new_root,text="c15",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(c15,7,15,"c15"))
    c15.grid(row=7,column=15)
    c16 = ct.CTkButton(new_root,text="c16",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(c16,7,16,"c16"))
    c16.grid(row=7,column=16)
    c17 = ct.CTkButton(new_root,text="c17",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(c17,7,17,"c17"))
    c17.grid(row=7,column=17)
    c18 = ct.CTkButton(new_root,text="c18",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(c18,7,18,"c18"))
    c18.grid(row=7,column=18)
    c19 = ct.CTkButton(new_root,text="c19",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(c19,7,19,"c19"))
    c19.grid(row=7,column=19)
    c20 = ct.CTkButton(new_root,text="c20",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(c20,7,20,"c20"))
    c20.grid(row=7,column=20)
    c21 = ct.CTkButton(new_root,text="c21",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(c21,7,21,"c21"))
    c21.grid(row=7,column=21)
    c22 = ct.CTkButton(new_root,text="c22",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(c22,7,22,"c22"))
    c22.grid(row=7,column=22)
    c23 = ct.CTkButton(new_root,text="c23",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(c23,7,23,"c23"))
    c23.grid(row=7,column=23)
    c24 = ct.CTkButton(new_root,text="c24",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(c24,7,24,"c24"))
    c24.grid(row=7,column=24)
    c25 = ct.CTkButton(new_root,text="c25",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(c25,7,25,"c25"))
    c25.grid(row=7,column=25)
    c26 = ct.CTkButton(new_root,text="c26",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(c26,7,26,"c26"))
    c26.grid(row=7,column=26)
    c27 = ct.CTkButton(new_root,text="c27",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(c27,7,27,"c27"))
    c27.grid(row=7,column=27)
    c28 = ct.CTkButton(new_root,text="c28",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(c28,7,28,"c28"))
    c28.grid(row=7,column=28)
    c29 = ct.CTkButton(new_root,text="c29",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(c29,7,29,"c29"))
    c29.grid(row=7,column=29)
    c30 = ct.CTkButton(new_root,text="c30",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(c30,7,30,"c30"))
    c30.grid(row=7,column=30)
    c31 = ct.CTkButton(new_root,text="c31",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(c31,7,31,"c31"))
    c31.grid(row=7,column=31)
    c32 = ct.CTkButton(new_root,text="c32",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(c32,7,32,"c32"))
    c32.grid(row=7,column=32)
    c33 = ct.CTkButton(new_root,text="c33",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(c33,7,33,"c33"))
    c33.grid(row=7,column=33)
    c34 = ct.CTkButton(new_root,text="c34",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(c34,7,34,"c34"))
    c34.grid(row=7,column=34)
    c35 = ct.CTkButton(new_root,text="c35",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(c35,7,35,"c35"))
    c35.grid(row=7,column=35)
    b1 = ct.CTkButton(new_root,text="b1",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(b1,8,1,"b1"))
    b1.grid(row=8,column=1)
    b2 = ct.CTkButton(new_root,text="b2",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(b2,8,2,"b2"))
    b2.grid(row=8,column=2)
    b3 = ct.CTkButton(new_root,text="b3",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(b3,8,3,"b3"))
    b3.grid(row=8,column=3)
    b4 = ct.CTkButton(new_root,text="b4",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(b4,8,4,"b4"))
    b4.grid(row=8,column=4)
    b5 = ct.CTkButton(new_root,text="b5",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(b5,8,5,"b5"))
    b5.grid(row=8,column=5)
    b6 = ct.CTkButton(new_root,text="b6",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(b6,8,6,"b6"))
    b6.grid(row=8,column=6)
    b7 = ct.CTkButton(new_root,text="b7",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(b7,8,7,"b7"))
    b7.grid(row=8,column=7)
    b8 = ct.CTkButton(new_root,text="b8",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(b8,8,8,"b8"))
    b8.grid(row=8,column=8)
    b9 = ct.CTkButton(new_root,text="b9",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(b9,8,9,"b9"))
    b9.grid(row=8,column=9)
    b10 = ct.CTkButton(new_root,text="b10",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(b10,8,10,"b10"))
    b10.grid(row=8,column=10)
    b11 = ct.CTkButton(new_root,text="b11",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(b11,8,11,"b11"))
    b11.grid(row=8,column=11)
    b12 = ct.CTkButton(new_root,text="b12",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(b12,8,12,"b12"))
    b12.grid(row=8,column=12)
    b13 = ct.CTkButton(new_root,text="b13",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(b13,8,13,"b13"))
    b13.grid(row=8,column=13)
    b14 = ct.CTkButton(new_root,text="b14",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(b14,8,14,"b14"))
    b14.grid(row=8,column=14)
    b15 = ct.CTkButton(new_root,text="b15",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(b15,8,15,"b15"))
    b15.grid(row=8,column=15)
    b16 = ct.CTkButton(new_root,text="b16",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(b16,8,16,"b16"))
    b16.grid(row=8,column=16)
    b17 = ct.CTkButton(new_root,text="b17",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(b17,8,17,"b17"))
    b17.grid(row=8,column=17)
    b18 = ct.CTkButton(new_root,text="b18",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(b18,8,18,"b18"))
    b18.grid(row=8,column=18)
    b19 = ct.CTkButton(new_root,text="b19",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(b19,8,19,"b19"))
    b19.grid(row=8,column=19)
    b20 = ct.CTkButton(new_root,text="b20",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(b20,8,20,"b20"))
    b20.grid(row=8,column=20)
    b21 = ct.CTkButton(new_root,text="b21",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(b21,8,21,"b21"))
    b21.grid(row=8,column=21)
    b22 = ct.CTkButton(new_root,text="b22",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(b22,8,22,"b22"))
    b22.grid(row=8,column=22)
    b23 = ct.CTkButton(new_root,text="b23",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(b23,8,23,"b23"))
    b23.grid(row=8,column=23)
    b24 = ct.CTkButton(new_root,text="b24",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(b24,8,24,"b24"))
    b24.grid(row=8,column=24)
    b25 = ct.CTkButton(new_root,text="b25",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(b25,8,25,"b25"))
    b25.grid(row=8,column=25)
    b26 = ct.CTkButton(new_root,text="b26",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(b26,8,26,"b26"))
    b26.grid(row=8,column=26)
    b27 = ct.CTkButton(new_root,text="b27",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(b27,8,27,"b27"))
    b27.grid(row=8,column=27)
    b28 = ct.CTkButton(new_root,text="b28",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(b28,8,28,"b28"))
    b28.grid(row=8,column=28)
    b29 = ct.CTkButton(new_root,text="b29",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(b29,8,29,"b29"))
    b29.grid(row=8,column=29)
    b30 = ct.CTkButton(new_root,text="b30",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(b30,8,30,"b30"))
    b30.grid(row=8,column=30)
    b31 = ct.CTkButton(new_root,text="b31",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(b31,8,31,"b31"))
    b31.grid(row=8,column=31)
    b32 = ct.CTkButton(new_root,text="b32",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(b32,8,32,"b32"))
    b32.grid(row=8,column=32)
    b33 = ct.CTkButton(new_root,text="b33",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(b33,8,33,"b33"))
    b33.grid(row=8,column=33)
    b34 = ct.CTkButton(new_root,text="b34",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(b34,8,34,"b34"))
    b34.grid(row=8,column=34)
    b35 = ct.CTkButton(new_root,text="b35",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(b35,8,35,"b35"))
    b35.grid(row=8,column=35)
    a1 = ct.CTkButton(new_root,text="a1",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(a1,9,1,"a1"))
    a1.grid(row=9,column=1)
    a2 = ct.CTkButton(new_root,text="a2",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(a2,9,2,"a2"))
    a2.grid(row=9,column=2)
    a3 = ct.CTkButton(new_root,text="a3",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(a3,9,3,"a3"))
    a3.grid(row=9,column=3)
    a4 = ct.CTkButton(new_root,text="a4",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(a4,9,4,"a4"))
    a4.grid(row=9,column=4)
    a5 = ct.CTkButton(new_root,text="a5",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(a5,9,5,"a5"))
    a5.grid(row=9,column=5)
    a6 = ct.CTkButton(new_root,text="a6",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(a6,9,6,"a6"))
    a6.grid(row=9,column=6)
    a7 = ct.CTkButton(new_root,text="a7",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(a7,9,7,"a7"))
    a7.grid(row=9,column=7)
    a8 = ct.CTkButton(new_root,text="a8",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(a8,9,8,"a8"))
    a8.grid(row=9,column=8)
    a9 = ct.CTkButton(new_root,text="a9",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(a9,9,9,"a9"))
    a9.grid(row=9,column=9)
    a10 = ct.CTkButton(new_root,text="a10",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(a10,9,10,"a10"))
    a10.grid(row=9,column=10)
    a11 = ct.CTkButton(new_root,text="a11",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(a11,9,11,"a11"))
    a11.grid(row=9,column=11)
    a12 = ct.CTkButton(new_root,text="a12",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(a12,9,12,"a12"))
    a12.grid(row=9,column=12)
    a13 = ct.CTkButton(new_root,text="a13",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(a13,9,13,"a13"))
    a13.grid(row=9,column=13)
    a14 = ct.CTkButton(new_root,text="a14",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(a14,9,14,"a14"))
    a14.grid(row=9,column=14)
    a15 = ct.CTkButton(new_root,text="a15",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(a15,9,15,"a15"))
    a15.grid(row=9,column=15)
    a16 = ct.CTkButton(new_root,text="a16",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(a16,9,16,"a16"))
    a16.grid(row=9,column=16)
    a17 = ct.CTkButton(new_root,text="a17",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(a17,9,17,"a17"))
    a17.grid(row=9,column=17)
    a18 = ct.CTkButton(new_root,text="a18",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(a18,9,18,"a18"))
    a18.grid(row=9,column=18)
    a19 = ct.CTkButton(new_root,text="a19",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(a19,9,19,"a19"))
    a19.grid(row=9,column=19)
    a20 = ct.CTkButton(new_root,text="a20",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(a20,9,20,"a20"))
    a20.grid(row=9,column=20)
    a21 = ct.CTkButton(new_root,text="a21",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(a21,9,21,"a21"))
    a21.grid(row=9,column=21)
    a22 = ct.CTkButton(new_root,text="a22",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(a22,9,22,"a22"))
    a22.grid(row=9,column=22)
    a23 = ct.CTkButton(new_root,text="a23",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(a23,9,23,"a23"))
    a23.grid(row=9,column=23)
    a24 = ct.CTkButton(new_root,text="a24",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(a24,9,24,"a24"))
    a24.grid(row=9,column=24)
    a25 = ct.CTkButton(new_root,text="a25",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(a25,9,25,"a25"))
    a25.grid(row=9,column=25)
    a26 = ct.CTkButton(new_root,text="a26",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(a26,9,26,"a26"))
    a26.grid(row=9,column=26)
    a27 = ct.CTkButton(new_root,text="a27",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(a27,9,27,"a27"))
    a27.grid(row=9,column=27)
    a28 = ct.CTkButton(new_root,text="a28",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(a28,9,28,"a28"))
    a28.grid(row=9,column=28)
    a29 = ct.CTkButton(new_root,text="a29",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(a29,9,29,"a29"))
    a29.grid(row=9,column=29)
    a30 = ct.CTkButton(new_root,text="a30",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(a30,9,30,"a30"))
    a30.grid(row=9,column=30)
    a31 = ct.CTkButton(new_root,text="a31",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(a31,9,31,"a31"))
    a31.grid(row=9,column=31)
    a32 = ct.CTkButton(new_root,text="a32",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(a32,9,32,"a32"))
    a32.grid(row=9,column=32)
    a33 = ct.CTkButton(new_root,text="a33",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(a33,9,33,"a33"))
    a33.grid(row=9,column=33)
    a34 = ct.CTkButton(new_root,text="a34",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(a34,9,34,"a34"))
    a34.grid(row=9,column=34)
    a35 = ct.CTkButton(new_root,text="a35",fg_color="transparent",width=1,height=1,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on(a35,9,35,"a35"))
    a35.grid(row=9,column=35)
    global k
    k =[]
    with open("newfile2.dat","rb") as f:
        while True:
            try:
                s= pickle.load(f)
                k.append(s)
            except:
                break
    for g in k:
        for k in g:
           if k == movie_pack:
               for i in g[k]:
                if i == "j1":
                   j1.configure(state="disabled",fg_color="green")
                if i == "j2":
                   j2.configure(state="disabled",fg_color="green")
                if i == "j3":
                   j3.configure(state="disabled",fg_color="green")
                if i == "j4":
                   j4.configure(state="disabled",fg_color="green")
                if i == "j5":
                   j5.configure(state="disabled",fg_color="green")
                if i == "j6":
                   j6.configure(state="disabled",fg_color="green")
                if i == "j7":
                   j7.configure(state="disabled",fg_color="green")
                if i == "j8":
                   j8.configure(state="disabled",fg_color="green")
                if i == "j9":
                   j9.configure(state="disabled",fg_color="green")
                if i == "j10":
                   j10.configure(state="disabled",fg_color="green")
                if i == "j11":
                   j11.configure(state="disabled",fg_color="green")
                if i == "j12":
                   j12.configure(state="disabled",fg_color="green")
                if i == "j13":
                   j13.configure(state="disabled",fg_color="green")
                if i == "j14":
                   j14.configure(state="disabled",fg_color="green")
                if i == "j15":
                   j15.configure(state="disabled",fg_color="green")
                if i == "j16":
                   j16.configure(state="disabled",fg_color="green")
                if i == "j17":
                   j17.configure(state="disabled",fg_color="green")
                if i == "j18":
                   j18.configure(state="disabled",fg_color="green")
                if i == "j19":
                   j19.configure(state="disabled",fg_color="green")
                if i == "j20":
                   j20.configure(state="disabled",fg_color="green")
                if i == "j21":
                   j21.configure(state="disabled",fg_color="green")
                if i == "j22":
                   j22.configure(state="disabled",fg_color="green")
                if i == "j23":
                   j23.configure(state="disabled",fg_color="green")
                if i == "j24":
                   j24.configure(state="disabled",fg_color="green")
                if i == "j25":
                   j25.configure(state="disabled",fg_color="green")
                if i == "j26":
                   j26.configure(state="disabled",fg_color="green")
                if i == "j27":
                   j27.configure(state="disabled",fg_color="green")
                if i == "j28":
                   j28.configure(state="disabled",fg_color="green")
                if i == "j29":
                   j29.configure(state="disabled",fg_color="green")
                if i == "j30":
                   j30.configure(state="disabled",fg_color="green")
                if i == "j31":
                   j31.configure(state="disabled",fg_color="green")
                if i == "j32":
                   j32.configure(state="disabled",fg_color="green")
                if i == "j33":
                   j33.configure(state="disabled",fg_color="green")
                if i == "j34":
                   j34.configure(state="disabled",fg_color="green")
                if i == "j35":
                   j35.configure(state="disabled",fg_color="green")
                if i == "j36":
                   j36.configure(state="disabled",fg_color="green")
                if i == "j37":
                   j37.configure(state="disabled",fg_color="green")
                if i == "j38":
                   j38.configure(state="disabled",fg_color="green")
                if i == "j39":
                   j39.configure(state="disabled",fg_color="green")
                if i == "j40":
                   j40.configure(state="disabled",fg_color="green")
                if i == "j41":
                   j41.configure(state="disabled",fg_color="green")
                if i == "j42":
                   j42.configure(state="disabled",fg_color="green")
                if i == "j43":
                   j43.configure(state="disabled",fg_color="green")
                if i == "j44":
                   j44.configure(state="disabled",fg_color="green")
                if i == "j45":
                   j45.configure(state="disabled",fg_color="green")
                if i == "j46":
                   j46.configure(state="disabled",fg_color="green")
                if i == "j47":
                   j47.configure(state="disabled",fg_color="green")
                if i == "j48":
                   j48.configure(state="disabled",fg_color="green")
                if i == "j49":
                   j49.configure(state="disabled",fg_color="green")
                if i == "j50":
                   j50.configure(state="disabled",fg_color="green")
                if i == "i1":
                   i1.configure(state="disabled",fg_color="green")
                if i == "i2":
                   i2.configure(state="disabled",fg_color="green")
                if i == "i3":
                   i3.configure(state="disabled",fg_color="green")
                if i == "i4":
                   i4.configure(state="disabled",fg_color="green")
                if i == "i5":
                   i5.configure(state="disabled",fg_color="green")
                if i == "i6":
                   i6.configure(state="disabled",fg_color="green")
                if i == "i7":
                   i7.configure(state="disabled",fg_color="green")
                if i == "i8":
                   i8.configure(state="disabled",fg_color="green")
                if i == "i9":
                   i9.configure(state="disabled",fg_color="green")
                if i == "i10":
                   i10.configure(state="disabled",fg_color="green")
                if i == "i11":
                   i11.configure(state="disabled",fg_color="green")
                if i == "i12":
                   i12.configure(state="disabled",fg_color="green")
                if i == "i13":
                   i13.configure(state="disabled",fg_color="green")
                if i == "i14":
                   i14.configure(state="disabled",fg_color="green")
                if i == "i15":
                   i15.configure(state="disabled",fg_color="green")
                if i == "i16":
                   i16.configure(state="disabled",fg_color="green")
                if i == "i17":
                   i17.configure(state="disabled",fg_color="green")
                if i == "i18":
                   i18.configure(state="disabled",fg_color="green")
                if i == "i19":
                   i19.configure(state="disabled",fg_color="green")
                if i == "i20":
                   i20.configure(state="disabled",fg_color="green")
                if i == "i21":
                   i21.configure(state="disabled",fg_color="green")
                if i == "i22":
                   i22.configure(state="disabled",fg_color="green")
                if i == "i23":
                   i23.configure(state="disabled",fg_color="green")
                if i == "i24":
                   i24.configure(state="disabled",fg_color="green")
                if i == "i25":
                   i25.configure(state="disabled",fg_color="green")
                if i == "i26":
                   i26.configure(state="disabled",fg_color="green")
                if i == "i27":
                   i27.configure(state="disabled",fg_color="green")
                if i == "i28":
                   i28.configure(state="disabled",fg_color="green")
                if i == "i29":
                   i29.configure(state="disabled",fg_color="green")
                if i == "i30":
                   i30.configure(state="disabled",fg_color="green")
                if i == "i31":
                   i31.configure(state="disabled",fg_color="green")
                if i == "i32":
                   i32.configure(state="disabled",fg_color="green")
                if i == "i33":
                   i33.configure(state="disabled",fg_color="green")
                if i == "i34":
                   i34.configure(state="disabled",fg_color="green")
                if i == "i35":
                   i35.configure(state="disabled",fg_color="green")
                if i == "i36":
                   i36.configure(state="disabled",fg_color="green")
                if i == "i37":
                   i37.configure(state="disabled",fg_color="green")
                if i == "i38":
                   i38.configure(state="disabled",fg_color="green")
                if i == "i39":
                   i39.configure(state="disabled",fg_color="green")
                if i == "i40":
                   i40.configure(state="disabled",fg_color="green")
                if i == "i41":
                   i41.configure(state="disabled",fg_color="green")
                if i == "i42":
                   i42.configure(state="disabled",fg_color="green")
                if i == "i43":
                   i43.configure(state="disabled",fg_color="green")
                if i == "i44":
                   i44.configure(state="disabled",fg_color="green")
                if i == "i45":
                   i45.configure(state="disabled",fg_color="green")
                if i == "i46":
                   i46.configure(state="disabled",fg_color="green")
                if i == "i47":
                   i47.configure(state="disabled",fg_color="green")
                if i == "i48":
                   i48.configure(state="disabled",fg_color="green")
                if i == "i49":
                   i49.configure(state="disabled",fg_color="green")
                if i == "i50":
                   i50.configure(state="disabled",fg_color="green")
                if i == "h1":
                   h1.configure(state="disabled",fg_color="green")
                if i == "h2":
                   h2.configure(state="disabled",fg_color="green")
                if i == "h3":
                   h3.configure(state="disabled",fg_color="green")
                if i == "h4":
                   h4.configure(state="disabled",fg_color="green")
                if i == "h5":
                   h5.configure(state="disabled",fg_color="green")
                if i == "h6":
                   h6.configure(state="disabled",fg_color="green")
                if i == "h7":
                   h7.configure(state="disabled",fg_color="green")
                if i == "h8":
                   h8.configure(state="disabled",fg_color="green")
                if i == "h9":
                   h9.configure(state="disabled",fg_color="green")
                if i == "h10":
                   h10.configure(state="disabled",fg_color="green")
                if i == "h11":
                   h11.configure(state="disabled",fg_color="green")
                if i == "h12":
                   h12.configure(state="disabled",fg_color="green")
                if i == "h13":
                   h13.configure(state="disabled",fg_color="green")
                if i == "h14":
                   h14.configure(state="disabled",fg_color="green")
                if i == "h15":
                   h15.configure(state="disabled",fg_color="green")
                if i == "h16":
                   h16.configure(state="disabled",fg_color="green")
                if i == "h17":
                   h17.configure(state="disabled",fg_color="green")
                if i == "h18":
                   h18.configure(state="disabled",fg_color="green")
                if i == "h19":
                   h19.configure(state="disabled",fg_color="green")
                if i == "h20":
                   h20.configure(state="disabled",fg_color="green")
                if i == "h21":
                   h21.configure(state="disabled",fg_color="green")
                if i == "h22":
                   h22.configure(state="disabled",fg_color="green")
                if i == "h23":
                   h23.configure(state="disabled",fg_color="green")
                if i == "h24":
                   h24.configure(state="disabled",fg_color="green")
                if i == "h25":
                   h25.configure(state="disabled",fg_color="green")
                if i == "h26":
                   h26.configure(state="disabled",fg_color="green")
                if i == "h27":
                   h27.configure(state="disabled",fg_color="green")
                if i == "h28":
                   h28.configure(state="disabled",fg_color="green")
                if i == "h29":
                   h29.configure(state="disabled",fg_color="green")
                if i == "h30":
                   h30.configure(state="disabled",fg_color="green")
                if i == "h31":
                   h31.configure(state="disabled",fg_color="green")
                if i == "h32":
                   h32.configure(state="disabled",fg_color="green")
                if i == "h33":
                   h33.configure(state="disabled",fg_color="green")
                if i == "h34":
                   h34.configure(state="disabled",fg_color="green")
                if i == "h35":
                   h35.configure(state="disabled",fg_color="green")
                if i == "h36":
                   h36.configure(state="disabled",fg_color="green")
                if i == "h37":
                   h37.configure(state="disabled",fg_color="green")
                if i == "h38":
                   h38.configure(state="disabled",fg_color="green")
                if i == "h39":
                   h39.configure(state="disabled",fg_color="green")
                if i == "h40":
                   h40.configure(state="disabled",fg_color="green")
                if i == "h41":
                   h41.configure(state="disabled",fg_color="green")
                if i == "h42":
                   h42.configure(state="disabled",fg_color="green")
                if i == "h43":
                   h43.configure(state="disabled",fg_color="green")
                if i == "h44":
                   h44.configure(state="disabled",fg_color="green")
                if i == "h45":
                   h45.configure(state="disabled",fg_color="green")
                if i == "h46":
                   h46.configure(state="disabled",fg_color="green")
                if i == "h47":
                   h47.configure(state="disabled",fg_color="green")
                if i == "h48":
                   h48.configure(state="disabled",fg_color="green")
                if i == "h49":
                   h49.configure(state="disabled",fg_color="green")
                if i == "h50":
                   h50.configure(state="disabled",fg_color="green")
                if i == "g1":
                   g1.configure(state="disabled",fg_color="green")
                if i == "g2":
                   g2.configure(state="disabled",fg_color="green")
                if i == "g3":
                   g3.configure(state="disabled",fg_color="green")
                if i == "g4":
                   g4.configure(state="disabled",fg_color="green")
                if i == "g5":
                   g5.configure(state="disabled",fg_color="green")
                if i == "g6":
                   g6.configure(state="disabled",fg_color="green")
                if i == "g7":
                   g7.configure(state="disabled",fg_color="green")
                if i == "g8":
                   g8.configure(state="disabled",fg_color="green")
                if i == "g9":
                   g9.configure(state="disabled",fg_color="green")
                if i == "g10":
                   g10.configure(state="disabled",fg_color="green")
                if i == "g11":
                   g11.configure(state="disabled",fg_color="green")
                if i == "g12":
                   g12.configure(state="disabled",fg_color="green")
                if i == "g13":
                   g13.configure(state="disabled",fg_color="green")
                if i == "g14":
                   g14.configure(state="disabled",fg_color="green")
                if i == "g15":
                   g15.configure(state="disabled",fg_color="green")
                if i == "g16":
                   g16.configure(state="disabled",fg_color="green")
                if i == "g17":
                   g17.configure(state="disabled",fg_color="green")
                if i == "g18":
                   g18.configure(state="disabled",fg_color="green")
                if i == "g19":
                   g19.configure(state="disabled",fg_color="green")
                if i == "g20":
                   g20.configure(state="disabled",fg_color="green")
                if i == "g21":
                   g21.configure(state="disabled",fg_color="green")
                if i == "g22":
                   g22.configure(state="disabled",fg_color="green")
                if i == "g23":
                   g23.configure(state="disabled",fg_color="green")
                if i == "g24":
                   g24.configure(state="disabled",fg_color="green")
                if i == "g25":
                   g25.configure(state="disabled",fg_color="green")
                if i == "g26":
                   g26.configure(state="disabled",fg_color="green")
                if i == "g27":
                   g27.configure(state="disabled",fg_color="green")
                if i == "g28":
                   g28.configure(state="disabled",fg_color="green")
                if i == "g29":
                   g29.configure(state="disabled",fg_color="green")
                if i == "g30":
                   g30.configure(state="disabled",fg_color="green")
                if i == "g31":
                   g31.configure(state="disabled",fg_color="green")
                if i == "g32":
                   g32.configure(state="disabled",fg_color="green")
                if i == "g33":
                   g33.configure(state="disabled",fg_color="green")
                if i == "g34":
                   g34.configure(state="disabled",fg_color="green")
                if i == "g35":
                   g35.configure(state="disabled",fg_color="green")
                if i == "g36":
                   g36.configure(state="disabled",fg_color="green")
                if i == "g37":
                   g37.configure(state="disabled",fg_color="green")
                if i == "g38":
                   g38.configure(state="disabled",fg_color="green")
                if i == "g39":
                   g39.configure(state="disabled",fg_color="green")
                if i == "g40":
                   g40.configure(state="disabled",fg_color="green")
                if i == "g41":
                   g41.configure(state="disabled",fg_color="green")
                if i == "g42":
                   g42.configure(state="disabled",fg_color="green")
                if i == "g43":
                   g43.configure(state="disabled",fg_color="green")
                if i == "g44":
                   g44.configure(state="disabled",fg_color="green")
                if i == "g45":
                   g45.configure(state="disabled",fg_color="green")
                if i == "g46":
                   g46.configure(state="disabled",fg_color="green")
                if i == "g47":
                   g47.configure(state="disabled",fg_color="green")
                if i == "g48":
                   g48.configure(state="disabled",fg_color="green")
                if i == "g49":
                   g49.configure(state="disabled",fg_color="green")
                if i == "g50":
                   g50.configure(state="disabled",fg_color="green")
                if i == "f1":
                   f1.configure(state="disabled",fg_color="green")
                if i == "f2":
                   f2.configure(state="disabled",fg_color="green")
                if i == "f3":
                   f3.configure(state="disabled",fg_color="green")
                if i == "f4":
                   f4.configure(state="disabled",fg_color="green")
                if i == "f5":
                   f5.configure(state="disabled",fg_color="green")
                if i == "f6":
                   f6.configure(state="disabled",fg_color="green")
                if i == "f7":
                   f7.configure(state="disabled",fg_color="green")
                if i == "f8":
                   f8.configure(state="disabled",fg_color="green")
                if i == "f9":
                   f9.configure(state="disabled",fg_color="green")
                if i == "f10":
                   f10.configure(state="disabled",fg_color="green")
                if i == "f11":
                   f11.configure(state="disabled",fg_color="green")
                if i == "f12":
                   f12.configure(state="disabled",fg_color="green")
                if i == "f13":
                   f13.configure(state="disabled",fg_color="green")
                if i == "f14":
                   f14.configure(state="disabled",fg_color="green")
                if i == "f15":
                   f15.configure(state="disabled",fg_color="green")
                if i == "f16":
                   f16.configure(state="disabled",fg_color="green")
                if i == "f17":
                   f17.configure(state="disabled",fg_color="green")
                if i == "f18":
                   f18.configure(state="disabled",fg_color="green")
                if i == "f19":
                   f19.configure(state="disabled",fg_color="green")
                if i == "f20":
                   f20.configure(state="disabled",fg_color="green")
                if i == "f21":
                   f21.configure(state="disabled",fg_color="green")
                if i == "f22":
                   f22.configure(state="disabled",fg_color="green")
                if i == "f23":
                   f23.configure(state="disabled",fg_color="green")
                if i == "f24":
                   f24.configure(state="disabled",fg_color="green")
                if i == "f25":
                   f25.configure(state="disabled",fg_color="green")
                if i == "f26":
                   f26.configure(state="disabled",fg_color="green")
                if i == "f27":
                   f27.configure(state="disabled",fg_color="green")
                if i == "f28":
                   f28.configure(state="disabled",fg_color="green")
                if i == "f29":
                   f29.configure(state="disabled",fg_color="green")
                if i == "f30":
                   f30.configure(state="disabled",fg_color="green")
                if i == "f31":
                   f31.configure(state="disabled",fg_color="green")
                if i == "f32":
                   f32.configure(state="disabled",fg_color="green")
                if i == "f33":
                   f33.configure(state="disabled",fg_color="green")
                if i == "f34":
                   f34.configure(state="disabled",fg_color="green")
                if i == "f35":
                   f35.configure(state="disabled",fg_color="green")
                if i == "f36":
                   f36.configure(state="disabled",fg_color="green")
                if i == "f37":
                   f37.configure(state="disabled",fg_color="green")
                if i == "f38":
                   f38.configure(state="disabled",fg_color="green")
                if i == "f39":
                   f39.configure(state="disabled",fg_color="green")
                if i == "f40":
                   f40.configure(state="disabled",fg_color="green")
                if i == "f41":
                   f41.configure(state="disabled",fg_color="green")
                if i == "f42":
                   f42.configure(state="disabled",fg_color="green")
                if i == "f43":
                   f43.configure(state="disabled",fg_color="green")
                if i == "f44":
                   f44.configure(state="disabled",fg_color="green")
                if i == "f45":
                   f45.configure(state="disabled",fg_color="green")
                if i == "f46":
                   f46.configure(state="disabled",fg_color="green")
                if i == "f47":
                   f47.configure(state="disabled",fg_color="green")
                if i == "f48":
                   f48.configure(state="disabled",fg_color="green")
                if i == "f49":
                   f49.configure(state="disabled",fg_color="green")
                if i == "f50":
                   f50.configure(state="disabled",fg_color="green")
                if i == "e1":
                   e1.configure(state="disabled",fg_color="green")
                if i == "e2":
                   e2.configure(state="disabled",fg_color="green")
                if i == "e3":
                   e3.configure(state="disabled",fg_color="green")
                if i == "e4":
                   e4.configure(state="disabled",fg_color="green")
                if i == "e5":
                   e5.configure(state="disabled",fg_color="green")
                if i == "e6":
                   e6.configure(state="disabled",fg_color="green")
                if i == "e7":
                   e7.configure(state="disabled",fg_color="green")
                if i == "e8":
                   e8.configure(state="disabled",fg_color="green")
                if i == "e9":
                   e9.configure(state="disabled",fg_color="green")
                if i == "e10":
                   e10.configure(state="disabled",fg_color="green")
                if i == "e11":
                   e11.configure(state="disabled",fg_color="green")
                if i == "e12":
                   e12.configure(state="disabled",fg_color="green")
                if i == "e13":
                   e13.configure(state="disabled",fg_color="green")
                if i == "e14":
                   e14.configure(state="disabled",fg_color="green")
                if i == "e15":
                   e15.configure(state="disabled",fg_color="green")
                if i == "e16":
                   e16.configure(state="disabled",fg_color="green")
                if i == "e17":
                   e17.configure(state="disabled",fg_color="green")
                if i == "e18":
                   e18.configure(state="disabled",fg_color="green")
                if i == "e19":
                   e19.configure(state="disabled",fg_color="green")
                if i == "e20":
                   e20.configure(state="disabled",fg_color="green")
                if i == "e21":
                   e21.configure(state="disabled",fg_color="green")
                if i == "e22":
                   e22.configure(state="disabled",fg_color="green")
                if i == "e23":
                   e23.configure(state="disabled",fg_color="green")
                if i == "e24":
                   e24.configure(state="disabled",fg_color="green")
                if i == "e25":
                   e25.configure(state="disabled",fg_color="green")
                if i == "e26":
                   e26.configure(state="disabled",fg_color="green")
                if i == "e27":
                   e27.configure(state="disabled",fg_color="green")
                if i == "e28":
                   e28.configure(state="disabled",fg_color="green")
                if i == "e29":
                   e29.configure(state="disabled",fg_color="green")
                if i == "e30":
                   e30.configure(state="disabled",fg_color="green")
                if i == "e31":
                   e31.configure(state="disabled",fg_color="green")
                if i == "e32":
                   e32.configure(state="disabled",fg_color="green")
                if i == "e33":
                   e33.configure(state="disabled",fg_color="green")
                if i == "e34":
                   e34.configure(state="disabled",fg_color="green")
                if i == "e35":
                   e35.configure(state="disabled",fg_color="green")
                if i == "e36":
                   e36.configure(state="disabled",fg_color="green")
                if i == "e37":
                   e37.configure(state="disabled",fg_color="green")
                if i == "e38":
                   e38.configure(state="disabled",fg_color="green")
                if i == "e39":
                   e39.configure(state="disabled",fg_color="green")
                if i == "e40":
                   e40.configure(state="disabled",fg_color="green")
                if i == "e41":
                   e41.configure(state="disabled",fg_color="green")
                if i == "e42":
                   e42.configure(state="disabled",fg_color="green")
                if i == "e43":
                   e43.configure(state="disabled",fg_color="green")
                if i == "e44":
                   e44.configure(state="disabled",fg_color="green")
                if i == "e45":
                   e45.configure(state="disabled",fg_color="green")
                if i == "e46":
                   e46.configure(state="disabled",fg_color="green")
                if i == "e47":
                   e47.configure(state="disabled",fg_color="green")
                if i == "e48":
                   e48.configure(state="disabled",fg_color="green")
                if i == "e49":
                   e49.configure(state="disabled",fg_color="green")
                if i == "e50":
                   e50.configure(state="disabled",fg_color="green")
                if i == "d1":
                   d1.configure(state="disabled",fg_color="green")
                if i == "d2":
                   d2.configure(state="disabled",fg_color="green")
                if i == "d3":
                   d3.configure(state="disabled",fg_color="green")
                if i == "d4":
                   d4.configure(state="disabled",fg_color="green")
                if i == "d5":
                   d5.configure(state="disabled",fg_color="green")
                if i == "d6":
                   d6.configure(state="disabled",fg_color="green")
                if i == "d7":
                   d7.configure(state="disabled",fg_color="green")
                if i == "d8":
                   d8.configure(state="disabled",fg_color="green")
                if i == "d9":
                   d9.configure(state="disabled",fg_color="green")
                if i == "d10":
                   d10.configure(state="disabled",fg_color="green")
                if i == "d11":
                   d11.configure(state="disabled",fg_color="green")
                if i == "d12":
                   d12.configure(state="disabled",fg_color="green")
                if i == "d13":
                   d13.configure(state="disabled",fg_color="green")
                if i == "d14":
                   d14.configure(state="disabled",fg_color="green")
                if i == "d15":
                   d15.configure(state="disabled",fg_color="green")
                if i == "d16":
                   d16.configure(state="disabled",fg_color="green")
                if i == "d17":
                   d17.configure(state="disabled",fg_color="green")
                if i == "d18":
                   d18.configure(state="disabled",fg_color="green")
                if i == "d19":
                   d19.configure(state="disabled",fg_color="green")
                if i == "d20":
                   d20.configure(state="disabled",fg_color="green")
                if i == "d21":
                   d21.configure(state="disabled",fg_color="green")
                if i == "d22":
                   d22.configure(state="disabled",fg_color="green")
                if i == "d23":
                   d23.configure(state="disabled",fg_color="green")
                if i == "d24":
                   d24.configure(state="disabled",fg_color="green")
                if i == "d25":
                   d25.configure(state="disabled",fg_color="green")
                if i == "d26":
                   d26.configure(state="disabled",fg_color="green")
                if i == "d27":
                   d27.configure(state="disabled",fg_color="green")
                if i == "d28":
                   d28.configure(state="disabled",fg_color="green")
                if i == "d29":
                   d29.configure(state="disabled",fg_color="green")
                if i == "d30":
                   d30.configure(state="disabled",fg_color="green")
                if i == "d31":
                   d31.configure(state="disabled",fg_color="green")
                if i == "d32":
                   d32.configure(state="disabled",fg_color="green")
                if i == "d33":
                   d33.configure(state="disabled",fg_color="green")
                if i == "d34":
                   d34.configure(state="disabled",fg_color="green")
                if i == "d35":
                   d35.configure(state="disabled",fg_color="green")
                if i == "d36":
                   d36.configure(state="disabled",fg_color="green")
                if i == "d37":
                   d37.configure(state="disabled",fg_color="green")
                if i == "d38":
                   d38.configure(state="disabled",fg_color="green")
                if i == "d39":
                   d39.configure(state="disabled",fg_color="green")
                if i == "d40":
                   d40.configure(state="disabled",fg_color="green")
                if i == "d41":
                   d41.configure(state="disabled",fg_color="green")
                if i == "d42":
                   d42.configure(state="disabled",fg_color="green")
                if i == "d43":
                   d43.configure(state="disabled",fg_color="green")
                if i == "d44":
                   d44.configure(state="disabled",fg_color="green")
                if i == "d45":
                   d45.configure(state="disabled",fg_color="green")
                if i == "d46":
                   d46.configure(state="disabled",fg_color="green")
                if i == "d47":
                   d47.configure(state="disabled",fg_color="green")
                if i == "d48":
                   d48.configure(state="disabled",fg_color="green")
                if i == "d49":
                   d49.configure(state="disabled",fg_color="green")
                if i == "d50":
                   d50.configure(state="disabled",fg_color="green")
                if i == "c1":
                   c1.configure(state="disabled",fg_color="green")
                if i == "c2":
                   c2.configure(state="disabled",fg_color="green")
                if i == "c3":
                   c3.configure(state="disabled",fg_color="green")
                if i == "c4":
                   c4.configure(state="disabled",fg_color="green")
                if i == "c5":
                   c5.configure(state="disabled",fg_color="green")
                if i == "c6":
                   c6.configure(state="disabled",fg_color="green")
                if i == "c7":
                   c7.configure(state="disabled",fg_color="green")
                if i == "c8":
                   c8.configure(state="disabled",fg_color="green")
                if i == "c9":
                   c9.configure(state="disabled",fg_color="green")
                if i == "c10":
                   c10.configure(state="disabled",fg_color="green")
                if i == "c11":
                   c11.configure(state="disabled",fg_color="green")
                if i == "c12":
                   c12.configure(state="disabled",fg_color="green")
                if i == "c13":
                   c13.configure(state="disabled",fg_color="green")
                if i == "c14":
                   c14.configure(state="disabled",fg_color="green")
                if i == "c15":
                   c15.configure(state="disabled",fg_color="green")
                if i == "c16":
                   c16.configure(state="disabled",fg_color="green")
                if i == "c17":
                   c17.configure(state="disabled",fg_color="green")
                if i == "c18":
                   c18.configure(state="disabled",fg_color="green")
                if i == "c19":
                   c19.configure(state="disabled",fg_color="green")
                if i == "c20":
                   c20.configure(state="disabled",fg_color="green")
                if i == "c21":
                   c21.configure(state="disabled",fg_color="green")
                if i == "c22":
                   c22.configure(state="disabled",fg_color="green")
                if i == "c23":
                   c23.configure(state="disabled",fg_color="green")
                if i == "c24":
                   c24.configure(state="disabled",fg_color="green")
                if i == "c25":
                   c25.configure(state="disabled",fg_color="green")
                if i == "c26":
                   c26.configure(state="disabled",fg_color="green")
                if i == "c27":
                   c27.configure(state="disabled",fg_color="green")
                if i == "c28":
                   c28.configure(state="disabled",fg_color="green")
                if i == "c29":
                   c29.configure(state="disabled",fg_color="green")
                if i == "c30":
                   c30.configure(state="disabled",fg_color="green")
                if i == "c31":
                   c31.configure(state="disabled",fg_color="green")
                if i == "c32":
                   c32.configure(state="disabled",fg_color="green")
                if i == "c33":
                   c33.configure(state="disabled",fg_color="green")
                if i == "c34":
                   c34.configure(state="disabled",fg_color="green")
                if i == "c35":
                   c35.configure(state="disabled",fg_color="green")
                if i == "c36":
                   c36.configure(state="disabled",fg_color="green")
                if i == "c37":
                   c37.configure(state="disabled",fg_color="green")
                if i == "c38":
                   c38.configure(state="disabled",fg_color="green")
                if i == "c39":
                   c39.configure(state="disabled",fg_color="green")
                if i == "c40":
                   c40.configure(state="disabled",fg_color="green")
                if i == "c41":
                   c41.configure(state="disabled",fg_color="green")
                if i == "c42":
                   c42.configure(state="disabled",fg_color="green")
                if i == "c43":
                   c43.configure(state="disabled",fg_color="green")
                if i == "c44":
                   c44.configure(state="disabled",fg_color="green")
                if i == "c45":
                   c45.configure(state="disabled",fg_color="green")
                if i == "c46":
                   c46.configure(state="disabled",fg_color="green")
                if i == "c47":
                   c47.configure(state="disabled",fg_color="green")
                if i == "c48":
                   c48.configure(state="disabled",fg_color="green")
                if i == "c49":
                   c49.configure(state="disabled",fg_color="green")
                if i == "c50":
                   c50.configure(state="disabled",fg_color="green")
                if i == "b1":
                   b1.configure(state="disabled",fg_color="green")
                if i == "b2":
                   b2.configure(state="disabled",fg_color="green")
                if i == "b3":
                   b3.configure(state="disabled",fg_color="green")
                if i == "b4":
                   b4.configure(state="disabled",fg_color="green")
                if i == "b5":
                   b5.configure(state="disabled",fg_color="green")
                if i == "b6":
                   b6.configure(state="disabled",fg_color="green")
                if i == "b7":
                   b7.configure(state="disabled",fg_color="green")
                if i == "b8":
                   b8.configure(state="disabled",fg_color="green")
                if i == "b9":
                   b9.configure(state="disabled",fg_color="green")
                if i == "b10":
                   b10.configure(state="disabled",fg_color="green")
                if i == "b11":
                   b11.configure(state="disabled",fg_color="green")
                if i == "b12":
                   b12.configure(state="disabled",fg_color="green")
                if i == "b13":
                   b13.configure(state="disabled",fg_color="green")
                if i == "b14":
                   b14.configure(state="disabled",fg_color="green")
                if i == "b15":
                   b15.configure(state="disabled",fg_color="green")
                if i == "b16":
                   b16.configure(state="disabled",fg_color="green")
                if i == "b17":
                   b17.configure(state="disabled",fg_color="green")
                if i == "b18":
                   b18.configure(state="disabled",fg_color="green")
                if i == "b19":
                   b19.configure(state="disabled",fg_color="green")
                if i == "b20":
                   b20.configure(state="disabled",fg_color="green")
                if i == "b21":
                   b21.configure(state="disabled",fg_color="green")
                if i == "b22":
                   b22.configure(state="disabled",fg_color="green")
                if i == "b23":
                   b23.configure(state="disabled",fg_color="green")
                if i == "b24":
                   b24.configure(state="disabled",fg_color="green")
                if i == "b25":
                   b25.configure(state="disabled",fg_color="green")
                if i == "b26":
                   b26.configure(state="disabled",fg_color="green")
                if i == "b27":
                   b27.configure(state="disabled",fg_color="green")
                if i == "b28":
                   b28.configure(state="disabled",fg_color="green")
                if i == "b29":
                   b29.configure(state="disabled",fg_color="green")
                if i == "b30":
                   b30.configure(state="disabled",fg_color="green")
                if i == "b31":
                   b31.configure(state="disabled",fg_color="green")
                if i == "b32":
                   b32.configure(state="disabled",fg_color="green")
                if i == "b33":
                   b33.configure(state="disabled",fg_color="green")
                if i == "b34":
                   b34.configure(state="disabled",fg_color="green")
                if i == "b35":
                   b35.configure(state="disabled",fg_color="green")
                if i == "b36":
                   b36.configure(state="disabled",fg_color="green")
                if i == "b37":
                   b37.configure(state="disabled",fg_color="green")
                if i == "b38":
                   b38.configure(state="disabled",fg_color="green")
                if i == "b39":
                   b39.configure(state="disabled",fg_color="green")
                if i == "b40":
                   b40.configure(state="disabled",fg_color="green")
                if i == "b41":
                   b41.configure(state="disabled",fg_color="green")
                if i == "b42":
                   b42.configure(state="disabled",fg_color="green")
                if i == "b43":
                   b43.configure(state="disabled",fg_color="green")
                if i == "b44":
                   b44.configure(state="disabled",fg_color="green")
                if i == "b45":
                   b45.configure(state="disabled",fg_color="green")
                if i == "b46":
                   b46.configure(state="disabled",fg_color="green")
                if i == "b47":
                   b47.configure(state="disabled",fg_color="green")
                if i == "b48":
                   b48.configure(state="disabled",fg_color="green")
                if i == "b49":
                   b49.configure(state="disabled",fg_color="green")
                if i == "b50":
                   b50.configure(state="disabled",fg_color="green")
                if i == "a1":
                   a1.configure(state="disabled",fg_color="green")
                if i == "a2":
                   a2.configure(state="disabled",fg_color="green")
                if i == "a3":
                   a3.configure(state="disabled",fg_color="green")
                if i == "a4":
                   a4.configure(state="disabled",fg_color="green")
                if i == "a5":
                   a5.configure(state="disabled",fg_color="green")
                if i == "a6":
                   a6.configure(state="disabled",fg_color="green")
                if i == "a7":
                   a7.configure(state="disabled",fg_color="green")
                if i == "a8":
                   a8.configure(state="disabled",fg_color="green")
                if i == "a9":
                   a9.configure(state="disabled",fg_color="green")
                if i == "a10":
                   a10.configure(state="disabled",fg_color="green")
                if i == "a11":
                   a11.configure(state="disabled",fg_color="green")
                if i == "a12":
                   a12.configure(state="disabled",fg_color="green")
                if i == "a13":
                   a13.configure(state="disabled",fg_color="green")
                if i == "a14":
                   a14.configure(state="disabled",fg_color="green")
                if i == "a15":
                   a15.configure(state="disabled",fg_color="green")
                if i == "a16":
                   a16.configure(state="disabled",fg_color="green")
                if i == "a17":
                   a17.configure(state="disabled",fg_color="green")
                if i == "a18":
                   a18.configure(state="disabled",fg_color="green")
                if i == "a19":
                   a19.configure(state="disabled",fg_color="green")
                if i == "a20":
                   a20.configure(state="disabled",fg_color="green")
                if i == "a21":
                   a21.configure(state="disabled",fg_color="green")
                if i == "a22":
                   a22.configure(state="disabled",fg_color="green")
                if i == "a23":
                   a23.configure(state="disabled",fg_color="green")
                if i == "a24":
                   a24.configure(state="disabled",fg_color="green")
                if i == "a25":
                   a25.configure(state="disabled",fg_color="green")
                if i == "a26":
                   a26.configure(state="disabled",fg_color="green")
                if i == "a27":
                   a27.configure(state="disabled",fg_color="green")
                if i == "a28":
                   a28.configure(state="disabled",fg_color="green")
                if i == "a29":
                   a29.configure(state="disabled",fg_color="green")
                if i == "a30":
                   a30.configure(state="disabled",fg_color="green")
                if i == "a31":
                   a31.configure(state="disabled",fg_color="green")
                if i == "a32":
                   a32.configure(state="disabled",fg_color="green")
                if i == "a33":
                   a33.configure(state="disabled",fg_color="green")
                if i == "a34":
                   a34.configure(state="disabled",fg_color="green")
                if i == "a35":
                   a35.configure(state="disabled",fg_color="green")
                if i == "a36":
                   a36.configure(state="disabled",fg_color="green")
                if i == "a37":
                   a37.configure(state="disabled",fg_color="green")
                if i == "a38":
                   a38.configure(state="disabled",fg_color="green")
                if i == "a39":
                   a39.configure(state="disabled",fg_color="green")
                if i == "a40":
                   a40.configure(state="disabled",fg_color="green")
                if i == "a41":
                   a41.configure(state="disabled",fg_color="green")
                if i == "a42":
                   a42.configure(state="disabled",fg_color="green")
                if i == "a43":
                   a43.configure(state="disabled",fg_color="green")
                if i == "a44":
                   a44.configure(state="disabled",fg_color="green")
                if i == "a45":
                   a45.configure(state="disabled",fg_color="green")
                if i == "a46":
                   a46.configure(state="disabled",fg_color="green")
                if i == "a47":
                   a47.configure(state="disabled",fg_color="green")
                if i == "a48":
                   a48.configure(state="disabled",fg_color="green")
                if i == "a49":
                   a49.configure(state="disabled",fg_color="green")
                if i == "a50":
                   a50.configure(state="disabled",fg_color="green")


        
    text = ct.CTkLabel(new_root,text = "SCREEN",font = ("Arial",15))
    text.grid(row = 18,column =22)   


def face2():
    def checker2():
        try:
            int(e2.get())
            messagebox.showerror("Wrong","Enter valid name!!")
        except ValueError:
            global name
            name = e2.get()
            try:
                int(e3.get())
                tickets = int(e3.get())
                if tickets>0:
                    if tickets>100:
                        messagebox.showinfo("Limit","Not more than 100 tickets can be booked")
                    else:
                        if l[e1.get()]-tickets >= 0:
                            global ticket
                            ticket = e3.get()
                            l[e1.get()]-=tickets
                            button_2.configure(state="disabled")
                            face3()
                        else:
                            messagebox.showerror("Wrong","Tickets not avilable,only {} available".format(l[e1.get()]))
                else:
                     messagebox.showinfo("Wrong","Can't be 0 or negative!!")

            except ValueError:
                messagebox.showerror("Wrong","Enter valid number!!")
        


    e2 = ct.CTkEntry(my_frame,placeholder_text="Type name...",width=300,text_color="#FFCC70",corner_radius= 15)
    e2.pack(pady=90)
    global e3
    e3 = ct.CTkEntry(my_frame,placeholder_text="Type no.of tickets...",width=300,text_color="#FFCC70",corner_radius= 15)
    e3.pack(pady=110)
    button_2 = ct.CTkButton(my_frame,text = "Click me",fg_color="transparent",
                  hover_color = "#4158D0",border_color = "#FFCC70",
                   corner_radius = 32 ,border_width=1.5,command=checker2)
    button_2.pack(pady=80)

def checker():
    try:
        int(e1.get())
        messagebox.showerror("Wrong input","Enter valid a movie!!")
    except ValueError:
        if e1.get() not in l:
            messagebox.showerror("Wrong","No movie found sorry!! :(")
        else:
            global movie_pack
            movie_pack = e1.get()
            e1.configure(state = "disabled")
            button_1.configure(state="disabled")
            face2()


    
my_frame = ct.CTkScrollableFrame(root,width=1500,height=800)
my_frame.pack(pady=40)
my_label  = ct.CTkLabel(my_frame,text= "𝐓𝐢𝐜𝐤𝐞𝐭 𝐁𝐨𝐨𝐤𝐢𝐧𝐠",font = ("Arial",35),text_color="#FFCC70") 
my_label.pack(padx = 0,pady = 0)


e1 = ct.CTkEntry(my_frame,placeholder_text="Type some movie...",width=300,text_color="#FFCC70",corner_radius= 15)
e1.pack(pady=70)


button_1 = ct.CTkButton(my_frame,text = "Click me",fg_color="transparent",
                  hover_color = "#4158D0",border_color = "#FFCC70",
                   corner_radius = 32 ,border_width=1.5,command=checker)
button_1.pack(pady=80)
root.mainloop()
