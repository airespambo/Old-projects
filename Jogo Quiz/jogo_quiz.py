from tkinter import *

class Actions():

    points = 0
    answer = str()
    n = 0
    levels = [
        'Nível 1',
        'Nível 2',
        'Nível 3',
        'Nível 4',
        'Nível 5'
    ]
    questions = [
        'Qual é o formato da Terra?',
        'O que significa CPU?',
        'O que é a ZRAM?',
        'Quem é o fabricante do sistema Android?',
        'O que é a resolução de tela?'
    ]
    answers = [
        'Circular',
        'Unidade Central de Processamento',
        'Memória Comprimida de Acesso Aleatório',
        'Google',
        'Medida da qualidade da tela'
    ]
    r1 = [
        'Quadrangular',
        'Unidade Central de Processamento',
        'Ram de vídeo',
        'Apple',
        'Tamanho da tela'
    ]
    r2 = [
        'Triangular',
        'Unidade Cognitiva de Pós-processamento',
        'Memória Comprimida de Acesso Aleatório',
        'Microsoft',
        'Borrão na tela'
    ]
    r3 = [
        'Circular',
        'Unidade de Procesamento Rápido',
        'Slot de memória',
        'Huawei',
        'Brilho da tela'
    ]
    r4 = [
        'Paralelograma',
        'Unidade de Processamento Gráfico',
        'Cache',
        'Google',
        'Luz noturna'
    ]
    r5 = [
        'Prismática',
        'Unidade de Disco',
        'Dispositivo USB',
        'Samsung',
        'Medida da qualidade da tela'
    ]
    r6 = [
        'Rectangular',
        'Unidade de SD',
        'GUI',
        'Poco',
        'Transparência'
    ]

    def iniciar(self):

        main.pack_forget()
        nvl.pack(fill = 'both', expand = True)
        btn_frm.place(relx = 0.5, rely = 0.6, anchor = 'center', width = 700, height = 300)
        Actions.avancar_de_nivel(self)
    
    def avancar_de_nivel(self):

        if Actions.n <= 4:
            level_text.set(Actions.levels[Actions.n])
            question_text.set(Actions.questions[Actions.n])
            Actions.answer = Actions.answers[Actions.n]

            op1_text.set(Actions.r1[Actions.n])
            op2_text.set(Actions.r2[Actions.n])
            op3_text.set(Actions.r3[Actions.n])
            op4_text.set(Actions.r4[Actions.n])
            op5_text.set(Actions.r5[Actions.n])
            op6_text.set(Actions.r6[Actions.n])
            
            Actions.n = Actions.n + 1
        else:

            nvl.pack_forget()
            end.pack(fill = 'both', expand = True)

            if Actions.points == 5:
                end_text.set('Você venceu!')
            else:
                end_text.set('Você perdeu!')
            end_points_text.set(Actions.points) 



    def opt1(self):
        
        if op1_text.get() == Actions.answer:

            Actions.points = Actions.points + 1

        Actions.avancar_de_nivel(self)
    
    def opt2(self):
        
        if op2_text.get() == Actions.answer:

            Actions.points = Actions.points + 1

        Actions.avancar_de_nivel(self)

    def opt3(self):
        
        if op3_text.get() == Actions.answer:

            Actions.points = Actions.points + 1

        Actions.avancar_de_nivel(self)

    def opt4(self):
        
        if op4_text.get() == Actions.answer:

            Actions.points = Actions.points + 1

        Actions.avancar_de_nivel(self)

    def opt5(self):
        
        if op5_text.get() == Actions.answer:

            Actions.points = Actions.points + 1

        Actions.avancar_de_nivel(self)
    
    def opt6(self):
        
        if op6_text.get() == Actions.answer:

            Actions.points = Actions.points + 1

        Actions.avancar_de_nivel(self)
    


main_window = Tk()
main_window.title('Jogo quiz')
main_window.geometry('700x600')
main_window.resizable(False, False)

main = Frame(main_window)
main.config(bg = "white")
main.pack(fill = 'both', expand = True)

title = Label(main, text = 'Jogo Quiz', font = ('Arial', 40), fg = 'white', bg = '#111B21')
title.place(relx = 0.5, rely = 0.4, anchor = 'center')

question_text = StringVar()
level_text = StringVar()
op1_text = StringVar()
op2_text = StringVar()
op3_text = StringVar()
op4_text = StringVar()
op5_text = StringVar()
op6_text = StringVar()

start = Button(main, text = 'Iniciar', fg = 'white', bg = "#18B300", font = ('Arial', 12), command = Actions().iniciar)
start.place(relx = 0.5, rely = 0.55, anchor = 'center', width = 130, height = 50)

nvl = Frame(main_window)
nvl.config(bg = '#111B21')

question = Label(nvl, bg = "#08371B",fg = 'white',font = ('Arial', 14), textvariable = question_text)
question.place(relx = 0.5, rely = 0.2, anchor = 'center', width = 650, height = 100)

level = Label(nvl, bg = '#111B21', font = ('Arial', 30), fg = 'white', textvariable = level_text)
level.pack(pady = 10)

btn_frm = Frame(nvl)
btn_frm.config(bg = '#111B21')

op1 = Button(btn_frm, fg = 'white', bg = "#18B300", font = ('Arial', 12), justify = 'center', wraplength = 120, textvariable = op1_text, command = Actions().opt1)
op1.place(relx = 0.20, rely = 0.20, anchor = 'center', width = 200, height = 100)

op2 = Button(btn_frm, fg = 'white', bg = "#18B300", font = ('Arial', 12), justify = 'center', wraplength = 120, textvariable = op2_text, command = Actions().opt2)
op2.place(relx = 0.5, rely = 0.20, anchor = 'center', width = 200, height = 100)

op3 = Button(btn_frm, fg = 'white', bg = "#18B300", font = ('Arial', 12), justify = 'center', wraplength = 120, textvariable = op3_text, command = Actions().opt3)
op3.place(relx = 0.8, rely = 0.20, anchor = 'center', width = 200, height = 100)

op4 = Button(btn_frm, fg = 'white', bg = "#18B300", font = ('Arial', 12), justify = 'center', wraplength = 120, textvariable = op4_text, command = Actions().opt4)
op4.place(relx = 0.20, rely = 0.7, anchor = 'center', width = 200, height = 100)

op5 = Button(btn_frm, fg = 'white', bg = "#18B300", font = ('Arial', 12), justify = 'center', wraplength = 120, textvariable = op5_text, command = Actions().opt5)
op5.place(relx = 0.5, rely = 0.7, anchor = 'center', width = 200, height = 100)

op6 = Button(btn_frm, fg = 'white', bg = "#18B300", font = ('Arial', 12), justify = 'center', wraplength = 120, textvariable = op6_text, command = Actions().opt6)
op6.place(relx = 0.8, rely = 0.7, anchor = 'center', width = 200, height = 100)

end = Frame(main_window)
end.config(bg = '#111B21')
end_text = StringVar()
end_points_text = IntVar()
end_title = Label(end, textvariable = end_text, bg = '#111B21', fg = 'white', font = ('Arial', 40))
end_title.place(relx = 0.5, rely = 0.4, anchor = 'center')
text = Label(end, text = 'Pontuação final:', bg = '#111B21', fg = 'white', font = ('Arial', 14))
text.place(relx = 0.5, rely = 0.55, anchor = 'center')
end_points = Label(end, textvariable = end_points_text, bg = '#111B21', fg = 'white', font = ('Arial', 12))
end_points.place(relx = 0.5, rely = 0.7, anchor = 'center')

main_window.mainloop()