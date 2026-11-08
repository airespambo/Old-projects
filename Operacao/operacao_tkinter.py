from tkinter import *

def operar():
    simbolos = {'+', '-', '*', '/', '='}
    numeros = {'1','2','3','4','5','6','7','8','9','0'}
    resultado = 0.0
    n = str()
    s = str()
    primeiro_num = True
    operacao = entrada.get()
    operacao = operacao + '='
    for i in operacao:
        if i in numeros:
            n = n + i
        elif i in simbolos:
            nc = float(n)
            match s:
                case '+':
                    resultado = resultado + nc
                case '-':
                    resultado = resultado - nc
                case '*':
                    resultado = resultado * nc
                case '/':
                    resultado = resultado / nc
            n = ''
            if primeiro_num:
                resultado = nc
                primeiro_num = False
            match i:
                case '=':
                    operacao = operacao + str(resultado)
                    texto['text'] = operacao
                case _:
                    s = i
        else:
            print('Operação inválida')
            break

janela = Tk()
janela.geometry('400x500')
janela.title('Calculadora Simples')

Label(janela, text = 'Digite a operação aqui').pack(padx = 20, pady = 10)
entrada = Entry(janela)
entrada.pack(padx = 20,pady = 20)
btn = Button(janela, text = 'calcular', command = operar)
btn.pack(padx = 20, pady = 20)
texto = Label(janela, text = '')
texto.pack(padx = 20, pady = 20)


janela.mainloop()