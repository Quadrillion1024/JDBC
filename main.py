#!/usr/bin/env python
# coding: utf-8

# In[1]:


import easygui as e


# In[5]:


def gui():
    order = e.ccbox(msg='请选择', title='小学四则运算', choices=['生成题目', '批改题目'])
    if order:
        msg = '请输入'
        title = '小学四则运算'
        fields = ['生成题目的个数']
        ret = e.multenterbox(msg, title, fields)
        #剩下的
        
        
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
        #剩下的
        
        
        
        order2 = e.ccbox(msg='请选择', title='小学四则运算', choices=['继续', '退出'])
        if order2:
            gui()
        elif not order2:
            e.msgbox(msg='退出', title='退出', ok_button='好耶！')
            


# In[6]:


def main():
    gui()


# In[7]:


main()   


# In[ ]:


def 


# In[ ]:




