from tkinter import *
from tkinter import ttk
from typing import Self
import time
import threading

dinheiro = 0
multiplicador = 1
dinheiroPorsegundo = 0
valorMultiplicador = 40
valorAutoclicker = 100
porcentagemDeAumento = 0.5
cliques = 0
cliquesMoni = 0


def Dinheiro_add():
  global dinheiro
  global dinheiroLb, cliquesMoni
  dinheiro += 1 * multiplicador
  dinheiro = round(dinheiro, 2)
  print("dinheiro:", dinheiro)
  cliquesMoni +=1

def Dinheiro_add_auto():
  global dinheiroPorsegundo
  global valorAutoclicker
  global dinheiro
  if (dinheiro >= valorAutoclicker):
    dinheiroPorsegundo = dinheiroPorsegundo * 2
    if(dinheiroPorsegundo == 0):
      dinheiroPorsegundo += 0.5

    dinheiro -= valorAutoclicker
    valorAutoclicker += valorAutoclicker * porcentagemDeAumento
    dinheiroPorsegundo = round(dinheiroPorsegundo, 2)
    dinheiro = round(dinheiro, 2)
    print("dinheiro por segundo:", dinheiroPorsegundo)
    print("valor do autoclicker:", valorAutoclicker)

  else:
    print("Dinheiro insuficiente")


def Multiplicador_add():
  global dinheiro
  global valorMultiplicador
  if (dinheiro >= valorMultiplicador):
    dinheiro -= valorMultiplicador
    dinheiro = round(dinheiro, 2)
    global multiplicador
    multiplicador += 1
    valorMultiplicador += valorMultiplicador * porcentagemDeAumento
    valorMultiplicador = round(valorMultiplicador, 2)
    print("valorMulti:", valorMultiplicador)
    print("multi", multiplicador)

  else:
    print("Dinheiro insuficiente")


Janela = Tk()
Janela.title("teste")
Janela.geometry("500x500")

ganhar = ttk.Button(Janela, text="Ganhar Dinheiro", command=Dinheiro_add)
ganhar.place(
    x=10,
    y=10,
    width=480,
    height=480,
)

comprar = ttk.Button(Janela, text="Aumentar Multi", command=Multiplicador_add)
comprar.place(x=300, y=90)

auto = ttk.Button(Janela, text="Comprar Auto", command=Dinheiro_add_auto)
auto.place(x=300, y=150)

def auto_money():
    global dinheiro, dinheiroPorsegundo, cliquesMoni, cliques
    while True:
        time.sleep(1)
        cliques = cliquesMoni
        cliquesMoni = 0
        if dinheiroPorsegundo > 0:
            
            dinheiro += dinheiroPorsegundo
            dinheiro = round(dinheiro, 2)
            print("dinheiro:" + str(dinheiro))

# Start auto money thread
threading.Thread(target=auto_money, daemon=True).start()

while True:
    time.sleep(0.05)
    comprarLb = Label(Janela, text="Preço: $" + str(valorMultiplicador))
    comprarLb.place(x=404, y=95)
    dinheiroLb = Label(Janela, text="Dinheiro: $" + str(dinheiro))
    dinheiroLb.place(x=0, y=0)
    dinheiroPorsegundoLb = Label(Janela,
                                text="Dinheiro por segundo: $" +
                                str(dinheiroPorsegundo + cliques*multiplicador))
    dinheiroPorsegundoLb.place(x=150, y=0)
    autoLb = Label(Janela, text="Preço: $" + str(valorAutoclicker))
    autoLb.place(x=404, y=150)

    cliquesLb = Label(Janela, text="Cliques/s: " + str(cliques))
    cliquesLb.place(x=0, y=50)
  
    Janela.update()
  
Janela.mainloop()
