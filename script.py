import pyautogui as pg
import pyperclip as py
import time
from tkinter import Tk, Label, Entry, Button

janela = Tk()

last_space_press_time = 0
Cos = []
quantidade = len(Cos)
py.copy("Olá! Somos da Sax Conta pra Gente! Venha nos conhecer")

janela.title("Automação de mensagens")
texto = Label(janela, text="Digite o nome do Cliente Oculto")
entrada = Tk.Entry(janela, width=30)
entrada.pack(padx=10, pady=10)

Co = entrada.get()
        
if Co == "  ":
    contador = 0

    Cos.append(Co)

def mensagens():
    tamanho = len(Cos)
    limite = 0

    pg.click(x=489, y=1048)
    time.sleep(0.5)


    while tamanho > limite:

        pg.click(x=584, y=255)
        pg.click()

        pg.click(x=330, y=265)

        time.sleep(0.5)
        pg.typewrite(Cos[limite])

        time.sleep(0.5)
        pg.click(x=820, y=958)
        pg.hotkey("ctrl", "v")

        time.sleep(0.5)
        pg.press('enter')

        time.sleep(0.5)
        pg.click(x=584, y=255)
        pg.click()

        time.sleep(0.5)

        limite = limite + 1

mensagens()
janela.mainloop()