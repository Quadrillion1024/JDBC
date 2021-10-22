#!/usr/bin/env python
# coding: utf-8

import easygui as e
import math
import random
from fractions import Fraction

#大家都喜欢的图形界面
def gui():
    order = e.ccbox(msg='请选择', title='小学四则运算', choices=['生成题目', '批改题目'])
    if order:
        msg = '请输入'
        title = '小学四则运算'
        fields = ['生成题目的个数','生成参数的范围']
        ret = e.multenterbox(msg, title,fields,values=[1,1])
        n = ret[0]
        r = ret[1]
        e.msgbox(msg='退出', title='退出', ok_button='好耶！')
        new_test(n,r)
        
        order2 = e.ccbox(msg='请选择', title='小学四则运算', choices=['继续', '退出'])
        if order2:
            gui()
        elif not order2:
            e.msgbox(msg='退出', title='退出', ok_button='好耶！')
    elif not order: 
        msg = '请输入'
        title = '小学四则运算'
        fields = ['题目文件路径','答案文件路径']
        ret = e.multenterbox(msg, title, fields,values=[0,0])
        path1 = ret[0]
        path2 = ret[1]
        e.msgbox(msg='还没写到这部分', title='退出', ok_button='好耶！')
        
        order2 = e.ccbox(msg='请选择', title='小学四则运算', choices=['继续', '退出'])
        if order2:
            gui()
        elif not order2:
            e.msgbox(msg='退出', title='退出', ok_button='好耶！')
#生成            
def new_test(n,r):
    Sanswer=''
    Sexercise=''
    d={} 
    for i in range(1,n+1):
        s=new_exercise(random.randint(1,r))
        answ=do_math(s)
        while(answ in d.keys() or int(answ)<=0) :
            s=new_exercise(random.randint(1,r))
            answ=do_math(s)
        else :    
            a=int(answ)  
            answ=answ-a
            if(a==0 or answ==0):    
                d[answ]=0
                Sexercise=Sexercise+str(i)+'.'+s+"\n"
                Sanswer=Sanswer+str(i)+'.'+str(answ)+"\n"
            else :     
                answ=str(a)+"'"+str(answ)
                d[answ]=0
                Sexercise=Sexercise+str(i)+'.'+s+"\n"
                Sanswer=Sanswer+str(i)+'.'+str(answ)+"\n"


    Exer=open('Exercise'+'.txt',"w",encoding='utf-8')    
    Answ=open('Answers'+'.txt',"w",encoding='utf-8')   
    Exer.write(Sexercise)
    Answ.write(Sanswer)    

#生成题目
def new_exercise(n):
def new_num(k):
def new_cal(k,n):
def do_math(s):
