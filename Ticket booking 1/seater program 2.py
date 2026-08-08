#c=0
#for i in range(106,96,-1):
#    for j in range(1,51):
#        print("""if i == "{}":""".format((chr(i)+str(j))))
#        print("""   {}.configure(state="disabled",fg_color="green")""".format((chr(i)+str(j))))
#   c+=1
for i in range(ord("H"),64,-1):
    for j in range(1,13):
        print(f"""if j == "self.{chr(i)+str(j)}":""")
        print(f"""    self.{chr(i)+str(j)}.configure(state = "disabled",fg_color = "yellow")""")
