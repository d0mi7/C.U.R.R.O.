import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
import numpy as np
import tkinter as tk
import ctypes
import math
# x = np.arange(0, 2, 0.01)
# y = 1 + np.sin(2 * np.ap * x)

# theta = np.linspace(0, 2 * np.ap, 100)

# x = 16 * ( np.sin(np.linspace(0, 2 * np.pi, 100)) ** 3 )
# y = 13 * np.cos(np.linspace(0, 2 * np.pi, 100)) - 5* np.cos(2*np.linspace(0, 2 * np.pi, 100)) - 2 * np.cos(3*np.linspace(0, 2 * np.pi, 100)) - np.cos(4*np.linspace(0, 2 * np.ap, 100))

# ax = plt.subplot()

# ax.plot(x, y)

# ax.set(xlabel="X -->", ylabel="Y -->", title="C.U.R.R.O.")
# ax.set(xlabel="X -->", ylabel="Y -->", title="<3")
# ax.grid()
# plt.show()


# colors = ["m", "r", "g", "b"]
#mettere sendInput su e il button mettere la funzione lambda e passare x ed y

def sendEquationInput():
    try:
        x = eval(xEquationEntry.get())
        y = eval(yEquationEntry.get())
        ax.plot(x,y)
        plt.show()
    except Exception as e:
        ctypes.windll.user32.MessageBoxW(
            0, "Qualcosa è andato storto, controlla gli input!", "Uh Oh!", 16)
        print(e)
        
        
def sendInput():
  try:
      # x1 = float(xEntry.get().split(",")[0])
      # y1 = float(yEntry.get().split(",")[0])
      
      # x2 = float(xEntry.get().split(",")[1])
      # y2 = float(yEntry.get().split(",")[1])

      x1 = float(xEntry.get().split(",")[0])
      x2 = float(yEntry.get().split(",")[0])
      
      y1 = float(xEntry.get().split(",")[1])
      y2 = float(yEntry.get().split(",")[1])

      xm = (x1+x2) / 2
      ym = (y1+y2) / 2
      

      v1 = [x1, x2]
      v2 = [y1, y2]


      ax.plot(v1, v2, "r-o")

      ax.plot(xm, ym, "ro")

    
      d1 = (x2-x1)**2
      d2 = (y2-y1)**2

      print(float(yEntry.get().split(",")[0]),
            float(xEntry.get().split(",")[0]))

      distance = math.sqrt(d1 + d2)

      text = AnchoredText("Distanza: {}\nPunto Medio: {}, {}".format(distance, xm, ym), loc=1, pad=0.5, borderpad=1)
      plt.gca().add_artist(text)

      print(distance)

      plt.show()


  except Exception as e:
        ctypes.windll.user32.MessageBoxW(
            0, "Qualcosa è andato storto, controlla gli input!", "Uh Oh!", 16)
        print(e)



#firs root for the normal drawed line

topDrawLine = tk.Tk()
topDrawLine.geometry('300x200')
topDrawLine.title('C.U.R.R.O Setup')
tk.Label(topDrawLine, text="Inserisci le coordinate separandole con una virgola!").pack()

tk.Label(topDrawLine, text="prima coordinata:").pack()


xEntry = tk.Entry(topDrawLine)
xEntry.pack()

tk.Label(topDrawLine, text="seconda coordinata:").pack()


yEntry = tk.Entry(topDrawLine)
yEntry.pack()




        # place a button on the root window
sendInputButton = tk.Button(topDrawLine, text="Disegna linea", command=sendInput)

sendInputButton.pack()

#second root for equation
topEquatio = tk.Tk()
topEquatio.geometry("300x100")

tk.Label(topEquatio, text="inserisci l'equazione di x:").pack()

xEquationEntry = tk.Entry(topEquatio)
xEquationEntry.pack()

tk.Label(topEquatio, text="inserisci l'equazione di y:").pack()
yEquationEntry = tk.Entry(topEquatio)
yEquationEntry.pack()

equationButton = tk.Button(topEquatio, text="Disegna equazione", command=sendEquationInput)

equationButton.pack()


xmin, xmax, ymin, ymax = -30, 30, -30, 30

v1 = [0,0]
v2 = [0,0]

ticks_freq = 1

fig = plt.gcf()
fig.set_size_inches(10,8)
ax = plt.subplot()

ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect="equal")

ax.spines["bottom"].set_position("zero")
ax.spines["left"].set_position("zero")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.set_xlabel("x", size=14, labelpad=-24, x=1.03)
ax.set_ylabel("y", size=14, labelpad=-21, y=1.02, rotation = 0)

x_ticks = np.arange(xmin, xmax+1, ticks_freq)
y_ticks = np.arange(ymin, ymax+1, ticks_freq)

ax.set_xticks(x_ticks[x_ticks!=0])
ax.set_yticks(y_ticks[y_ticks!=0])

ax.set_xticks(np.arange(xmin, xmax+1), minor=True)
ax.set_xticks(np.arange(ymin, ymax+1), minor=True)

ax.axis([-10, 10, -10, 10])

ax.grid(which="both", color="grey", linewidth=1, linestyle="-", alpha=0.2)

arrow_fmt = dict(markersize=4, color="black", clip_on=False)

ax.plot((1), (0), marker=">", transform=ax.get_yaxis_transform(), **arrow_fmt)
ax.plot((0), (1), marker="^", transform=ax.get_xaxis_transform(), **arrow_fmt)


plt.show()
topDrawLine.mainloop()
topEquatio.mainloop() 