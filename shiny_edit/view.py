from Tkinter import *
SCHEMA_FILE='../schema.json'
class App(Frame):
  def saveIt(self):
    print "saved!"
  def createHead(self):
    top = Frame(self,borderwidth=4)
    top.pack(fill=BOTH,expand=NO)
    top.columnconfigure(0,weight=1)
    top.columnconfigure(1,weight=1)
    top.columnconfigure(2,weight=1)
    top.columnconfigure(3,weight=1)
    top.columnconfigure(4,weight=1)
    top.columnconfigure(5,weight=1)

    lKey = Label(top,text='Key:',bg='grey',width=1)
    lKey.grid(sticky=E+W,column=0,row=0)
    t = self.review['key'] = Entry(top,width=1)
    t.grid(sticky=W+E,column=1,row=0)

    lName = Label(top,text='Name:',bg='grey',width=1)
    lName .grid(sticky=E+W,column=2,row=0)
    t = self.review['name'] = Entry(top,width=1)
    t.grid(sticky=W+E,column=3,row=0)

    lCO = Label(top,text='CO2:',bg='grey',width=1)
    lCO.grid(sticky=E+W,column=4,row=0)
    self.review['CO2'] = BooleanVar()
    t = Checkbutton(top,variable=self.review['CO2'],onvalue=True,offvalue=False,width=1)
    t.grid(sticky=W+E,column=5,row=0)


  def createCenter(self):
    center_frame = Frame(self)
    center_frame.pack(fill=BOTH,expand=YES)
    self.createReviewField(center_frame)
    self.createIngredientField(center_frame)

  def createReviewField(self,f):
    mwidth = 30
    mheight=5
    msticky=E+N+W+S
    row = 0
    rev_frame = Frame(f,borderwidth=4)
    rev_frame.pack(side=LEFT,fill=BOTH,expand=YES)
    rev_frame.columnconfigure(0,weight=1)
    rev_frame.columnconfigure(1,weight=2)

    rev_frame.rowconfigure(row,weight=1)
    lTaste = Label(rev_frame,text='Taste:',bg='grey')
    lTaste.grid(sticky=msticky,row=row)
    t = self.review['taste'] = Text(rev_frame,height=mheight,width=mwidth)
    t.grid(sticky=W+E+N+S,column=1,row=row)
    row+=1

    rev_frame.rowconfigure(row,weight=1)
    lLook= Label(rev_frame,text='Look:',bg='lightgrey')
    lLook.grid(sticky=msticky,row=row)
    l = self.review['look'] = Text(rev_frame,height=mheight,width=mwidth)
    l.grid(sticky=W+E+N+S,column=1,row=row)
    row+=1

    rev_frame.rowconfigure(2,weight=1)
    lOverall = Label(rev_frame,text='Overall:',bg='grey')
    lOverall.grid(sticky=msticky,row=2)
    o = self.review['overall'] = Text(rev_frame,height=mheight,width=mwidth)
    o.grid(sticky=W+E+N+S,column=1,row=row)
    row+=1

    rev_frame.rowconfigure(row,weight=0)
    lBought = Label(rev_frame,text='Bought from:',bg='lightgrey')
    lBought.grid(sticky=msticky,row=row)
    b = self.review['bought from'] = Entry(rev_frame,width=mwidth)
    b.grid(sticky=W+E,column=1,row=row)
    row+=1

    rev_frame.rowconfigure(row,weight=0)
    lBought = Label(rev_frame,text='Paid:',bg='grey')
    lBought.grid(sticky=msticky,row=row)
    p = self.review['paid'] = Entry(rev_frame,width=mwidth)
    p.grid(sticky=W+E,column=1,row=row)
    row+=1

    rev_frame.rowconfigure(row,weight=0)
    lBought = Label(rev_frame,text='URL:',bg='lightgrey')
    lBought.grid(sticky=msticky,row=row)
    p = self.review['url'] = Entry(rev_frame,width=mwidth)
    p.grid(sticky=W+E,column=1,row=row)
    row+=1

    rev_frame.rowconfigure(row,weight=0)
    lRating = Label(rev_frame,text='Rating:',bg='grey',font='courier 20 bold')
    lRating.grid(sticky=N+S+E+W,row=row)
    r = self.review['rating'] = Entry(rev_frame,font='courier 30 bold',width=mwidth/6)
    r.grid(sticky=W+E+N+S,column=1,row=row)

  def createIngredientField(self,f):
    ingFrame = Frame(f,borderwidth=4)
    ingFrame.pack(side=RIGHT,fill=BOTH,expand=YES)
    ingFrame.columnconfigure(0,weight=2)
    #ingFrame.columnconfigure(1,weight=1)
    ingFrame.rowconfigure(0,weight=1)
    ingFrame.rowconfigure(1,weight=1)
    lab = Label(ingFrame,text='Label',bg='grey')
    lab.grid(sticky=W+E+N+S)
    e1 = Entry(ingFrame)
    e1.grid(sticky=W+E,column=1,row=0)
    lab2 = Label(ingFrame,text='Label 2',bg='grey')
    lab2.grid(sticky=W+E,row=1)
    e2 = Entry(ingFrame)
    e2.grid(sticky=W+E,column=1,row=1)

  def createBottom(self):
    bottom = Frame(self,borderwidth=4)
    bottom.columnconfigure(0,weight=1)
    bottom.pack(side=BOTTOM,fill=X,expand=NO)

    save = Button(bottom)
    save['text'] = 'Save!'
    save['bg'] = 'grey'
    save['command'] = self.saveIt
    save.grid(sticky=W+E)

  def createWidgets(self):
    self.createHead()
    self.createCenter()
    self.createBottom()

  def __init__(self,master=None):
    Frame.__init__(self,master)
    self.review = {}
    self.review['Nutritions'] = {}
    self.pack(fill=BOTH,expand=YES)
    self.createWidgets()

root = Tk()
app = App(master=root)
app.mainloop()
