import tkinter as tk
from tkinter import messagebox
import random

class num():

    def __init__(self, a, b, d, h):

        self.gus = int(a)
        self.ans = int(b)
        self.ow = int(d)
        self.hi = int(h)

        if self.gus != self.ans:
            if self.gus > self.ans:
                if self.gus < self.hi:
                    self.hi = self.gus
            elif self.gus < self.ans or self.gus < self.ow:
                if self.gus > self.ow:
                    self.ow = self.gus
        else:
            tk.messagebox.showwarning(title='嘿', message='猜對了')
            self.ow = 1
            self.hi = 100
            self.ans = int(random.randint(2, 99))
            self.oo()
            self.hh()
            self.www()


    def oo(self):
        aa = self.ow
        return aa

    def hh(self):
        bb = self.hi
        return bb

    def www(self):
        c = self.ans
        return c

    '''def rd(self):
        dd = int(random.randint(2, 99))
        return dd'''