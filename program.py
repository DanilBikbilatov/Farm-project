#!/usr/bin/env python
# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import *
from tkinter.ttk import *

from PIL import ImageTk, Image
import Animal
import Owner
import numpy as np
import random
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class MakeTable(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.create_ui()
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

    def create_ui(self):
        treev = Treeview(self)

        treev['columns'] = ('Начало года', 'Конец года')
        treev.heading("#0", text='Животные')
        treev.column("#0", anchor='center', width=80)

        treev.heading('Начало года', text='Начало года')
        treev.column('Начало года', anchor='center', width=80)

        treev.heading('Конец года', text='Конец года')
        treev.column('Конец года', anchor='center', width=80)

        treev.grid(sticky=(N, S, W, E))
        self.treeview = treev
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def load_table(self, dic, year):
        if year == 0:
            self.treeview.insert('', 'end', text="Молодые",
                                 values=(int(dic.get('y_amount')), int(dic.get('y_Oldamount'))))
            self.treeview.insert('', 'end', text="Взрослые",
                                 values=(int(dic.get('a_amount')), int(dic.get('a_Oldamount'))))
            self.treeview.insert('', 'end', text="Старые",
                                 values=(int(dic.get('o_amount')), int(dic.get('o_Oldamount'))))
            self.treeview.insert('', 'end', text="", values=('', ''))
        else:
            self.treeview.insert('', 'end', text="Молодые",
                                 values=(int(dic.get('y_Oldamount')), int(dic.get('y_amount'))))
            self.treeview.insert('', 'end', text="Взрослые",
                                 values=(int(dic.get('a_Oldamount')), int(dic.get('a_amount'))))
            self.treeview.insert('', 'end', text="Старые",
                                 values=(int(dic.get('o_Oldamount')), int(dic.get('o_amount'))))
            self.treeview.insert('', 'end', text="", values=('', ''))

class Interface(tk.Frame):
    """docstring for Experiment"""
    diction = {}
    cur_year = 0
    active_widjets = {}
    used_btns = {}
    arr_capital = []

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.gui()

    def gui(self):
        self.master.title("Молочная ферма")
        self.pack(fill=BOTH, expand=True)
        self.center_window()

#---------- Зона активных действий с животными -----------------------
        panel_active = tk.Frame(self, bg='white')
        panel_active.place(x=10, y=10, width=680, height=400)
# рисование
        self.img = Image.open("farm.jpg")
        self.tatras = ImageTk.PhotoImage(self.img.resize((680, 350), Image.ANTIALIAS))

        canvas = Canvas(self, width=674, height=350)
        self.active_widjets['canvas'] = canvas
        canvas.place(x=10, y=10)

        canvas.create_image(0, 0, anchor=NW, image=self.tatras)
    
# кнопка завершения
        def end_action(event):
            exit()

        def show_params():

            def put_in_right_place(name, widget, pointx, pointy, wid_name):
                if '.!interface.!scale' in str(widget):
                    self.diction[name] = int(widget.get())
                    wid = tk.Label(text=str(widget.get()), fg='black', font='arial 15')
                    widget.destroy()
                    self.active_widjets[wid_name] = wid
                    wid.place(x=pointx, y=pointy)
                else:
                    pass

            put_in_right_place('feed_cost', self.active_widjets['scale_feedcost'], 880,
                               130, 'scale_feedcost')
            put_in_right_place('all_food', self.active_widjets['scale_allfood'], 1000,
                               170, 'scale_allfood')
            put_in_right_place('young_sell', self.active_widjets['scale_y_sell'], 880,
                               250, 'scale_y_sell')
            put_in_right_place('young_cost', self.active_widjets['scale_y_cost'], 1000,
                               250, 'scale_y_cost')
            put_in_right_place('adult_sell', self.active_widjets['scale_a_sell'], 880,
                               290, 'scale_a_sell')
            put_in_right_place('adult_cost', self.active_widjets['scale_a_cost'], 1000, 290,
                               'scale_a_cost')
            put_in_right_place('old_sell', self.active_widjets['scale_o_sell'], 880,
                               330, 'scale_o_sell')
            put_in_right_place('old_cost', self.active_widjets['scale_o_cost'], 1000,
                               330, 'scale_o_cost')
            put_in_right_place('penalty', self.active_widjets['scale_penalty'], 880,
                               370, 'scale_penalty')

            if self.cur_year == 0:

                put_in_right_place('contract_time', self.active_widjets['scale_contract'],
                                   880, 90, 'scale_contract')
                put_in_right_place('capital', self.active_widjets['scale_capital'],
                                   880, 510, 'scale_capital')
                put_in_right_place('y_amount', self.active_widjets['scale_y_amount'],
                                   980, 570, 'scale_y_amount')
                put_in_right_place('a_amount', self.active_widjets['scale_a_amount'],
                                   980, 610, 'scale_a_amount')
                put_in_right_place('o_amount', self.active_widjets['scale_o_amount'],
                                   980, 650, 'scale_o_amount')


            animal = Animal.Animal(self.diction, self.cur_year)
            animal_amount = animal.count_newamount_animal()
            if self.diction.get('all_food') < animal.count_need_food():
                arr = np.array(animal_amount)
                animal_amount = arr * 0.8  

            self.diction['y_Oldamount'] = self.diction.get('y_amount')
            self.diction['a_Oldamount'] = self.diction.get('a_amount')
            self.diction['o_Oldamount'] = self.diction.get('o_amount')

            self.diction['y_amount'] = animal_amount[0]
            self.diction['a_amount'] = animal_amount[1]
            self.diction['o_amount'] = animal_amount[2]

            owner = Owner.Owner(self.diction, self.cur_year)
            self.diction['capital'] = owner.sell()
            self.diction['flag'] = owner.paying_capacity()

            self.arr_capital.append(int(self.diction.get('capital')))

            if self.cur_year > 0 and self.cur_year <= self.diction.get('contract_time'):
                self.used_btns['g_btn1'].destroy()
                self.used_btns['g_btn2'].destroy()

            if self.cur_year < self.diction.get('contract_time'):

                self.cur_year = self.cur_year + 1

                if self.cur_year == 1:
                    self.used_btns['s_btn'].destroy()

                if self.cur_year <= self.diction.get('contract_time'):

                    g_btn = Button(self, text=u'Следующий шаг', command=next_step_all)
                    self.used_btns['g_btn'] = g_btn
                    g_btn.place(x=30, y=370, width=150, height=30)


#---------- Зона изменения начальных параметров ----------------------

        panel_param = tk.Frame(self, bg='white')
        panel_param.place(x=700, y=420, width=490, height=290)

        l11 = tk.Label(text='Начальные данные', width=20, bg='lightgreen',
                       fg='black', font='arial 25')
        l11.place(x=800, y=440)

        l22 = tk.Label(text='Капитал :', fg='black', font='arial 15', bg='white')
        l22.place(x=750, y=510)
        scale_capital = tk.Scale(self, length=100, orient=HORIZONTAL, from_=50000,
                                 to=100000, resolution=5000)
        self.active_widjets['scale_capital'] = scale_capital
        scale_capital.place(x=880, y=490)

        l33 = tk.Label(text='Количество голов  :', fg='black', font='arial 15', bg='white')
        l33.place(x=750, y=550)

        l44 = tk.Label(text='- молодых  ', fg='black', font='arial 15', bg='white')
        l44.place(x=870, y=570)
        scale_y_amount = tk.Scale(self, length=100, orient=HORIZONTAL, from_=30,
                                  to=60, resolution=5)
        self.active_widjets['scale_y_amount'] = scale_y_amount
        scale_y_amount.place(x=980, y=550)

        l55 = tk.Label(text='- взрослых  ', fg='black', font='arial 15', bg='white')
        l55.place(x=870, y=610)
        scale_a_amount = tk.Scale(self, length=100, orient=HORIZONTAL, from_=50,
                                  to=100, resolution=5)
        self.active_widjets['scale_a_amount'] = scale_a_amount
        scale_a_amount.place(x=980, y=590)

        l66 = tk.Label(text='- старых  ', fg='black', font='arial 15', bg='white')
        l66.place(x=870, y=650)
        scale_o_amount = tk.Scale(self, length=100, orient=HORIZONTAL, from_=20,
                                  to=70, resolution=5)
        self.active_widjets['scale_o_amount'] = scale_o_amount
        scale_o_amount.place(x=980, y=630)

    def center_window(self):
        width = 1200
        height = 720
        screen_w = self.master.winfo_screenwidth()
        screen_h = self.master.winfo_screenheight()
        osx = (screen_w - width)/2
        osy = (screen_h - height)/2
        self.master.geometry('%dx%d+%d+%d' % (width, height, osx, osy))


if __name__ == '__main__':
    root = Tk()
    Interface(root)
    root.resizable(False, False)
    root.mainloop()
