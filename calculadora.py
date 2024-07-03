import math
from tkinter import *

simbolo = "0"
primeiro_num = "0"
segundo_num = "0"
igual = False
ja_foi_feita_uma_operacao = False

def soma(x,y):
    return (x+y)

def subtracao(x,y):
    return (x-y)

def multiplicacao(x,y):
    return(x*y)

def divisao(x,y):
    return(x/y)

def potenciacao(x,y):
    if y == 1:
        return (x)
    else:
        return (x * potenciacao(x,y-1))
    
def raiz_quadrada(x):
    return (math.isqrt(x))

def calculadora(operando):
    global simbolo
    global igual
    global primeiro_num
    global segundo_num
    global ja_foi_feita_uma_operacao

    if operando == "=":
        igual = True
        
    if operando == "end all":
        texto_resultados.delete(2.0,"end")
        texto_resultados.delete(1.0,"end")
        simbolo = "0"
        primeiro_num = "0"
        segundo_num = "0"
        igual  = False
        return

    if simbolo == "Raiz de ":
        if igual:
            texto_resultados.delete(2.0,"end")
            texto_resultados.delete(1.0,"end")
            primeiro_num = raiz_quadrada(int(segundo_num))
            texto_resultados.insert(2.0,primeiro_num)
            segundo_num = "0"
            simbolo = "0"
            igual = False
            return

    if operando == "+" or operando == "-"  or operando == "*" or operando == "/" or operando == "^" or operando == "Raiz de ":
        simbolo = operando
        print(simbolo)
        texto_resultados.insert(2.0,simbolo)
        return

    if simbolo != "0" and operando != "=":
        segundo_num += operando
        print(segundo_num)
        texto_resultados.insert(2.0,operando)
        return

    if simbolo != "0":
        if igual:
            if simbolo == "+":
                texto_resultados.delete(2.0,"end")
                texto_resultados.delete(1.0,"end")
                primeiro_num = soma(int(primeiro_num),int(segundo_num))
                texto_resultados.insert(2.0,primeiro_num)
                segundo_num = "0"
                simbolo = "0"
                igual = False
                ja_foi_feita_uma_operacao = True
                return
            
            if simbolo == "-":
                texto_resultados.delete(2.0,"end")
                texto_resultados.delete(1.0,"end")
                primeiro_num = subtracao(int(primeiro_num),int(segundo_num))
                texto_resultados.insert(2.0,primeiro_num)
                segundo_num = "0"
                simbolo = "0"
                igual = False
                ja_foi_feita_uma_operacao = True
                return
            
            if simbolo == "*":
                texto_resultados.delete(2.0,"end")
                texto_resultados.delete(1.0,"end")
                primeiro_num = multiplicacao(int(primeiro_num),int(segundo_num))
                texto_resultados.insert(2.0,primeiro_num)
                segundo_num = "0"
                simbolo = "0"
                igual = False
                ja_foi_feita_uma_operacao = True
                return
            
            if simbolo == "/":
                texto_resultados.delete(2.0,"end")
                texto_resultados.delete(1.0,"end")
                primeiro_num = divisao(int(primeiro_num),int(segundo_num))
                texto_resultados.insert(2.0,primeiro_num)
                segundo_num = "0"
                simbolo = "0"
                igual = False
                ja_foi_feita_uma_operacao = True
                return
            
            if simbolo == "^":
                texto_resultados.delete(2.0,"end")
                texto_resultados.delete(1.0,"end")
                primeiro_num = potenciacao(int(primeiro_num),int(segundo_num))
                texto_resultados.insert(2.0,primeiro_num)
                segundo_num = "0"
                simbolo = "0"
                igual = False
                ja_foi_feita_uma_operacao = True
                return
    
    if ja_foi_feita_uma_operacao:
        primeiro_num = operando
        texto_resultados.delete(2.0,"end")
        texto_resultados.delete(1.0,"end")
        texto_resultados.insert(2.0,primeiro_num)
        ja_foi_feita_uma_operacao = False
        return


    primeiro_num += operando
    print(primeiro_num)
    texto_resultados.insert(2.0,operando)
    return

janela = Tk()
janela.title("Calculadora")
janela.geometry("400x450")

texto_resultados = Text(janela,height = 3, width=22, font=("Arial",25))
texto_resultados.grid(columnspan = 4)
botao1 = Button(janela,text = "1",command = lambda:calculadora("1"),width = 5,font=("Arial",20))
botao1.grid(column = 0,row = 3)
botao2 = Button(janela,text = "2",command = lambda:calculadora("2"),width = 5,font=("Arial",20))
botao2.grid(column = 1,row = 3)
botao3 = Button(janela,text = "3",command = lambda:calculadora("3"),width = 5,font=("Arial",20))
botao3.grid(column = 2,row = 3)
botao4 = Button(janela,text = "4",command = lambda:calculadora("0","4"),width = 5,font=("Arial",20))
botao4.grid(column = 3,row = 3)
botao5 = Button(janela,text = "5",command = lambda:calculadora("5"),width = 5,font=("Arial",20))
botao5.grid(column = 0,row = 4)
botao6 = Button(janela,text = "6",command = lambda:calculadora("6"),width = 5,font=("Arial",20))
botao6.grid(column = 1,row = 4)
botao7 = Button(janela,text = "7",command = lambda:calculadora("7"),width = 5,font=("Arial",20))
botao7.grid(column = 2,row = 4)
botao8 = Button(janela,text = "8",command = lambda:calculadora("8"),width = 5,font=("Arial",20))
botao8.grid(column = 3,row = 4)
botao9 = Button(janela,text = "9",command = lambda:calculadora("9"),width = 5,font=("Arial",20))
botao9.grid(column = 0,row = 5)
botao0 = Button(janela,text = "0",command = lambda:calculadora("0"),width = 5,font=("Arial",20))
botao0.grid(column = 1,row = 5)
botaosoma = Button(janela,text = "+",command = lambda:calculadora("+"),width = 5,font=("Arial",20))
botaosoma.grid(column = 0,row = 6)
botaosubtracao = Button(janela,text = "-",command = lambda:calculadora("-"),width = 5,font=("Arial",20))
botaosubtracao.grid(column = 1,row = 6)
botaomultiplicacao = Button(janela,text = "*",command = lambda:calculadora("*"),width = 5,font=("Arial",20))
botaomultiplicacao.grid(column = 0,row = 7)
botaodivisao = Button(janela,text = "/",command = lambda:calculadora("/"),width = 5,font=("Arial",20))
botaodivisao.grid(column = 1,row = 7)
botaopotenciacao = Button(janela,text = "^",command = lambda:calculadora("^"),width = 5,font=("Arial",20))
botaopotenciacao.grid(column = 0,row = 8)
botaoporaiz = Button(janela,text = "Raiz",command = lambda:calculadora("Raiz de "),width = 5,font=("Arial",20))
botaoporaiz.grid(column = 1,row = 8)
botaopoigual = Button(janela,text = "=",command = lambda:calculadora("="),width = 5,font=("Arial",20))
botaopoigual.grid(column = 3,row = 8)
botaopodeleteall = Button(janela,text = "C",command = lambda:calculadora("end all"),width = 5,font=("Arial",20))
botaopodeleteall.grid(column = 3,row = 7)





janela.mainloop()

