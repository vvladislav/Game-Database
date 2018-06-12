#!/usr/bin/python
# -*- coding: utf-8 -*-


def display():
    # first part
    import main
    import tkinter as tk
    class scrollFrame(tk.Frame):
        def __init__(self, parent, *args, **kw):
            tk.Frame.__init__(self, parent, *args, **kw)            

            # create a canvas object and a vertical scrollbar for scrolling it
            vscrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
            vscrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
            canvas = tk.Canvas(self, bd=0, highlightthickness=0,
                            yscrollcommand=vscrollbar.set)
            canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
            vscrollbar.config(command=canvas.yview)

            # reset the view
            canvas.xview_moveto(0)
            canvas.yview_moveto(0)

            # create a frame inside the canvas which will be scrolled with it
            self.interior = interior = tk.Frame(canvas)
            interior_id = canvas.create_window(0, 0, window=interior,
                                               anchor=tk.NW)

            # track changes to the canvas and frame width and sync them,
            # also updating the scrollbar
            def _configure_interior(event):
                # update the scrollbars to match the size of the inner frame
                size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
                canvas.config(scrollregion="0 0 %s %s" % size)
                if interior.winfo_reqwidth() != canvas.winfo_width():
                    # update the canvas's width to fit the inner frame
                    canvas.config(width=interior.winfo_reqwidth())
            interior.bind('<Configure>', _configure_interior)

            def _configure_canvas(event):
                if interior.winfo_reqwidth() != canvas.winfo_width():
                    # update the inner frame's width to fill the canvas
                    canvas.itemconfigure(interior_id, width=canvas.winfo_width())
            canvas.bind('<Configure>', _configure_canvas)

    class MainWindow:
        def __init__(self):
            self.flagSort = 0
            self.currSort = ""
            self.base = main.readData()
            self.p = []
            self.im = tk.Label(root)
            self.im.place(x=0, y=0, relwidth=1, relheight=1)
            self.frame_all = tk.Frame(self.im)
            self.scrollF = scrollFrame(self.frame_all)
            self.frame_sort = tk.Frame(self.frame_all)
            self.frame_add =  tk.Frame(self.frame_all)
            self.frame_search =  tk.Frame(self.frame_all)
            self.frame_exit =  tk.Frame(self.frame_all)
            self.sequence = [0,2,1,3,5,6,4]
            self.width = [12,8,9,9,2,16,16]


            class skip:
                def __init__(self, name):
                    self.s = name
                    self.i1 = -1
                    self.j = 9
                    self.focus = self.s[self.i1:self.j]
                    self.flag = 0
                    self.flagButScroll = 0
                def cancelSkip(self):
                    self.flagButScroll = 1
                def scroll(self,but):
                    self.flagButScroll = 0
                    self.i1 = -1
                    self.j = 9
                    def change():
                        if ( self.j < len(self.s) or self.i1 == -1):
                            self.i1 = self.i1 + 1
                            self.j = self.j + 1
                            self.focus = self.s[self.i1:self.j]
                    change()
                    but["text"] = self.focus
                    def flagPlus():
                        self.flag = self.flag + 1
                    self.flag = self.j
                    while (self.flag < len(self.s) ):
                        but["text"] = self.focus
                        flagPlus()
                        if (self.flagButScroll == 1):
                            root.after_cancel(a)
                            root.after_cancel(b)
                            break
                        a = root.after(300, change())
                        but["text"] = self.focus
                        but.update()
                    self.flag = 0
                    b = root.after(1000)
                    self.focus = self.s[0:10]
                    but["text"] = self.focus
                    but.update()
                def getName(self):
                    return self.s
                def setName(self,name):
                    self.s = name


#Поле = {"Название игры":0, "Жанр":1, "Платформа":2, "Год выпуска":3, "Цена":4, "Разработчик":5, "Издатель":6}
            # Search
            self.exit = tk.Button( self.frame_exit, text = "Exit", command = root.destroy, bg = "white", fg="black")

            self.pSkip = []
            self.pos = []
            for j in range(7):#self.sequence:
                self.pos.append(tk.Button( self.frame_sort, width = self.width[j], text = main.unfield[j], bg = "white", fg="black"))
                toP = []
                pToSkip = []
                i = 0
                while ( i < len(self.base) ):
                    pToSkip.append(skip(self.base[i][self.sequence[j]]))
                    toP.append(tk.Button(self.scrollF.interior, width = self.width[self.sequence[j]]))
                    i = i + 1
                self.pSkip.append(pToSkip)
                self.p.append(toP)
                i = 0
                while ( i < len(self.base) ):
                    self.p[j][i - 1].bind( "<Enter>", lambda event, i=i, j=j: self.pSkip[j][i-1].scroll(self.p[j][i-1]))
                    self.p[j][i - 1].bind( "<Leave>", lambda event, i=i, j=j: self.pSkip[j][i-1].cancelSkip())
                    i = i + 1

            # Add
            self.addSpace = tk.Label( self.frame_add, width = 2 )
            self.add =  tk.Button( self.frame_add, text = "Add", bg = "white", fg="black")
            self.addNameGame = tk.Entry( self.frame_add, width = 15 )
            self.addPlat = tk.Entry( self.frame_add, width = 12 )
            self.addGenre = tk.Entry( self.frame_add, width = 10 )
            self.addYear = tk.Entry( self.frame_add, width = 12 )
            self.addDevel = tk.Entry( self.frame_add, width = 19 )
            self.addPublisher = tk.Entry( self.frame_add, width = 19 )
            self.addPrice = tk.Entry( self.frame_add, width = 5 )

            # init
            self.init_widget()
        def init_widget(self):
            for i in range(7):
                self.pos[i].bind('<ButtonRelease-1>', lambda event, i=i: self.sortDisp(event, main.unfield[self.sequence[i]]))
                self.pos[i].grid( row = 0, column = i )


            self.exit.grid()
            #self.scrollF.config(width = 500, heigth = 400)
            self.frame_all.place( x = 100, y = 50, width = 2791, height = 1500 )
            
            self.exit.bind('<ButtonRelease-1>')
            #self.exit.place(x = 1050, y = 650, width = 75, height = 40)

            self.frame_sort.grid( row = 0, column = 0)
            self.scrollF.grid( row = 1, column = 0)
            self.frame_add.grid( row = 2, column = 0)
            self.frame_search.grid( row = 1, column = 1)
            self.frame_exit.grid( row = 3, column = 1)

            # add
            self.add.bind('<ButtonRelease-1>', lambda event: self.buttAdd(event))
            self.addSpace.grid( row = 0, column = 0)
            self.addNameGame.grid( row = 0, column = 1)
            self.addPlat.grid( row = 0, column = 2)
            self.addGenre.grid( row = 0, column = 3)
            self.addYear.grid( row = 0, column = 4)
            self.addDevel.grid( row = 0, column = 5)
            self.addPublisher.grid( row = 0, column = 6)
            self.addPrice.grid( row = 0, column = 7)
            self.add.grid( row = 0, column = 8)
            # functions
            self.buttSort()
            
        def buttSort(self):
            for j in range(7):
                i = 0
                while ( i < len(self.base)):
                    self.pSkip[j][i].setName(self.base[i][self.sequence[j]])
                    self.p[j][i]["text"] = self.pSkip[j][i].getName()[0:10]
                    self.p[self.sequence[j]][i].grid( row = i, column = self.sequence[j])
                    #self.pNG[i].delete(1,tk.END)
                    #self.pNG[i].insert(0,self.base[i][0])
                    i = i + 1
        #def buChange(self, i, j ):
            #///grid
        def buttAdd(self, event):
                a = []
                # appends
                a.append(self.addNameGame.get())
                a.append(self.addGenre.get())
                a.append(self.addPlat.get())
                a.append(self.addYear.get())
                a.append(self.addPrice.get())
                a.append(self.addDevel.get())
                a.append(self.addPublisher.get())
                flag = 1
                for i in a:
                    if (len(i) == 0):
                        flag = 0
                if (flag == 1):
                    # delete
                    self.addNameGame.delete(1,tk.END)
                    self.addPlat.delete(1,tk.END)
                    self.addGenre.delete(1,tk.END)
                    self.addYear.delete(1,tk.END)
                    self.addDevel.delete(1,tk.END)
                    self.addPublisher.delete(1,tk.END)
                    self.addPrice.delete(1,tk.END)
                    # add to base
                    main.addRecord(self.base,a)
                    self.base.append(a)
                    self.buttSort()
                self.addNameGame.place( x = 100, y = 600)
                self.addPlat.place( x = 226, y = 600)
                self.addGenre.place( x = 328, y = 600)
                self.addYear.place( x = 413, y = 600)
                self.addDevel.place( x = 515, y = 600)
                self.addPublisher.place( x = 674, y = 600)
                self.addPrice.place( x = 833, y = 600)
            
        def sortDisp(self, event, newSort):
            if ( self.currSort == newSort ):
                self.flagSort = (self.flagSort + 1) % 2
            else: 
                self.flagSort = 1
            self.base = main.sort(newSort, self.flagSort)
            self.currSort = newSort
            self.buttSort()

    root = tk.Tk()
    root.title("Games Date Base")
    root.geometry('1280x720')
    window = MainWindow()
    root.mainloop()
display()
