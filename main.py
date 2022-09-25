import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import numpy as np
import tkinter as tk
import ctypes
import math
from math import *

# TODO: fare tante cose!
# TODO: sistemare il grafico (zoom e non zoom)
# example of some equation for plot

# Draw Hearth
# x = 16 * ( np.sin(np.linspace(0, 2 * np.pi, 100)) ** 3 )
# y = 13 * np.cos(np.linspace(0, 2 * np.pi, 100)) - 5 * np.cos(2 * np.linspace(0, 2 * np.pi, 100)) - 2 * np.cos(3 * np.linspace(0, 2 * np.pi, 100)) - np.cos(4 * np.linspace(0, 2 * np.pi, 100))


# Draw Normal Distribution
# x = np.linspace(-4, 4, 100)
# y = 1/(2 * np.pi)**0.5 * np.exp(-x**2 / 2)

# Draw Line Second Grade Equation

# (x-1)*(x+1)

# Draw Equation Sinc :>

# x = np.arange(-2*np.pi, 2*np.pi, 0.01)
# y = np.sinc(x)

# Draw Sine

#   x = np.arange(-3*np.pi, 3*np.pi, 0.01)

#   y = np.sin(x)
# Draw Circle


# x = radius * np.cos(np.linspace(0, 2 * np.pi, 100))

# y = radius * np.sin(np.linspace(0, 2 * np.pi, 100))


entryFontSize = 16
titleFontSize = 18
fontSize = 14

buttonWidth = 25
entryWidth = 31

backgroundColor = "#2F3136"
buttonBackgroundColor = "#393B40"
activeBackgroundColor = "#292b2F"

foregroundColor = "white"
textColor = foregroundColor

fontFamily = 'Verdana, sans-serif'


fig = plt.gcf()
fig.set_size_inches(10, 8)
ax = plt.subplot()
fig.subplots_adjust(left=0, top=0.95, right=1, bottom=0.015)


def sendEquationInput(xEquationEntry, yEquationEntry):
    try:
        x, y = 0, 0

        x = eval(xEquationEntry)
        y = eval(yEquationEntry)

        ax.plot(x, y)
        plt.show()
    except Exception as e:
        ctypes.windll.user32.MessageBoxW(
            0, "Qualcosa è andato storto, controlla gli input!", "Uh Oh!", 16)
        print(e)


def sendLineInput(equationEntry):
    try:
        x = np.linspace(-30, 30, 100)
        y = eval(equationEntry)
        ax.plot(x, y)
        plt.show()
    except Exception as e:
        ctypes.windll.user32.MessageBoxW(
            0, "Qualcosa è andato storto, controlla gli input!", "Uh Oh!", 16)
        print(e)


def sendInput(xEntry, yEntry):
    try:
        # x1 = float(xEntry.get().split(",")[0])
        # y1 = float(yEntry.get().split(",")[0])

        # x2 = float(xEntry.get().split(",")[1])
        # y2 = float(yEntry.get().split(",")[1])

        x1 = float(xEntry.split(",")[0])
        x2 = float(yEntry.split(",")[0])

        y1 = float(xEntry.split(",")[1])
        y2 = float(yEntry.split(",")[1])

        xm = (x1+x2) / 2
        ym = (y1+y2) / 2

        v1 = [x1, x2]
        v2 = [y1, y2]
        ax.plot(v1, v2, "-o")

        ax.plot(xm, ym, "o")
        d1 = (x2-x1)**2
        d2 = (y2-y1)**2

        print(float(yEntry.split(",")[0]),
              float(xEntry.split(",")[0]))

        distance = math.sqrt(d1 + d2)

        plt.text(-0.5, 20, "Distanza: {}\nPunto Medio: {}, {}".format(
            round(distance, 2), xm, ym), size=fontSize,
            ha="left", va="top",
            bbox=dict(boxstyle="round",
                      #    ec=(1., 0.5, 0.5),
                      fc=("#D3D3D3"),
                      )
        )

        print(distance)

        plt.show()
    except Exception as e:
        ctypes.windll.user32.MessageBoxW(
            0, "Qualcosa è andato storto, controlla gli input!", "Uh Oh!", 16)
        print(e)


def DrawSegment():
    top = tk.Tk()
    top.configure(bg=backgroundColor)
    top.title('Disegna segmento')

    top.resizable(False, False)

    top.geometry('450x250')

    tk.Label(top, text="Inserisci le coordinate separandole con una virgola!",
             fg=foregroundColor, bg=backgroundColor, font=(fontFamily, fontSize)).pack()

    tk.Label(top, text="Prima Coordinata:", fg=foregroundColor,
             bg=backgroundColor, font=(fontFamily, fontSize)).pack(pady=10)

    xEntry = tk.Entry(top, width=entryWidth, font=(
        fontFamily, entryFontSize), bg=buttonBackgroundColor, fg=foregroundColor, border=0)
    xEntry.pack()

    tk.Label(top, text="Seconda coordinata:", fg=foregroundColor,
             bg=backgroundColor, font=(fontFamily, fontSize)).pack(pady=10)

    yEntry = tk.Entry(top, width=entryWidth, font=(
        fontFamily, entryFontSize), bg=buttonBackgroundColor, fg=foregroundColor, border=0)
    yEntry.pack()

    # place a button on the root window
    sendInputButton = tk.Button(
        top, text="Disegna segmento", border=0, disabledforeground=foregroundColor, bg=buttonBackgroundColor, width=15, activebackground=activeBackgroundColor,
        activeforeground=foregroundColor, fg=foregroundColor, font=(fontFamily, titleFontSize), command=lambda: sendInput(xEntry.get(), yEntry.get()))

    sendInputButton.pack(pady=entryFontSize)

    top.mainloop()


def DrawEquation():

    top = tk.Tk()
    top.configure(bg=backgroundColor)
    top.title('Disegna con equazione, per veri C.U.R.R.O')

    top.resizable(False, False)

    top.geometry("450x250")

    tk.Label(top, text="Inserisci l'equazione di x:", fg=foregroundColor,
             bg=backgroundColor, font=(fontFamily, fontSize)).pack(pady=10)

    xEquationEntry = tk.Entry(top, width=entryWidth, font=(
        fontFamily, entryFontSize), bg=buttonBackgroundColor, fg=foregroundColor, border=0)
    xEquationEntry.pack()

    tk.Label(top, text="Inserisci l'equazione di y:", fg=foregroundColor,
             bg=backgroundColor, font=(fontFamily, fontSize)).pack(pady=10)
    yEquationEntry = tk.Entry(top, width=entryWidth, font=(
        fontFamily, entryFontSize), bg=buttonBackgroundColor, fg=foregroundColor, border=0)
    yEquationEntry.pack()

    equationButton = tk.Button(
        top, text="Disegna equazione", border=0, disabledforeground=foregroundColor, bg=buttonBackgroundColor, width=15, activebackground=activeBackgroundColor,
        activeforeground=foregroundColor, fg=foregroundColor, font=(fontFamily, titleFontSize), command=lambda: sendEquationInput(xEquationEntry.get(), yEquationEntry.get()))

    equationButton.pack(pady=entryFontSize)
    top.mainloop()


def DrawLine():
    top = tk.Tk()
    top.configure(bg=backgroundColor)
    top.title('Disegna linea')

    top.resizable(False, False)

    top.geometry("300x150")

    tk.Label(top, text="Inserisci l'equazione della retta y=", fg=foregroundColor,
             bg=backgroundColor, font=(fontFamily, fontSize)).pack(pady=10)

    lineEntry = tk.Entry(top, width=23, font=(
        fontFamily, entryFontSize), bg=buttonBackgroundColor, fg=foregroundColor, border=0)
    lineEntry.pack()

    lineButton = tk.Button(
        top, text="Disegna retta", border=0, disabledforeground=foregroundColor, bg=buttonBackgroundColor, width=15, activebackground=activeBackgroundColor,
        activeforeground=foregroundColor, fg=foregroundColor, font=(fontFamily, titleFontSize), command=lambda: sendLineInput(lineEntry.get()))

    lineButton.pack(pady=15)

    top.mainloop()


############################################################################################
# configure the root window
root = tk.Tk()
root.title('C.U.R.R.O Setup')
root.geometry('450x250')
root.configure(bg=backgroundColor)
root.resizable(False, False)

# button
segmentButton = tk.Button(
    root, text='Disegna un segmento', border=0, disabledforeground=foregroundColor, width=buttonWidth, pady=10, bg=buttonBackgroundColor, activebackground=activeBackgroundColor,
    activeforeground=foregroundColor, fg=foregroundColor, font=(fontFamily, titleFontSize))

segmentButton['command'] = DrawSegment

segmentButton.pack(anchor=tk.CENTER, pady=10)

lineButton = tk.Button(
    root, text='Disegna una retta', border=0, disabledforeground=foregroundColor, width=buttonWidth, pady=10, bg=buttonBackgroundColor, activebackground=activeBackgroundColor,
    activeforeground=foregroundColor, fg=foregroundColor, font=(fontFamily, titleFontSize))


lineButton['command'] = DrawLine

lineButton.pack(anchor=tk.CENTER, pady=10)

equationButton = tk.Button(
    root, text='Disegna con equazione', border=0, disabledforeground=foregroundColor, width=buttonWidth, pady=10, bg=buttonBackgroundColor, activebackground=activeBackgroundColor,
    activeforeground=foregroundColor, fg=foregroundColor, font=(fontFamily, titleFontSize))


equationButton['command'] = DrawEquation

equationButton.pack(anchor=tk.CENTER, pady=10)

# def button_clicked(root):

#   showinfo(title='Information', message='Hello, rootinter!')


def createCartesianPlane():

    xmin, xmax, ymin, ymax = -30, 30, -30, 30

    v1 = [0, 0]
    v2 = [0, 0]

    ticks_freq = 1

    ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect="equal")

    ax.spines["bottom"].set_position("zero")
    ax.spines["left"].set_position("zero")

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.set_xlabel("x", size=14, labelpad=-24, x=1.03)
    ax.set_ylabel("y", size=14, labelpad=-21, y=1.02, rotation=0)

    x_ticks = np.arange(xmin, xmax+1, ticks_freq)
    y_ticks = np.arange(ymin, ymax+1, ticks_freq)

    ax.set_xticks(x_ticks[x_ticks != 0])
    ax.set_yticks(y_ticks[y_ticks != 0])

    ax.set_xticks(np.arange(xmin, xmax+1), minor=True)
    ax.set_xticks(np.arange(ymin, ymax+1), minor=True)

    ax.axis([-10, 10, -10, 10])

    ax.grid(which="both", color="grey",
            linewidth=1, linestyle="-", alpha=0.2)

    arrow_fmt = dict(markersize=4, color="black", clip_on=False)

    ax.plot((1), (0), marker=">",
            transform=ax.get_yaxis_transform(), **arrow_fmt)
    ax.plot((0), (1), marker="^",
            transform=ax.get_xaxis_transform(), **arrow_fmt)

    def clear(val):
        for i in range(0, len(ax.lines)):
            ax.lines.remove(ax.lines[0])

    axclear = fig.add_axes([0.84, 0.015, 0.14, 0.045])

    clearBtn = Button(axclear, "Pulisci il grafico")
    clearBtn.on_clicked(clear)

    plt.show()


createCartesianPlane()
