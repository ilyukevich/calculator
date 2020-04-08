# coding=utf-8
# graphical calculator v2
# 08 apr 2020

from tkinter import *

class Application(Frame):
    """GUI application, calculator with graphical interface"""

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """create widgets"""
        self.result = Entry(self, width = 20, font = ("Impact", 24))
        self.result.grid(row = 0, column = 0)
        Button(self, text = "1", width = 5, height = 0, font = ("Impact", 24), bg = '#808080',
               activebackground = '#555555', command = self.bttn_1).grid(row = 1, column = 0, sticky = W)
        Button(self, text = "2", width = 5, height = 0, font = ("Impact", 24), bg = '#808080',
               activebackground = '#555555', command = self.bttn_2).grid(row = 1, column = 0, sticky = S)
        Button(self, text = "3", width = 5, height = 0, font = ("Impact", 24), bg = '#808080',
               activebackground = '#555555', command = self.bttn_3).grid(row = 1, column = 0, sticky = E)
        Button(self, text = "4", width = 5, height = 0, font = ("Impact", 24), bg = '#808080',
               activebackground = '#555555', command = self.bttn_4).grid(row = 2, column = 0, sticky = W)
        Button(self, text = "5", width = 5, height = 0, font = ("Impact", 24), bg = '#808080',
               activebackground = '#555555', command = self.bttn_5).grid(row = 2, column = 0, sticky = S)
        Button(self, text = "6", width = 5, height = 0, font = ("Impact", 24), bg = '#808080',
               activebackground = '#555555', command = self.bttn_6).grid(row = 2, column = 0, sticky = E)
        Button(self, text = "7", width = 5, height = 0, font = ("Impact", 24), bg = '#808080',
               activebackground = '#555555', command = self.bttn_7).grid(row = 3, column = 0, sticky = W)
        Button(self, text = "8", width = 5, height = 0, font = ("Impact", 24), bg = '#808080',
               activebackground = '#555555', command = self.bttn_8).grid(row = 3, column = 0, sticky = S)
        Button(self, text = "9", width = 5, height = 0, font = ("Impact", 24), bg = '#808080',
               activebackground = '#555555', command = self.bttn_9).grid(row = 3, column = 0, sticky = E)
        Button(self, text = "0", width = 5, height = 0, font = ("Impact", 24), bg = '#808080',
               activebackground = '#555555', command = self.bttn_0).grid(row = 4, column = 0, sticky = S)
        Button(self, text = "*", width = 5, height = 0, font = ("Impact", 24), activebackground = '#555555',
               command = self.multiplication).grid(row = 4, column = 0, sticky = W)
        Button(self, text = "/", width = 5, height = 0, font = ("Impact", 24), activebackground = '#555555',
               command = self.division).grid(row = 4, column = 0, sticky = E)
        Button(self, text = "=", width = 5, height = 0, font = ("Impact", 24), activebackground = '#555555',
               command = self.calculation).grid(row = 6, column = 0, sticky = S)
        Button(self, text = "Quit", width = 5, height = 0, font = ("Impact", 24), activebackground = '#555555',
               command = self.quit).grid(row = 6, column = 0, sticky = E)
        Button(self, text = ".", width = 5, height = 0, font = ("Impact", 24), activebackground = '#555555',
               command = self.bttn_dot).grid(row = 6, column = 0, sticky = W)
        Button(self, text = "С", width = 5, height = 0, font = ("Impact", 24), activebackground = '#555555',
               command = self.clear).grid(row = 5, column = 0, sticky = E)
        Button(self, text = "+", width = 5, height = 0, font = ("Impact", 24), activebackground = '#555555',
               command = self.addition).grid(row = 5, column = 0, sticky = W)
        Button(self, text = "-", width = 5, height = 0, font = ("Impact", 24), activebackground = '#555555',
               command = self.subtraction).grid(row = 5, column = 0, sticky = S)

    def clear(self):
        """clear results screen"""
        self.result.delete(0, END)

    def bttn_1(self):
        """Button '1'"""
        self.result.insert(END, "1")

    def bttn_2(self):
        """Button '2'"""
        self.result.insert(END, "2")

    def bttn_3(self):
        """Button '3'"""
        self.result.insert(END, "3")

    def bttn_4(self):
        """Button '4'"""
        self.result.insert(END, "4")

    def bttn_5(self):
        """Button '5'"""
        self.result.insert(END, "5")

    def bttn_6(self):
        """Button '6'"""
        self.result.insert(END, "6")

    def bttn_7(self):
        """Button '7'"""
        self.result.insert(END, "7")

    def bttn_8(self):
        """Button '8'"""
        self.result.insert(END, "8")

    def bttn_9(self):
        """Button '9'"""
        self.result.insert(END, "9")

    def bttn_0(self):
        """Button '0'"""
        self.result.insert(END, "0")

    def bttn_dot(self):
        """Button '.'"""
        self.result.insert(END, ".")

    def addition(self):
        """Button '+'"""
        #self.result.delete(0.0, END)
        self.result.insert(END, "+")

    def subtraction(self):
        """Button '-'"""
        #self.result.delete(0.0, END)
        self.result.insert(END, "-")

    def multiplication(self):
        """Button '*'"""
        #self.result.delete(0.0, END)
        self.result.insert(END, "*")

    def division(self):
        """Button '/'"""
        #self.result.delete(0.0, END)
        self.result.insert(END, "/")


    def calculation(self):
        """calculation, button '='"""
        act = str(self.result.get())
        self.result.delete(0, END)

        if "+" in act:
            list = act.split('+')
            rez = float(list[0]) + float(list[1])
            self.result.insert(END, rez)

        elif "-" in act:
            list = act.split('-')
            rez = float(list[0]) - float(list[1])
            self.result.insert(END, rez)

        elif "*" in act:
            list = act.split('*')
            num1 = float(list[0])
            num2 = float(list[1])
            rez = num1 * num2
            self.result.insert(END, rez)

        elif "/" in act:
            list = act.split('/')
            num1 = float(list[0])
            num2 = float(list[1])
            if num2 == 0:
                self.result.insert(END, "Can not be divided by '0'!")
            else:
                rez = num1 / num2
                self.result.insert(END, rez)

        else:
            self.result.insert(END, "Error!")

# main part
root = Tk()
root.title("Calculator v2")
app = Application(root)
root.mainloop()
