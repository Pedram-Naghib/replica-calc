from tkinter import END
from math import sqrt, pow
from src.calc import e


class Calc:
    operation = ''
    f_num = 0

    def click(num):
        current = e.get()
        if current == "0":
            e.delete(0, END)
            e.insert(0, str(num))
        else:
            e.delete(0, END)
            e.insert(0, str(current) + str(num))

    def c_clear():
        e.delete(0, END)
        e.insert(0, "0")

    def back_space():
        current = str(e.get())
        e.delete(0, END)
        current = current[0:-1]
        if current == "":
            e.insert(0, "0")
        else:
            e.insert(0, str(current))

    def add():
        Calc.f_num = float(e.get())
        Calc.operation = "add"
        e.delete(0, END)

    def sub():
        firstnum = e.get()
        Calc.operation = "sub"
        Calc.f_num = float(firstnum)
        e.delete(0, END)

    def mul():
        firstnum = e.get()
        Calc.f_num = float(firstnum)
        Calc.operation = "mul"
        e.delete(0, END)

    def dev():
        firstnum = e.get()
        Calc.f_num = float(firstnum)
        Calc.operation = "dev"
        e.delete(0, END)

    def power():
        firstnum = e.get()
        Calc.f_num = float(firstnum)
        Calc.operation = "power"
        e.delete(0, END)

    def point():
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + ".")

    def sign():
        current = e.get()
        current = float(current) * -1
        e.delete(0, END)
        e.insert(0, str(current))

    def kasrline():
        current = e.get()
        try:
            amal = 1/float(current)
            e.delete(0, END)
            if float("%.0f" % amal) == amal:
                e.insert(0, "%.0f" % amal)
            else:
                e.insert(0, amal)
        except ZeroDivisionError:
            e.delete(0, END)
            e.insert(0, "Cannot divide by zero")

    def sroot():
        current = e.get()
        amal = sqrt(float(current))
        e.delete(0, END)
        if float("%.0f" % amal) == amal:
            e.insert(0, "%.0f" % amal)
        else:
            e.insert(0, amal)

    def percentage():
        current = e.get()
        num = (float(current)) / 100
        e.delete(0, END)
        e.insert(0, num)

    def equal():
        second_number = e.get()
        f_num = Calc.f_num
        e.delete(0, END)
        try:
            if Calc.operation == "add":
                result = f_num + float(second_number)
                if float("%.0f" % result) == result:
                    e.insert(0, int(result))
                else:
                    e.insert(0, f_num + float(second_number))

            elif Calc.operation == "sub":
                result = f_num - float(second_number)
                if float("%.0f" % result) == result:
                    e.insert(0, "%.0f" % result)
                else:
                    e.insert(0, f_num - float(second_number))

            elif Calc.operation == "mul":
                result = f_num * float(second_number)
                if float("%.0f" % result) == result:
                    e.insert(0, "%.0f" % result)
                else:
                    e.insert(0, f_num * float(second_number))

            elif Calc.operation == "dev":
                try:
                    result = f_num / float(second_number)
                    if float("%.0f" % result) == result:
                        e.insert(0, "%.0f" % result)
                    else:
                        e.insert(0, f_num / float(second_number))
                except ZeroDivisionError:
                    e.delete(0, END)
                    e.insert(0, "Cannot divide by zero")
            elif Calc.operation == "power":
                result = pow(f_num, float(second_number))
                if float("%.0f" % result) == result:
                    e.insert(0, "%.0f" % result)
                else:
                    e.insert(0, pow(f_num, float(second_number)))
        except NameError:
            e.insert(0, "0")
