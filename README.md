# Python-Clicker
apenas testando coisas
Código python:

from tkinter import *
from tkinter import ttk
from typing import Self
import time

dinheiro = 0
multiplicador = 1
dinheiroPorsegundo = 1
valorMultiplicador = 4
porcentagemDeAumento = 0.5

  
def Dinheiro_add():
  global dinheiro
  global dinheiroLb
  dinheiro += 1 * multiplicador
  dinheiro = round(dinheiro, 2)
  print("dinheiro:", dinheiro)

def Dinheiro_add_auto():
  global dinheiroPorsegundo
  dinhheiroPorsegundo = dinheiroPorsegundo* 2
  dinheiroPorsegundo = round(dinheiroPorsegundo, 2)
  print("dinheiro por segundo:", dinheiroPorsegundo)


def Multiplicador_add():
  global dinheiro
  global valorMultiplicador
  global atualizar
  if(dinheiro >= valorMultiplicador):
    dinheiro -= valorMultiplicador
    dinheiro = round(dinheiro,2)
    global multiplicador
    multiplicador += 1
    valorMultiplicador += valorMultiplicador * porcentagemDeAumento
    valorMultiplicador = round(valorMultiplicador, 2)
    print("valorMulti:",valorMultiplicador)
    print("multi",multiplicador)
  
  else:
    print("Dinheiro insuficiente")
    

Janela = Tk()
Janela.title("teste")
Janela.geometry("500x500")

ganhar = ttk.Button(Janela, text="Ganhar Dinheiro",command=Dinheiro_add)
ganhar.place(x=10, y= 10,width=480, height=480,)


comprar = ttk.Button(Janela, text="Aumentar Multi", command=Multiplicador_add)
comprar.place(x=300, y= 90)

while(True):
  time.sleep(0.05)
  comprarLb = Label(Janela, text="Preço: $"+str(valorMultiplicador))
  comprarLb.place(x=404, y=95)
  dinheiroLb = Label(Janela, text="Dinheiro: $"+str(dinheiro))
  dinheiroLb.place(x=0, y=0) 
  dinheiroPorsegundoLb = Label(Janela, text="Dinheiro por segundo: $"+str(dinheiroPorsegundo))
  dinheiroPorsegundoLb.place(x=0, y=20)
  
  Janela.update()
  while(True):
    time.sleep(1)
    dinheiro += 1 * dinheiroPorsegundo
    dinheiro =round(dinheiro, 2)
    print("dinheiro:", dinheiro)
    Janela.update()
#Entry().grid(row=0, column=0)
#texto = Entry().get()
#print(texto)
Janela.mainloop()
