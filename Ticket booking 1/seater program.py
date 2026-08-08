#c=0
#for i in range(106,96,-1):
#    for j in range(1,51):
#        print("""{} = ct.CTkButton(new_root,text="{}",fg_color="transparent",width=20,height=20,border_color="red",hover_color="green",border_width = 1,command=lambda:seat_checker_on({},{},{},"{}"))""".format((chr(i)+str(j)),(chr(i)+str(j)),(chr(i)+str(j)),c,j,(chr(i)+str(j))))
#        print("{}.grid(row={},column={})".format((str(j)),c,j))
#   c+=1
#####
y=10
x=50
for i in range(ord("H"),64,-1):
    for j in range(1,7):
        print(f"""self.{chr(i)+str(j)} = CTkButton(self.screen,image=self.cinema,text="{str(j)}",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.{chr(i)+str(j)},{str(j)},"self.{chr(i)+str(j)}",{x/100},{y/10}))""")
        print(f"""self.{chr(i)+str(j)}.place(relx = {x/1000},rely = {y/100})""")
        x+=72
    x = 50
    y+= 10
y=10
x=540
for i in range(ord("H"),64,-1):
    for j in range(7,13):
        print(f"""self.{chr(i)+str(j)} = CTkButton(self.screen,image=self.cinema,text="{str(j)}",fg_color="white",hover_color="green",width=12,text_color="black",height=20,command = lambda:app.seat(self,u,self.{chr(i)+str(j)},{str(j)},"self.{chr(i)+str(j)}",{x/100},{y/10}))""")
        print(f"""self.{chr(i)+str(j)}.place(relx = {x/1000},rely = {y/100})""")
        x+=72
    x = 540
    y+= 10
