from tkinter import *
import pyautogui as pg
import pyperclip as py
import time

def mensagem(repeticao):
    global texto_inicial, entradaMensagem
    jnlMensagem.deiconify()
    jnlMensagem.title('Mensagem a ser enviada')

    texto_inicial = Label(jnlMensagem, text="Digite a mensagem a ser enviada:")
    texto_inicial.grid(column=0, row=0, padx=10)

    entradaMensagem = Entry(jnlMensagem)
    entradaMensagem.grid(column=0, row=2, pady=25)

    botaoAdicionar = Button(jnlMensagem, text="Adicionar", command=lambda: verificarTextoMensagem(entradaMensagem.get(), repeticao))
    botaoAdicionar.grid(column=0, row=3)

def salvarMensagem(mensagem, repeticao):
    py.copy(mensagem)
    jnlMensagem.withdraw()   
    jnlLista.deiconify()
    coletaInformacoes(repeticao)
    print(mensagem)

def verificarTextoMensagem(entrada, repeticao):
    global texto_inicial

    if entrada == "":
        texto_inicial.config(text="Inválido. Digite novamente")
    else:
        salvarMensagem(entrada, repeticao)

def coletaInformacoes(repeticao):
    global texto_inicial, entrada, texto_clientes

    jnlLista.title('Automação de Envio de Mensagens')

    texto_inicial = Label(jnlLista, text="Digite o nome do Cliente Oculto:")
    texto_inicial.grid(column=0, row=0, padx=10, columnspan=2)

    entrada = Entry(jnlLista)
    entrada.grid(column=0, row=2, pady=25, columnspan=2)

    botaoAdicionar = Button(jnlLista, text="Adicionar", command=incrementarLista)
    botaoAdicionar.grid(column=0, row=3)

    botaoAdicionar = Button(jnlLista, text="Iniciar", command= lambda: enviarMensagens(repeticao))
    botaoAdicionar.grid(column=1, row=3, padx=1)

    texto_clientes = Label(jnlLista, text="")
    texto_clientes.grid(column=0, row=4, pady=6)
    

def incrementarLista():
    global tamanho

    clienteOculto = entrada.get()

    if clienteOculto == "":
        texto_inicial.config(text="Nome inválido. Digite novamente")
    else:
        
        Cos.append(clienteOculto)
        entrada.delete(0, END)
        texto_inicial.config(text="Digite o nome do Cliente Oculto")

        texto_clientes['text'] = Cos[tamanho]
        
        print(Cos, tamanho)

        tamanho = tamanho + 1

def enviarMensagens(repeticao):


    jnlLista.withdraw()
    tamanho = len(Cos)
    limite = 0

    print(repeticao)
    if tamanho ==0:
        texto_inicial.config(text='Erro. Não há nenhum nome')
        return
    
    # Verifica se é a primeira vez que o programa foi executado
        # Clica no ícone do navegador na barra de tarefas
    if repeticao == 'Primeiro':
        pg.click(x=498, y=1046)
    
    # Clica na primeira guia aberta no navegador (Whatsapp)
    time.sleep(0.7)
    pg.click(x=178, y=23)

    while tamanho > limite:

        # Clica na barra de pesquisa do Whatsapp
        time.sleep(0.7)
        pg.click(x=443, y=254)

        # Digita o nome do cliente oculto
        time.sleep(0.7)
        pg.write(Cos[limite])

        # Clica no cartão de contato correspondente à pesquisa
        time.sleep(0.7)
        pg.click(x=306, y=458)

        # Clica na barra para enviar a mensagem
        time.sleep(0.7)
        pg.click(x=1132, y=959)

        # Cola a mensagem
        time.sleep(0.7)
        pg.hotkey('ctrl', 'v')

        # Envia a mensagem
        time.sleep(0.7)
        pg.click(x=1842, y=954)

        limite = limite + 1
    
    reinicio()

def reinicio():
    jnlReinicio.deiconify()
    jnlReinicio.title('Deseja reiniciar')

    texto_inicial = Label(jnlReinicio, text='Mensagens enviadas. Deseja enviar novas mensagens?')
    texto_inicial.grid(column=0, row=0, padx=10, pady=20, columnspan=2)



    botaoAdicionar = Button(jnlReinicio, text="Sim", command=recomecar)
    botaoAdicionar.grid(column=0, row=4)

    botaoAdicionar = Button(jnlReinicio, text="Não", command= fim)
    botaoAdicionar.grid(column=1, row=4)


def recomecar():
    jnlReinicio.withdraw()
    mensagem("Dinovo")

def fim():
    jnlMensagem.destroy()


tamanho = 0

Cos = []
quantidade = len(Cos)

jnlMensagem = Tk()
jnlMensagem.withdraw()

jnlLista = Toplevel(jnlMensagem)
jnlLista.withdraw()

jnlReinicio = Toplevel(jnlMensagem)
jnlReinicio.withdraw()

mensagem("Primeiro")

jnlMensagem.mainloop()