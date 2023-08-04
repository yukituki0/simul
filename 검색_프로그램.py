import os
from difflib import SequenceMatcher
import tkinter as tk
import tkinter.font as tkFont

r = os.path.join(os.getcwd(),'시뮬레이션')
similarity = {}
search = ''
maximum = ''

def discovery():
    global similarity , r , search
    sense = os.listdir(r)
    for i in sense:
        r = os.path.join(r,i)
        if os.listdir(r) == []:
            r = os.path.join(r,os.path.dirname(r))
            similarity[f'{i}'] = SequenceMatcher(None, i, search).ratio()
        else:
            if [x for i in os.listdir(r) for x in similarity.keys() if i in x] == os.listdir(r):
                r = os.path.join(r,os.path.dirname(r))
            else:
                similarity[f'{i}'] = SequenceMatcher(None, i, search).ratio()
                discovery()
    r = os.path.join(r,os.path.dirname(r))

def Enter(event):
    global similarity , r , search, maximum
    r = os.path.join(os.getcwd(),'시뮬레이션')
    similarity = {}
    search = input_value.get()
    discovery()
    del similarity['과학']
    del similarity['수학']
    maximum = max(similarity,key=similarity.get)
    result.configure(text="검색한 값과 가장 유사한 결과 : "+str(maximum))
    loding.configure(text=f'{maximum}시뮬레이션을 실행할까요?')
    select.pack(side='top',pady=100)

def Enter1():
    global  maximum
    os.system(f'{maximum}.py')

program = tk.Tk()
program.title("simulation search program")
program.geometry("1920x1080")
program.resizable()

input_value = tk.StringVar()

title = tk.Label(program,text='Simulation Search Program',font=tkFont.Font(family="맑은 고딕", size=45))
result = tk.Label(program,text='검색한 값과 가장 유사한 결과 : ')
search_value = tk.Entry(program,width=105,font=tkFont.Font(family="맑은 고딕", size=10),textvariable=input_value)
search_value.bind("<Return>",Enter)
expl = tk.Label(program,text='Enter를 눌러 입력하세요',anchor='e',width=105)
wartermark = tk.Label(program,text='making by E.S.C.',font=tkFont.Font(family="", size=15))
loding = tk.Label(program,text='',font=tkFont.Font(family="", size=25))
select = tk.Button(program,text='실행',command=Enter1)
list = tk.Listbox(program,width=21)
list.insert(0,'몬테카를로 실험')
list.insert(0,'입자의 운동 실험')
list.insert(0,'[추가되어있는 시뮬레이션]')

list.pack(side='left',fill='y')
title.pack(side='top',fill='y',pady=80)
search_value.pack(side='top',ipady=5)
expl.pack(side='top')
result.pack(side='top',ipady=30)
loding.pack(side='top')
wartermark.pack(side='right',anchor='s')

program.mainloop()
