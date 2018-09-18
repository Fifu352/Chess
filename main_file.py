import tkinter as tk
from tkinter import *



LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)

class Gui():
        def __init__(self, root, conf):
            self.root=root
            self.conf =conf
            self.canvas = tk.Canvas(root, width=1000, height=1000, background='lightgreen')
            self.location = []


            for i in range(8):
                for j in range(8):
                    if (i + j) % 2 == 0:

                        conf[i][j][0] = Label(root, borderwidth=50, bg="grey")
                        conf[i][j][0].grid(row=i, column=j)
                        conf[i][j][0].bind("<Button-1>", lambda event, arg=self: self.clicka(event))
                        conf[i][j][1] = "grey"
                        conf[i][j][2] = True
                        conf[i][j][3] = Cheessman




                    else:

                        conf[i][j][0] = Label(root, borderwidth=50, bg="#B0E0E6")
                        conf[i][j][0].grid(row=i, column=j)
                        conf[i][j][0].bind("<Button-1>", lambda event, arg=self: self.clicka(event))
                        conf[i][j][1] = "#B0E0E6"
                        conf[i][j][2] = True
                        conf[i][j][3] = Cheessman


        def clicka(self, event):
            if events:
                x=str(event.widget)
                y = x[-2:-1]
                if y == 'l':
                    y=x[-1]
                else:
                    y = x[-2:]

                if y == "el":
                    i = 0
                    j = 0
                else:
                    i = int(int(y)/8)
                    j = int(y) - i*8-1

                if j == -1:
                    i-=1
                    j=7
                if conf[i][j][0].cget("bg") ==  "lightgray" or  conf[i][j][0].cget("bg") == "#7adbe8":
                    events[0].move(i,j)

                if conf[i][j][0].cget("bg") ==  "#610B0B" or  conf[i][j][0].cget("bg") == "#F5A9E1":
                    if not isinstance(conf[i][j][3],King):
                        events[0].capture(i, j)




            k = {"grey": "lightgray", "#B0E0E6": "#7adbe8"}
            b = {"grey": "#610B0B", "#B0E0E6": "#F5A9E1"}



class Cheessman():

        def __init__(self, coloring, i, j):
            self.color=""






class King():
        def __init__(self,root, color, conf, events):
            self.type = "King"
            self.lives = "True"
            self.color = color
            self.root = root
            self.click=0
            self.moves = 0
            self.check=0

            if color == 'White':
                self.photo = tk.PhotoImage(file=r"C:\Users\Fifu\Documents\Chess\icons\w_king.png")
                self.position=[0,4]
            elif color=="Black":
                self.photo = tk.PhotoImage(file=r"C:\Users\Fifu\Documents\Chess\icons\b_king.png")
                self.position=[7,4]
        def place(self):
            self.label = Label(root,image=self.photo,font = "Times 12 bold", fg = self.color, bg= conf[self.position[0]][self.position[1]][1])
            self.label.grid(row=self.position[0],column=self.position[1])
            self.label.bind("<Button-1>", lambda event, arg=self: self.clicka(event))
            conf[self.position[0]][self.position[1]][2] = False
            conf[self.position[0]][self.position[1]][3] = self

        def clicka(self, event):
            global tour
            if self.color==tour:
                if self.click == 0:
                    if event != 0:
                        checker()
                    self.label.config(bg="blue")
                    self.click = 1
                    events.append(self)
                    k={"grey":"lightgray","#B0E0E6":"#7adbe8" }
                    b = {"grey":"#610B0B" ,"#B0E0E6":"#F5A9E1" }
                    if self.position[0]>0:
                        if conf[self.position[0]-1][self.position[1]][2] == True :
                            conf[self.position[0] - 1][self.position[1]][0].config(bg=k[conf[self.position[0] - 1][self.position[1]][1]])
                        elif conf[self.position[0]-1][self.position[1]][2] == False  and  conf[self.position[0]-1][self.position[1]][3].color !=  "" and conf[self.position[0]-1][self.position[1]][3].color !=  self.color:
                            conf[self.position[0] - 1][self.position[1]][0].config(bg=b[conf[self.position[0] - 1][self.position[1]][1]])
                    if self.position[0]<7:
                        if conf[self.position[0] + 1][self.position[1]][2] == True :
                            conf[self.position[0] + 1][self.position[1]][0].config(bg=k[conf[self.position[0] + 1][self.position[1]][1]])
                        elif conf[self.position[0]+1][self.position[1]][2] == False  and  conf[self.position[0]+1][self.position[1]][3].color !=  "" and conf[self.position[0]+1][self.position[1]][3].color !=  self.color:
                            conf[self.position[0] + 1][self.position[1]][0].config(bg=b[conf[self.position[0] +1][self.position[1]][1]])

                    if self.position[1] > 0:
                        if conf[self.position[0]][self.position[1]-1][2] == True :
                            conf[self.position[0]][self.position[1]-1][0].config(bg=k[conf[self.position[0]][self.position[1]-1][1]])
                        elif conf[self.position[0]][self.position[1]-1][2] == False  and  conf[self.position[0]][self.position[1]-1][3].color !=  "" and conf[self.position[0]][self.position[1]-1][3].color !=  self.color:
                            conf[self.position[0]][self.position[1]-1][0].config(bg=b[conf[self.position[0]][self.position[1]-1][1]])

                    if self.position[1]<7:
                        if conf[self.position[0]][self.position[1]+1][2] == True :
                            conf[self.position[0]][self.position[1]+1][0].config(bg=k[conf[self.position[0]][self.position[1]+1][1]])
                        elif conf[self.position[0]][self.position[1]+1][2] == False  and  conf[self.position[0]][self.position[1]+1][3].color !=  "" and conf[self.position[0]][self.position[1]+1][3].color !=  self.color:
                            conf[self.position[0]][self.position[1]+1][0].config(bg=b[conf[self.position[0]][self.position[1]+1][1]])
                    if self.position[0]> 0   and self.position[1]> 0 :
                        if conf[self.position[0] - 1][self.position[1]-1][2] == True:
                            conf[self.position[0] - 1][self.position[1]-1][0].config(bg=k[ conf[self.position[0] - 1][self.position[1]-1][1]])
                        elif conf[self.position[0]-1][self.position[1]-1][2] == False  and  conf[self.position[0]-1][self.position[1]-1][3].color !=  "" and conf[self.position[0]-1][self.position[1]-1][3].color !=  self.color:
                            conf[self.position[0]-1][self.position[1]-1][0].config(bg=b[conf[self.position[0]-1][self.position[1]-1][1]])
                    if self.position[0]<7   and self.position[1]< 7 :
                        if conf[self.position[0] + 1][self.position[1]+1][2] == True:
                            conf[self.position[0] + 1][self.position[1]+1][0].config(bg=k[ conf[self.position[0] + 1][self.position[1]+1][1]])
                        elif conf[self.position[0]+1][self.position[1]+1][2] == False  and  conf[self.position[0]+1][self.position[1]+1][3].color !=  "" and conf[self.position[0]+1][self.position[1]+1][3].color !=  self.color:
                            conf[self.position[0]+1][self.position[1]+1][0].config(bg=b[conf[self.position[0]+1][self.position[1]+1][1]])
                    if self.position[0]< 7   and self.position[1]>  0 :
                        if conf[self.position[0]+1][self.position[1] - 1][2] == True:
                            conf[self.position[0]+1][self.position[1] - 1][0].config(bg=k[ conf[self.position[0]+1][self.position[1] - 1][1]])
                        elif conf[self.position[0]+1][self.position[1]-1][2] == False  and  conf[self.position[0]+1][self.position[1]-1][3].color !=  "" and conf[self.position[0]+1][self.position[1]-1][3].color !=  self.color:
                            conf[self.position[0]+1][self.position[1]-1][0].config(bg=b[conf[self.position[0]+1][self.position[1]-1][1]])
                    if self.position[0]>0   and self.position[1]< 7 :
                        if conf[self.position[0]-1][self.position[1] + 1][2] == True:
                            conf[self.position[0]-1][self.position[1] + 1][0].config(bg=k[conf[self.position[0]-1][self.position[1] + 1][1]])
                        elif conf[self.position[0]-1][self.position[1]+1][2] == False  and  conf[self.position[0]-1][self.position[1]+1][3].color !=  "" and conf[self.position[0]-1][self.position[1]+1][3].color !=  self.color:
                            conf[self.position[0]-1][self.position[1]+1][0].config(bg=b[conf[self.position[0]-1][self.position[1]+1][1]])
                    if self.color == "White" and self.moves == 0 and conf[0][5][2] == True and conf[0][6][2] == True and conf[0][7][2] == False:
                        if conf[0][7][3].moves ==0:
                            conf[0][7][0].config(bg=k[conf[0][7][1]])
                    if self.color == "White" and self.moves == 0 and conf[0][1][2] == True and conf[0][2][2] == True and conf[0][3][2] == True and conf[0][0][2]== False:
                        if conf[0][0][3].moves ==0:
                            conf[0][0][0].config(bg=k[conf[0][0][1]])
                    if self.color == "Black" and self.moves == 0 and conf[7][5][2] == True and conf[7][6][2] == True and conf[7][7][2] == False:
                        if conf[7][7][3].moves ==0:
                            conf[7][7][0].config(bg=k[conf[7][7][1]])
                    if self.color == "Black" and self.moves == 0 and conf[7][1][2] == True and conf[7][2][2] == True and conf[7][3][2] == True and conf[7][0][2]== False:
                        if conf[7][0][3].moves ==0:
                            conf[7][0][0].config(bg=k[conf[7][0][1]])


                else:
                    self.label.config(bg = conf[self.position[0]][self.position[1]][1])
                    if self.position[0] > 0:
                        conf[self.position[0] - 1][self.position[1]][0].config(bg=conf[self.position[0] - 1][self.position[1]][1])
                    if self.position[0] < 7:
                        conf[self.position[0] + 1][self.position[1]][0].config(bg=conf[self.position[0] + 1][self.position[1]][1])
                    if self.position[1] > 0:
                        conf[self.position[0]][self.position[1]-1][0].config(bg=conf[self.position[0] ][self.position[1]-1][1])
                    if self.position[1] < 7:
                        conf[self.position[0]][self.position[1]+1][0].config(bg=conf[self.position[0] ][self.position[1]+1][1])
                    if self.position[0] > 0 and self.position[1] > 0:
                        conf[self.position[0] - 1][self.position[1]-1][0].config(bg=conf[self.position[0] - 1][self.position[1]-1][1])
                    if self.position[0] < 7 and self.position[1] < 7:
                        conf[self.position[0] + 1][self.position[1]+1][0].config(bg=conf[self.position[0] + 1][self.position[1]+1][1])
                    if self.position[0] < 7 and self.position[1] > 0:
                        conf[self.position[0]+1][self.position[1] - 1][0].config(bg=conf[self.position[0] + 1][self.position[1]-1][1])
                    if self.position[0] > 0 and self.position[1] < 7:
                        conf[self.position[0]-1][self.position[1] + 1][0].config(bg=conf[self.position[0] - 1][self.position[1]+1][1])
                    self.click = 0
                    events.remove(self)
        def move(self,i,j):
            global tour
            if i == 0 and j ==7 and conf[i][j][2]==False:
                if self.check!=0:
                    popupmsg("Can't do that - under check!")
                    return
                checker()
                conf[0][6][3]= conf[0][4][3]
                conf[0][6][3].position = [0,6]
                conf[0][6][2] = False
                conf[0][4][3] = Cheessman
                conf[0][4][2] = True

                conf[0][5][3] = conf[0][7][3]
                conf[0][5][3].position = [0, 5]
                conf[0][5][2] = False
                conf[0][7][3] = Cheessman
                conf[0][7][2] = True





                conf[0][5][3].label.config(bg=conf[0][5][1])
                conf[0][6][3].label.config(bg= conf[0][6][1])

                conf[0][5][3].label.grid(row = 0 , column = 5)
                conf[0][6][3].label.grid(row = 0 , column = 6)

            elif i == 0 and j ==0 and conf[i][j][2]==False:
                if self.check != 0:
                    popupmsg("Can't do that - under check!")
                    return
                checker()
                conf[0][2][3]= conf[0][4][3]
                conf[0][2][3].position = [0,2]
                conf[0][2][2] = False
                conf[0][4][3] = Cheessman
                conf[0][4][2] = True

                conf[0][3][3] = conf[0][0][3]
                conf[0][3][3].position = [0, 3]
                conf[0][3][2] = False
                conf[0][0][3] = Cheessman
                conf[0][0][2] = True





                conf[0][2][3].label.config(bg=conf[0][2][1])
                conf[0][3][3].label.config(bg= conf[0][3][1])

                conf[0][2][3].label.grid(row = 0 , column = 2)
                conf[0][3][3].label.grid(row = 0 , column = 3)

            elif i == 7 and j ==7 and conf[i][j][2]==False:
                if self.check != 0:
                    popupmsg("Can't do that - under check!")
                    return
                checker()
                conf[7][6][3]= conf[7][4][3]
                conf[7][6][3].position = [7,6]
                conf[7][6][2] = False
                conf[7][4][3] = Cheessman
                conf[7][4][2] = True

                conf[7][5][3] = conf[7][7][3]
                conf[7][5][3].position = [7, 5]
                conf[7][5][2] = False
                conf[7][7][3] = Cheessman
                conf[7][7][2] = True





                conf[7][5][3].label.config(bg=conf[7][5][1])
                conf[7][6][3].label.config(bg= conf[7][6][1])

                conf[7][5][3].label.grid(row = 7, column = 5)
                conf[7][6][3].label.grid(row = 7 , column = 6)

            elif i == 7 and j ==0 and conf[i][j][2]==False:
                if self.check != 0:
                    popupmsg("Can't do that - under check!")
                    return
                checker()
                conf[7][2][3]= conf[7][4][3]
                conf[7][2][3].position = [7,2]
                conf[7][2][2] = False
                conf[7][4][3] = Cheessman
                conf[7][4][2] = True

                conf[7][3][3] = conf[7][0][3]
                conf[7][3][3].position = [7, 3]
                conf[7][3][2] = False
                conf[7][0][3] = Cheessman
                conf[7][0][2] = True


                checker()


                conf[7][2][3].label.config(bg=conf[7][2][1])
                conf[7][3][3].label.config(bg= conf[7][3][1])

                conf[7][2][3].label.grid(row = 7 , column = 2)
                conf[7][3][3].label.grid(row = 7 , column = 3)

            else:
                x=self.position[0]
                y = self.position[1]

                conf[self.position[0]][self.position[1]][2] = True
                events[0].label.config(bg=conf[i][j][1])
                events[0].label.grid(row=i, column=j)

                conf[self.position[0]][self.position[1]][3] = Cheessman
                checker()
                self.position = [i, j]
                self.label.config(bg=conf[self.position[0]][self.position[1]][1])
                self.label.grid(row=i, column=j)
                conf[self.position[0]][self.position[1]][3] = self
                conf[self.position[0]][self.position[1]][2] = False
                rulez(0)
                if self.check>0:
                    i=x
                    j=y
                    popupmsg("Can't do that - check incoming!")
                    conf[self.position[0]][self.position[1]][2] = True
                    conf[self.position[0]][self.position[1]][3].label.config(bg=conf[i][j][1])
                    conf[self.position[0]][self.position[1]][3].label.grid(row=i, column=j)

                    conf[self.position[0]][self.position[1]][3] = Cheessman
                    self.position = [i, j]
                    self.label.config(bg=conf[self.position[0]][self.position[1]][1])
                    self.label.grid(row=i, column=j)
                    conf[self.position[0]][self.position[1]][3] = self
                    conf[self.position[0]][self.position[1]][2] = False
                    self.check=0
                    if tour == "White":
                        tour = "Black"
                    else:
                        tour = "White"



            self.moves += 1

            if tour == "White":
                tour = "Black"
            else:
                tour = "White"
            rulez(0)

        def capture(self, i, j):



            global tour
            global whites
            global blacks
            temp = conf[i][j][3]
            x= self.position[0]
            y=self.position[1]
            checker()
            conf[self.position[0]][self.position[1]][2] = True
            if conf[i][j][3].color == "White":
                whites.remove(conf[i][j][3])
            else:
                blacks.remove(conf[i][j][3])
            conf[i][j][3].label.destroy()

            self.label.grid(row=i, column=j)
            conf[self.position[0]][self.position[1]][3] = Cheessman

            self.position = [i, j]
            self.label.config(bg=conf[self.position[0]][self.position[1]][1])
            self.label.grid(row=i, column=j)
            conf[self.position[0]][self.position[1]][3] = self
            self.moves += 1
            conf[self.position[0]][self.position[1]][0].config(bg=conf[self.position[0]][self.position[1]][1])
            rulez(0)
            if tour == "White":
                tour = "Black"
            else:
                tour = "White"

            if self.check > 0:
                conf[x][y][3] = conf[i][j][3]
                conf[x][y][2]= False
                conf[x][y][3].position = (x,y)



                conf[i][j][3] = temp
                conf[i][j][2] = False
                conf[i][j][3].position = (i, j)

                conf[i][j][3].label = Label(root, image=conf[i][j][3].photo, font="Times 12 bold", fg=conf[i][j][3].color,
                                   bg=conf[conf[i][j][3].position[0]][conf[i][j][3].position[1]][1])

                conf[i][j][3].label.bind("<Button-1>", lambda event, arg=conf[i][j][3]: conf[i][j][3].clicka(event))


                conf[x][y][3].label.config(bg=conf[x][y][1])
                conf[i][j][3].label.config(bg=conf[i][j][1])

                conf[x][y][3].label.grid(row=x, column=y)
                conf[i][j][3].label.grid(row=i, column=j)

                if conf[i][j][3].color == "White":
                    whites.append(conf[i][j][3])
                else:
                    blacks.append(conf[i][j][3])
                if tour == "White":
                    tour = "Black"
                else:
                    tour = "White"





                popupmsg("Can't do that - check incoming!")





class Queen():
    def __init__(self, root, color, conf, events):
        self.type = "Queen"
        self.lives = "True"
        self.color = color
        self.root = root
        self.click = 0
        self.moves = 0

        if color == 'White':
            self.photo = tk.PhotoImage(file=r"C:\Users\Fifu\Documents\Chess\icons\w_queen.png")
            self.position = [0, 3]
        elif color == "Black":
            self.photo = tk.PhotoImage(file=r"C:\Users\Fifu\Documents\Chess\icons\b_queen.png")
            self.position = [7, 3]

    def place(self):
        self.label = Label(root, image=self.photo, font="Times 12 bold", fg=self.color,
                           bg=conf[self.position[0]][self.position[1]][1])
        self.label.grid(row=self.position[0], column=self.position[1])
        self.label.bind("<Button-1>", lambda event, arg=self: self.clicka(event))
        conf[self.position[0]][self.position[1]][2] = False
        conf[self.position[0]][self.position[1]][3] = self

    def clicka(self, event):
        global tour
        if self.color == tour:
            if self.click == 0:
                if event != 0:
                    checker()
                self.label.config(bg="blue")
                self.click = 1
                events.append(self)
                k = {"grey": "lightgray", "#B0E0E6": "#7adbe8"}
                b = {"grey": "#610B0B", "#B0E0E6": "#F5A9E1"}

                for i in range(self.position[0]):
                    if conf[self.position[0] - 1-i][self.position[1]][2] == True:
                        conf[self.position[0] - 1-i][self.position[1]][0].config(
                            bg=k[conf[self.position[0] - 1-i][self.position[1]][1]])
                    elif conf[self.position[0] - 1-i][self.position[1]][2] == False and conf[self.position[0] - 1-i][self.position[1]][3].color != "" and conf[self.position[0] - 1-i][self.position[1]][3].color != self.color:
                        conf[self.position[0] - 1-i][self.position[1]][0].config(bg=b[conf[self.position[0] - 1-i][self.position[1]][1]])
                        break
                    else:
                        break

                for i in range(self.position[1]):
                    if conf[self.position[0]][self.position[1]-1-i][2] == True:
                        conf[self.position[0] ][self.position[1]- 1-i][0].config(
                            bg=k[conf[self.position[0]][self.position[1]- 1-i][1]])
                    elif conf[self.position[0] ][self.position[1]- 1-i][2] == False and conf[self.position[0] ][self.position[1]- 1-i][3].color != "" and conf[self.position[0]][self.position[1] - 1-i][3].color != self.color:
                        conf[self.position[0]][self.position[1] - 1-i][0].config(bg=b[conf[self.position[0]][self.position[1] - 1-i][1]])
                        break
                    else:
                        break

                for i in range(7-self.position[0]):
                    if conf[self.position[0] + 1 + i][self.position[1]][2] == True:
                        conf[self.position[0] + 1 + i][self.position[1]][0].config(
                            bg=k[conf[self.position[0] + 1 + i][self.position[1]][1]])
                    elif conf[self.position[0] +1+i][self.position[1]][2] == False and conf[self.position[0] +1+i][self.position[1]][3].color != "" and conf[self.position[0] +1+i][self.position[1]][3].color != self.color:
                        conf[self.position[0] +1+i][self.position[1]][0].config(bg=b[conf[self.position[0] +1+i][self.position[1]][1]])
                        break
                    else:
                        break

                for i in range(7-self.position[1]):
                    if conf[self.position[0]][self.position[1]+1+i][2] == True:
                        conf[self.position[0]][self.position[1]+1+i][0].config(
                            bg=k[conf[self.position[0]][self.position[1]+ 1+i][1]])
                    elif conf[self.position[0] ][self.position[1]+1+i][2] == False and conf[self.position[0] ][self.position[1]+1+i][3].color != "" and conf[self.position[0]][self.position[1] +1+i][3].color != self.color:
                        conf[self.position[0]][self.position[1] +1+i][0].config(bg=b[conf[self.position[0]][self.position[1]+1+i][1]])
                        break
                    else:
                        break

                for i in range(min(self.position[0],self.position[1])):
                    if conf[self.position[0] - 1-i][self.position[1]-1-i][2] == True:
                        conf[self.position[0] - 1-i][self.position[1]-1-i][0].config(
                            bg=k[conf[self.position[0] - 1-i][self.position[1]-1-i][1]])
                    elif conf[self.position[0] - 1 - i][self.position[1]- 1 - i][2] == False and \
                            conf[self.position[0] - 1 - i][self.position[1]- 1 - i][3].color != "" and \
                            conf[self.position[0] - 1 - i][self.position[1]- 1 - i][3].color != self.color:
                        conf[self.position[0] - 1 - i][self.position[1]- 1 - i][0].config(
                            bg=b[conf[self.position[0] - 1 - i][self.position[1]- 1 - i][1]])
                        break
                    else:
                        break


                for i in range(7-max(self.position[0],self.position[1])):
                    if conf[self.position[0] + 1+i][self.position[1]+1+i][2] == True:
                        conf[self.position[0] + 1+i][self.position[1]+1+i][0].config(
                            bg=k[conf[self.position[0] + 1+i][self.position[1]+1+i][1]])
                    elif conf[self.position[0] +1+i][self.position[1] +1+i][2] == False and conf[self.position[0] +1+i][self.position[1] +1+i][3].color != "" and conf[self.position[0] +1+i][self.position[1] +1+i][3].color != self.color:
                        conf[self.position[0] +1+i][self.position[1] +1+i][0].config(bg=b[conf[self.position[0] +1+i][self.position[1] +1+i][1]])
                        break

                    else:
                        break

                for i in range(min(self.position[0], 7 - self.position[1])):
                    if conf[self.position[0] - 1-i][self.position[1]+1+i][2] == True:
                        conf[self.position[0] - 1-i][self.position[1]+1+i][0].config(
                            bg=k[conf[self.position[0] - 1-i][self.position[1]+1+i][1]])
                    elif conf[self.position[0]- 1-i ][self.position[1]+1+i][2] == False and conf[self.position[0]- 1-i ][self.position[1]+1+i][3].color != "" and conf[self.position[0]- 1-i][self.position[1] +1+i][3].color != self.color:
                        conf[self.position[0]- 1-i][self.position[1] +1+i][0].config(bg=b[conf[self.position[0]- 1-i][self.position[1]+1+i][1]])
                        break
                    else:
                        break

                for i in range(min(7 - self.position[0], self.position[1])):
                    if conf[self.position[0] + 1+i][self.position[1]-1-i][2] == True:
                        conf[self.position[0] + 1+i][self.position[1]-1-i][0].config(
                            bg=k[conf[self.position[0] + 1+i][self.position[1]-1-i][1]])
                    elif conf[self.position[0] + 1+i ][self.position[1]- 1-i][2] == False and conf[self.position[0]  + 1+i][self.position[1]- 1-i][3].color != "" and conf[self.position[0] + 1+i][self.position[1] - 1-i][3].color != self.color:
                        conf[self.position[0] + 1+i][self.position[1] - 1-i][0].config(bg=b[conf[self.position[0] + 1+i][self.position[1] - 1-i][1]])
                        break
                    else:
                        break



            else:
                self.label.config(bg=conf[self.position[0]][self.position[1]][1])

                for i in range(self.position[0]):

                    conf[self.position[0] - 1 - i][self.position[1]][0].config(
                    bg=conf[self.position[0] - 1 - i][self.position[1]][1])

                for i in range(self.position[1]):

                    conf[self.position[0]][self.position[1] - 1 - i][0].config(
                    bg=conf[self.position[0]][self.position[1] - 1 - i][1])


                for i in range(7 - self.position[0]):

                    conf[self.position[0] + 1 + i][self.position[1]][0].config(
                    bg=conf[self.position[0] + 1 + i][self.position[1]][1])


                for i in range(7 - self.position[1]):

                    conf[self.position[0]][self.position[1] + 1 + i][0].config(
                    bg=conf[self.position[0]][self.position[1] + 1 + i][1])


                for i in range(min(self.position[0],self.position[1])):

                    conf[self.position[0] - 1 - i][self.position[1] - 1 - i][0].config(
                    bg=conf[self.position[0] - 1 - i][self.position[1] - 1 - i][1])


                for i in range(7 - max(self.position[0],self.position[1])):

                    conf[self.position[0] + 1 + i][self.position[1] + 1 + i][0].config(
                    bg=conf[self.position[0] + 1 + i][self.position[1] + 1 + i][1])

                for i in range(min(self.position[0], 7 - self.position[1])):

                    conf[self.position[0] - 1 - i][self.position[1] + 1 + i][0].config(
                    bg=conf[self.position[0] - 1 - i][self.position[1] + 1 + i][1])

                for i in range(min(7 - self.position[0], self.position[1])):

                    conf[self.position[0] + 1 + i][self.position[1] - 1 - i][0].config(
                    bg=conf[self.position[0] + 1 + i][self.position[1] - 1 - i][1])

                events.remove(self)
                self.click = 0

    def move(self, i, j):
        global tour
        x = self.position[0]
        y = self.position[1]

        conf[self.position[0]][self.position[1]][2] = True
        events[0].label.config(bg=conf[i][j][1])
        events[0].label.grid(row=i, column=j)
        checker()
        conf[self.position[0]][self.position[1]][3] = Cheessman

        self.position = [i, j]
        self.label.config(bg=conf[self.position[0]][self.position[1]][1])
        self.label.grid(row=i, column=j)
        conf[self.position[0]][self.position[1]][3] = self
        conf[self.position[0]][self.position[1]][2] = False
        rulez(0)
        if tour == "White":

            king = white_king
        else:

            king = black_king
        if king.check > 0:
            i = x
            j = y
            popupmsg("Can't do that - check incoming!")
            conf[self.position[0]][self.position[1]][2] = True
            conf[self.position[0]][self.position[1]][3].label.config(bg=conf[i][j][1])
            conf[self.position[0]][self.position[1]][3].label.grid(row=i, column=j)

            conf[self.position[0]][self.position[1]][3] = Cheessman
            self.position = [i, j]
            self.label.config(bg=conf[self.position[0]][self.position[1]][1])
            self.label.grid(row=i, column=j)
            conf[self.position[0]][self.position[1]][3] = self
            conf[self.position[0]][self.position[1]][2] = False
            king.check = 0
        else:
            if tour == "White":
                tour = "Black"
            else:
                tour = "White"
            rulez(1)

    def capture(self, i, j):

        global tour
        global whites
        global blacks
        temp = conf[i][j][3]
        x = self.position[0]
        y = self.position[1]
        checker()
        conf[self.position[0]][self.position[1]][2] = True
        if conf[i][j][3].color == "White":
            whites.remove(conf[i][j][3])
        else:
            blacks.remove(conf[i][j][3])
        conf[i][j][3].label.destroy()

        self.label.grid(row=i, column=j)
        conf[self.position[0]][self.position[1]][3] = Cheessman

        self.position = [i, j]
        self.label.config(bg=conf[self.position[0]][self.position[1]][1])
        self.label.grid(row=i, column=j)
        conf[self.position[0]][self.position[1]][3] = self
        self.moves += 1
        conf[self.position[0]][self.position[1]][0].config(bg=conf[self.position[0]][self.position[1]][1])
        rulez(1)
        if tour == "White":
            tour = "Black"
            king = white_king
        else:
            tour = "White"
            king = black_king


        if king.check > 0:
            conf[x][y][3] = conf[i][j][3]
            conf[x][y][2] = False
            conf[x][y][3].position = (x, y)

            conf[i][j][3] = temp
            conf[i][j][2] = False
            conf[i][j][3].position = (i, j)

            conf[i][j][3].label = Label(root, image=conf[i][j][3].photo, font="Times 12 bold",
                                        fg=conf[i][j][3].color,
                                        bg=conf[conf[i][j][3].position[0]][conf[i][j][3].position[1]][1])

            conf[i][j][3].label.bind("<Button-1>", lambda event, arg=conf[i][j][3]: conf[i][j][3].clicka(event))

            conf[x][y][3].label.config(bg=conf[x][y][1])
            conf[i][j][3].label.config(bg=conf[i][j][1])

            conf[x][y][3].label.grid(row=x, column=y)
            conf[i][j][3].label.grid(row=i, column=j)

            if conf[i][j][3].color == "White":
                whites.append(conf[i][j][3])
            else:
                blacks.append(conf[i][j][3])
            if tour == "White":
                tour = "Black"
            else:
                tour = "White"

class Bishop():
    def __init__(self, root, color, conf, events):
        self.type = "Bishop"
        self.lives = "True"
        self.color = color
        self.root = root
        self.click = 0
        self.moves = 0

        if color == 'White':
            self.photo = tk.PhotoImage(file=r"C:\Users\Fifu\Documents\Chess\icons\w_bishop.png")
            if  conf[0][2][2] == True:
                self.position = [0, 2]
            else:
                self.position = [0, 5]
        elif color == "Black":
            self.photo = tk.PhotoImage(file=r"C:\Users\Fifu\Documents\Chess\icons\b_bishop.png")
            if  conf[7][2][2] == True:
                self.position = [7, 2]
            else:
                self.position = [7, 5]

    def place(self):
        self.label = Label(root, image=self.photo  , font="Times 12 bold", fg=self.color,
                           bg=conf[self.position[0]][self.position[1]][1])
        self.label.grid(row=self.position[0], column=self.position[1])
        self.label.bind("<Button-1>", lambda event, arg=self: self.clicka(event))
        conf[self.position[0]][self.position[1]][2] = False
        conf[self.position[0]][self.position[1]][3] = self

    def clicka(self, event):
        global tour
        if self.color == tour:
            if self.click == 0:
                if event != 0:
                    checker()
                self.label.config(bg="blue")
                self.click = 1
                events.append(self)
                k = {"grey": "lightgray", "#B0E0E6": "#7adbe8"}
                b = {"grey": "#610B0B", "#B0E0E6": "#F5A9E1"}



                for i in range(min(self.position[0], self.position[1])):
                    if conf[self.position[0] - 1 - i][self.position[1] - 1 - i][2] == True:
                        conf[self.position[0] - 1 - i][self.position[1] - 1 - i][0].config(
                            bg=k[conf[self.position[0] - 1 - i][self.position[1] - 1 - i][1]])
                    elif conf[self.position[0] - 1 - i][self.position[1] - 1 - i][2] == False and \
                            conf[self.position[0] - 1 - i][self.position[1] - 1 - i][3].color != "" and \
                            conf[self.position[0] - 1 - i][self.position[1] - 1 - i][3].color != self.color:
                        conf[self.position[0] - 1 - i][self.position[1] - 1 - i][0].config(
                            bg=b[conf[self.position[0] - 1 - i][self.position[1] - 1 - i][1]])
                        break
                    else:
                        break

                for i in range(7 - max(self.position[0], self.position[1])):
                    if conf[self.position[0] + 1 + i][self.position[1] + 1 + i][2] == True:
                        conf[self.position[0] + 1 + i][self.position[1] + 1 + i][0].config(
                            bg=k[conf[self.position[0] + 1 + i][self.position[1] + 1 + i][1]])
                    elif conf[self.position[0] + 1 + i][self.position[1] + 1 + i][2] == False and \
                            conf[self.position[0] + 1 + i][self.position[1] + 1 + i][3].color != "" and \
                            conf[self.position[0] + 1 + i][self.position[1] + 1 + i][3].color != self.color:
                        conf[self.position[0] + 1 + i][self.position[1] + 1 + i][0].config(
                            bg=b[conf[self.position[0] + 1 + i][self.position[1] + 1 + i][1]])
                        break

                    else:
                        break

                for i in range(min(self.position[0], 7 - self.position[1])):
                    if conf[self.position[0] - 1 - i][self.position[1] + 1 + i][2] == True:
                        conf[self.position[0] - 1 - i][self.position[1] + 1 + i][0].config(
                            bg=k[conf[self.position[0] - 1 - i][self.position[1] + 1 + i][1]])
                    elif conf[self.position[0] - 1 - i][self.position[1] + 1 + i][2] == False and \
                            conf[self.position[0] - 1 - i][self.position[1] + 1 + i][3].color != "" and \
                            conf[self.position[0] - 1 - i][self.position[1] + 1 + i][3].color != self.color:
                        conf[self.position[0] - 1 - i][self.position[1] + 1 + i][0].config(
                            bg=b[conf[self.position[0] - 1 - i][self.position[1] + 1 + i][1]])
                        break
                    else:
                        break

                for i in range(min(7 - self.position[0], self.position[1])):
                    if conf[self.position[0] + 1 + i][self.position[1] - 1 - i][2] == True:
                        conf[self.position[0] + 1 + i][self.position[1] - 1 - i][0].config(
                            bg=k[conf[self.position[0] + 1 + i][self.position[1] - 1 - i][1]])
                    elif conf[self.position[0] + 1 + i][self.position[1] - 1 - i][2] == False and \
                            conf[self.position[0] + 1 + i][self.position[1] - 1 - i][3].color != "" and \
                            conf[self.position[0] + 1 + i][self.position[1] - 1 - i][3].color != self.color:
                        conf[self.position[0] + 1 + i][self.position[1] - 1 - i][0].config(
                            bg=b[conf[self.position[0] + 1 + i][self.position[1] - 1 - i][1]])
                        break
                    else:
                        break

            else:
                self.label.config(bg=conf[self.position[0]][self.position[1]][1])


                for i in range(min(self.position[0],self.position[1])):

                    conf[self.position[0] - 1 - i][self.position[1] - 1 - i][0].config(
                    bg=conf[self.position[0] - 1 - i][self.position[1] - 1 - i][1])


                for i in range(7 - max(self.position[0],self.position[1])):

                    conf[self.position[0] + 1 + i][self.position[1] + 1 + i][0].config(
                    bg=conf[self.position[0] + 1 + i][self.position[1] + 1 + i][1])

                for i in range(min(self.position[0], 7 - self.position[1])):

                    conf[self.position[0] - 1 - i][self.position[1] + 1 + i][0].config(
                    bg=conf[self.position[0] - 1 - i][self.position[1] + 1 + i][1])

                for i in range(min(7 - self.position[0], self.position[1])):

                    conf[self.position[0] + 1 + i][self.position[1] - 1 - i][0].config(
                    bg=conf[self.position[0] + 1 + i][self.position[1] - 1 - i][1])

                events.remove(self)
                self.click = 0

    def move(self, i, j):
        global tour
        x = self.position[0]
        y = self.position[1]

        conf[self.position[0]][self.position[1]][2] = True
        events[0].label.config(bg=conf[i][j][1])
        events[0].label.grid(row=i, column=j)
        checker()
        conf[self.position[0]][self.position[1]][3] = Cheessman

        self.position = [i, j]
        self.label.config(bg=conf[self.position[0]][self.position[1]][1])
        self.label.grid(row=i, column=j)
        conf[self.position[0]][self.position[1]][3] = self
        conf[self.position[0]][self.position[1]][2] = False
        rulez(0)
        if tour == "White":

            king = white_king
        else:

            king = black_king
        if king.check > 0:
            i = x
            j = y
            popupmsg("Can't do that - check incoming!")
            conf[self.position[0]][self.position[1]][2] = True
            conf[self.position[0]][self.position[1]][3].label.config(bg=conf[i][j][1])
            conf[self.position[0]][self.position[1]][3].label.grid(row=i, column=j)

            conf[self.position[0]][self.position[1]][3] = Cheessman
            self.position = [i, j]
            self.label.config(bg=conf[self.position[0]][self.position[1]][1])
            self.label.grid(row=i, column=j)
            conf[self.position[0]][self.position[1]][3] = self
            conf[self.position[0]][self.position[1]][2] = False
            king.check = 0
        else:
            if tour == "White":
                tour = "Black"
            else:
                tour = "White"
            rulez(1)

    def capture(self, i, j):

        global tour
        global whites
        global blacks
        temp = conf[i][j][3]
        x = self.position[0]
        y = self.position[1]
        checker()
        conf[self.position[0]][self.position[1]][2] = True
        if conf[i][j][3].color == "White":
            whites.remove(conf[i][j][3])
        else:
            blacks.remove(conf[i][j][3])
        conf[i][j][3].label.destroy()

        self.label.grid(row=i, column=j)
        conf[self.position[0]][self.position[1]][3] = Cheessman

        self.position = [i, j]
        self.label.config(bg=conf[self.position[0]][self.position[1]][1])
        self.label.grid(row=i, column=j)
        conf[self.position[0]][self.position[1]][3] = self
        self.moves += 1
        conf[self.position[0]][self.position[1]][0].config(bg=conf[self.position[0]][self.position[1]][1])
        rulez(1)
        if tour == "White":
            tour = "Black"
            king = white_king
        else:
            tour = "White"
            king = black_king

        if king.check > 0:
            conf[x][y][3] = conf[i][j][3]
            conf[x][y][2] = False
            conf[x][y][3].position = (x, y)

            conf[i][j][3] = temp
            conf[i][j][2] = False
            conf[i][j][3].position = (i, j)

            conf[i][j][3].label = Label(root, image=conf[i][j][3].photo, font="Times 12 bold",
                                        fg=conf[i][j][3].color,
                                        bg=conf[conf[i][j][3].position[0]][conf[i][j][3].position[1]][1])

            conf[i][j][3].label.bind("<Button-1>", lambda event, arg=conf[i][j][3]: conf[i][j][3].clicka(event))

            conf[x][y][3].label.config(bg=conf[x][y][1])
            conf[i][j][3].label.config(bg=conf[i][j][1])

            conf[x][y][3].label.grid(row=x, column=y)
            conf[i][j][3].label.grid(row=i, column=j)

            if conf[i][j][3].color == "White":
                whites.append(conf[i][j][3])
            else:
                blacks.append(conf[i][j][3])
            if tour == "White":
                tour = "Black"
            else:
                tour = "White"




class Knight():
    def __init__(self, root, color, conf, events):
        self.type = "Knight"
        self.lives = "True"
        self.color = color
        self.root = root
        self.click = 0
        self.moves = 0

        if color == 'White':
            self.photo = tk.PhotoImage(file=r"C:\Users\Fifu\Documents\Chess\icons\w_knight.png")
            if  conf[0][1][2] == True:
                self.position = [0, 1]
            else:
                self.position = [0, 6]
        elif color == "Black":
            self.photo = tk.PhotoImage(file=r"C:\Users\Fifu\Documents\Chess\icons\b_knight.png")
            if  conf[7][1][2] == True:
                self.position = [7, 1]
            else:
                self.position = [7, 6]

    def place(self):
        self.label = Label(root, image=self.photo, font="Times 12 bold", fg=self.color,
                           bg=conf[self.position[0]][self.position[1]][1])
        self.label.grid(row=self.position[0], column=self.position[1])
        self.label.bind("<Button-1>", lambda event, arg=self: self.clicka(event))
        conf[self.position[0]][self.position[1]][2] = False
        conf[self.position[0]][self.position[1]][3] = self

    def clicka(self, event):
        global tour
        if self.color == tour:
            if self.click == 0:
                if event != 0:
                    checker()
                self.label.config(bg="blue")
                self.click = 1
                events.append(self)
                k = {"grey": "lightgray", "#B0E0E6": "#7adbe8"}
                b = {"grey": "#610B0B", "#B0E0E6": "#F5A9E1"}


                if self.position[0]>0 and self.position[1]>1:
                    if conf[self.position[0] - 1][self.position[1] - 2][2] == True:
                        conf[self.position[0] - 1][self.position[1]-2][0].config(
                            bg=k[conf[self.position[0] - 1][self.position[1]-2][1]])
                    if conf[self.position[0] - 1 ][self.position[1] - 2][2] == False and conf[self.position[0] - 1][self.position[1] - 2][3].color != "" and conf[self.position[0] - 1][self.position[1] - 2][3].color != self.color:
                        conf[self.position[0] - 1][self.position[1] - 2][0].config(bg=b[conf[self.position[0] - 1][self.position[1] - 2][1]])

                if self.position[0]>1 and self.position[1]>0:
                    if conf[self.position[0] - 2][self.position[1] - 1][2] == True:
                        conf[self.position[0] - 2][self.position[1]-1][0].config(
                            bg=k[conf[self.position[0] - 2][self.position[1]-1][1]])
                    if conf[self.position[0] - 2 ][self.position[1] - 1][2] == False and conf[self.position[0] - 2][self.position[1] - 1][3].color != "" and conf[self.position[0] - 2][self.position[1] - 1][3].color != self.color:
                        conf[self.position[0] - 2][self.position[1] - 1][0].config(bg=b[conf[self.position[0] - 2][self.position[1] - 1][1]])
                if self.position[0] < 7  and self.position[1] < 6:
                    if conf[self.position[0] + 1][self.position[1] + 2][2] == True:
                        conf[self.position[0] + 1][self.position[1] + 2][0].config(
                            bg=k[conf[self.position[0] + 1][self.position[1] + 2][1]])
                    if conf[self.position[0] + 1 ][self.position[1] + 2][2] == False and conf[self.position[0] + 1][self.position[1] + 2][3].color != "" and conf[self.position[0] + 1][self.position[1] + 2][3].color != self.color:
                        conf[self.position[0] + 1][self.position[1] + 2][0].config(bg=b[conf[self.position[0] + 1][self.position[1] + 2][1]])


                if self.position[0] <6  and self.position[1] < 7:
                    if conf[self.position[0] + 2][self.position[1] + 1][2] == True:
                        conf[self.position[0] + 2][self.position[1] + 1][0].config(
                            bg=k[conf[self.position[0] + 2][self.position[1] + 1][1]])
                    if conf[self.position[0] + 2 ][self.position[1] + 1][2] == False and conf[self.position[0] + 2][self.position[1] + 1][3].color != "" and conf[self.position[0] + 2][self.position[1] + 1][3].color != self.color:
                        conf[self.position[0] + 2][self.position[1] + 1][0].config(bg=b[conf[self.position[0] + 2][self.position[1] + 1][1]])



                if self.position[0]>0 and self.position[1]<6:
                    if conf[self.position[0] - 1][self.position[1] + 2][2] == True:
                        conf[self.position[0] - 1][self.position[1]+2][0].config(
                            bg=k[conf[self.position[0] - 1][self.position[1]+2][1]])
                    if conf[self.position[0] - 1 ][self.position[1] + 2][2] == False and conf[self.position[0] - 1][self.position[1] + 2][3].color != "" and conf[self.position[0] - 1][self.position[1] + 2][3].color != self.color:
                        conf[self.position[0] - 1][self.position[1] + 2][0].config(bg=b[conf[self.position[0] - 1][self.position[1] + 2][1]])

                if self.position[0]>1 and self.position[1]<7:
                    if conf[self.position[0] - 2][self.position[1] + 1][2] == True:
                        conf[self.position[0] - 2][self.position[1]+1][0].config(
                          bg=k[conf[self.position[0] - 2][self.position[1]+1][1]])
                    if conf[self.position[0] - 2 ][self.position[1] + 1][2] == False and conf[self.position[0] - 2][self.position[1] + 1][3].color != "" and conf[self.position[0] - 2][self.position[1] + 1][3].color != self.color:
                        conf[self.position[0] - 2][self.position[1] + 1][0].config(bg=b[conf[self.position[0] - 2][self.position[1] + 1][1]])

                if self.position[0] < 7  and self.position[1] > 1:
                    if conf[self.position[0] + 1][self.position[1] - 2][2] == True:
                        conf[self.position[0] + 1][self.position[1] - 2][0].config(
                            bg=k[conf[self.position[0] + 1][self.position[1]- 2][1]])
                    if conf[self.position[0] + 1 ][self.position[1] - 2][2] == False and conf[self.position[0] + 1][self.position[1] - 2][3].color != "" and conf[self.position[0] + 1][self.position[1] - 2][3].color != self.color:
                        conf[self.position[0] + 1][self.position[1] -2][0].config(bg=b[conf[self.position[0] + 1][self.position[1] - 2][1]])

                if self.position[0] <6  and self.position[1] > 0:
                    if conf[self.position[0] + 2][self.position[1] - 1][2] == True:
                        conf[self.position[0] + 2][self.position[1] - 1][0].config(
                            bg=k[conf[self.position[0] + 2][self.position[1] - 1][1]])
                    if conf[self.position[0] + 2 ][self.position[1] - 1][2] == False and conf[self.position[0] + 2][self.position[1] - 1][3].color != "" and conf[self.position[0] + 2][self.position[1] - 1][3].color != self.color:
                        conf[self.position[0] + 2][self.position[1] - 1][0].config(bg=b[conf[self.position[0] + 2][self.position[1] - 1][1]])



            else:
                self.label.config(bg=conf[self.position[0]][self.position[1]][1])


                if self.position[0]>0 and self.position[1]>1:
                    conf[self.position[0] - 1][self.position[1]-2][0].config(
                        bg=conf[self.position[0] - 1][self.position[1]-2][1])

                if self.position[0]>1 and self.position[1]>0:
                    conf[self.position[0] - 2][self.position[1]-1][0].config(
                        bg=conf[self.position[0] - 2][self.position[1]-1][1])

                if self.position[0] < 7  and self.position[1] < 6:
                    conf[self.position[0] + 1][self.position[1] + 2][0].config(
                        bg=conf[self.position[0] + 1][self.position[1] + 2][1])

                if self.position[0] <6  and self.position[1] < 7:
                    conf[self.position[0] + 2][self.position[1] + 1][0].config(
                        bg=conf[self.position[0] + 2][self.position[1] + 1][1])



                if self.position[0]>0 and self.position[1]<6:
                    conf[self.position[0] - 1][self.position[1]+2][0].config(
                        bg=conf[self.position[0] - 1][self.position[1]+2][1])

                if self.position[0]>1 and self.position[1]<7:
                    conf[self.position[0] - 2][self.position[1]+1][0].config(
                        bg=conf[self.position[0] - 2][self.position[1]+1][1])

                if self.position[0] < 7  and self.position[1] > 1:
                    conf[self.position[0] + 1][self.position[1] - 2][0].config(
                        bg=conf[self.position[0] + 1][self.position[1]-+ 2][1])

                if self.position[0] <6  and self.position[1] > 0:
                    conf[self.position[0] + 2][self.position[1] - 1][0].config(
                        bg=conf[self.position[0] + 2][self.position[1] - 1][1])
                events.remove(self)
                self.click = 0

    def move(self, i, j):
        global tour
        x = self.position[0]
        y = self.position[1]

        conf[self.position[0]][self.position[1]][2] = True
        events[0].label.config(bg=conf[i][j][1])
        events[0].label.grid(row=i, column=j)
        checker()
        conf[self.position[0]][self.position[1]][3] = Cheessman

        self.position = [i, j]
        self.label.config(bg=conf[self.position[0]][self.position[1]][1])
        self.label.grid(row=i, column=j)
        conf[self.position[0]][self.position[1]][3] = self
        conf[self.position[0]][self.position[1]][2] = False
        rulez(0)
        if tour == "White":

            king = white_king
        else:

            king = black_king
        if king.check > 0:
            i = x
            j = y
            popupmsg("Can't do that - check incoming!")
            conf[self.position[0]][self.position[1]][2] = True
            conf[self.position[0]][self.position[1]][3].label.config(bg=conf[i][j][1])
            conf[self.position[0]][self.position[1]][3].label.grid(row=i, column=j)

            conf[self.position[0]][self.position[1]][3] = Cheessman
            self.position = [i, j]
            self.label.config(bg=conf[self.position[0]][self.position[1]][1])
            self.label.grid(row=i, column=j)
            conf[self.position[0]][self.position[1]][3] = self
            conf[self.position[0]][self.position[1]][2] = False
            king.check = 0
        else:
            if tour == "White":
                tour = "Black"
            else:
                tour = "White"
            rulez(1)

    def capture(self, i, j):

        global tour
        global whites
        global blacks
        temp = conf[i][j][3]
        x = self.position[0]
        y = self.position[1]
        checker()
        conf[self.position[0]][self.position[1]][2] = True
        if conf[i][j][3].color == "White":
            whites.remove(conf[i][j][3])
        else:
            blacks.remove(conf[i][j][3])
        conf[i][j][3].label.destroy()

        self.label.grid(row=i, column=j)
        conf[self.position[0]][self.position[1]][3] = Cheessman

        self.position = [i, j]
        self.label.config(bg=conf[self.position[0]][self.position[1]][1])
        self.label.grid(row=i, column=j)
        conf[self.position[0]][self.position[1]][3] = self
        self.moves += 1
        conf[self.position[0]][self.position[1]][0].config(bg=conf[self.position[0]][self.position[1]][1])
        rulez(1)
        if tour == "White":
            tour = "Black"
            king = white_king
        else:
            tour = "White"
            king = black_king

        if king.check > 0:
            conf[x][y][3] = conf[i][j][3]
            conf[x][y][2] = False
            conf[x][y][3].position = (x, y)

            conf[i][j][3] = temp
            conf[i][j][2] = False
            conf[i][j][3].position = (i, j)

            conf[i][j][3].label = Label(root, image=conf[i][j][3].photo, font="Times 12 bold",
                                        fg=conf[i][j][3].color,
                                        bg=conf[conf[i][j][3].position[0]][conf[i][j][3].position[1]][1])

            conf[i][j][3].label.bind("<Button-1>", lambda event, arg=conf[i][j][3]: conf[i][j][3].clicka(event))

            conf[x][y][3].label.config(bg=conf[x][y][1])
            conf[i][j][3].label.config(bg=conf[i][j][1])

            conf[x][y][3].label.grid(row=x, column=y)
            conf[i][j][3].label.grid(row=i, column=j)

            if conf[i][j][3].color == "White":
                whites.append(conf[i][j][3])
            else:
                blacks.append(conf[i][j][3])
            if tour == "White":
                tour = "Black"
            else:
                tour = "White"


class Rook():
    def __init__(self, root, color, conf, events):
        self.type = "Rook"
        self.lives = "True"
        self.color = color
        self.root = root
        self.click = 0
        self.moves = 0


        if color == 'White':
            self.photo = tk.PhotoImage(file=r"C:\Users\Fifu\Documents\Chess\icons\w_rook.png")
            if  conf[0][0][2] == True:
                self.position = [0, 0]
            else:
                self.position = [0, 7]
        elif color == "Black":
            self.photo = tk.PhotoImage(file=r"C:\Users\Fifu\Documents\Chess\icons\b_rook.png")
            if  conf[7][0][2] == True:
                self.position = [7, 0]
            else:
                self.position = [7, 7]

    def place(self):
        self.label = Label(root, image = self.photo, font="Times 12 bold", fg=self.color,
                           bg=conf[self.position[0]][self.position[1]][1])
        self.label.grid(row=self.position[0], column=self.position[1])
        self.label.bind("<Button-1>", lambda event, arg=self: self.clicka(event))
        conf[self.position[0]][self.position[1]][2] = False
        conf[self.position[0]][self.position[1]][3] = self

    def clicka(self, event):
        global tour
        if self.color == tour:
            if self.click == 0:
                if event != 0:
                    checker()
                self.label.config(bg="blue")
                self.click = 1
                events.append(self)
                k = {"grey": "lightgray", "#B0E0E6": "#7adbe8"}
                b = {"grey": "#610B0B", "#B0E0E6": "#F5A9E1"}

                for i in range(self.position[0]):
                    if conf[self.position[0] - 1-i][self.position[1]][2] == True:
                        conf[self.position[0] - 1-i][self.position[1]][0].config(
                            bg=k[conf[self.position[0] - 1-i][self.position[1]][1]])
                    elif conf[self.position[0] - 1-i][self.position[1]][2] == False and conf[self.position[0] - 1-i][self.position[1]][3].color != "" and conf[self.position[0] - 1-i][self.position[1]][3].color != self.color:
                        conf[self.position[0] - 1-i][self.position[1]][0].config(bg=b[conf[self.position[0] - 1-i][self.position[1]][1]])
                        break
                    else:
                        break

                for i in range(self.position[1]):
                    if conf[self.position[0]][self.position[1]-1-i][2] == True:
                        conf[self.position[0] ][self.position[1]- 1-i][0].config(
                            bg=k[conf[self.position[0]][self.position[1]- 1-i][1]])
                    elif conf[self.position[0] ][self.position[1]- 1-i][2] == False and conf[self.position[0] ][self.position[1]- 1-i][3].color != "" and conf[self.position[0]][self.position[1] - 1-i][3].color != self.color:
                        conf[self.position[0]][self.position[1] - 1-i][0].config(bg=b[conf[self.position[0]][self.position[1] - 1-i][1]])
                        break
                    else:
                        break

                for i in range(7-self.position[0]):
                    if conf[self.position[0] + 1 + i][self.position[1]][2] == True:
                        conf[self.position[0] + 1 + i][self.position[1]][0].config(
                            bg=k[conf[self.position[0] + 1 + i][self.position[1]][1]])
                    elif conf[self.position[0] +1+i][self.position[1]][2] == False and conf[self.position[0] +1+i][self.position[1]][3].color != "" and conf[self.position[0] +1+i][self.position[1]][3].color != self.color:
                        conf[self.position[0] +1+i][self.position[1]][0].config(bg=b[conf[self.position[0] +1+i][self.position[1]][1]])
                        break
                    else:
                        break

                for i in range(7-self.position[1]):
                    if conf[self.position[0]][self.position[1]+1+i][2] == True:
                        conf[self.position[0]][self.position[1]+1+i][0].config(
                            bg=k[conf[self.position[0]][self.position[1]+ 1+i][1]])
                    elif conf[self.position[0] ][self.position[1]+1+i][2] == False and conf[self.position[0] ][self.position[1]+1+i][3].color != "" and conf[self.position[0]][self.position[1] +1+i][3].color != self.color:
                        conf[self.position[0]][self.position[1] +1+i][0].config(bg=b[conf[self.position[0]][self.position[1]+1+i][1]])
                        break
                    else:
                        break



            else:
                self.label.config(bg=conf[self.position[0]][self.position[1]][1])

                for i in range(self.position[0]):
                    conf[self.position[0] - 1 - i][self.position[1]][0].config(
                        bg=conf[self.position[0] - 1 - i][self.position[1]][1])

                for i in range(self.position[1]):
                    conf[self.position[0]][self.position[1] - 1 - i][0].config(
                        bg=conf[self.position[0]][self.position[1] - 1 - i][1])

                for i in range(7 - self.position[0]):
                    conf[self.position[0] + 1 + i][self.position[1]][0].config(
                        bg=conf[self.position[0] + 1 + i][self.position[1]][1])

                for i in range(7 - self.position[1]):
                    conf[self.position[0]][self.position[1] + 1 + i][0].config(
                        bg=conf[self.position[0]][self.position[1] + 1 + i][1])



                events.remove(self)
                self.click = 0

    def move(self, i, j):
        global tour
        x = self.position[0]
        y = self.position[1]

        conf[self.position[0]][self.position[1]][2] = True
        events[0].label.config(bg=conf[i][j][1])
        events[0].label.grid(row=i, column=j)
        checker()
        conf[self.position[0]][self.position[1]][3] = Cheessman

        self.position = [i, j]
        self.label.config(bg=conf[self.position[0]][self.position[1]][1])
        self.label.grid(row=i, column=j)
        conf[self.position[0]][self.position[1]][3] = self
        conf[self.position[0]][self.position[1]][2] = False
        rulez(0)
        if tour == "White":

            king = white_king
        else:

            king = black_king
        if king.check > 0:
            i = x
            j = y
            popupmsg("Can't do that - check incoming!")
            conf[self.position[0]][self.position[1]][2] = True
            conf[self.position[0]][self.position[1]][3].label.config(bg=conf[i][j][1])
            conf[self.position[0]][self.position[1]][3].label.grid(row=i, column=j)

            conf[self.position[0]][self.position[1]][3] = Cheessman
            self.position = [i, j]
            self.label.config(bg=conf[self.position[0]][self.position[1]][1])
            self.label.grid(row=i, column=j)
            conf[self.position[0]][self.position[1]][3] = self
            conf[self.position[0]][self.position[1]][2] = False
            king.check = 0
        else:
            if tour == "White":
                tour = "Black"
            else:
                tour = "White"
            rulez(1)

    def capture(self, i, j):

        global tour
        global whites
        global blacks
        temp = conf[i][j][3]
        x = self.position[0]
        y = self.position[1]
        checker()
        conf[self.position[0]][self.position[1]][2] = True
        if conf[i][j][3].color == "White":
            whites.remove(conf[i][j][3])
        else:
            blacks.remove(conf[i][j][3])
        conf[i][j][3].label.destroy()

        self.label.grid(row=i, column=j)
        conf[self.position[0]][self.position[1]][3] = Cheessman

        self.position = [i, j]
        self.label.config(bg=conf[self.position[0]][self.position[1]][1])
        self.label.grid(row=i, column=j)
        conf[self.position[0]][self.position[1]][3] = self
        self.moves += 1
        conf[self.position[0]][self.position[1]][0].config(bg=conf[self.position[0]][self.position[1]][1])
        rulez(1)
        if tour == "White":
            tour = "Black"
            king = white_king
        else:
            tour = "White"
            king = black_king

        if king.check > 0:
            conf[x][y][3] = conf[i][j][3]
            conf[x][y][2] = False
            conf[x][y][3].position = (x, y)

            conf[i][j][3] = temp
            conf[i][j][2] = False
            conf[i][j][3].position = (i, j)

            conf[i][j][3].label = Label(root, image=conf[i][j][3].photo, font="Times 12 bold",
                                        fg=conf[i][j][3].color,
                                        bg=conf[conf[i][j][3].position[0]][conf[i][j][3].position[1]][1])

            conf[i][j][3].label.bind("<Button-1>", lambda event, arg=conf[i][j][3]: conf[i][j][3].clicka(event))

            conf[x][y][3].label.config(bg=conf[x][y][1])
            conf[i][j][3].label.config(bg=conf[i][j][1])

            conf[x][y][3].label.grid(row=x, column=y)
            conf[i][j][3].label.grid(row=i, column=j)

            if conf[i][j][3].color == "White":
                whites.append(conf[i][j][3])
            else:
                blacks.append(conf[i][j][3])
            if tour == "White":
                tour = "Black"
            else:
                tour = "White"


class Pawn():
    def __init__(self, root, color, conf, i, events):
        self.type = "Pawn"
        self.lives = "True"
        self.color = color
        self.root = root
        self.i=i
        self.moves = 0
        self.click = 0

        if color == 'White':
            self.position = [1, i]
            self.photo = tk.PhotoImage(file=r"C:\Users\Fifu\Documents\Chess\icons\w_pawn.png")

        elif color == "Black":
            self.position = [6, i]
            self.photo = tk.PhotoImage(file=r"C:\Users\Fifu\Documents\Chess\icons\b_pawn.png")
    def place(self):
        self.label = Label(root, image=self.photo, font="Times 12 bold", fg=self.color,
                           bg=conf[self.position[0]][self.position[1]][1])
        self.label.grid(row=self.position[0], column=self.position[1])
        self.label.bind("<Button-1>", lambda event, arg=self: self.clicka(event))
        conf[self.position[0]][self.position[1]][2] = False
        conf[self.position[0]][self.position[1]][3] = self

    def clicka(self, event):
        global tour
        if self.color == tour:
            if self.click == 0:
                if event != 0:
                    checker()
                self.label.config(bg="blue")
                self.click = 1
                events.append(self)
                k = {"grey": "lightgray", "#B0E0E6": "#7adbe8"}
                b = {"grey": "#610B0B", "#B0E0E6": "#F5A9E1"}

                if self.color == 'White':

                    if self.position[0]<6:
                        if conf[self.position[0] + 1][self.position[1]][2] == True:
                            conf[self.position[0] + 1][self.position[1]][0].config(
                                bg=k[conf[self.position[0] + 1][self.position[1]][1]])
                            if conf[self.position[0] + 2][self.position[1]][2] == True and self.moves == 0:
                                conf[self.position[0] + 2][self.position[1]][0].config(
                                    bg=k[conf[self.position[0] + 2][self.position[1]][1]])
                    if self.position[1]>0:
                        if conf[self.position[0] +1][self.position[1]-1][2] == False and  conf[self.position[0]+1][self.position[1]-1][3].color !=  "" and conf[self.position[0]+1][self.position[1]-1][3].color !=  self.color:
                            conf[self.position[0]+1][self.position[1]-1][0].config(bg=b[conf[self.position[0]+1][self.position[1]-1][1]])
                    if self.position[1]<7:
                        if conf[self.position[0] +1][self.position[1]+1][2] == False and  conf[self.position[0]+1][self.position[1]+1][3].color !=  "" and conf[self.position[0]+1][self.position[1]+1][3].color !=  self.color:
                            conf[self.position[0]+1][self.position[1]+1][0].config(bg=b[conf[self.position[0]+1][self.position[1]+1][1]])




                    elif self.position[0]<7:
                        if conf[self.position[0] +1][self.position[1]][2] == True:
                            conf[self.position[0] + 1][self.position[1]][0].config(bg=k[conf[self.position[0] +1][self.position[1]][1]])
                        if self.position[1] < 7:
                            if conf[self.position[0] +1][self.position[1]+1][2] == False and  conf[self.position[0]+1][self.position[1]+1][3].color !=  "" and conf[self.position[0]+1][self.position[1]+1][3].color !=  self.color:
                                conf[self.position[0]+1][self.position[1]+1][0].config(bg=b[conf[self.position[0]+1][self.position[1]+1][1]])
                        if self.position[1] > 0:
                            if conf[self.position[0] +1][self.position[1]-1][2] == False and  conf[self.position[0]+1][self.position[1]-1][3].color !=  "" and conf[self.position[0]+1][self.position[1]-1][3].color !=  self.color:
                                conf[self.position[0]+1][self.position[1]-1][0].config(bg=b[conf[self.position[0]+1][self.position[1]-1][1]])







                elif self.color == 'Black':
                    if self.position[0] > 1:
                        if conf[self.position[0] - 1][self.position[1]][2] == True:
                            conf[self.position[0] - 1][self.position[1]][0].config(
                                bg=k[conf[self.position[0] + 1][self.position[1]][1]])
                            if conf[self.position[0] - 2][self.position[1]][2] == True and self.moves == 0:
                                conf[self.position[0] - 2][self.position[1]][0].config(
                                    bg=k[conf[self.position[0] - 2][self.position[1]][1]])

                        if self.position[1] > 0:
                            if conf[self.position[0] - 1][self.position[1] - 1][2] == False and \
                                    conf[self.position[0] - 1][self.position[1] - 1][3].color != "" and \
                                    conf[self.position[0] - 1][self.position[1] - 1][3].color != self.color:
                                conf[self.position[0] - 1][self.position[1] - 1][0].config(
                                    bg=b[conf[self.position[0] - 1][self.position[1] - 1][1]])
                        if self.position[1] < 7:
                            if conf[self.position[0] - 1][self.position[1] + 1][2] == False and \
                                    conf[self.position[0] - 1][self.position[1] + 1][3].color != "" and \
                                    conf[self.position[0] - 1][self.position[1] + 1][3].color != self.color:
                                conf[self.position[0] - 1][self.position[1] + 1][0].config(
                                    bg=b[conf[self.position[0] - 1][self.position[1] + 1][1]])



                    elif self.position[0]>0:
                        if conf[self.position[0] -1][self.position[1]][2] == True:
                            conf[self.position[0] - 1][self.position[1]][0].config(bg=k[conf[self.position[0] +1][self.position[1]][1]])
                        if self.position[1] > 0:
                            if conf[self.position[0] -1][self.position[1]-1][2] == False and  conf[self.position[0]-1][self.position[1]-1][3].color !=  "" and conf[self.position[0]-1][self.position[1]-1][3].color !=  self.color:
                                conf[self.position[0]-1][self.position[1]-1][0].config(bg=b[conf[self.position[0]-1][self.position[1]-1][1]])
                        if self.position[1] < 7:
                            if conf[self.position[0] -1][self.position[1]+1][2] == False and  conf[self.position[0]-1][self.position[1]+1][3].color !=  "" and conf[self.position[0]-1][self.position[1]+1][3].color !=  self.color:
                                conf[self.position[0]-1][self.position[1]+1][0].config(bg=b[conf[self.position[0]-1][self.position[1]+1][1]])



            else:
                self.label.config(bg=conf[self.position[0]][self.position[1]][1])
                if self.color == 'White':
                    if self.position[0] < 7:

                        conf[self.position[0] + 1][self.position[1]][0].config(bg=conf[self.position[0] + 1][self.position[1]][1])
                    if self.position[1] < 7:
                        conf[self.position[0] + 1][self.position[1] + 1][0].config(bg=conf[self.position[0] + 1][self.position[1] + 1][1])
                    if self.position[1] > 0:
                        conf[self.position[0] + 1][self.position[1] - 1][0].config(bg=conf[self.position[0] + 1][self.position[1] - 1][1])

                    if self.position[0] < 6:
                        conf[self.position[0] + 2][self.position[1]][0].config(bg=conf[self.position[0] + 2][self.position[1]][1])

                elif self.color == 'Black':
                    if self.position[0]>0:

                        conf[self.position[0] - 1][self.position[1]][0].config(bg=conf[self.position[0] +1][self.position[1]][1])
                    if self.position[1] > 0 :
                        conf[self.position[0]-1][self.position[1]-1][0].config(bg=conf[self.position[0]-1][self.position[1]-1][1])
                    if self.position[1] < 7:
                        conf[self.position[0]-1][self.position[1]+1][0].config(bg=conf[self.position[0]-1][self.position[1]+1][1])
                    if self.position[0] > 1:

                        conf[self.position[0] - 2][self.position[1]][0].config(bg=conf[self.position[0] - 2][self.position[1]][1])

                self.click = 0
                events.remove(self)

    def move(self, i, j):
        global tour
        x = self.position[0]
        y = self.position[1]

        conf[self.position[0]][self.position[1]][2] = True
        events[0].label.config(bg=conf[i][j][1])
        events[0].label.grid(row=i, column=j)
        checker()
        conf[self.position[0]][self.position[1]][3] = Cheessman

        self.position = [i, j]
        self.label.config(bg=conf[self.position[0]][self.position[1]][1])
        self.label.grid(row=i, column=j)
        conf[self.position[0]][self.position[1]][3] = self
        conf[self.position[0]][self.position[1]][2] = False
        rulez(0)
        if tour == "White":

            king = white_king
        else:

            king = black_king
        if king.check > 0:
            i = x
            j = y
            popupmsg("Can't do that - check incoming!")
            conf[self.position[0]][self.position[1]][2] = True
            conf[self.position[0]][self.position[1]][3].label.config(bg=conf[i][j][1])
            conf[self.position[0]][self.position[1]][3].label.grid(row=i, column=j)

            conf[self.position[0]][self.position[1]][3] = Cheessman
            self.position = [i, j]
            self.label.config(bg=conf[self.position[0]][self.position[1]][1])
            self.label.grid(row=i, column=j)
            conf[self.position[0]][self.position[1]][3] = self
            conf[self.position[0]][self.position[1]][2] = False
            king.check = 0
        else:
            if tour == "White":
                tour = "Black"
            else:
                tour = "White"
            rulez(1)

    def capture(self, i, j):

        global tour
        global whites
        global blacks
        temp = conf[i][j][3]
        x = self.position[0]
        y = self.position[1]
        checker()
        conf[self.position[0]][self.position[1]][2] = True
        if conf[i][j][3].color == "White":
            whites.remove(conf[i][j][3])
        else:
            blacks.remove(conf[i][j][3])
        conf[i][j][3].label.destroy()

        self.label.grid(row=i, column=j)
        conf[self.position[0]][self.position[1]][3] = Cheessman

        self.position = [i, j]
        self.label.config(bg=conf[self.position[0]][self.position[1]][1])
        self.label.grid(row=i, column=j)
        conf[self.position[0]][self.position[1]][3] = self
        self.moves += 1
        conf[self.position[0]][self.position[1]][0].config(bg=conf[self.position[0]][self.position[1]][1])
        rulez(1)
        if tour == "White":
            tour = "Black"
            king = white_king
        else:
            tour = "White"
            king = black_king

        if king.check > 0:
            conf[x][y][3] = conf[i][j][3]
            conf[x][y][2] = False
            conf[x][y][3].position = (x, y)

            conf[i][j][3] = temp
            conf[i][j][2] = False
            conf[i][j][3].position = (i, j)

            conf[i][j][3].label = Label(root, image=conf[i][j][3].photo, font="Times 12 bold",
                                        fg=conf[i][j][3].color,
                                        bg=conf[conf[i][j][3].position[0]][conf[i][j][3].position[1]][1])

            conf[i][j][3].label.bind("<Button-1>", lambda event, arg=conf[i][j][3]: conf[i][j][3].clicka(event))

            conf[x][y][3].label.config(bg=conf[x][y][1])
            conf[i][j][3].label.config(bg=conf[i][j][1])

            conf[x][y][3].label.grid(row=x, column=y)
            conf[i][j][3].label.grid(row=i, column=j)

            if conf[i][j][3].color == "White":
                whites.append(conf[i][j][3])
            else:
                blacks.append(conf[i][j][3])
            if tour == "White":
                tour = "Black"
            else:
                tour = "White"


def checker():
    if events:
        x = 0
        events[0].clicka(events[0])
    else:
        x =1

def rulez(v):
    global tour
    temp = tour
    checker()
    tour = "White"
    b = {"grey": "#610B0B", "#B0E0E6": "#F5A9E1"}
    black_king.check = 0
    white_king.check = 0
    for i in whites:
        i.clicka(1)
        if conf[black_king.position[0]][black_king.position[1]][0].cget("bg")==b[conf[black_king.position[0]][black_king.position[1]][1]]:
            black_king.check+=1
    checker()
    tour = "Black"




    for i in blacks:
        i.clicka(1)
        if conf[white_king.position[0]][white_king.position[1]][0].cget("bg")==b[conf[white_king.position[0]][white_king.position[1]][1]]:
            white_king.check += 1


    checker()
    tour = temp

    if black_king.check>0 and v ==1:
        popupmsg("Black king check")
    if white_king.check>0 and v ==1:
        popupmsg("White king check")



def popupmsg(msg):
    top = Toplevel()
    top.title("Check!")

    msga = Message(top, width = 100,  text=msg)
    msga.pack()

    button = Button(top,width = 50, text="Ok", command=top.destroy)
    button.pack()

if __name__== '__main__':
    root=tk.Tk()

    conf=[[[0 for x in range(4)] for y in range(8)] for z in range(8)]
    events=[]
    whites=[]
    blacks=[]



    gui=Gui(root, conf)
    white_king=King(root,"White", conf, events)
    white_king.place()

    black_king = King(root, "Black", conf, events)
    black_king.place()

    white_queen = Queen(root, "White", conf, events)
    white_queen.place()
    whites.append(white_queen)

    black_queen = Queen(root, "Black", conf, events)
    black_queen.place()
    blacks.append(black_queen)

    white_bishop1 = Bishop(root, "White", conf, events)
    white_bishop1.place()
    whites.append(white_bishop1)

    black_bishop1 = Bishop(root, "Black", conf, events)
    black_bishop1.place()
    blacks.append(black_bishop1)

    white_bishop2 = Bishop(root, "White", conf, events)
    white_bishop2.place()
    whites.append(white_bishop2)

    black_bishop2 = Bishop(root, "Black", conf, events)
    black_bishop2.place()
    blacks.append(black_bishop2)

    white_knight1 = Knight(root, "White", conf, events)
    white_knight1.place()
    whites.append(white_knight1)

    black_knight1 = Knight(root, "Black", conf, events)
    black_knight1.place()
    blacks.append(black_knight1)

    white_knight2 = Knight(root, "White", conf, events)
    white_knight2.place()
    whites.append(white_knight2)

    black_knight2 = Knight(root, "Black", conf, events)
    black_knight2.place()
    blacks.append(black_knight2)

    white_Rook1 = Rook(root, "White", conf, events)
    white_Rook1.place()
    whites.append(white_Rook1)

    black_Rook1 = Rook(root, "Black", conf, events)
    black_Rook1.place()
    blacks.append(black_Rook1)

    white_Rook2 = Rook(root, "White", conf, events)
    white_Rook2.place()
    whites.append(white_Rook2)

    black_Rook2 = Rook(root, "Black", conf, events)
    black_Rook2.place()
    blacks.append(black_Rook2)


    white_pawn=[]
    black_pawn=[]
    for i in range (8):
        white_pawn.append(Pawn(root, "White", conf,i, events))
        white_pawn[i].place()
        whites.append(white_pawn[i])

        black_pawn.append(Pawn(root, "Black", conf,i, events))
        black_pawn[i].place()
        blacks.append(black_pawn[i])

    tour ="White"

    root.mainloop()