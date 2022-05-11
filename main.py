import tkinter as tk
from datetime import datetime


cor1 = "#3d3d3d" # preta
cor2 = "#fafcff" # branca
cor3 = "#21c25c" # verde
cor4 = "eb463b"  # vermelha
cor5 = "dedcdc" # cinza
cor6 = "#3080f0" # azul

fundo = cor1 
cor = cor6

janela = tk.Tk()
janela.title("")
janela.geometry('550x200')
janela.resizable(width=False, height=False)
janela.configure(bg=cor1)

def relogio():
    tempo = datetime.now()
    hora = tempo.strftime('%H:%M:%S')
    dia_semana = tempo.strftime('%A')
    dia = tempo.day
    mes = tempo.strftime('%b')
    ano = tempo.strftime('%Y')

    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config(text=dia_semana +"  " + str(dia) + "/" + str(mes) + "/" + str(ano))

l1 = tk.Label(janela, text='', font=('digital-7 100'), bg=fundo, fg=cor)
l1.grid(row=0, column=0, sticky='NW', padx=5)

l2 = tk.Label(janela, text='', font=('digital-7 20'), bg=fundo, fg=cor)
l2.grid(row=1, column=0, sticky='NW', padx=5)

relogio()
janela.mainloop()