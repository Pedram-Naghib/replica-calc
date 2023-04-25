import tkinter as tk
from src.calc import root
from src.operations import Calc


percentage = tk.Button(root, text="%", command=Calc.percentage,
                       width=10, height=3, bg="#696969", fg="white")
CE = tk.Button(root, text="CE", width=10, height=3, bg="#696969", fg="white")
c_lear = tk.Button(root, text="C", command=Calc.c_clear, width=10,
                   height=3, bg="#696969", fg="white")
back_space = tk.Button(root, text="<-", command=Calc.back_space, width=10,
                       height=3, bg="#696969", fg="white")
kasrline = tk.Button(root, text="1/x", command=Calc.kasrline,
                     width=10, height=3, bg="#696969", fg="white")
power = tk.Button(root, text="x^x", command=Calc.power, width=10,
                  height=3, bg="#696969", fg="white")
sroot = tk.Button(root, text="√", command=Calc.sroot, width=10,
                  height=3, bg="#696969", fg="white")
devide = tk.Button(root, text="÷", command=Calc.dev, width=10,
                   height=3, bg="#696969", fg="white")
seven = tk.Button(root, text="7", command=lambda: Calc.click(
    7), width=10, height=3, bg="#1f1f1f", fg="white")
eight = tk.Button(root, text="8", command=lambda: Calc.click(
    8), width=10, height=3, bg="#1f1f1f", fg="white")
nine = tk.Button(root, text="9", command=lambda: Calc.click(
    9), width=10, height=3, bg="#1f1f1f", fg="white")
mult = tk.Button(root, text="×", command=Calc.mul, width=10,
                 height=3, bg="#696969", fg="white")
four = tk.Button(root, text="4", command=lambda: Calc.click(
    4), width=10, height=3, bg="#1f1f1f", fg="white")
five = tk.Button(root, text="5", command=lambda: Calc.click(
    5), width=10, height=3, bg="#1f1f1f", fg="white")
six = tk.Button(root, text="6", command=lambda: Calc.click(
    6), width=10, height=3, bg="#1f1f1f", fg="white")
minus = tk.Button(root, text="-", command=Calc.sub, width=10,
                  height=3, bg="#696969", fg="white")
one = tk.Button(root, text="1", command=lambda: Calc.click(
    1), width=10, height=3, bg="#1f1f1f", fg="white")
two = tk.Button(root, text="2", command=lambda: Calc.click(
    2), width=10, height=3, bg="#1f1f1f", fg="white")
three = tk.Button(root, text="3", command=lambda: Calc.click(
    3), width=10, height=3, bg="#1f1f1f", fg="white")
plus = tk.Button(root, text="+", command=Calc.add, width=10,
                 height=3, bg="#696969", fg="white")
sign = tk.Button(root, text="±", command=Calc.sign, width=10,
                 height=3, bg="#1f1f1f", fg="white")
zero = tk.Button(root, text="0", command=lambda: Calc.click(0), width=10,
                 height=3, bg="#1f1f1f", fg="white", font=("Helvetica", 9))
point = tk.Button(root, text=".", command=Calc.point, width=10,
                  height=3, bg="#1f1f1f", fg="white")
equal = tk.Button(root, text="=", command=Calc.equal,
                  width=10, height=3, bg="#036fc4", fg="white")


percentage.grid(row=1, column=0)
CE.grid(row=1, column=1)
c_lear.grid(row=1, column=2)
back_space.grid(row=1, column=3)
kasrline.grid(row=2, column=0)
power.grid(row=2, column=1)
sroot.grid(row=2, column=2)
devide.grid(row=2, column=3)
seven.grid(row=3, column=0)
eight.grid(row=3, column=1)
nine.grid(row=3, column=2)
mult.grid(row=3, column=3)
four.grid(row=4, column=0)
five.grid(row=4, column=1)
six.grid(row=4, column=2)
minus.grid(row=4, column=3)
one.grid(row=5, column=0)
two.grid(row=5, column=1)
three.grid(row=5, column=2)
plus.grid(row=5, column=3)
sign.grid(row=6, column=0)
zero.grid(row=6, column=1)
point.grid(row=6, column=2)
equal.grid(row=6, column=3)
