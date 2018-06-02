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
            self.pNG = []
            self.pP = []
            self.pG = []
            self.pY = []
            self.pD = []
            self.pPu = []
            self.pPr = []
            self.scrollF = scrollFrame(root)

#Поле = {"Название игры":0, "Жанр":1, "Платформа":2, "Год выпуска":3, "Цена":4, "Разработчик":5, "Издатель":6}
            # Search
            self.posNameGame = tk.Button( root, text = "Название игры", bg = "white", fg="black")
            i = 0
            self.exit = tk.Button( root, text = "Exit", command = root.destroy, bg = "white", fg="black")
            while ( i < len(self.base)):
                self.pNG.append(tk.Entry(self.scrollF.interior, width = 15  ))
                i = i + 1
            self.posPlat = tk.Button( root, text = "Платформа", bg = "white", fg="black")
            i = 0
            while ( i < len(self.base)):
                self.pP.append(tk.Entry(self.scrollF.interior, width = 12 ))
                i = i + 1
            self.posGenre = tk.Button( root, text = "Жанр", bg = "white", fg="black")
            i = 0
            while ( i < len(self.base)):
                self.pG.append(tk.Entry(self.scrollF.interior, width = 10 ))
                i = i + 1
            self.posYear = tk.Button( root, text = "Год выпуска", bg = "white", fg="black")
            i = 0
            while ( i < len(self.base)):
                self.pY.append(tk.Entry(self.scrollF.interior, width = 12 ))
                i = i + 1
            self.posDevel = tk.Button( root, text = "Разработчик", bg = "white", fg="black")
            i = 0
            while ( i < len(self.base)):
                self.pD.append(tk.Entry(self.scrollF.interior, width = 19 ))
                i = i + 1
            self.posPublisher = tk.Button( root, text = "Издатель", bg = "white", fg="black")
            i = 0
            while ( i < len(self.base)):
                self.pPu.append(tk.Entry(self.scrollF.interior, width = 19 ))
                i = i + 1
            self.posPrice = tk.Button( root, text = "Цена", bg = "white", fg="black")
            i = 0
            while ( i < len(self.base)):
                self.pPr.append(tk.Entry(self.scrollF.interior, width = 5 ))
                i = i + 1

            # Add
            self.add =  tk.Button( root, text = "Add", bg = "white", fg="black")
            self.addNameGame = tk.Entry( root, width = 15 )
            self.addPlat = tk.Entry( root, width = 12 )
            self.addGenre = tk.Entry( root, width = 10 )
            self.addYear = tk.Entry( root, width = 12 )
            self.addDevel = tk.Entry( root, width = 19 )
            self.addPublisher = tk.Entry( root, width = 19 )
            self.addPrice = tk.Entry( root, width = 5 )

            # init
            self.init_widget()
        def init_widget(self):
            self.posNameGame.bind('<ButtonRelease-1>',
                         lambda event: self.sortDisp(event, "Название игры"))
            self.posNameGame.place(x = 100, y = 50, width = 126, height = 25)
            self.posPlat.bind('<ButtonRelease-1>',
                         lambda event: self.sortDisp(event, "Платформа"))
            self.posPlat.place(x = 226, y = 50, width = 102, height = 25)
            self.posGenre.bind('<ButtonRelease-1>',
                         lambda event: self.sortDisp(event, "Жанр"))
            self.posGenre.place(x = 328, y = 50, width = 85, height = 25)
            self.posYear.bind('<ButtonRelease-1>',
                         lambda event: self.sortDisp(event, "Год выпуска"))
            self.posYear.place(x = 413, y = 50, width = 103, height = 25)
            self.posDevel.bind('<ButtonRelease-1>',
                         lambda event: self.sortDisp(event, "Разработчик"))
            self.posDevel.place(x = 515, y = 50, width = 159, height = 25)
            self.posPublisher.bind('<ButtonRelease-1>',
                         lambda event: self.sortDisp(event, "Издатель"))
            self.posPublisher.place(x = 674, y = 50, width = 159, height = 25)
            self.posPrice.bind('<ButtonRelease-1>',
                         lambda event: self.sortDisp(event, "Цена"))
            self.posPrice.place(x = 833, y = 50, width = 44, height = 25)
            self.exit.bind('<ButtonRelease-1>')
            self.exit.place(x = 1050, y = 650, width = 75, height = 40)
            self.scrollF.place( x = 100, y = 75, width = 791, height = 500 )
            # add
            self.add.bind('<ButtonRelease-1>', lambda event: self.buttAdd(event))
            self.add.place( x = 895, y = 600)
            self.addNameGame.place( x = 100, y = 600)
            self.addPlat.place( x = 226, y = 600)
            self.addGenre.place( x = 328, y = 600)
            self.addYear.place( x = 413, y = 600)
            self.addDevel.place( x = 515, y = 600)
            self.addPublisher.place( x = 674, y = 600)
            self.addPrice.place( x = 833, y = 600)
            # functions
            self.buttSort()
            
#Поле = {"Название игры":0, "Жанр":1, "Платформа":2, "Год выпуска":3, "Цена":4, "Разработчик":5, "Издатель":6}
        def buttSort(self):
            i = 0
            while ( i < len(self.base)):
                self.pNG[i].delete(1,tk.END)
                self.pNG[i].insert(0,self.base[i][0])
                self.pNG[i].grid( row = i, column = 1)
                self.pP[i].delete(1,tk.END)
                self.pP[i].insert(0,self.base[i][2])
                self.pP[i].grid( row = i, column = 2)
                self.pG[i].delete(1,tk.END)
                self.pG[i].insert(0,self.base[i][1])
                self.pG[i].grid( row = i, column = 3)
                self.pY[i].delete(1,tk.END)
                self.pY[i].insert(0,self.base[i][3])
                self.pY[i].grid( row = i, column = 4)
                self.pD[i].delete(1,tk.END)
                self.pD[i].insert(0,self.base[i][5])
                self.pD[i].grid( row = i, column = 5)
                self.pPu[i].delete(1,tk.END)
                self.pPu[i].insert(0,self.base[i][6])
                self.pPu[i].grid( row = i, column = 6)
                self.pPr[i].delete(1,tk.END)
                self.pPr[i].insert(0,self.base[i][4])
                self.pPr[i].grid( row = i, column = 7)
                i = i + 1
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
