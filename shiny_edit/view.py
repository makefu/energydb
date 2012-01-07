#!/usr/bin/python2
from Tkinter import *
import simplejson as json
from decimal import Decimal
SCHEMA_FILE='../schema.json'

json_file="../model.json"

def todec(s):
    return Decimal(str(round(float(s),3)))
class App(Frame):
  def saveIt(self):
    drink = {}
    drink['Nutritions'] = nutr = {}
    for k,v in self.review.iteritems():
      if k is 'Nutritions':
        for ingredient,val in v.iteritems():
          if ingredient is not 'others':
            try: 
              nutr[ingredient] = todec(val.get())
            except: 
              print ingredient,"fixed from",val," to 0"
              nutr[ingredient] = 0
          else:
            nutr[ingredient] = val.get()

      else:
        if k in ['taste','look','overall','tribute']:
          drink[k] = v.get(1.0,END)[:-1] #kill trailing \n from text field
        else:
          drink[k] = v.get()

    for v in ['rating','volume','paid']:
      try:
        drink[v] = todec(self.review[v].get())
      except Exception as e:
        print 'could not convert',v,'to decimal'
        drink[v] = 0
    drink['CO2'] = True if drink['CO2'] else False
    print drink
    if raw_input('really want to save????').upper() not in ['Y','YES','1']:
      print 'aborting'
      return

    drinktab = {}
    key = drink['key']
    del(drink['key'])

    f = open(json_file)
    drinktab = json.load(f,parse_float=todec)
    f.close()
    if key in drinktab:
        print "already have this key included!"
        return
    drinktab[key]= drink
    f = open(json_file,'w+')
    f.write(json.dumps(drinktab,indent=4,use_decimal=True,sort_keys=True))
    f.close()
    print 'saved!'

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
    row = 0
    rev_frame = Frame(f,borderwidth=4)
    rev_frame.pack(side=LEFT,fill=BOTH,expand=YES)
    rev_frame.columnconfigure(0,weight=1)
    rev_frame.columnconfigure(1,weight=2)
    big_fields = ['taste','look','overall','tribute']
    small_fields = ['bought from','paid','url','volume','rating']
    all_fields = big_fields + small_fields
    for k in all_fields:
      bground = 'grey' if not row %2 else 'lightgrey'
      l = Label(rev_frame,text=k.capitalize()+':',bg=bground)
      t = ''
      align = ''
      if k in big_fields:
        print k,'is a big field'
        t =  Text(rev_frame,height=mheight,width=mwidth)
        align = N+E+W+S
        weight = 1
      if k in small_fields:
        print k,'is a small field'
        align = E+W
        weight = 0
        if k is not 'rating':
          t =  Entry(rev_frame,width=mwidth)
        else:
          l= Label(rev_frame,text='Rating:',bg=bground,font='courier 20 bold')
          t = Entry(rev_frame,font='courier 30 bold',width=mwidth/6)

      self.review[k] = t
      rev_frame.rowconfigure(row,weight=weight)
      l.grid(sticky=align,row=row)
      t.grid(row=row,column=1,sticky=align)
      row+=1

  def createIngredientField(self,f):
    mwidth = 10
    mheight=5
    msticky=E+W+N
    row = 0
    ingFrame = Frame(f,borderwidth=4)
    ingFrame.pack(side=RIGHT,fill=BOTH,expand=YES)
    ingFrame.columnconfigure(0,weight=1)
    ingFrame.columnconfigure(1,weight=1)

    ingFrame.rowconfigure(row,weight=1)
    lTaste = Label(ingFrame,text='Nutritions',bg='grey')
    lTaste.grid(sticky=E+W,row=row,columnspan=3)
    row+=1

    scheme = {}
    with open(SCHEMA_FILE) as s:
      scheme =json.load(s) 
    nut = scheme['Nutritions']

    for ingredient,t in nut.iteritems():
      ingFrame.rowconfigure(row,weight=1)
      bground = 'grey' if row %2 else 'lightgrey'
      lTaste = Label(ingFrame,text=ingredient,bg=bground)
      lTaste.grid(sticky=E+W,row=row)
      p = self.review['Nutritions'][ingredient] = Entry(ingFrame,width=mwidth)
      p.grid(sticky=W+E,column=1,row=row)

      lTaste = Label(ingFrame,text=t,bg=bground)
      lTaste.grid(row=row,column=2,sticky=E+W)
      row+=1



    

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
