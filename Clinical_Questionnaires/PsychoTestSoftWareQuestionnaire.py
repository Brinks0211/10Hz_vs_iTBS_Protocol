'''
青少年问卷评估测试
author: Zhang Yihao
Time: 2024/1218
'''

# import the third pypi
import tkinter as tk
import subprocess
import datetime
import sys
import numpy as np
import pandas as pd
import threading
import pygame
import os
import time
import json
import cv2
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk
from pypinyin import pinyin
from QuestionnaireAnalysis import Analysis
from moviepy.editor import VideoFileClip


def save_to_json(json_filename, input_dict):
    """
    将字典保存为 JSON 文件
    Parameters:
        json_filename (str): 要保存的 JSON 文件名
        input_dict (dict): 要保存的字典
    """
    with open(json_filename, 'w') as json_file:
        json.dump(input_dict, json_file, indent=4, ensure_ascii=False)
    print(f"字典已保存为 JSON 文件: {json_filename}")

def log_activity(activity_log):
    global start_time
    current_time = datetime.datetime.now()
    elapsed_time = current_time - start_time
    elapsed_time_str = f"{elapsed_time.total_seconds():.2f} seconds"
    activity = f"{current_time.strftime('%Y-%m-%d %H:%M:%S')} ({elapsed_time_str}): {activity_log}\n"
    save_activity(activity)

def save_activity(activity):
    global dirname
    with open(scri_path+"/result/{}/{}".format(dirname, dirname+'_log.txt'), "a") as file:
        file.write(activity)

# exit confirm
def on_closing():
    global dirname, audio_recorder,scri_path,video_recorder
    if messagebox.askokcancel("Quit", "您确定想要退出吗？"):
        try:
            log_activity(activity_log='exit the application via fucntion "on_closing" and stop recording')
            # audio_recorder.stop_recording(scri_path+"/result/{}/{}.wav".format(dirname,dirname))
            # video_recorder.stop_recording(scri_path+"/result/{}/{}.avi".format(dirname,dirname))
            save_to_json('./json/'+'/'+str(dirname)+'.json', JsonDict)
            save_to_json('./result/{}/{}.json'.format(str(dirname), str(dirname)), JsonDict)
            sys.exit()
        except NameError :
            # audio_recorder.stop_recording('temp.wav')
            # video_recorder.stop_recording('temp.avi')
            sys.exit()

def Refresh():
    PSQIBtn.config(state='normal')
    PSQIBtn.config(text='1.睡眠评估')
    SpeakingBtn.config(state='normal')
    PLETestBtn.config(state='normal')
    InitialFrame.update()

# save parameters
def Para():
    global dirname, scri_path, name, name_pinyin, gender, birthtime, time, age, ParaList,JsonDict
    today = datetime.datetime.now()
    year = today.year
    month = today.month
    day = today.day
    hour = today.hour
    min = today.minute
    birthyear = int(output_data.loc['year', 'answer'])
    birthmonth = int(output_data.loc['month', 'answer'])
    birthday = int(output_data.loc['day', 'answer'])
    age = int(year) - int(birthyear)
    if birthmonth>month:
        age = age - 1
    output_data.loc['age', 'answer'] = age
    time = "_".join([str(year)+str('{:0>2d}'.format(month))+str('{:0>2d}'.format(day))+\
                     str('{:0>2d}'.format(hour))+str('{:0>2d}'.format(min))])
    birthtime = str(birthyear)+str('{:0>2d}'.format(birthmonth))+str('{:0>2d}'.format(birthday))
    scri_path = os.getcwd()
    dirname = '_'.join([name_pinyin, birthtime, gender_num, time])
    ParaList = [dirname, name, name_pinyin, gender_num, age, time, birthtime]
    # output_data.to_csv(scri_path+'/info.csv', encoding="GBK")
    try: os.mkdir('result')
    except: pass
    try: os.mkdir('json')
    except: pass
    try: 
        os.mkdir(scri_path+'/result/'+dirname)
        log_activity(activity_log=' {} (0.00 secondes): start the application'.format(start_time))
        log_activity(activity_log=RecordTimeStr+'start record video')
    except: pass
    JsonDict = {'Name': name_pinyin,'Birth':birthtime, 'Age':age, 'Gender': gender, 'TimeQues': time, 'HosID':HosID, 
                'PSQI':0, 'PLE':0, 'Read':0, 'Talk':0}

def Start():
    global  scri_path, name, name_pinyin, gender, birthtime,time,age, ParaList, gender_num, HosID
    name = NameEntry.get()
    output_data.loc['name', 'answer'] = name
    name_pinyin_list = pinyin(name,style=0)
    name_pinyin = ''
    for i in name_pinyin_list:
            name_pinyin += ''.join(i)
    output_data.loc['name_pinyin', 'answer'] = name_pinyin
    year = YearEntry.get()
    output_data.loc['year', 'answer'] = year
    month = MonthEntry.get()
    output_data.loc['month', 'answer'] = month
    day = DayEntry.get()
    output_data.loc['day', 'answer'] = day
    gender = GenderEntry.get()
    if gender == '男':
        output_data.loc['gender','answer'] = 1
        gender_num = '1'
    elif gender == '女':
        output_data.loc['gender', 'answer'] = 2
        gender_num = '2'
    ethnic = EthnicEntry.get()
    output_data.loc['ethnic', 'answer'] = ethnic
    height = HeightEntry.get()
    output_data.loc['height', 'answer'] = height
    weight = WeightEntry.get()
    output_data.loc['weight', 'answer'] = weight
    hand = HandEntry.get()
    output_data.loc['hand', 'answer'] = hand
    home = HomeEntry.get()
    output_data.loc['home', 'answer'] = home
    parent = ParentEntry.get()
    output_data.loc['parent', 'answer'] = parent
    sibling = SiblingEntry.get()
    output_data.loc['sibling', 'answer'] = sibling
    education = EducationEntry.get()
    output_data.loc['education', 'answer'] = education
    institution = LocationEntry.get()
    output_data.loc['institution', 'answer'] = institution
    HosID = HosIDEntry.get()
    output_data.loc['HosID', 'answer'] = HosID
    SuperViseList = ['name', 'name_pinyin', 'year', 'month', 'day', 'age','gender','ethnic', 
                            'height', 'weight', 'hand', 'home', 'parent', 'sibling', 
                            'education', 'institution', 'HosID']
    SuperViseSwitch = 0
    for i in SuperViseList:
        if output_data.loc[i, 'answer'] == '':
                SuperViseSwitch = 1
    if SuperViseSwitch == 1:
        # InfoFrame1.destroy()
        messagebox.showinfo('  提示','请补全信息！')
    else:
        Para()
        InfoFrame1.destroy()
        MainWin2()

def StartFrame2():
    output_data.loc['InfoQuestion-13', 'question'] = '13.近半年内,临床医生是否给予诊断如下心理问题:'
    output_data.loc['InfoQuestion-13', 'answer'] = InfoQues13Entry.get()
    output_data.loc['InfoQuestion-14', 'question'] = '14.如有13项里的诊断，为首发还是复发:'
    output_data.loc['InfoQuestion-14', 'answer'] = InfoQues14Entry.get()
    output_data.loc['InfoQuestion-15_1', 'question'] = '15.如有13项里的诊断，首发的年龄(岁):'
    output_data.loc['InfoQuestion-15_1', 'answer'] = InfoQues15_1Entry.get()
    output_data.loc['InfoQuestion-15_2', 'question'] = '15.如有13项里的诊断，首发的年龄(个月):'
    output_data.loc['InfoQuestion-15_2', 'answer'] = InfoQues15_2Entry.get()
    output_data.loc['InfoQuestion-16', 'question'] = '16. 如有13项里的诊断，复发的次数:'
    output_data.loc['InfoQuestion-16', 'answer'] = InfoQues16Entry.get()
    output_data.loc['InfoQuestion-17_1', 'question'] = '17.除13项里的诊断外，共病类型还有(第一种类型):'
    output_data.loc['InfoQuestion-17_1', 'answer'] = InfoQues17_1Entry.get()
    output_data.loc['InfoQuestion-17_2', 'question'] = '17.除13项里的诊断外，共病类型还有(第二种类型):'
    output_data.loc['InfoQuestion-17_2', 'answer'] = InfoQues17_2Entry.get()
    output_data.loc['InfoQuestion-18_1', 'question'] = '18.如有13项里的诊断，用药时长:'
    output_data.loc['InfoQuestion-18_1', 'answer'] = InfoQues18_1Entry.get()
    output_data.loc['InfoQuestion-18_2', 'question'] = '18.如有13项里的诊断，用药类型1:'
    output_data.loc['InfoQuestion-18_2', 'answer'] = InfoQues18_2Entry.get()
    output_data.loc['InfoQuestion-18_3', 'question'] = '18.如有13项里的诊断，用药类型2:'
    output_data.loc['InfoQuestion-18_3', 'answer'] = InfoQues18_3Entry.get()
    output_data.loc['InfoQuestion-18_4', 'question'] = '18.如有13项里的诊断，用药类型3:'
    output_data.loc['InfoQuestion-18_4', 'answer'] = InfoQues18_4Entry.get()
    output_data.loc['InfoQuestion-18_5', 'question'] = '18.如有13项里的诊断，用药类型4:'
    output_data.loc['InfoQuestion-18_5', 'answer'] = InfoQues18_5Entry.get()
    output_data.loc['InfoQuestion-19', 'question'] = '19.半年前病史，临床医生是否给予诊断'
    output_data.loc['InfoQuestion-19', 'answer'] = InfoQues19Entry.get()
    output_data.loc['InfoQuestion-20_1', 'question'] = '20.家族史,两系三代内血亲谁'
    output_data.loc['InfoQuestion-20_1', 'answer'] = InfoQues20_1Entry.get()
    output_data.loc['InfoQuestion-20_2', 'question'] = '20.家族史,两系三代内血亲是否有以下临床诊断'
    output_data.loc['InfoQuestion-20_2', 'answer'] = InfoQues20_2Entry.get()
    output_data.loc['InfoQuestion-21_1', 'question'] = '21.家族史,两系三代内血亲是否有以下临床诊断'
    output_data.loc['InfoQuestion-21_1', 'answer'] = InfoQues21_1Entry.get()
    output_data.loc['InfoQuestion-21_2', 'question'] = '21.家族史,两系三代内血亲是否有以下临床诊断'
    output_data.loc['InfoQuestion-21_2', 'answer'] = InfoQues21_2Entry.get()
    output_data.loc['InfoQuestion-21_3', 'question'] = '21.家族史,两系三代内血亲是否有以下临床诊断'
    output_data.loc['InfoQuestion-21_3', 'answer'] = InfoQues21_3Entry.get()
    log_activity(activity_log='get the noncompulsory info and the info frame (noncompulsory) destroy')
    # print(output_data)
    InfoFrame2.destroy()
    MainWin3()

# # set the function of InformConcentBtn
# waittime = 1
waittime = 10
def timer_handler_inform():
    global InformConcentBtn, waittime, InformFrame
    if waittime >0:
        InformFrame.after(1000, timer_handler_inform)
        waittime-=1
        InformConcentBtn['text'] = '知情同意书（'+str(waittime)+'秒）'
    else:
        InformConcentBtn['text'] = '知情同意书'
        InformConcentBtn.config(state="normal")
        # waittime = 1
        waittime = 10

# exit confirm
def ExitInformWin():
    global  InformFrame, waittime
    log_activity(activity_log='exit the paradigm because of refusing the inform consent')
    InformWin.destroy()
    # InformBtn.config('disable')
    # waittime = 1
    waittime = 10

# set time_handler about accept and refuse
def timer_handler_concent():
        global waittime, ConcentBtn, RefuseBtn
        if waittime > 0:
                InformWin.protocol('WM_DELETE_WINDOW', False)
                InformFrame.after(1000, timer_handler_concent)
                waittime-=1
                ConcentBtn['text'] = '接受 （'+str(waittime)+'秒）'
                RefuseBtn['text'] = '退出 （'+str(waittime)+'秒）'
        else:
                InformWin.protocol('WM_DELETE_WINDOW', True)
                ConcentBtn['text'] = '接受'
                ConcentBtn.config(state='normal')
                RefuseBtn['text'] = ' 退出'
                RefuseBtn.config(state='normal')
                InformWin.state = 'normal'

# set the function of accept and refuse
def Accept():
    global TestSwitch, waittime
    if messagebox.showinfo('提示', '您已同意参加评估，请点击‘1.睡眠评估’。') :
        TestSwitch = 1
        InformWin.destroy()
        PSQIBtn.config(state='normal') 
        InformBtn.config(state='disabled')
        InformBtn.config(text='已签订知情同意书')
        PSQIBtn.config(state='normal')
        # waittime = 1
        waittime = 10           

def Refuse():
    if messagebox.askokcancel('quit', '您确定要退出吗'):
        log_activity(activity_log='exit the paradigm because of refusing the inform consent')
        sys.exit()
    else:
        try: InformWin.deiconify()
        except: pass
        #   except : TestWin.deiconify()

# set the function of Concentbutton show the informed concent 
def ConcentShow():
    global InformSwitch, InformWin, ConcentBtn, InformFrame, RefuseBtn, ConcentFrame
    InformFrame.destroy()
    ConcentFrame = tk.Frame(InformWin, width=1280 ,height=720, bg='white')
    ConcentFrame.pack()
    ConcentFrame_title = tk.Label(ConcentFrame, text='知情同意书', font='黑体 25 bold', bg='white')
    ConcentFrame_title.place(x=550, y=50)
    f = open("./material/Concent.txt", "r", encoding='utf-8')
    concent_data = f.read()
    f.close()
    ConcentTextScroll = tk.Scrollbar(InformWin, )
    ConcentText = tk.Text(ConcentFrame, font='宋体 13 bold',  width=105, bg='white', 
                        height=25, yscrollcommand=ConcentTextScroll.set)
    ConcentText.place(x=100, y=130)
    ConcentText.insert(index='end', chars=concent_data)
    ConcentText.config(state='disabled')
    ConcentTextScroll.config(command=ConcentText.yview)
    ConcentTextScroll.place(x=1152, y=129  , relheight=0.6)
    ConcentBtn = tk.Button(ConcentFrame, text='接受（10s）', state='disabled', width=15, 
                        font='宋体 15 bold', command=Accept, bg='WhiteSmoke', relief='ridge',)
    ConcentBtn.place(x=400, y=600)
    RefuseBtn = tk.Button(ConcentFrame, text='退出（10s）', state='disabled', width=15, 
                        font='宋体 15 bold', command=Refuse, bg='WhiteSmoke', relief='ridge',)
    RefuseBtn.place(x=800, y=600)
    InformWin.after(1000, timer_handler_concent)
    tip = tk.Label(ConcentFrame, text='版权所有和解释权  @山东师范大学心理学院', font='宋体 10 ', bg='white')
    tip.place(x=500, y=690)
    log_activity(activity_log='show the Inform Consent')

def InformShow():
# prevent repeated windows
    global  InformWin, InformConcentBtn, InformFrame
# set a toplevel window 'InformWin'
    # set geometry and location
    log_activity(activity_log='click the inform button')
    InformWin = tk.Toplevel(MainWin)
    InformWin.iconbitmap(ico_path)
    InformWin.wm_iconbitmap(ico_path)
    InformWin.title('评估须知')
    InformWin.geometry('1280x720')
    InformWin.resizable(False, False)
    InformFrame = tk.Frame(InformWin, width=1280 ,height=720, bg='white')
    InformFrame.pack()
    InformFrame_title = tk.Label(InformFrame, text='评估须知', font='黑体 25 bold', bg='white')
    InformFrame_title.place(x=600, y=50)
    NotificationList = ['1、在评估开始前，您需要【认真阅读和接受知情同意书】。',
                        '2、本评估共计3个部分，约14分钟时间（睡眠评估：3分钟；精神状态评估：3分钟；情绪评估：约8分钟）。',
                        '3、本评估3个部分，请按顺序完成每个部分。',
                        '4、在评估过程中，请您正对电脑屏幕，端正坐姿，认真作答。']
    for i in range(len(NotificationList)):
            NotificationLabel = tk.Label(InformFrame, text=NotificationList[i], font='楷体 15 bold', bg='white', width=80, wraplength=800)
            NotificationLabel.place(x=150 , y= i*80 + 120)
    InformConcentBtn = tk.Button(InformFrame,width=20, text='知情同意书（10秒）',font='宋体 13 bold', state='disabled', command=ConcentShow,
                                bg='WhiteSmoke', relief='ridge')
    InformConcentBtn.place(x=550, y=630)
    InformFrame.after(1000, timer_handler_inform)
    tip = tk.Label(InformFrame, text='版权所有和解释权  @山东师范大学心理学院', font='宋体 10 ', bg='white')
    tip.place(x=500, y=690)
    InformWin.protocol('WM_DELETE_WINDOW', ExitInformWin)
    InformWin.mainloop()

# 2 PSQI part 
# 2.4 PSQI button click
def PsqiButton1Click():
    global QuestionIndex, dirname,JsonDict
    if QuestionIndex < 19: 
        log_activity(activity_log='PSQIButton1 was clicked facing the Question-{}'.format(QuestionIndex+5))
        output_data.loc[Questions.loc[QuestionIndex, 'index'], 'answer'] = 0    
        output_data.loc[Questions.loc[QuestionIndex, 'index'], 'question'] = Questions.loc[QuestionIndex, 'question']
        output_data.loc[Questions.loc[QuestionIndex, 'index'], 'sequence'] = QuestionIndex+1    
        QuestionIndex += 1
        QuestionLabel.config(text=str(QuestionIndex+5)+'.'+Questions.loc[QuestionIndex, 'question'])
        PsqiButton1.config(text=Questions.loc[QuestionIndex, 'answer1'])
        PsqiButton2.config(text=Questions.loc[QuestionIndex, 'answer2'])
        PsqiButton3.config(text=Questions.loc[QuestionIndex, 'answer3'])
        PsqiButton4.config(text=Questions.loc[QuestionIndex, 'answer4'])
        TestProgressor.config(value=QuestionIndex+1)
        PsqiFrame_2.update()
        log_activity(activity_log='PSQIButton1 was clicked facing the Question-{}'.format(QuestionIndex+6))
    else:
        log_activity(activity_log='PSQIButton1 was clicked facing the Question-{}'.format(QuestionIndex+5))
        output_data.loc[Questions.loc[QuestionIndex, 'index'], 'answer'] = 0            
        output_data.loc[Questions.loc[QuestionIndex, 'index'], 'question'] = Questions.loc[QuestionIndex, 'question']
        output_data.loc[Questions.loc[QuestionIndex, 'index'], 'sequence'] = QuestionIndex+1    
        PsqiWin.destroy()
        JsonDict['PSQI'] = 1
        messagebox.showinfo('评估结束','睡眠评估结束，请点击“2.精神状况评估”继续测评！')
        PSQIBtn.config(text='已完成睡眠评估')
        PSQIBtn.config(state='disabled')
        PLETestBtn.config(state='normal')
        log_activity(activity_log='output the PSQI data to participant\'s dir')
        output_data.to_csv('./result/'+str(dirname)+'/'+str(dirname)+'_PSQI.csv', encoding='GBK')

def PsqiButton2Click():
    global QuestionIndex, dirname
    if QuestionIndex < 19: 
        log_activity(activity_log='PSQIButton2 was clicked facing the Question-{}'.format(QuestionIndex+5))
        output_data.loc[Questions.loc[QuestionIndex, 'index'], 'answer'] = 1    
        output_data.loc[Questions.loc[QuestionIndex, 'index'], 'question'] = Questions.loc[QuestionIndex, 'question']
        output_data.loc[Questions.loc[QuestionIndex, 'index'], 'sequence'] = QuestionIndex+1    
        QuestionIndex += 1
        QuestionLabel.config(text=str(QuestionIndex+5)+'.'+Questions.loc[QuestionIndex, 'question'])
        PsqiButton1.config(text=Questions.loc[QuestionIndex, 'answer1'])
        PsqiButton2.config(text=Questions.loc[QuestionIndex, 'answer2'])
        PsqiButton3.config(text=Questions.loc[QuestionIndex, 'answer3'])
        PsqiButton4.config(text=Questions.loc[QuestionIndex, 'answer4'])
        TestProgressor.config(value=QuestionIndex+1)
        PsqiFrame_2.update()
        log_activity(activity_log='PSQIButton1 was clicked facing the Question-{}'.format(QuestionIndex+6))
    else:
        log_activity(activity_log='PSQIButton2 was clicked facing the Question-{}'.format(QuestionIndex+5))
        output_data.loc[Questions.loc[QuestionIndex, 'index'], 'answer'] = 1            
        output_data.loc[Questions.loc[QuestionIndex, 'index'], 'question'] = Questions.loc[QuestionIndex, 'question']
        output_data.loc[Questions.loc[QuestionIndex, 'index'], 'sequence'] = QuestionIndex+1    
        PsqiWin.destroy()
        JsonDict['PSQI'] = 1
        messagebox.showinfo('评估结束','睡眠评估结束，请点击“2.精神状况评估”继续测评！')
        PSQIBtn.config(text='已完成睡眠评估')
        PSQIBtn.config(state='disabled')
        PLETestBtn.config(state='normal')
        log_activity(activity_log='output the PSQI data to participant\'s dir')
        output_data.to_csv('./result/'+str(dirname)+'/'+str(dirname)+'_PSQI.csv', encoding='GBK')



def PsqiButton3Click():
    global QuestionIndex, dirname
    if QuestionIndex < 19: 
        log_activity(activity_log='PSQIButton3 was clicked facing the Question-{}'.format(QuestionIndex+5))
        output_data.loc[Questions.loc[QuestionIndex, 'index'], 'answer'] = 2    
        output_data.loc[Questions.loc[QuestionIndex, 'index'], 'question'] = Questions.loc[QuestionIndex, 'question']
        output_data.loc[Questions.loc[QuestionIndex, 'index'], 'sequence'] = QuestionIndex+1    
        QuestionIndex += 1
        QuestionLabel.config(text=str(QuestionIndex+5)+'.'+Questions.loc[QuestionIndex, 'question'])
        PsqiButton1.config(text=Questions.loc[QuestionIndex, 'answer1'])
        PsqiButton2.config(text=Questions.loc[QuestionIndex, 'answer2'])
        PsqiButton3.config(text=Questions.loc[QuestionIndex, 'answer3'])
        PsqiButton4.config(text=Questions.loc[QuestionIndex, 'answer4'])
        TestProgressor.config(value=QuestionIndex+1)
        PsqiFrame_2.update()
        log_activity(activity_log='PSQIButton1 was clicked facing the Question-{}'.format(QuestionIndex+6))
    else:
        log_activity(activity_log='PSQIButton3 was clicked facing the Question-{}'.format(QuestionIndex+5))
        output_data.loc[Questions.loc[QuestionIndex, 'index'], 'answer'] = 2            
        output_data.loc[Questions.loc[QuestionIndex, 'index'], 'question'] = Questions.loc[QuestionIndex, 'question']
        output_data.loc[Questions.loc[QuestionIndex, 'index'], 'sequence'] = QuestionIndex+1    
        PsqiWin.destroy()
        JsonDict['PSQI'] = 1
        messagebox.showinfo('评估结束','睡眠评估结束，请点击“2.精神状况评估”继续测评！')
        PSQIBtn.config(text='已完成睡眠评估')
        PSQIBtn.config(state='disabled')
        PLETestBtn.config(state='normal')
        log_activity(activity_log='output the PSQI data to participant\'s dir')
        output_data.to_csv('./result/'+str(dirname)+'/'+str(dirname)+'_PSQI.csv', encoding='GBK')


def PsqiButton4Click():
    global QuestionIndex, dirname
    if QuestionIndex < 19: 
        log_activity(activity_log='PSQIButton4 was clicked facing the Question-{}'.format(QuestionIndex+5))
        output_data.loc[Questions.loc[QuestionIndex, 'index'], 'answer'] = 3    
        output_data.loc[Questions.loc[QuestionIndex, 'index'], 'question'] = Questions.loc[QuestionIndex, 'question']
        output_data.loc[Questions.loc[QuestionIndex, 'index'], 'sequence'] = QuestionIndex+1    
        QuestionIndex += 1
        QuestionLabel.config(text=str(QuestionIndex+5)+'.'+Questions.loc[QuestionIndex, 'question'])
        PsqiButton1.config(text=Questions.loc[QuestionIndex, 'answer1'])
        PsqiButton2.config(text=Questions.loc[QuestionIndex, 'answer2'])
        PsqiButton3.config(text=Questions.loc[QuestionIndex, 'answer3'])
        PsqiButton4.config(text=Questions.loc[QuestionIndex, 'answer4'])
        TestProgressor.config(value=QuestionIndex+1)
        PsqiFrame_2.update()
        log_activity(activity_log='PSQIButton1 was clicked facing the Question-{}'.format(QuestionIndex+6))
    else:
        log_activity(activity_log='PSQIButton4 was clicked facing the Question-{}'.format(QuestionIndex+5))
        output_data.loc[Questions.loc[QuestionIndex, 'index'], 'answer'] = 3            
        output_data.loc[Questions.loc[QuestionIndex, 'index'], 'question'] = Questions.loc[QuestionIndex, 'question']
        output_data.loc[Questions.loc[QuestionIndex, 'index'], 'sequence'] = QuestionIndex+1    
        PsqiWin.destroy()
        JsonDict['PSQI'] = 1
        messagebox.showinfo('评估结束','睡眠评估结束，请点击“2.精神状况评估”继续测评！')
        PSQIBtn.config(text='已完成睡眠评估')
        PSQIBtn.config(state='disabled')
        PLETestBtn.config(state='normal')
        log_activity(activity_log='output the PSQI data to participant\'s dir')
        output_data.to_csv('./result/'+str(dirname)+'/'+str(dirname)+'_PSQI.csv', encoding='GBK')


# PSQI 2.3
def PsqiTest():
    global QuestionIndex, Questions, QuestionLabel, PsqiFrame_2, TestProgressor, PsqiButton1, PsqiButton2,\
    PsqiButton3, PsqiButton4
    log_activity(activity_log='show the PSQI test Question 5-25 window')
    PsqiFrame_2 = tk.Frame(PsqiWin, width=1280, height=720, bg='white')
    PsqiFrame_2.pack()
    Questions = pd.read_csv(scri_path+'/material/PSQI.csv', encoding='GBK')
    QuestionIndex = 0
    QuestionLabel = tk.Label(PsqiFrame_2, font='宋体 20 bold', width=80, wraplength=800, justify='left', text='5.'+Questions.loc[QuestionIndex, 'question'], bg='white')
    QuestionLabel.place(relx=0, rely=0.15)
    PsqiButton1 = tk.Button(PsqiFrame_2, font='宋体 20 bold', width=25, text=Questions.loc[QuestionIndex, 'answer1'], command=PsqiButton1Click, bg='WhiteSmoke', relief='ridge')
    PsqiButton1.place(relx=0.35, rely=0.3)
    PsqiButton2 = tk.Button(PsqiFrame_2, font='宋体 20 bold', width=25, text=Questions.loc[QuestionIndex, 'answer2'], command=PsqiButton2Click, bg='WhiteSmoke', relief='ridge')
    PsqiButton2.place(relx=0.35, rely=0.4)
    PsqiButton3 = tk.Button(PsqiFrame_2, font='宋体 20 bold', width=25, text=Questions.loc[QuestionIndex, 'answer3'], command=PsqiButton3Click, bg='WhiteSmoke', relief='ridge')
    PsqiButton3.place(relx=0.35, rely=0.5)
    PsqiButton4 = tk.Button(PsqiFrame_2, font='宋体 20 bold', width=25, text=Questions.loc[QuestionIndex, 'answer4'], command=PsqiButton4Click,bg='WhiteSmoke', relief='ridge')
    PsqiButton4.place(relx=0.35, rely=0.6)
    TestProgressor = ttk.Progressbar(PsqiFrame_2, orient='horizontal', mode='determinate',
                                        length=1000, maximum=20, value=QuestionIndex+1)
    TestProgressor.place(relx=0.1, rely=0.8)
    tip = tk.Label(PsqiFrame_2, text='版权所有和解释权  @山东师范大学心理学院', font='宋体 10 ',bg='white')
    tip.place(x=500, y=690)

# PSQI next frame
def PsqiNextFrame():
    log_activity(activity_log='get the answers of the PSQI test Question 1-4 window')
    PsqiQues1Hour = PsqiQues1HourEntry.get()
    PsqiQues1Min = PsqiQues1MinEntry.get()
    PsqiQues2 = PsqiQues2Entry.get()
    PsqiQues3Hour = PsqiQues3HourEntry.get()
    PsqiQues3Min = PsqiQues3MinEntry.get()
    PsqiQues4 = PsqiQues4Entry.get()
    output_data.loc['PSQI-1_Hour', 'answer'] = PsqiQues1Hour
    output_data.loc['PSQI-1_Min', 'answer'] = PsqiQues1Min
    if PsqiQues2 == '小于15分钟':
        output_data.loc['PSQI-2', 'answer'] = 0
    elif PsqiQues2 == '16-30分钟':
        output_data.loc['PSQI-2', 'answer'] = 1
    elif PsqiQues2 == '31-60分钟':
        output_data.loc['PSQI-2', 'answer'] = 2
    elif PsqiQues2 == '大于60分钟':
        output_data.loc['PSQI-2', 'answer'] = 3
    output_data.loc['PSQI-3_Hour', 'answer'] = PsqiQues3Hour
    output_data.loc['PSQI-3_Hour', 'answer'] = PsqiQues3Hour
    output_data.loc['PSQI-3_Min', 'answer'] = PsqiQues3Min
    output_data.loc['PSQI-3_Min', 'answer'] = PsqiQues3Min
    if PsqiQues4 == '大于7小时':
        output_data.loc['PSQI-4', 'answer'] = 0
    elif PsqiQues4 == '6-7小时':
        output_data.loc['PSQI-4', 'answer'] = 1
    elif PsqiQues4 == '5-6小时':
        output_data.loc['PSQI-4', 'answer'] = 2
    elif PsqiQues4 == '小于5小时':
        output_data.loc['PSQI-4', 'answer'] = 3
    SuperViseSwitch = 0
    for i in ['PSQI-1_Hour', 'PSQI-1_Min', 'PSQI-2', 'PSQI-3_Hour', 'PSQI-3_Min','PSQI-4']:
        if output_data.loc[i, 'answer'] == '':
            SuperViseSwitch = 1
    if SuperViseSwitch == 1:
        # PsqiFrame1.destroy()
        log_activity(activity_log='remind for completion information of PSQI 1-4 questions')
        messagebox.showinfo('提示','请补全信息！')
        PsqiWin.lift()
    else:
        log_activity(activity_log='The frame of PSQI 1-4 questions was destroyed')
        PsqiFrame1.destroy()
        PsqiTest()

# 2.1 PSQIframe1
def PSQI():
    global PsqiFrame1, PsqiQues1HourEntry, PsqiQues1MinEntry, PsqiQues2Entry, PsqiQues3HourEntry, PsqiQues3MinEntry, PsqiQues4Entry, PsqiWin
    log_activity(activity_log='Show the PSQI test Question 1-4 window')
    PsqiWin = tk.Toplevel(MainWin)
    PsqiWin.resizable(False,False)
    PsqiFrame1 = tk.Frame(PsqiWin, width=1280, height=720, bg='white')
    PsqiFrame1.pack()
    PsqiFrame1_title = tk.Label(PsqiFrame1, text='1.睡眠评估', font='黑体 25 bold', bg='white')
    PsqiFrame1_title.place(relx=0.45, rely=0.1)
    PsqiInstruc = tk.Label(PsqiFrame1, text='以下的问题仅与您过去一个月的睡眠习惯有关\n\n请您对过去一个月中多数白天和晚上的睡眠情况作精确的回答',
                            font='宋体 18 bold', justify='center', bg='white')
    PsqiInstruc.place(relx=0.25, rely=0.2)
    PsqiQues1Label = tk.Label(PsqiFrame1, text='1. 过去一个月，你通常上床睡觉的时间是？上床睡觉的时间是     :     （24小时制）', 
                            font='宋体 15 bold', bg='white')
    PsqiQues1Label.place(relx=0.15, y=250)
    PsqiQues1HourEntry = ttk.Combobox(PsqiFrame1, textvariable=tk.StringVar(), value=([str('{:0>2d}'.format(i)) for i in range(24,0,-1)]),
                                    width=4, justify='center', state='readonly')  
    PsqiQues1HourEntry.place(x=776, y=250)
    PsqiQues1MinEntry = ttk.Combobox(PsqiFrame1, textvariable=tk.StringVar(), value=([str('{:0>2d}'.format(i)) for i in range(0,61)]),
                                    width=4, justify='center', state='readonly')
    PsqiQues1MinEntry.place(x=840, y=250)
    PsqiQues2Label = tk.Label(PsqiFrame1, text='2. 过去一个月，你每晚通常要多长时间（分钟）才能入睡？            ', 
                            font='宋体 15 bold', bg='white')
    PsqiQues2Label.place(x=193, y=320)
    PsqiQues2Entry = ttk.Combobox(PsqiFrame1, textvariable=tk.StringVar(), value=(['小于15分钟', '16-30分钟', '31-60分钟', '大于60分钟']),
                                    width=10, justify='center', state='readonly')
    PsqiQues2Entry.place(x=760, y=320)
    PsqiQues3Label = tk.Label(PsqiFrame1, text='3. 过去一个月，你通常早上起床的时间是？早上起床的时间是     :     （24小时制）', 
                            font='宋体 15 bold', bg='white')
    PsqiQues3Label.place(x=193, y=390)
    PsqiQues3HourEntry = ttk.Combobox(PsqiFrame1, textvariable=tk.StringVar(), value=([str('{:0>2d}'.format(i)) for i in range(1,25,1)]),
                                    width=4, justify='center', state='readonly')  
    PsqiQues3HourEntry.place(x=776, y=390)
    PsqiQues3MinEntry = ttk.Combobox(PsqiFrame1, textvariable=tk.StringVar(), value=([str('{:0>2d}'.format(i)) for i in range(0,61)]),
                                    width=4, justify='center', state='readonly')
    PsqiQues3MinEntry.place(x=840, y=390)
    PsqiQues4Label = tk.Label(PsqiFrame1, text='4. 过去一个月你每晚实际睡眠的时间有多少？每晚实际睡眠的时间          (不等于卧床时间)。', 
                            font='宋体 15 bold', bg='white')
    PsqiQues4Label.place(x=193, y=460)
    PsqiQues4Entry = ttk.Combobox(PsqiFrame1, textvariable=tk.StringVar(), value=(['大于7小时', '6-7小时', '5-6小时', '小于5小时']),
                                    width=10, justify='center', state='readonly')
    PsqiQues4Entry.place(x=820, y=460)
    NextFrameBtn = tk.Button(PsqiFrame1, text='继续测评', width=15, font='宋体 15 bold', bg='WhiteSmoke', relief='ridge', command=PsqiNextFrame)
    NextFrameBtn.place(x=550, y=530)
    sep_hor1 = ttk.Separator(PsqiFrame1, orient='horizontal')
    sep_hor2 = ttk.Separator(PsqiFrame1, orient='horizontal')
    sep_ver1 = ttk.Separator(PsqiFrame1, orient='vertical')
    sep_ver2 = ttk.Separator(PsqiFrame1, orient='vertical')
    sep_hor1.place(x=150, y=130, width=1000)
    sep_hor2.place(x=150, y=630, width=1000)
    sep_ver1.place(x=150, y=130, height=500)
    sep_ver2.place(x=1150, y=130, height=500) 

# 2.3 Speaking Test Part: talking
TalkTopicList = ['1.请您简要介绍一些自己在过去半年内的学校/学习情况（如果休学了，请谈谈休学前的一学期学习情况）', '2.请您简要介绍自己和朋友的一些经历情况',
            '3.请您介绍一些您喜欢的食物以及最近饮食情况', '4.请您介绍您所喜欢的游戏、电视、运动或者其他娱乐等活动',
            '5.请介绍您在家里的一些活动或者与父母之间的活动情况', '6.请您介绍一下儿时的一些经历']
PicList = ['school.png', 'friendship.png', 'food.png', 'entertainment.png', 'family.png', 'childhood.png']
TalkIndex = 0
TalkTime = 60
# TalkTime = 12
def NextTopic():
    global TalkTime, TalkIndex, TalkTopicList, SpeakingFrame4, TalkImgLabel, TalkImg, TalkImgPath
    TalkImgPath = './material/TalkPic/'+PicList[TalkIndex]
    TalkImg = tk.PhotoImage(file=TalkImgPath)
    # Destroy the previous image label before updating
    try: TalkImgLabel.destroy()
    except:pass
    TalkImgLabel = tk.Label(SpeakingFrame6, image=TalkImg, width=400, height=300, bg='white')
    TalkTime -= 1
    if (TalkTime > 0) and (TalkTime % 10 != 0):
        NextQuestionBtn.place(relx=0.75, rely=0.15)
        TalkImgLabel.place(relx=0.35, rely=0.5)
        NextQuestionBtn.after(1000, NextTopic)
        # print(TalkTime)
    elif (TalkTime % 10 == 0) and (TalkTime != 0):
        TalkImgLabel.place(relx=0.4, rely=0.65)
        NextQuestionBtn.place(relx=0.75, rely=0.15)
        NextQuestionBtn.config(state='disabled')
        NextQuestionBtn.config(text='剩余'+str(TalkTime)+'秒')
        TalkImgLabel.place(relx=0.35, rely=0.5)
        NextQuestionBtn.after(1000, NextTopic)
    elif TalkTime == 0:
        TalkTime = 60
        # TalkTime = 12
        if TalkIndex < 5:
            TalkIndex += 1
            NextQuestionBtn.config(text='开始1分钟访谈')
            NextQuestionBtn.config(state='normal')
            TalkTopicLabel.config(text=TalkTopicList[TalkIndex])
            NextQuestionBtn.place(relx=0.4, rely=0.5)
            SpeakingFrame6.update()
        else: 
            SpeakingWin1.destroy()
            SpeakingBtn.config(state='disabled')
            messagebox.showinfo('提示','您已完成朗读评估！\n请点击确认或退出后联系医生。')
            JsonDict['Talk'] = 1
    
def timer_handler_nexttopic():
    global TalkIndex
    NextQuestionBtn.config(state='disabled')
    log_activity(activity_log='click the next free talk topic button, the topic-{} starts talking'.format(TalkIndex))
    NextQuestionBtn.config(text='剩余60秒')
    NextQuestionBtn.after(1000, NextTopic)

def StartTalk():
    global NextQuestionBtn, TalkTopicLabel, SpeakingFrame6
    SpeakingFrame5.destroy()
    log_activity(activity_log='The free talk instruction is over and Show the free talk:Topic-1')
    SpeakingFrame6 = tk.Frame(SpeakingWin1, width=1280, height=720, bg='white')
    SpeakingFrame6.pack()
    BehavourInstruc = tk.Label(SpeakingFrame6, text='请保持端正坐姿，面对电脑',
                        font='楷体 15 ', justify='center', bg='white')
    BehavourInstruc.place(relx=0.4, rely=0)
    TalkInstruc = tk.Label(SpeakingFrame6, text='请您根据自身情况，谈一谈下面的话题：',
                        font='宋体 18 bold', justify='center', bg='white')
    TalkInstruc.place(relx=0.1, rely=0.15)
    TalkTopicLabel = tk.Label(SpeakingFrame6, text=TalkTopicList[TalkIndex], wraplength=1000, width=100,
                        font='宋体 20 bold', justify='center', bg='white')
    TalkTopicLabel.place(relx=-0.1, rely=0.3)
    NextQuestionBtn = tk.Button(SpeakingFrame6, font='宋体 18 bold', width=20, 
                                text='开始1分钟访谈', command=timer_handler_nexttopic,
                                bg='WhiteSmoke', relief='ridge')
    NextQuestionBtn.place(relx=0.4, rely=0.5)

def TalkInstruction():
    global TalkIndex, SpeakingFrame5
    SpeakingFrame3.destroy()
    SpeakingWin1.lift()
    log_activity(activity_log='Show the free talk instruction')
    SpeakingFrame5 = tk.Frame(SpeakingWin1, width=1280, height=720, bg='white')
    SpeakingFrame5.pack()
    TalkTopic = tk.Label(SpeakingFrame5, text='开放式部分',
                        font='黑体 25 bold', justify='center', bg='white')
    TalkTopic.place(relx=0.45, rely=0.1)
    TalkInstruc = tk.Label(SpeakingFrame5, text='下面，我们将提供6个访谈话题。\
请您思考清楚后，根据自身情况，开始自由访谈这些话题。每个访谈话题回答1分钟左右时间。请使用普通话。\n\n\
1分钟倒计时结束后，在点击下一话题的‘开始1分钟访谈’按钮前，\
仍可访谈当前话题。',
            font='宋体 20 bold', justify='left', bg='white', width=70,
            wraplength=700)
    TalkInstruc.place(relx=0.1, rely=0.3)
    NextQuestionBtn = tk.Button(SpeakingFrame5, font='宋体 18 bold', width=35, 
                                text='已清楚要求；开始访谈话题', command=StartTalk,
                                bg='WhiteSmoke', relief='ridge')
    log_activity(activity_log='start analysis quesionnaire result')
    Analysis(dirname=dirname)
    log_activity(activity_log='finish quesionnaire analysis, report pdf has been generated.')
    NextQuestionBtn.place(relx=0.35, rely=0.7)  

# 2.2 Speaking Test
ReadList = []
MinusIndex = 20
def timer_handler_example():
        global waittime, ExampleBtn
        if waittime > 0:
                SpeakingWin1.protocol('WM_DELETE_WINDOW', False)
                SpeakingFrame1.after(1000, timer_handler_example)
                waittime-=1
                ExampleBtn['text'] = '已清楚要求，继续选择题部分('+str(waittime)+'秒)'
        else:
                log_activity(activity_log='config the state of ExampleBtn from "disabled" to "normal"')
                # SpeakingWin1.protocol('WM_DELETE_WINDOW', True)
                ExampleBtn['text'] = '已清楚要求，继续选择题部分'
                ExampleBtn.config(state='normal')

def QuesOver():
    global SpeakingWin2
    SpeakingBtn.config(state='disabled')
    SpeakingBtn.config(text="已完成情绪评估")
    JsonDict['Read'] = 1
    log_activity('CDI MASC PLE is over')
    log_activity(activity_log='start analysis quesionnaire result')
    Analysis(dirname=dirname)
    log_activity(activity_log='finish quesionnaire analysis, report pdf has been generated.')
    SpeakingWin1.destroy()
    SpeakingBtn.config(state='disabled')
    messagebox.showinfo('提示','您已完成情绪评估！\n请点击确认或退出后联系医生。')
    MainWin.lift()



def NextQuestion():
    global SpeakingIndex, MinusIndex
    NextQuestionBtn.config(state='disabled')
    NextQuestionBtn.after(1000, lambda: NextQuestionBtn.config(state='normal'))
    # NextQuestionBtn.after(100, lambda: NextQuestionBtn.config(state='normal'))
    if MinusIndex > 1:
        log_activity('Read the answer selected： {}'.format(ReadList[SpeakingIndex-MinusIndex]))
        MinusIndex -= 1
        SpeakQuestionLabel.config(text=ReadList[SpeakingIndex-MinusIndex])
    elif SpeakingIndex == 79: 
            log_activity('Read the answer selected： {}'.format(ReadList[SpeakingIndex-MinusIndex]))
            log_activity('Reading the answer is over and show the free talk messagebox')
            SpeakingWin2.destroy()
            messagebox.showinfo('提示', '朗读阶段结束！\n 请开始开放式部分！')
            JsonDict['Read'] = 1
            TalkInstruction()
    elif MinusIndex == 1:
        SpeakingWin2.destroy()
        log_activity('Read the answer selected： {}'.format(ReadList[SpeakingIndex-MinusIndex]))
        log_activity('Reading the answer is phased over and show the rest messagebox')
        messagebox.showinfo('休息一下', '朗读结束，休息一下吧！\n 休息过后请按确定继续哦！')
        SpeakingWin1.attributes('-disabled',0)
        SpeakingWin1.lift()
        MinusIndex = 20

def RecordSpeaking2():
    global MinusIndex, SpeakQuestionLabel, SpeakingWin2, SpeakingIndex, SpeakingFrame5,NextQuestionBtn
    SpeakingFrame5.destroy()
    log_activity('The instruction of read answer the participant selected is over, start read answer 1')
    SpeakingFrame4 = tk.Frame(SpeakingWin2, width=1280, height=720, bg='white')
    SpeakingFrame4.pack()
    PleaseSpeakLabel = tk.Label(SpeakingFrame4, font='宋体 20 ', text='请您出声朗读如下内容：', bg='white')
    PleaseSpeakLabel.place(relx=0.1, rely=0.2)
    SpeakQuestionLabel = tk.Label(SpeakingFrame4, font='宋体 20 bold', text=ReadList[SpeakingIndex-MinusIndex], bg='white')
    SpeakQuestionLabel.place(relx=0.2, rely=0.4)
    NextQuestionBtn = tk.Button(SpeakingFrame4, font='宋体 18 ', text='已完成朗读；继续下一题目', bg='WhiteSmoke', 
                    relief='ridge', command=NextQuestion)
    NextQuestionBtn.place(relx=0.4, rely=0.7)
    SpeakingWin2.protocol('WM_DELETE_WINDOW', False)
    SpeakingWin2.mainloop()

def RecordSpeaking():
    global MinusIndex, SpeakQuestionLabel, SpeakingWin2, SpeakingIndex, SpeakingFrame5
    log_activity('Show the Instruction of read answer the participant selected')
    SpeakingWin2 = tk.Toplevel(MainWin)
    SpeakingFrame5 = tk.Frame(SpeakingWin2, width=1280, height=720, bg='white')
    SpeakingFrame5.pack()
    InfoLabel = tk.Label(SpeakingFrame5, font='宋体 20 ', text='接下来请您出声朗读如下内容\n\n点击‘确定’开始',justify='center', bg='white')
    InfoLabel.place(relx=0.35, rely=0.4)
    NextQuestionBtn = tk.Button(SpeakingFrame5, font='宋体 18 ', text='确定', bg='WhiteSmoke', 
                    relief='ridge', command=RecordSpeaking2)
    NextQuestionBtn.place(relx=0.45, rely=0.7)
    SpeakingWin2.protocol('WM_DELETE_WINDOW', False)
    SpeakingWin2.mainloop()

def SpeakingBtn1Click():
    global SpeakingIndex, SpeakingBtn1, SpeakingBtn2, SpeakingBtn3, SpeakingBtn4, ReadList, SpeakingWin2
    log_activity('SpeakingBtn1 is clikced, and Speaking question: Index-{}, Speaking Question-{}, Speaking Answer-{}'.format((SpeakingIndex+1),\
             SpeakingQuestions.loc[SpeakingIndex, 'question'], SpeakingQuestions.loc[SpeakingIndex, 'read1']))
    # if (SpeakingIndex < 79) & ((SpeakingIndex+1) % 20 !=0): 
    if (SpeakingIndex < 79) : 
        output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'answer'] = 0    
        output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'question'] = SpeakingQuestions.loc[SpeakingIndex, 'question']
        output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'sequence'] = SpeakingIndex+1
        output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'read'] = SpeakingQuestions.loc[SpeakingIndex, 'read1']
        ReadList.append(SpeakingQuestions.loc[SpeakingIndex, 'read1'])
        SpeakingIndex += 1
        TestProgressor.config(value=SpeakingIndex+1)
        QuestionLabel.config(text=str(SpeakingIndex+1)+'.'+SpeakingQuestions.loc[SpeakingIndex, 'question'])
        SpeakingBtn1.config(text = SpeakingQuestions.loc[SpeakingIndex, 'answer1'])
        SpeakingBtn2.config(text = SpeakingQuestions.loc[SpeakingIndex, 'answer2'])
        SpeakingBtn3.config(text = SpeakingQuestions.loc[SpeakingIndex, 'answer3'])
        SpeakingBtn4.config(text = SpeakingQuestions.loc[SpeakingIndex, 'answer4'])
        SpeakingWin1.update()
        if SpeakingQuestions.loc[SpeakingIndex, 'answer4'] == '此处为空': 
            SpeakingBtn4.config(state='disabled')
            if SpeakingQuestions.loc[SpeakingIndex, 'answer3'] == '此处为空': 
                SpeakingBtn3.config(state='disabled'), SpeakingWin1.update()
            else: 
                SpeakingBtn3.config(state='normal')
                SpeakingWin1.update()
        else: SpeakingBtn4.config(state='normal'),SpeakingBtn3.config(state='normal'),SpeakingWin1.update()
    # elif (SpeakingIndex < 79) & ((SpeakingIndex+1) % 20 ==0): 
    #     SpeakingWin1.attributes('-disabled',1)
    #     output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'answer'] = 0    
    #     output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'question'] = SpeakingQuestions.loc[SpeakingIndex, 'question']
    #     output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'sequence'] = SpeakingIndex+1
    #     output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'read'] = SpeakingQuestions.loc[SpeakingIndex, 'read1']
    #     ReadList.append(SpeakingQuestions.loc[SpeakingIndex, 'read1'])
    #     SpeakingIndex += 1
    #     TestProgressor.config(value=SpeakingIndex+1)
    #     QuestionLabel.config(text=str(SpeakingIndex+1)+'.'+SpeakingQuestions.loc[SpeakingIndex, 'question'])
    #     SpeakingBtn1.config(text = SpeakingQuestions.loc[SpeakingIndex, 'answer1'])
    #     SpeakingBtn2.config(text = SpeakingQuestions.loc[SpeakingIndex, 'answer2'])
    #     SpeakingBtn3.config(text = SpeakingQuestions.loc[SpeakingIndex, 'answer3'])
    #     SpeakingBtn4.config(text = SpeakingQuestions.loc[SpeakingIndex, 'answer4'])
    #     SpeakingWin1.update()
    #     if SpeakingQuestions.loc[SpeakingIndex, 'answer4'] == '此处为空': 
    #         SpeakingBtn4.config(state='disabled')
    #         if SpeakingQuestions.loc[SpeakingIndex, 'answer3'] == '此处为空': 
    #             SpeakingBtn3.config(state='disabled'), SpeakingWin1.update()
    #         else: 
    #             SpeakingBtn3.config(state='normal')
    #             SpeakingWin1.update()
    #     else: SpeakingBtn4.config(state='normal'),SpeakingBtn3.config(state='normal'),SpeakingWin1.update()
    #     RecordSpeaking()
    else:
        output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'answer'] = 0            
        output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'question'] = SpeakingQuestions.loc[SpeakingIndex, 'question']
        output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'sequence'] = SpeakingIndex+1 
        output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'read'] = SpeakingQuestions.loc[SpeakingIndex, 'read1']
        log_activity(activity_log='output the MASC data to participant\'s dir')
        output_data.to_csv('./result/'+str(dirname)+'/'+str(dirname)+'_MASC.csv', encoding='GBK')
        QuesOver()
        # RecordSpeaking()

def SpeakingBtn2Click():
    global SpeakingIndex, SpeakingBtn1, SpeakingBtn2, SpeakingBtn3, SpeakingBtn4, ReadList, SpeakingWin2
    log_activity('SpeakingBtn2 is clikced, and Speaking question: Index-{}, Speaking Question-{}, Speaking Answer-{}'.format((SpeakingIndex+1),\
             SpeakingQuestions.loc[SpeakingIndex, 'question'], SpeakingQuestions.loc[SpeakingIndex, 'read2']))
    # if (SpeakingIndex < 79) & ((SpeakingIndex+1) % 20 !=0): 
    if (SpeakingIndex < 79) : 
        output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'answer'] = 1    
        output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'question'] = SpeakingQuestions.loc[SpeakingIndex, 'question']
        output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'sequence'] = SpeakingIndex+1
        output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'read'] = SpeakingQuestions.loc[SpeakingIndex, 'read2']
        ReadList.append(SpeakingQuestions.loc[SpeakingIndex, 'read2'])
        SpeakingIndex += 1
        TestProgressor.config(value=SpeakingIndex+1)
        QuestionLabel.config(text=str(SpeakingIndex+1)+'.'+SpeakingQuestions.loc[SpeakingIndex, 'question'])
        SpeakingBtn1.config(text = SpeakingQuestions.loc[SpeakingIndex, 'answer1'])
        SpeakingBtn2.config(text = SpeakingQuestions.loc[SpeakingIndex, 'answer2'])
        SpeakingBtn3.config(text = SpeakingQuestions.loc[SpeakingIndex, 'answer3'])
        SpeakingBtn4.config(text = SpeakingQuestions.loc[SpeakingIndex, 'answer4'])
        SpeakingWin1.update()
        if SpeakingQuestions.loc[SpeakingIndex, 'answer4'] == '此处为空': 
            SpeakingBtn4.config(state='disabled')
            if SpeakingQuestions.loc[SpeakingIndex, 'answer3'] == '此处为空': 
                SpeakingBtn3.config(state='disabled'), SpeakingWin1.update()
            else: 
                SpeakingBtn3.config(state='normal')
                SpeakingWin1.update()
        else: SpeakingBtn4.config(state='normal'),SpeakingBtn3.config(state='normal'),SpeakingWin1.update()
    # elif (SpeakingIndex < 79) & ((SpeakingIndex+1) % 20 ==0): 
    #     SpeakingWin1.attributes('-disabled',1)
    #     output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'answer'] = 1    
    #     output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'question'] = SpeakingQuestions.loc[SpeakingIndex, 'question']
    #     output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'sequence'] = SpeakingIndex+1
    #     output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'read'] = SpeakingQuestions.loc[SpeakingIndex, 'read2']
    #     ReadList.append(SpeakingQuestions.loc[SpeakingIndex, 'read2'])
    #     SpeakingIndex += 1
    #     TestProgressor.config(value=SpeakingIndex+1)
    #     QuestionLabel.config(text=str(SpeakingIndex+1)+'.'+SpeakingQuestions.loc[SpeakingIndex, 'question'])
    #     SpeakingBtn1.config(text = SpeakingQuestions.loc[SpeakingIndex, 'answer1'])
    #     SpeakingBtn2.config(text = SpeakingQuestions.loc[SpeakingIndex, 'answer2'])
    #     SpeakingBtn3.config(text = SpeakingQuestions.loc[SpeakingIndex, 'answer3'])
    #     SpeakingBtn4.config(text = SpeakingQuestions.loc[SpeakingIndex, 'answer4'])
    #     SpeakingWin1.update()
    #     if SpeakingQuestions.loc[SpeakingIndex, 'answer4'] == '此处为空': 
    #         SpeakingBtn4.config(state='disabled')
    #         if SpeakingQuestions.loc[SpeakingIndex, 'answer3'] == '此处为空': 
    #             SpeakingBtn3.config(state='disabled'), SpeakingWin1.update()
    #         else: 
    #             SpeakingBtn3.config(state='normal')
    #             SpeakingWin1.update()
    #     else: SpeakingBtn4.config(state='normal'),SpeakingBtn3.config(state='normal'),SpeakingWin1.update()
    #     RecordSpeaking()
    else:
        output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'answer'] = 1            
        output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'question'] = SpeakingQuestions.loc[SpeakingIndex, 'question']
        output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'sequence'] = SpeakingIndex+1 
        output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'read'] = SpeakingQuestions.loc[SpeakingIndex, 'read2']
        log_activity(activity_log='output the MASC data to participant\'s dir')
        output_data.to_csv('./result/'+str(dirname)+'/'+str(dirname)+'_MASC.csv', encoding='GBK')
        # RecordSpeaking()
        QuesOver()


def SpeakingBtn3Click():
    global SpeakingIndex, SpeakingBtn1, SpeakingBtn2, SpeakingBtn3, SpeakingBtn4, ReadList, SpeakingWin2
    log_activity('SpeakingBtn3 is clikced, and Speaking question: Index-{}, Speaking Question-{}, Speaking Answer-{}'.format((SpeakingIndex+1),\
             SpeakingQuestions.loc[SpeakingIndex, 'question'], SpeakingQuestions.loc[SpeakingIndex, 'read3']))
    # if (SpeakingIndex < 79) & ((SpeakingIndex+1) % 20 !=0): 
    if (SpeakingIndex < 79) : 
        output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'answer'] = 2    
        output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'question'] = SpeakingQuestions.loc[SpeakingIndex, 'question']
        output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'sequence'] = SpeakingIndex+1
        output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'read'] = SpeakingQuestions.loc[SpeakingIndex, 'read3']
        ReadList.append(SpeakingQuestions.loc[SpeakingIndex, 'read3'])
        SpeakingIndex += 1
        TestProgressor.config(value=SpeakingIndex+1)
        QuestionLabel.config(text=str(SpeakingIndex+1)+'.'+SpeakingQuestions.loc[SpeakingIndex, 'question'])
        SpeakingBtn1.config(text = SpeakingQuestions.loc[SpeakingIndex, 'answer1'])
        SpeakingBtn2.config(text = SpeakingQuestions.loc[SpeakingIndex, 'answer2'])
        SpeakingBtn3.config(text = SpeakingQuestions.loc[SpeakingIndex, 'answer3'])
        SpeakingBtn4.config(text = SpeakingQuestions.loc[SpeakingIndex, 'answer4'])
        SpeakingWin1.update()
        if SpeakingQuestions.loc[SpeakingIndex, 'answer4'] == '此处为空': 
            SpeakingBtn4.config(state='disabled')
            if SpeakingQuestions.loc[SpeakingIndex, 'answer3'] == '此处为空': 
                SpeakingBtn3.config(state='disabled'), SpeakingWin1.update()
            else: 
                SpeakingBtn3.config(state='normal')
                SpeakingWin1.update()
        else: SpeakingBtn4.config(state='normal'),SpeakingBtn3.config(state='normal'),SpeakingWin1.update()
    # elif (SpeakingIndex < 79) & ((SpeakingIndex+1) % 20 ==0): 
    #     SpeakingWin1.attributes('-disabled',1)
    #     output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'answer'] = 2    
    #     output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'question'] = SpeakingQuestions.loc[SpeakingIndex, 'question']
    #     output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'sequence'] = SpeakingIndex+1
    #     output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'read'] = SpeakingQuestions.loc[SpeakingIndex, 'read3']
    #     ReadList.append(SpeakingQuestions.loc[SpeakingIndex, 'read3'])
    #     SpeakingIndex += 1
    #     TestProgressor.config(value=SpeakingIndex+1)
    #     QuestionLabel.config(text=str(SpeakingIndex+1)+'.'+SpeakingQuestions.loc[SpeakingIndex, 'question'])
    #     SpeakingBtn1.config(text = SpeakingQuestions.loc[SpeakingIndex, 'answer1'])
    #     SpeakingBtn2.config(text = SpeakingQuestions.loc[SpeakingIndex, 'answer2'])
    #     SpeakingBtn3.config(text = SpeakingQuestions.loc[SpeakingIndex, 'answer3'])
    #     SpeakingBtn4.config(text = SpeakingQuestions.loc[SpeakingIndex, 'answer4'])
    #     SpeakingWin1.update()
    #     if SpeakingQuestions.loc[SpeakingIndex, 'answer4'] == '此处为空': 
    #         SpeakingBtn4.config(state='disabled')
    #         if SpeakingQuestions.loc[SpeakingIndex, 'answer3'] == '此处为空': 
    #             SpeakingBtn3.config(state='disabled'), SpeakingWin1.update()
    #         else: 
    #             SpeakingBtn3.config(state='normal')
    #             SpeakingWin1.update()
    #     else: SpeakingBtn4.config(state='normal'),SpeakingBtn3.config(state='normal'),SpeakingWin1.update()
    #     RecordSpeaking()
    else:
        output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'answer'] = 2            
        output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'question'] = SpeakingQuestions.loc[SpeakingIndex, 'question']
        output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'sequence'] = SpeakingIndex+1 
        output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'read'] = SpeakingQuestions.loc[SpeakingIndex, 'read3']
        log_activity(activity_log='output the MASC data to participant\'s dir')
        output_data.to_csv('./result/'+str(dirname)+'/'+str(dirname)+'_MASC.csv', encoding='GBK')
        # RecordSpeaking()
        QuesOver()


def SpeakingBtn4Click():
    global SpeakingIndex, SpeakingBtn1, SpeakingBtn2, SpeakingBtn3, SpeakingBtn4, ReadList, SpeakingWin2
    log_activity('SpeakingBtn4 is clikced, and Speaking question: Index-{}, Speaking Question-{}, Speaking Answer-{}'.format((SpeakingIndex+1),\
             SpeakingQuestions.loc[SpeakingIndex, 'question'], SpeakingQuestions.loc[SpeakingIndex, 'read4']))
    # if (SpeakingIndex < 79) & ((SpeakingIndex+1) % 20 !=0): 
    if (SpeakingIndex < 79) : 
        output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'answer'] = 3    
        output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'question'] = SpeakingQuestions.loc[SpeakingIndex, 'question']
        output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'sequence'] = SpeakingIndex+1
        output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'read'] = SpeakingQuestions.loc[SpeakingIndex, 'read4']
        ReadList.append(SpeakingQuestions.loc[SpeakingIndex, 'read4'])
        SpeakingIndex += 1
        TestProgressor.config(value=SpeakingIndex+1)
        QuestionLabel.config(text=str(SpeakingIndex+1)+'.'+SpeakingQuestions.loc[SpeakingIndex, 'question'])
        SpeakingBtn1.config(text = SpeakingQuestions.loc[SpeakingIndex, 'answer1'])
        SpeakingBtn2.config(text = SpeakingQuestions.loc[SpeakingIndex, 'answer2'])
        SpeakingBtn3.config(text = SpeakingQuestions.loc[SpeakingIndex, 'answer3'])
        SpeakingBtn4.config(text = SpeakingQuestions.loc[SpeakingIndex, 'answer4'])
        SpeakingWin1.update()
        if SpeakingQuestions.loc[SpeakingIndex, 'answer4'] == '此处为空': 
            SpeakingBtn4.config(state='disabled')
            if SpeakingQuestions.loc[SpeakingIndex, 'answer3'] == '此处为空': 
                SpeakingBtn3.config(state='disabled'), SpeakingWin1.update()
            else: 
                SpeakingBtn3.config(state='normal')
                SpeakingWin1.update()
        else: SpeakingBtn4.config(state='normal'),SpeakingBtn3.config(state='normal'),SpeakingWin1.update()
    # elif (SpeakingIndex < 79) & ((SpeakingIndex+1) % 20 ==0): 
    #     SpeakingWin1.attributes('-disabled',1)
    #     output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'answer'] = 3    
    #     output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'question'] = SpeakingQuestions.loc[SpeakingIndex, 'question']
    #     output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'sequence'] = SpeakingIndex+1
    #     output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'read'] = SpeakingQuestions.loc[SpeakingIndex, 'read4']
    #     ReadList.append(SpeakingQuestions.loc[SpeakingIndex, 'read4'])
    #     SpeakingIndex += 1
    #     TestProgressor.config(value=SpeakingIndex+1)
    #     QuestionLabel.config(text=str(SpeakingIndex+1)+'.'+SpeakingQuestions.loc[SpeakingIndex, 'question'])
    #     SpeakingBtn1.config(text = SpeakingQuestions.loc[SpeakingIndex, 'answer1'])
    #     SpeakingBtn2.config(text = SpeakingQuestions.loc[SpeakingIndex, 'answer2'])
    #     SpeakingBtn3.config(text = SpeakingQuestions.loc[SpeakingIndex, 'answer3'])
    #     SpeakingBtn4.config(text = SpeakingQuestions.loc[SpeakingIndex, 'answer4'])
    #     SpeakingWin1.update()
    #     if SpeakingQuestions.loc[SpeakingIndex, 'answer4'] == '此处为空': 
    #         SpeakingBtn4.config(state='disabled')
    #         if SpeakingQuestions.loc[SpeakingIndex, 'answer3'] == '此处为空': 
    #             SpeakingBtn3.config(state='disabled'), SpeakingWin1.update()
    #         else: 
    #             SpeakingBtn3.config(state='normal')
    #             SpeakingWin1.update()
    #     else: SpeakingBtn4.config(state='normal'),SpeakingBtn3.config(state='normal'),SpeakingWin1.update()
    #     RecordSpeaking()
    else:
        output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'answer'] = 3            
        output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'question'] = SpeakingQuestions.loc[SpeakingIndex, 'question']
        output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'sequence'] = SpeakingIndex+1 
        output_data.loc[SpeakingQuestions.loc[SpeakingIndex, 'index'], 'read'] = SpeakingQuestions.loc[SpeakingIndex, 'read4']
        log_activity(activity_log='output the MASC data to participant\'s dir')
        output_data.to_csv('./result/'+str(dirname)+'/'+str(dirname)+'_MASC.csv', encoding='GBK')
        # RecordSpeaking()
        QuesOver()


def StartSpeaking():
    global SpeakingIndex, SpeakingQuestions, QuestionLabel, SpeakingFrame2, TestProgressor, SpeakingBtn1,SpeakingBtn2,SpeakingBtn3,SpeakingBtn4, SpeakingFrame3
    log_activity(activity_log='The Instruction of Speaking Test Selection Part is over and start select the answer of CDI and MASC')
    SpeakingFrame2.destroy()
    SpeakingQuestions = pd.read_csv(scri_path+'/material/SpeakingTest.csv', encoding='GBK',) 
    # print(SpeakingQuestions)
    np.random.shuffle(SpeakingQuestions.values)
    # print(SpeakingQuestions)  
    SpeakingIndex = 0
    SpeakingFrame3 = tk.Frame(SpeakingWin1, width=1280, height=720, bg='white')
    SpeakingFrame3.pack()
    QuestionLabel = tk.Label(SpeakingFrame3, font='宋体 20 bold', width=80, wraplength=800, justify='left', text='1.'+SpeakingQuestions.loc[SpeakingIndex, 'question'], bg='white')
    QuestionLabel.place(relx=0, rely=0.15)
    SpeakingBtn1 = tk.Button(SpeakingFrame3, font='宋体 18 bold', width=35, 
                             text=SpeakingQuestions.loc[SpeakingIndex, 'answer1'], command=SpeakingBtn1Click, bg='WhiteSmoke', relief='ridge')
    SpeakingBtn1.place(relx=0.3, rely=0.3)
    SpeakingBtn2 = tk.Button(SpeakingFrame3, font='宋体 18 bold', width=35, 
                             text=SpeakingQuestions.loc[SpeakingIndex, 'answer2'], command=SpeakingBtn2Click, bg='WhiteSmoke', relief='ridge')
    SpeakingBtn2.place(relx=0.3, rely=0.4)
    SpeakingBtn3 = tk.Button(SpeakingFrame3, font='宋体 18 bold', width=35, 
                             text=SpeakingQuestions.loc[SpeakingIndex, 'answer3'], command=SpeakingBtn3Click, bg='WhiteSmoke', relief='ridge')
    SpeakingBtn3.place(relx=0.3, rely=0.5)
    SpeakingBtn4 = tk.Button(SpeakingFrame3, font='宋体 18 bold', width=35, 
                             text=SpeakingQuestions.loc[SpeakingIndex, 'answer4'], command=SpeakingBtn4Click,bg='WhiteSmoke', relief='ridge')
    SpeakingBtn4.place(relx=0.3, rely=0.6)
    if SpeakingQuestions.loc[SpeakingIndex, 'answer3'] == '此处为空': SpeakingBtn3.config(state='disabled')
    else :SpeakingBtn3.config(state='normal')
    if SpeakingQuestions.loc[SpeakingIndex, 'answer4'] == '此处为空': SpeakingBtn4.config(state='disabled') 
    else :SpeakingBtn4.config(state='normal')
    TestProgressor = ttk.Progressbar(SpeakingFrame3, orient='horizontal', mode='determinate',
                                        length=1000, maximum=80, value=SpeakingIndex+1)
    TestProgressor.place(relx=0.1, rely=0.8)
    tip = tk.Label(SpeakingFrame3, text='版权所有和解释权  @山东师范大学心理学院', font='宋体 10 ', bg='white')
    tip.place(x=500, y=690)
    SpeakingWin1.mainloop()

def ExampleBtnClick():
    global scri_path, SpeakingFrame2
    log_activity(activity_log='the Instrucion of Speaking Test is over and Show the Instruction\
of Speaking Test Selection Part')
    SpeakingFrame1.destroy()
    SpeakingFrame2 = tk.Frame(SpeakingWin1, width=1280, height=720, bg='white')
    SpeakingFrame2.pack()
    SpeakingFrame2_title = tk.Label(SpeakingFrame2, text='选择题部分', font='黑体 25 bold', bg='white')
    SpeakingFrame2_title.place(relx=0.42, rely=0.1)
    f = open("./material/SpeakingTestInstruction.txt", "r", encoding='utf-8')
    instruction_data = f.read()
    f.close()
    SpeakingFrame2Instruc = tk.Label(SpeakingFrame2, text=instruction_data, font='宋体 20', bg='white', wraplength=1000, width=100, justify='left')
    SpeakingFrame2Instruc.place(relx=-0.05, rely=0.35)
    StartSpeakingBtn = tk.Button(SpeakingFrame2, width=15, font='宋体 18 bold', bg='WhiteSmoke', 
                    relief='ridge',text='开始评估', command=StartSpeaking)
    StartSpeakingBtn.place(relx=0.4, rely=0.75)
    SpeakingWin1.mainloop()

def SpeakingTest():
    global SpeakingWin1, SpeakingFrame1, ExampleBtn
    log_activity(activity_log='Generate the Win of Speaking Test')
    SpeakingWin1 = tk.Toplevel(MainWin)
    SpeakingWin1.resizable(False,False)
    SpeakingFrame1 = tk.Frame(SpeakingWin1, width=1280, height=720, bg='white')
    SpeakingFrame1.pack()
    SpeakingFrame1_title = tk.Label(SpeakingFrame1, text='3.情绪评估', font='黑体 25 bold', bg='white')
    SpeakingFrame1_title.place(relx=0.45, rely=0.1)
    f = open(scri_path+"/material/SpeakingInstruction.txt", "r", encoding='utf-8')
    SpeakingInstruc =  f.read()
    f.close()
    SpeakingInstruc1Text = tk.Label(SpeakingFrame1, text=SpeakingInstruc, font='宋体 18 bold', 
                                    justify='left', wraplength=900, width=90, bg='white')
    SpeakingInstruc1Text.place(x=70, y=180)
    sep_hor1 = ttk.Separator(SpeakingFrame1, orient='horizontal')
    sep_hor2 = ttk.Separator(SpeakingFrame1, orient='horizontal')
    sep_ver1 = ttk.Separator(SpeakingFrame1, orient='vertical')
    sep_ver2 = ttk.Separator(SpeakingFrame1, orient='vertical')
    sep_hor1.place(x=150, y=130, width=1000)
    sep_hor2.place(x=150, y=630, width=1000)
    sep_ver1.place(x=150, y=130, height=500)
    sep_ver2.place(x=1150, y=130, height=500) 
    ExampleBtn = tk.Button(SpeakingFrame1, text='已清楚要求，继续选择题部分(10秒)', width=35, font='宋体 15 bold', bg='WhiteSmoke', 
                        relief='ridge', command=ExampleBtnClick, state='disabled')
    ExampleBtn.place(x=500, y=550)
    SpeakingFrame1.after(1000, timer_handler_example)

def main():
    global output_data, StartBtn,ExitBtn,InformBtn, MemoryBtn,RefuseBtn, SwitchBtn, \
    ConcentBtn,GuessingBtn,ExampleBtn,RefreshBtn,MainWin,scri_path, ico_path,InfoFrame1, NameLabel,\
    NameEntry,AgeLabel,YearEntry,MonthEntry,DayEntry,VerifyEntry, InstitutionEntry,\
    VerifyWin,GenderEntry, EthnicEntry, HeightEntry, WeightEntry,\
    HandEntry,HomeEntry, ParentEntry, SiblingEntry, EducationEntry, LocationEntry,\
    PSQIBtn,SpeakingBtn, InfoFrame2, InfoQues13Entry, InfoQues14Entry,InfoQues15_1Entry, InfoQues15_2Entry, \
    InfoQues16Entry,InfoQues17_1Entry, InfoQues17_2Entry, InfoQues18_1Entry, InfoQues18_2Entry, \
    InfoQues18_3Entry,InfoQues19Entry,InfoQues20_1Entry, InfoQues20_2Entry, InitialFrame,start_time,\
    audio_recorder,video_recorder, RecordTime, RecordTimeStr

    start_time = datetime.datetime.now()
    scri_path = os.getcwd()
    ico_path = scri_path+'/material/logo.ico'
    # creat a Dataframe
    output_data = pd.DataFrame(columns=['answer', 'question','sequence','read'],
                        index=['name', 'name_pinyin','age' , 'year', 'month', 'day', 'gender','ethnic', 
                        'height', 'weight', 'hand', 'home', 'parent', 'sibling', 
                        'education', 'institution', 'HosID', 'InfoQuestion-13', 'InfoQuestion-14', 'InfoQuestion-15_1', 'InfoQuestion-15_2',
                        'InfoQuestion-16', 'InfoQuestion-17_1','InfoQuestion-17_2', 'InfoQuestion-18_1', 'InfoQuestion-18_2', 
                        'InfoQuestion-18_3','InfoQuestion-18_4','InfoQuestion-18_5','InfoQuestion-19', 'InfoQuestion-20_1','InfoQuestion-20_2',
                        'InfoQuestion-21_1','InfoQuestion-21_2','InfoQuestion-21_3',
                        'PSQI-1_Hour', 'PSQI-1_Min',
                        'PSQI-2', 'PSQI-3_Hour', 'PSQI-3_Min','PSQI-4', 'PSQI-5a', 
                        'PSQI-5b', 'PSQI-5c', 'PSQI-5d', 'PSQI-5e', 'PSQI-5f', 'PSQI-5g', 
                        'PSQI-5h', 'PSQI-5i', 'PSQI-5j', 'PSQI-6', 'PSQI-7', 'PSQI-8', 
                        'PSQI-9', 'PSQI-10', 'PSQI-10a', 'PSQI-10b', 'PSQI-10c', 'PSQI-10d','PSQI-10e',
                        'PLE-B1', 'PLE-B2', 'PLE-B3', 'PLE-B4', 'PLE-B5', 'PLE-B6', 'PLE-B7', 'PLE-B8', 
                        'PLE-B9', 'PLE-B10', 'PLE-B11', 'PLE-B12', 'PLE-B13', 'PLE-B14', 'PLE-B15', 'PLE-B16', 
                        'PLE-B17', 'PLE-B18', 'PLE-B19', 'PLE-B20', 'PLE-B21', 'PLE-BD1', 'PLE-BD2', 'PLE-BD3', 
                        'PLE-BD4', 'PLE-BD5', 'PLE-BD6', 'PLE-BD7', 'PLE-BD8', 'PLE-BD9', 'PLE-BD10', 'PLE-BD11', 
                        'PLE-BD12', 'PLE-BD13', 'PLE-BD14', 'PLE-BD15', 'PLE-BD16', 'PLE-BD17', 'PLE-BD18', 
                        'PLE-BD19', 'PLE-BD20', 'PLE-BD21',
                        'CDI-1', 'CDI-2', 'CDI-3', 'CDI-4', 'CDI-5', 'CDI-6', 'CDI-7', 'CDI-8', 
                        'CDI-9', 'CDI-10', 'CDI-11', 'CDI-12', 'CDI-13', 'CDI-14', 'CDI-15', 
                        'CDI-16', 'CDI-17', 'CDI-18', 'CDI-19', 'CDI-20', 'CDI-21', 'CDI-22', 
                        'CDI-23', 'CDI-24', 'CDI-25', 'CDI-26', 'CDI-27', 'MASC-1', 'MASC-2', 
                        'MASC-3', 'MASC-4', 'MASC-5', 'MASC-6', 'MASC-7', 'MASC-8', 'MASC-9', 
                        'MASC-10', 'MASC-11', 'MASC-12', 'MASC-13', 'MASC-14', 'MASC-15', 'MASC-16', 
                        'MASC-17', 'MASC-18', 'MASC-19', 'MASC-20', 'MASC-21', 'MASC-22', 'MASC-23', 
                        'MASC-24', 'MASC-25', 'MASC-26', 'MASC-27', 'MASC-28', 'MASC-29', 'MASC-30', 
                        'MASC-31', 'MASC-32', 'MASC-33', 'MASC-34', 'MASC-35', 'MASC-36', 'MASC-37', 
                        'MASC-38', 'MASC-39', 'Random-1', 'Random-2', 'Random-3', 'Random-4', 'Random-5', 
                        'Random-6', 'Random-7', 'Random-8', 'Random-9', 'Random-10', 'Random-11', 
                        'Random-12', 'Random-13', 'Random-14'])

    # start record video & audio
    # audio_recorder = RecordAudio.AudioRecorder()
    # video_recorder = RecordVideo.VideoRecorder()
    # audio_recorder.start_recording() 
    # video_recorder.start_recording()
    # RecordTime = datetime.datetime.now() - start_time
    # RecordTimeStr = f"{RecordTime.total_seconds():.2f} seconds"
    Verify()


# function of 'sign in'
def SignIn():
    today = datetime.datetime.now()
    VerifyTime = int("{:0>2d}{:0>2d}{:0>2d}".format(today.year,today.month,today.day))
    password = VerifyEntry.get()
    institution = InstitutionEntry.get()
    password_list = ['sandBrain','sandBrain1000','sandBrain10000']
# 设置多个邀请码（5个）
    if (password in password_list) & (institution == '山东省精神卫生中心'):
        if VerifyTime <= 20501231:
            VerifyWin.destroy()
            MainWin0()
        else: 
            messagebox.showinfo('过期提示','该软件仅限2050年12月31日可用，继续使用请联系开发者！')
            VerifyWin.destroy()
            # audio_recorder.stop_recording('temp.wav')
            # video_recorder.stop_recording('temp.avi')
            sys.exit()  
    else :
        ReminderWin = tk.Tk()
        ReminderWin.title('认证错误')
        ReminderWin.geometry('400x170+750+400')
        ReminderWin.resizable(False, False)
        ReminderTip = tk.Label(ReminderWin,  text='您输入的评估机构或邀请码有误，请重新输入',
                             font='宋体 10')
        ReminderTip.place(x=60, y=50)
        ReminderBtn = tk.Button(ReminderWin, text='确定', font='宋体 10 bold', command=ReminderWin.destroy)
        ReminderBtn.place(x=170, y=120)

# 视频函数
def update_image(img):
    global VideoPanel, IsRunning
    if IsRunning:
        img = ImageTk.PhotoImage(image=img)
        VideoPanel.configure(image=img)
        VideoPanel.image = img

def stream():
    global cap, delay_between_frames, IsRunning, MainWin
    try:
        while IsRunning:
            ret, frame = cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.resize(frame, (908, 480))
                im = Image.fromarray(frame)
                MainWin.after(0, update_image, im)
            else:
                break
            time.sleep(delay_between_frames)
    except RuntimeError as e:
        print(f"RuntimeError in stream: {e}")

def VideoClose():
    global IsRunning, cap
    IsRunning = False
    cap.release()
    pygame.mixer.music.stop()
    VideoFrame.destroy()
    MainWin1()

def Verify():
    global output_data, StartBtn,ExitBtn,InformBtn, MemoryBtn,RefuseBtn, SwitchBtn, \
    ConcentBtn,GuessingBtn,ExampleBtn,RefreshBtn,MainWin,scri_path, ico_path,InfoFrame1, NameLabel,\
    NameEntry,AgeLabel,YearEntry,MonthEntry,DayEntry,VerifyEntry, InstitutionEntry,\
    VerifyWin, ico_path, scri_path, GenderEntry, EthnicEntry, HeightEntry, WeightEntry,\
    HandEntry,HomeEntry, ParentEntry, SiblingEntry, EducationEntry, LocationEntry,\
    PSQIBtn,SpeakingBtn, InfoFrame2, InfoQues13Entry, InfoQues14Entry,InfoQues15_1Entry, InfoQues15_2Entry, \
    InfoQues16Entry,InfoQues17_1Entry, InfoQues17_2Entry, InfoQues18_1Entry, InfoQues18_2Entry, \
    InfoQues18_3Entry,InfoQues19Entry,InfoQues20_1Entry, InfoQues20_2Entry, InitialFrame,start_time,\
    audio_recorder,video_recorder, HosIDEntry, cap, fps, delay_between_frames, video_panel,\
    VideoFrame, IsRunning, audio_source, VideoPanel
    # verifywin
    VerifyWin = tk.Tk()
    # set geometry and location
    VerifyWin.iconbitmap(ico_path)
    VerifyWin.wm_iconbitmap(ico_path)
    VerifyWin.title('儿童青少年情绪状态识别')
    VerifyWin.config(bg='white')
    VerifyWin.geometry('1280x720')
    VerifyWin.resizable(False, False)
    # set seperator
    VerifyWin_title = tk.Label(VerifyWin, text='儿童青少年情绪状态识别', font='黑体 25 bold', bg='white')
    VerifyWin_title.place(x=470, y=50)
    sep_hor1 = ttk.Separator(VerifyWin, orient='horizontal')
    sep_hor2 = ttk.Separator(VerifyWin, orient='horizontal')
    sep_ver1 = ttk.Separator(VerifyWin, orient='vertical')
    sep_ver2 = ttk.Separator(VerifyWin, orient='vertical')
    sep_hor1.place(x=150, y=130, width=1000)
    sep_hor2.place(x=150, y=630, width=1000)
    sep_ver1.place(x=150, y=130, height=500)
    sep_ver2.place(x=1150, y=130, height=500)
    welcome = tk.Label(VerifyWin, text='欢迎使用儿童青少年情绪状态识别软件', font='宋体 20 ', bg='white')
    welcome.place(x=450, y=200)
    Institution = tk.Label(VerifyWin, text='评估机构：', font='宋体 20 bold', bg='white')
    Institution.place(x=350, y=300)
    verify_code = tk.Label(VerifyWin, text='邀请码：', font='宋体 20 bold', bg='white')
    verify_code.place(x=350, y=400)
    InstitutionEntry = ttk.Combobox(VerifyWin, textvariable=tk.StringVar(), value=['山东省精神卫生中心'],
                                     width=30, font='宋体 20', state='readonly')
    VerifyEntry = tk.Entry(VerifyWin, width=30, font='宋体 20', bg='white', show="*" )
    InstitutionEntry.place(x=550, y=300)
    VerifyEntry.place(x=550, y=400)
    BrainImage = tk.PhotoImage(file=scri_path+'/material/brain.png')
    BrainImageLabel = tk.Label(VerifyWin, image=BrainImage, height=126, width=126, bg='white')
    BrainImageLabel.place(relx=0.9, rely=0)
    btn1 = tk.Button(VerifyWin, text='登录', font='宋体 15 bold', command=SignIn, bg='WhiteSmoke', relief='ridge')
    btn1.place(x=600, y=500)
    tip = tk.Label(VerifyWin, text='版权所有和解释权  @山东师范大学心理学院', font='宋体 10 ', bg='white')
    tip.place(x=500, y=690)
    VerifyWin.protocol('WM_DELETE_WINDOW', on_closing)
    VerifyWin.mainloop()

def MainWin0():
    global output_data, StartBtn,ExitBtn,InformBtn, MemoryBtn,RefuseBtn, SwitchBtn, \
    ConcentBtn,GuessingBtn,ExampleBtn,RefreshBtn,MainWin,scri_path, ico_path,InfoFrame1, NameLabel,\
    NameEntry,AgeLabel,YearEntry,MonthEntry,DayEntry,VerifyEntry, InstitutionEntry,\
    VerifyWin, ico_path, scri_path, GenderEntry, EthnicEntry, HeightEntry, WeightEntry,\
    HandEntry,HomeEntry, ParentEntry, SiblingEntry, EducationEntry, LocationEntry,\
    PSQIBtn,SpeakingBtn, InfoFrame2, InfoQues13Entry, InfoQues14Entry,InfoQues15_1Entry, InfoQues15_2Entry, \
    InfoQues16Entry,InfoQues17_1Entry, InfoQues17_2Entry, InfoQues18_1Entry, InfoQues18_2Entry, \
    InfoQues18_3Entry,InfoQues19Entry,InfoQues20_1Entry, InfoQues20_2Entry, InitialFrame,start_time,\
    audio_recorder,video_recorder, HosIDEntry, cap, fps, delay_between_frames, video_panel,\
    VideoFrame, IsRunning, audio_source, VideoPanel
    # set geometry and location
    MainWin = tk.Tk()
    MainWin.iconbitmap(ico_path)
    MainWin.wm_iconbitmap(ico_path)
    MainWin.config(background='white')
    MainWin.title('儿童青少年情绪状态精准识别')
    MainWin.geometry('1280x720')
    MainWin.resizable(False, False)
# 视频播放
    IsRunning = True
    video_source = "./material/Instruction.mp4"
    audio_source = "./material/Instruction.mp3"
    VideoFrame = tk.Frame(MainWin, bg='white', background='white')  # 用于视频播放的Frame
    VideoFrame.pack(fill=tk.BOTH, expand=True)
    VideoPanel = tk.Label(VideoFrame, background='white')  # 在Frame内创建Label用于显示视频
    VideoPanel.pack(fill=tk.BOTH, expand=True)
    # 设置视频播放和音频播放
    cap = cv2.VideoCapture(video_source)
    fps = cap.get(cv2.CAP_PROP_FPS)
    delay_between_frames = 1 / fps if fps > 0 else 0.033
    btn_close = tk.Button(VideoFrame, text="确定", font='宋体 15 bold', command=VideoClose,bg='WhiteSmoke', relief='ridge')
    btn_close.place(x=620, y=600)
    pygame.mixer.init()
    pygame.mixer.music.load(audio_source)
    pygame.mixer.music.play()
    threading.Thread(target=stream, daemon=True).start()
    tip = tk.Label(VideoFrame, text='版权所有和解释权  @山东师范大学心理学院', font='宋体 10 ', bg='white')
    tip.place(x=500, y=690)
    MainWin.protocol("WM_DELETE_WINDOW", VideoClose)
    MainWin.mainloop()

def MainWin1():
    global output_data, StartBtn,ExitBtn,InformBtn, MemoryBtn,RefuseBtn, SwitchBtn, \
    ConcentBtn,GuessingBtn,ExampleBtn,RefreshBtn,MainWin,scri_path, ico_path,InfoFrame1, NameLabel,\
    NameEntry,AgeLabel,YearEntry,MonthEntry,DayEntry,VerifyEntry, InstitutionEntry,\
    VerifyWin, ico_path, scri_path, GenderEntry, EthnicEntry, HeightEntry, WeightEntry,\
    HandEntry,HomeEntry, ParentEntry, SiblingEntry, EducationEntry, LocationEntry,\
    PSQIBtn,SpeakingBtn, InfoFrame2, InfoQues13Entry, InfoQues14Entry,InfoQues15_1Entry, InfoQues15_2Entry, \
    InfoQues16Entry,InfoQues17_1Entry, InfoQues17_2Entry, InfoQues18_1Entry, InfoQues18_2Entry, \
    InfoQues18_3Entry,InfoQues19Entry,InfoQues20_1Entry, InfoQues20_2Entry, InitialFrame,start_time,\
    audio_recorder,video_recorder, HosIDEntry, cap, fps, delay_between_frames, video_panel,\
    VideoFrame

    # creat a infomation frame/cavans
    InfoFrame1 = tk.Frame(MainWin,width=1280, height=720, bg='white')
    InfoFrame1.pack()
    InfoFrame1_title = tk.Label(InfoFrame1, text='儿童青少年情绪状态精准识别',
                            font='黑体 23 bold', bg='white')
    InfoFrame1_title.place(x=350, y=50)
    sep_hor1 = ttk.Separator(InfoFrame1, orient='horizontal')
    sep_hor2 = ttk.Separator(InfoFrame1, orient='horizontal')
    sep_ver1 = ttk.Separator(InfoFrame1, orient='vertical')
    sep_ver2 = ttk.Separator(InfoFrame1, orient='vertical')
    sep_hor1.place(x=150, y=130, width=1000)
    sep_hor2.place(x=150, y=630, width=1000)
    sep_ver1.place(x=150, y=130, height=500)
    sep_ver2.place(x=1150, y=130, height=500)
    Title = tk.Label(InfoFrame1, text='信息登记', font='黑体 18 bold', bg='white')
    Title.place(x=590, y=140)
    Title_supplement = tk.Label(InfoFrame1, text='(必填项)', font='黑体 15 bold', bg='white')
    Title_supplement.place(x=600, y=175)
    # the first line info
    NameLabel = tk.Label(InfoFrame1, text='1. 姓名/昵称：', font='宋体 13 bold', bg='white')
    NameLabel.place(x=220, y=220)
    NameEntry = tk.Entry(InfoFrame1, width=10,  justify='center', bg='white')
    NameEntry.place(x=350, y=220)
    AgeLabel = tk.Label(InfoFrame1, text='2. 生日：', font='宋体 13 bold', bg='white')
    AgeLabel.place(x=500, y=220)
    var = tk.StringVar()
    YearEntry = ttk.Combobox(InfoFrame1, textvariable=var, value=([str(i) for i in range(1980,2051,1)]), width=5, state = 'readonly')
    YearEntry.place(x=580, y=220)
    YearLabel = tk.Label(InfoFrame1, text='年', font='宋体 13 bold', bg='white')
    YearLabel.place(x=640, y=220)
    var = tk.StringVar()
    MonthEntry = ttk.Combobox(InfoFrame1, textvariable=var, value=([str('{:0>2d}'.format(i)) for i in range(1,13,1)]), width=2, state = 'readonly')
    MonthEntry.place(x=670, y=220)
    MonthLabel = tk.Label(InfoFrame1, text='月', font='宋体 13 bold', bg='white')
    MonthLabel.place(x=710, y=220)
    var = tk.StringVar()
    DayEntry = ttk.Combobox(InfoFrame1, textvariable=var, value=([str('{:0>2d}'.format(i)) for i in range(1,32,1)]), width=2, state = 'readonly')
    DayEntry.place(x=740, y=220)
    DayLabel = tk.Label(InfoFrame1, text='日', font='宋体 13 bold', bg='white')
    DayLabel.place(x=780, y=220)
    GenderLabel = tk.Label(InfoFrame1, text='3. 性别：', font='宋体 13 bold', width=10, anchor='w', bg='white')
    GenderLabel.place(x=870, y=220)
    var = tk.StringVar()
    GenderEntry = ttk.Combobox(InfoFrame1, textvariable=var, value=(['男', '女']), width=10, state = 'readonly')
    GenderEntry.place(x=950, y=220)
    # the second line info 
    EthnicLabel = tk.Label(InfoFrame1, text='4. 民族：', font='宋体 13 bold', bg='white')
    EthnicLabel.place(x=220, y=300)
    var = tk.StringVar()
    EthnicList = ['汉族', '回族', '壮族', '满族', '苗族', '维吾尔族', '土家族', '彝族', '蒙古族', '藏族', '布依族', '侗族', '瑶族', \
                '朝鲜族', '白族', '哈尼族', '哈萨克族', '黎族', '傣族', '畲族', '傈僳族', '仡佬族', '东乡族', '高山族', '拉祜族', \
                    '水族', '佤族', '纳西族', '羌族', '土族', '仫佬族', '锡伯族', '柯尔克孜族', '达斡尔族', '景颇族', '毛南族', '撒拉族',\
                    '布朗族', '塔吉克族', '阿昌族', '普米族', '鄂温克族', '怒族', '京族', '基诺族', '德昂族', '保安族', \
                    '俄罗斯族', '裕固族', '乌孜别克族', '门巴族', '鄂伦春族', '独龙族', '塔塔尔族', '赫哲族', '珞巴族', '其他']
    EthnicEntry = ttk.Combobox(InfoFrame1, textvariable=var, value=(EthnicList), width=9, state = 'readonly')
    EthnicEntry.place(x=300, y=300)
    HeightLabel = tk.Label(InfoFrame1, text='5. 身高：', font='宋体 13 bold', bg='white')
    HeightLabel.place(x=430, y=300)
    HeightEntry = tk.Entry(InfoFrame1, width=4, justify='center')
    HeightEntry.place(x=510, y=300)
    HeightLabel_1 = tk.Label(InfoFrame1, text='厘米', font='宋体 13 bold', bg='white')
    HeightLabel_1.place(x=550, y=300)
    WeightLabel = tk.Label(InfoFrame1, text='6. 体重：', font='宋体 13 bold', bg='white')
    WeightLabel.place(x=640, y=300)
    WeightEntry = tk.Entry(InfoFrame1, width=4,  justify='center',)
    WeightEntry.place(x=720, y=300)
    WeightLabel_1 = tk.Label(InfoFrame1, text='千克', font='宋体 13 bold', bg='white')
    WeightLabel_1.place(x=760, y=300)
    HandLabel = tk.Label(InfoFrame1, text='7. 利手：', font='宋体 13 bold', bg='white')
    HandLabel.place(x=870, y=300)
    var = tk.StringVar()
    HandEntry = ttk.Combobox(InfoFrame1, textvariable=var, value=(['右手', '左手']), width=10, state = 'readonly')
    HandEntry.place(x=950, y=300)
    # the third line info
    HomeLabel = tk.Label(InfoFrame1, text='8. 家庭所在地：', font='宋体 13 bold', bg='white')
    HomeLabel.place(x=220, y=380)
    var = tk.StringVar()
    HomeEntry = ttk.Combobox(InfoFrame1, textvariable=var, 
            value=(['城市', '县城', '乡镇', '农村']), width=8, justify='center', state = 'readonly')
    HomeEntry.place(x=355, y=380)
    ParentLabel = tk.Label(InfoFrame1, text='9. 父母状况：', font='宋体 13 bold', bg='white')
    ParentLabel.place(x=520, y=380)
    var = tk.StringVar()
    ParentEntry = ttk.Combobox(InfoFrame1, textvariable=var, 
            value=(['正常', '离异单亲', '一方未健在', '双方未健在']), width=13, justify='center', state = 'readonly')
    ParentEntry.place(x=640, y=380)
    SiblingLabel = tk.Label(InfoFrame1, text='10. 独生情况：', font='宋体 13 bold', bg='white')
    SiblingLabel.place(x=870, y=380)
    var = tk.StringVar()
    SiblingEntry = ttk.Combobox(InfoFrame1, textvariable=var, 
            value=(['独生', '仅有弟弟或妹妹', '仅有哥哥或姐姐', '有多个兄弟姐妹']), width=15, justify='center', state = 'readonly')
    SiblingEntry.place(x=1000, y=380)
    # the forth line info 
    EducationLabel = tk.Label(InfoFrame1, text='11. 教育程度：', font='宋体 13 bold', bg='white')
    EducationLabel.place(x=220, y=460)
    var = tk.StringVar()
    EducationEntry = ttk.Combobox(InfoFrame1, textvariable=var, value=([str(i) for i in range(1,31,1)]), width=3, state = 'readonly')
    EducationEntry.place(x=350, y=460)
    EducationLabel_1 = tk.Label(InfoFrame1, text='年（按照小学5/6年制，初中3/4年制，高中(中专)3年制，大学4年制计算）', font='宋体 13 bold', bg='white')
    EducationLabel_1.place(x=400, y=460)
    # the fifth line info
    LocationLabel = tk.Label(InfoFrame1, text='12. 评估机构地点：', font='宋体 13 bold', bg='white')
    LocationLabel.place(x=220, y=540)
    var = tk.StringVar()
    LocationEntry = ttk.Combobox(InfoFrame1, textvariable=var, value=(['山东省精神卫生中心']), width=30, state = 'readonly')
    LocationEntry.place(x=400, y=540)
    HosIDLabel = tk.Label(InfoFrame1, text='13. 住院号/门诊号：', font='宋体 13 bold', bg='white')
    HosIDLabel.place(x=670, y=540)
    HosIDEntry = tk.Entry(InfoFrame1, width=30,  justify='center', )
    HosIDEntry.place(x=850, y=540)
    StartBtn = tk.Button(InfoFrame1, text='确定', font='宋体 13 bold',  command=Start, bg='WhiteSmoke', relief='ridge',)
    StartBtn.place(x=620, y=600)
    ExitBtn = tk.Button(InfoFrame1, text='退出', font='宋体 13 bold', command=on_closing, bg='WhiteSmoke', relief='ridge')
    ExitBtn.place(x=1100, y=600)
    tip = tk.Label(InfoFrame1, text='版权所有和解释权  @山东师范大学心理学院', font='宋体 10 ', bg='white')
    tip.place(x=500, y=690)
    MainWin.protocol('WM_DELETE_WINDOW', on_closing)

def MainWin2():
    global output_data, StartBtn,ExitBtn,InformBtn, MemoryBtn,RefuseBtn, SwitchBtn, \
    ConcentBtn,GuessingBtn,ExampleBtn,RefreshBtn,MainWin,scri_path, ico_path,InfoFrame1, NameLabel,\
    NameEntry,AgeLabel,YearEntry,MonthEntry,DayEntry,VerifyEntry, InstitutionEntry,\
    VerifyWin, ico_path, scri_path, GenderEntry, EthnicEntry, HeightEntry, WeightEntry,\
    HandEntry,HomeEntry, ParentEntry, SiblingEntry, EducationEntry, LocationEntry,\
    PSQIBtn,SpeakingBtn, InfoFrame2, InfoQues13Entry, InfoQues14Entry,InfoQues15_1Entry, InfoQues15_2Entry, \
    InfoQues16Entry,InfoQues17_1Entry, InfoQues17_2Entry, InfoQues18_1Entry, InfoQues18_2Entry, \
    InfoQues18_3Entry,InfoQues18_4Entry,InfoQues18_5Entry,InfoQues19Entry,InfoQues20_1Entry, InfoQues20_2Entry,\
    InfoQues21_1Entry, InfoQues21_2Entry, InfoQues21_3Entry, InitialFrame,start_time,\
    audio_recorder,video_recorder
    InfoFrame2 = tk.Frame(MainWin,width=1280, height=720, bg='white')
    InfoFrame2.pack()
    InfoFrame2_title = tk.Label(InfoFrame2, text='儿童青少年情绪状态精准识别',
                            font='黑体 23 bold', bg='white')
    InfoFrame2_title.place(x=350, y=50)
    sep_hor1 = ttk.Separator(InfoFrame2, orient='horizontal')
    sep_hor2 = ttk.Separator(InfoFrame2, orient='horizontal')
    sep_ver1 = ttk.Separator(InfoFrame2, orient='vertical')
    sep_ver2 = ttk.Separator(InfoFrame2, orient='vertical')
    sep_hor1.place(x=150, y=130, width=1000)
    sep_hor2.place(x=150, y=630, width=1000)
    sep_ver1.place(x=150, y=130, height=500)
    sep_ver2.place(x=1150, y=130, height=500)
    Title = tk.Label(InfoFrame2, text='信息登记', font='黑体 18 bold', bg='white')
    Title.place(x=590, y=140)
    Title_supplement = tk.Label(InfoFrame2, text='(非必填项)', font='黑体 15 bold', bg='white')
    Title_supplement.place(x=590, y=175)
    InfoQues13Label = tk.Label(InfoFrame2, text='13.近半年内，临床医生是否给予诊断如下心理问题:' ,font='宋体 13 bold', bg='white')
    InfoQues13Label.place(x=200, y=220)
    InfoQues13Entry= ttk.Combobox(InfoFrame2, value=(['不清楚/以下全无', '抑郁症','焦虑症','自闭症',
                '多动症','双相情感障碍','精神分裂症','强迫症','恐惧症','分离/转换障碍','创伤后应激障碍']), width=20, state = 'readonly', justify='center')
    InfoQues13Entry.place(x=630, y=220)
    InfoQues14Label = tk.Label(InfoFrame2, text='14.如有13项里的诊断，为首发还是复发:' ,font='宋体 13 bold', bg='white')
    InfoQues14Label.place(x=200, y=260)
    InfoQues14Entry= ttk.Combobox(InfoFrame2, textvariable=tk.StringVar(), value=(['无13项诊断','首发','复发']), 
                                  width=20, state = 'readonly', justify='center')
    InfoQues14Entry.place(x=540, y=260)
    InfoQues15_1Label = tk.Label(InfoFrame2, text='15.如有13项里的诊断，首发的年龄:                  岁                  个月' ,font='宋体 13 bold', bg='white')
    InfoQues15_1Label.place(x=200, y=300)
    InfoQues15_1Entry= ttk.Combobox(InfoFrame2, textvariable=tk.StringVar(), value=(['无13项诊断', '1', '2', '3', '4', 
        '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', 
        '15', '16', '17', '18', '19','20', '21', '22', '23', '24', '25']), 
        width=20, state = 'readonly', justify='center')
    InfoQues15_1Entry.place(x=510, y=300)
    InfoQues15_2Entry= ttk.Combobox(InfoFrame2, textvariable=tk.StringVar(), value=(['无13项诊断', '1', '2', '3', '4', 
        '5', '6', '7', '8', '9', '10', '11', '12']), 
        width=20, state = 'readonly', justify='center')
    InfoQues15_2Entry.place(x=710, y=300)
    InfoQues16Label = tk.Label(InfoFrame2, text='16. 如有13项里的诊断，复发的次数:' ,font='宋体 13 bold', bg='white')
    InfoQues16Label.place(x=200, y=340)
    InfoQues16Entry= ttk.Combobox(InfoFrame2, textvariable=tk.StringVar(), value=(['无13项诊断',  '0次',
        '1次', '2次', '3次', '4次']), width=20, state = 'readonly', justify='center')
    InfoQues16Entry.place(x=510, y=340)
    InfoQues17_1Label = tk.Label(InfoFrame2, text='17.除13项里的诊断外，共病类型还有: (1)                  (2)' ,font='宋体 13 bold', bg='white')
    InfoQues17_1Label.place(x=200, y=380)
    InfoQues17_1Entry= ttk.Combobox(InfoFrame2, textvariable=tk.StringVar(), value=(['不清楚/以下全无', '抑郁症','焦虑症','自闭症',
                '多动症','双相情感障碍','精神分裂症','强迫症','恐惧症','分离/转换障碍','创伤后应激障碍','睡眠障碍','社交恐惧']), width=20, state = 'readonly', justify='center')
    InfoQues17_1Entry.place(x=560, y=380)
    InfoQues17_2Entry= ttk.Combobox(InfoFrame2, textvariable=tk.StringVar(), value=(['不清楚/以下全无', '抑郁症','焦虑症','自闭症',
                '多动症','双相情感障碍','精神分裂症','强迫症','恐惧症','分离/转换障碍','创伤后应激障碍','睡眠障碍','社交恐惧']), width=20, state = 'readonly', justify='center')
    InfoQues17_2Entry.place(x=770, y=380)
    InfoQues18_1Label = tk.Label(InfoFrame2, text='18. 如有13项里的诊断，用药时长:               用药类型:(1)               (2)' ,font='宋体 13 bold', bg='white')
    InfoQues18_1Label.place(x=200, y=420)
    InfoQues18_1Entry= ttk.Combobox(InfoFrame2, textvariable=tk.StringVar(), value=(['无13项诊断',  
        '1个月', '2个月', '3个月', '4个月', '5个月', '6个月', '7个月', '8个月', '9个月', 
        '10个月', '11个月', '12个月', '13个月', '20个月', '15个月', '16个月', '17个月', 
        '18个月', '19个月', '20个月', '21个月', '22个月', '23个月', '24个月', 
        '大于24小于30','大于30小于36','大于36']), width=15, state = 'readonly', justify='center')
    InfoQues18_1Entry.place(x=500, y=420)
    InfoQues18_2Entry= ttk.Combobox(InfoFrame2, textvariable=tk.StringVar(), value=['无用药', '抗抑郁症药物', '抗焦虑症药物', '抗自闭症药物',
            '抗多动症药物', '抗双相情感障碍药物', '抗精神分裂症药物', '抗强迫症药物', '抗恐惧症药物', '抗分离/转换障碍药物', 
            '抗创伤后应激障碍药物'], width=18, state = 'readonly', justify='center')
    InfoQues18_2Entry.place(x=750, y=420)
    InfoQues18_3Entry= ttk.Combobox(InfoFrame2, textvariable=tk.StringVar(), value=['无用药', '抗抑郁症药物', '抗焦虑症药物', '抗自闭症药物',
            '抗多动症药物', '抗双相情感障碍药物', '抗精神分裂症药物', '抗强迫症药物', '抗恐惧症药物', '抗分离/转换障碍药物', 
            '抗创伤后应激障碍药物'], width=18, state = 'readonly', justify='center')
    InfoQues18_3Entry.place(x=930, y=420)
    InfoQues18_2Label = tk.Label(InfoFrame2, text='                                                    (3)               (4)' ,font='宋体 13 bold', bg='white')
    InfoQues18_2Label.place(x=200, y=460)
    InfoQues18_1Entry.place(x=500, y=420)
    InfoQues18_4Entry= ttk.Combobox(InfoFrame2, textvariable=tk.StringVar(), value=['无用药', '抗抑郁症药物', '抗焦虑症药物', '抗自闭症药物',
            '抗多动症药物', '抗双相情感障碍药物', '抗精神分裂症药物', '抗强迫症药物', '抗恐惧症药物', '抗分离/转换障碍药物', 
            '抗创伤后应激障碍药物'], width=18, state = 'readonly', justify='center')
    InfoQues18_4Entry.place(x=750, y=460)
    InfoQues18_5Entry= ttk.Combobox(InfoFrame2, textvariable=tk.StringVar(), value=['无用药', '抗抑郁症药物', '抗焦虑症药物', '抗自闭症药物',
            '抗多动症药物', '抗双相情感障碍药物', '抗精神分裂症药物', '抗强迫症药物', '抗恐惧症药物', '抗分离/转换障碍药物', 
            '抗创伤后应激障碍药物'], width=18, state = 'readonly', justify='center')
    InfoQues18_5Entry.place(x=930, y=460)
    InfoQues19Label = tk.Label(InfoFrame2, text='19. 半年前病史，临床医生是否给予诊断:' ,font='宋体 13 bold', bg='white')
    InfoQues19Label.place(x=200, y=500)
    InfoQues19Entry= ttk.Combobox(InfoFrame2, textvariable=tk.StringVar(), value=(['不清楚/以下全无', '抑郁症','焦虑症','自闭症',
        '多动症','双相情感障碍','精神分裂症','强迫症','恐惧症','分离/转换障碍','创伤后应激障碍']), width=20, state = 'readonly', justify='center')
    InfoQues19Entry.place(x=540, y=500)
    InfoQues20_1Label = tk.Label(InfoFrame2, text='20. 家族史，两系三代内血亲          是否有以下临床诊断:' ,font='宋体 13 bold', bg='white')
    InfoQues20_1Label.place(x=200, y=540)
    InfoQues20_1Entry= ttk.Combobox(InfoFrame2, textvariable=tk.StringVar(), value=(['无/不确定','爸爸','妈妈','爷爷','奶奶',
            '姥姥','姥爷','叔叔','伯伯','姑妈','姨妈','舅舅']), width=10, state = 'readonly', justify='center')
    InfoQues20_1Entry.place(x=440, y=540)
    InfoQues20_2Entry= ttk.Combobox(InfoFrame2, textvariable=tk.StringVar(), value=(['不清楚/以下全无', '抑郁症','焦虑症','自闭症',
        '多动症','双相情感障碍','精神分裂症','强迫症','恐惧症','药物滥用','分离/转换障碍','创伤后应激障碍']), width=20, state = 'readonly', justify='center')
    InfoQues20_2Entry.place(x=710, y=540)
    InfoQues21Label = tk.Label(InfoFrame2, text='21. 个人史，个人有以下行为:(1)               (2)               (3)' ,font='宋体 13 bold', bg='white')
    InfoQues21Label.place(x=200, y=580)
    InfoQues21_1Entry= ttk.Combobox(InfoFrame2,  value=(['不清楚/以下全无', '饮酒',
        '吸烟','休学','自伤','受到家长/监护人虐待','吸食毒品','遭霸凌']), width=18, 
        state = 'readonly', justify='center')
    InfoQues21_1Entry.place(x=480, y=580)
    InfoQues21_2Entry= ttk.Combobox(InfoFrame2,  value=(['不清楚/以下全无', '饮酒',
        '吸烟','休学','自伤','受到家长/监护人虐待','吸食毒品','遭霸凌']), width=18, 
        state = 'readonly', justify='center')
    InfoQues21_2Entry.place(x=660, y=580)
    InfoQues21_3Entry= ttk.Combobox(InfoFrame2,  value=(['不清楚/以下全无', '饮酒',
        '吸烟','休学','自伤','受到家长/监护人虐待','吸食毒品','遭霸凌']), width=18, 
        state = 'readonly', justify='center')
    InfoQues21_3Entry.place(x=840, y=580)
    StartBtn = tk.Button(InfoFrame2, text='确定', font='宋体 13 bold',  command=StartFrame2, bg='WhiteSmoke', relief='ridge',)
    StartBtn.place(x=620, y=640)
    ExitBtn = tk.Button(InfoFrame2, text='退出', font='宋体 13 bold', command=on_closing, bg='WhiteSmoke', relief='ridge')
    ExitBtn.place(x=1100, y=640)
    tip = tk.Label(InfoFrame2, text='版权所有和解释权  @山东师范大学心理学院', font='宋体 10 ', bg='white')
    tip.place(x=500, y=690)


# PLE
def PLEYesBtnClick():
    global PLEIndex, PLEQuestions, PLEYesBtn, PLENoBtn, PLEDistressBtn1,\
    PLEDistressBtn2, PLEDistressBtn3, PLEDistressBtn4, PLEDistressBtn5,\
    output_data, QuestionLabel1
    PLEYesBtn.config(state='disabled')
    PLENoBtn.config(state='disabled')
    PLEDistressBtn1.config(state='normal')
    PLEDistressBtn2.config(state='normal')
    PLEDistressBtn3.config(state='normal')
    PLEDistressBtn4.config(state='normal')
    PLEDistressBtn5.config(state='normal') 
    log_activity(activity_log='the users select "YES" facing the PLE question-{} :{}'.format(PLEIndex+1,PLEQuestions.loc[PLEIndex, 'question']))
    if PLEIndex < 20:
        output_data.loc[PLEQuestions.loc[PLEIndex, 'index'], 'answer'] = 1
        output_data.loc[PLEQuestions.loc[PLEIndex, 'index'], 'question'] = PLEQuestions.loc[PLEIndex, 'question']
        output_data.loc[PLEQuestions.loc[PLEIndex, 'index'], 'sequence'] = PLEIndex+1
    elif PLEIndex == 20:
        output_data.loc[PLEQuestions.loc[PLEIndex, 'index'], 'answer'] = 1
        output_data.loc[PLEQuestions.loc[PLEIndex, 'index'], 'question'] = PLEQuestions.loc[PLEIndex, 'question']
        output_data.loc[PLEQuestions.loc[PLEIndex, 'index'], 'sequence'] = PLEIndex+1

def PLENoBtnClick():
    global PLEIndex, PLEQuestions, PLEYesBtn, PLENoBtn, PLEDistressBtn1,\
    PLEDistressBtn2, PLEDistressBtn3, PLEDistressBtn4, PLEDistressBtn5,\
    output_data, TestProgressor, QuestionIndex, PLEFrame2, PLEBtn
    log_activity(activity_log='the users select "No" facing the PLE question-{} :{}'.format(PLEIndex+1,PLEQuestions.loc[PLEIndex, 'question']))
    if PLEIndex <20:
        output_data.loc[PLEQuestions.loc[PLEIndex, 'index'], 'answer'] = 0
        output_data.loc[PLEQuestions.loc[PLEIndex, 'index'], 'question'] = PLEQuestions.loc[PLEIndex, 'question']
        output_data.loc[PLEQuestions.loc[PLEIndex, 'index'], 'sequence'] = PLEIndex+1
        output_data.loc[PLEQuestions.loc[PLEIndex+21, 'index'], 'answer'] = 0
        output_data.loc[PLEQuestions.loc[PLEIndex+21, 'index'], 'question'] = PLEQuestions.loc[PLEIndex+21, 'question']
        output_data.loc[PLEQuestions.loc[PLEIndex+21, 'index'], 'sequence'] = PLEIndex+1
        PLEIndex += 1
        QuestionLabel1.config(text='{}.{}'.format(PLEIndex+1,PLEQuestions.loc[PLEIndex, 'question']))
        TestProgressor.config(value=PLEIndex+1)
        PLEFrame2.update()
    elif PLEIndex == 20:
        output_data.loc[PLEQuestions.loc[PLEIndex, 'index'], 'answer'] = 0
        output_data.loc[PLEQuestions.loc[PLEIndex, 'index'], 'question'] = PLEQuestions.loc[PLEIndex, 'question']
        output_data.loc[PLEQuestions.loc[PLEIndex, 'index'], 'sequence'] = PLEIndex+1
        output_data.loc[PLEQuestions.loc[PLEIndex+21, 'index'], 'answer'] = 0
        output_data.loc[PLEQuestions.loc[PLEIndex+21, 'index'], 'question'] = PLEQuestions.loc[PLEIndex+21, 'question']
        output_data.loc[PLEQuestions.loc[PLEIndex+21, 'index'], 'sequence'] = PLEIndex+1
        output_data.to_csv('./result/'+str(dirname)+'/'+str(dirname)+'_PLE.csv', encoding='GBK')
        PLEWin.destroy()
        messagebox.showinfo('评估结束','精神状况评估结束，请点击“3.情绪评估”继续测评！')
        PLETestBtn.config(text='已完成精神状况评估')
        PLETestBtn.config(state='disabled')
        SpeakingBtn.config(state='normal')
        JsonDict['PLE'] = 1
        log_activity(activity_log='the PLE questionnaire has been finished.')
 
def PLEDistressBtn1Click():
    global PLEIndex, PLEQuestions, PLEYesBtn, PLENoBtn, PLEDistressBtn1,\
    PLEDistressBtn2, PLEDistressBtn3, PLEDistressBtn4, PLEDistressBtn5,\
    output_data, TestProgressor, QuestionIndex, PLEFrame2, PLEBtn
    log_activity(activity_log='the users select "Distress1（没有影响）" after select "YES" facing the PLE question-{} :{}'.format(PLEIndex+1,PLEQuestions.loc[PLEIndex, 'question']))
    if PLEIndex < 20:
        PLEYesBtn.config(state='normal')
        PLENoBtn.config(state='normal')
        PLEDistressBtn1.config(state='disabled')
        PLEDistressBtn2.config(state='disabled')
        PLEDistressBtn3.config(state='disabled')
        PLEDistressBtn4.config(state='disabled')
        PLEDistressBtn5.config(state='disabled') 
        output_data.loc[PLEQuestions.loc[PLEIndex+21, 'index'], 'answer'] = 2
        output_data.loc[PLEQuestions.loc[PLEIndex+21, 'index'], 'question'] = PLEQuestions.loc[PLEIndex+21, 'question']
        output_data.loc[PLEQuestions.loc[PLEIndex+21, 'index'], 'sequence'] = PLEIndex+1
        PLEIndex += 1
        QuestionLabel1.config(text='{}.{}'.format(PLEIndex+1,PLEQuestions.loc[PLEIndex, 'question']))
        TestProgressor.config(value=PLEIndex+1)
        PLEFrame2.update()
    else:
        output_data.loc[PLEQuestions.loc[PLEIndex+21, 'index'], 'answer'] = 2
        output_data.loc[PLEQuestions.loc[PLEIndex+21, 'index'], 'question'] = PLEQuestions.loc[PLEIndex+21, 'question']
        output_data.loc[PLEQuestions.loc[PLEIndex+21, 'index'], 'sequence'] = PLEIndex+1
        output_data.to_csv('./result/'+str(dirname)+'/'+str(dirname)+'_PLE.csv', encoding='GBK')
        PLEWin.destroy()
        messagebox.showinfo('评估结束','精神状况评估结束，请点击“3.情绪评估”继续测评！')
        PLETestBtn.config(text='已完成精神状况评估')
        PLETestBtn.config(state='disabled')
        SpeakingBtn.config(state='normal')
        JsonDict['PLE'] = 1
        log_activity(activity_log='the PLE questionnaire has been finished.')

def PLEDistressBtn2Click():
    global PLEIndex, PLEQuestions, PLEYesBtn, PLENoBtn, PLEDistressBtn1,\
    PLEDistressBtn2, PLEDistressBtn3, PLEDistressBtn4, PLEDistressBtn5,\
    output_data, TestProgressor, QuestionIndex, PLEFrame2, PLEBtn
    log_activity(activity_log='the users select "Distress2（轻微影响）" after select "YES" facing the PLE question-{} :{}'.format(PLEIndex+1,PLEQuestions.loc[PLEIndex, 'question']))
    if PLEIndex < 20:
        PLEYesBtn.config(state='normal')
        PLENoBtn.config(state='normal')
        PLEDistressBtn1.config(state='disabled')
        PLEDistressBtn2.config(state='disabled')
        PLEDistressBtn3.config(state='disabled')
        PLEDistressBtn4.config(state='disabled')
        PLEDistressBtn5.config(state='disabled') 
        output_data.loc[PLEQuestions.loc[PLEIndex+21, 'index'], 'answer'] = 3
        output_data.loc[PLEQuestions.loc[PLEIndex+21, 'index'], 'question'] = PLEQuestions.loc[PLEIndex+21, 'question']
        output_data.loc[PLEQuestions.loc[PLEIndex+21, 'index'], 'sequence'] = PLEIndex+1
        PLEIndex += 1
        QuestionLabel1.config(text='{}.{}'.format(PLEIndex+1,PLEQuestions.loc[PLEIndex, 'question']))
        TestProgressor.config(value=PLEIndex+1)
        PLEFrame2.update()
    else:
        output_data.loc[PLEQuestions.loc[PLEIndex+21, 'index'], 'answer'] = 3
        output_data.loc[PLEQuestions.loc[PLEIndex+21, 'index'], 'question'] = PLEQuestions.loc[PLEIndex+21, 'question']
        output_data.loc[PLEQuestions.loc[PLEIndex+21, 'index'], 'sequence'] = PLEIndex+1
        output_data.to_csv('./result/'+str(dirname)+'/'+str(dirname)+'_PLE.csv', encoding='GBK')
        PLEWin.destroy()
        messagebox.showinfo('评估结束','精神状况评估结束，请点击“3.情绪评估”继续测评！')
        PLETestBtn.config(text='已完成精神状况评估')
        PLETestBtn.config(state='disabled')
        SpeakingBtn.config(state='normal')
        JsonDict['PLE'] = 1
        log_activity(activity_log='the PLE questionnaire has been finished.')

def PLEDistressBtn3Click():
    global PLEIndex, PLEQuestions, PLEYesBtn, PLENoBtn, PLEDistressBtn1,\
    PLEDistressBtn2, PLEDistressBtn3, PLEDistressBtn4, PLEDistressBtn5,\
    output_data, TestProgressor, QuestionIndex, PLEFrame2, PLEBtn
    log_activity(activity_log='the users select "Distress3（中等影响）" after select "YES" facing the PLE question-{} :{}'.format(PLEIndex+1,PLEQuestions.loc[PLEIndex, 'question']))
    if PLEIndex < 20:
        PLEYesBtn.config(state='normal')
        PLENoBtn.config(state='normal')
        PLEDistressBtn1.config(state='disabled')
        PLEDistressBtn2.config(state='disabled')
        PLEDistressBtn3.config(state='disabled')
        PLEDistressBtn4.config(state='disabled')
        PLEDistressBtn5.config(state='disabled') 
        output_data.loc[PLEQuestions.loc[PLEIndex+21, 'index'], 'answer'] = 4
        output_data.loc[PLEQuestions.loc[PLEIndex+21, 'index'], 'question'] = PLEQuestions.loc[PLEIndex+21, 'question']
        output_data.loc[PLEQuestions.loc[PLEIndex+21, 'index'], 'sequence'] = PLEIndex+1
        PLEIndex += 1
        QuestionLabel1.config(text='{}.{}'.format(PLEIndex+1,PLEQuestions.loc[PLEIndex, 'question']))
        TestProgressor.config(value=PLEIndex+1)
        PLEFrame2.update()
    else:
        output_data.loc[PLEQuestions.loc[PLEIndex+21, 'index'], 'answer'] = 4
        output_data.loc[PLEQuestions.loc[PLEIndex+21, 'index'], 'question'] = PLEQuestions.loc[PLEIndex+21, 'question']
        output_data.loc[PLEQuestions.loc[PLEIndex+21, 'index'], 'sequence'] = PLEIndex+1
        output_data.to_csv('./result/'+str(dirname)+'/'+str(dirname)+'_PLE.csv', encoding='GBK')
        PLEWin.destroy()
        messagebox.showinfo('评估结束','精神状况评估结束，请点击“3.情绪评估”继续测评！')
        PLETestBtn.config(text='已完成精神状况评估')
        PLETestBtn.config(state='disabled')
        SpeakingBtn.config(state='normal')
        JsonDict['PLE'] = 1
        log_activity(activity_log='the PLE questionnaire has been finished.')

def PLEDistressBtn4Click():
    global PLEIndex, PLEQuestions, PLEYesBtn, PLENoBtn, PLEDistressBtn1,\
    PLEDistressBtn2, PLEDistressBtn3, PLEDistressBtn4, PLEDistressBtn5,\
    output_data, TestProgressor, QuestionIndex, PLEFrame2, PLEBtn
    log_activity(activity_log='the users select "Distress4（较严重影响）" after select "YES" facing the PLE question-{} :{}'.format(PLEIndex+1,PLEQuestions.loc[PLEIndex, 'question']))
    if PLEIndex < 20:
        PLEYesBtn.config(state='normal')
        PLENoBtn.config(state='normal')
        PLEDistressBtn1.config(state='disabled')
        PLEDistressBtn2.config(state='disabled')
        PLEDistressBtn3.config(state='disabled')
        PLEDistressBtn4.config(state='disabled')
        PLEDistressBtn5.config(state='disabled') 
        output_data.loc[PLEQuestions.loc[PLEIndex+21, 'index'], 'answer'] = 5
        output_data.loc[PLEQuestions.loc[PLEIndex+21, 'index'], 'question'] = PLEQuestions.loc[PLEIndex+21, 'question']
        output_data.loc[PLEQuestions.loc[PLEIndex+21, 'index'], 'sequence'] = PLEIndex+1
        PLEIndex += 1
        QuestionLabel1.config(text='{}.{}'.format(PLEIndex+1,PLEQuestions.loc[PLEIndex, 'question']))
        TestProgressor.config(value=PLEIndex+1)
        PLEFrame2.update()
    else:
        output_data.loc[PLEQuestions.loc[PLEIndex+21, 'index'], 'answer'] = 5
        output_data.loc[PLEQuestions.loc[PLEIndex+21, 'index'], 'question'] = PLEQuestions.loc[PLEIndex+21, 'question']
        output_data.loc[PLEQuestions.loc[PLEIndex+21, 'index'], 'sequence'] = PLEIndex+1
        output_data.to_csv('./result/'+str(dirname)+'/'+str(dirname)+'_PLE.csv', encoding='GBK')
        PLEWin.destroy()
        messagebox.showinfo('评估结束','精神状况评估结束，请点击“3.情绪评估”继续测评！')
        PLETestBtn.config(text='已完成精神状况评估')
        PLETestBtn.config(state='disabled')
        SpeakingBtn.config(state='normal')
        JsonDict['PLE'] = 1
        log_activity(activity_log='the PLE questionnaire has been finished.')

def PLEDistressBtn5Click():
    global PLEIndex, PLEQuestions, PLEYesBtn, PLENoBtn, PLEDistressBtn1,\
    PLEDistressBtn2, PLEDistressBtn3, PLEDistressBtn4, PLEDistressBtn5,\
    output_data, TestProgressor, QuestionIndex, PLEFrame2, PLEBtn
    log_activity(activity_log='the users select "Distress5（严重影响）" after select "YES" facing the PLE question-{} :{}'.format(PLEIndex+1,PLEQuestions.loc[PLEIndex, 'question']))
    if PLEIndex < 20:
        PLEYesBtn.config(state='normal')
        PLENoBtn.config(state='normal')
        PLEDistressBtn1.config(state='disabled')
        PLEDistressBtn2.config(state='disabled')
        PLEDistressBtn3.config(state='disabled')
        PLEDistressBtn4.config(state='disabled')
        PLEDistressBtn5.config(state='disabled') 
        output_data.loc[PLEQuestions.loc[PLEIndex+21, 'index'], 'answer'] = 6
        output_data.loc[PLEQuestions.loc[PLEIndex+21, 'index'], 'question'] = PLEQuestions.loc[PLEIndex+21, 'question']
        output_data.loc[PLEQuestions.loc[PLEIndex+21, 'index'], 'sequence'] = PLEIndex+1
        PLEIndex += 1
        QuestionLabel1.config(text='{}.{}'.format(PLEIndex+1,PLEQuestions.loc[PLEIndex, 'question']))
        TestProgressor.config(value=PLEIndex+1)
        PLEFrame2.update()
    else:
        output_data.loc[PLEQuestions.loc[PLEIndex+21, 'index'], 'answer'] = 6
        output_data.loc[PLEQuestions.loc[PLEIndex+21, 'index'], 'question'] = PLEQuestions.loc[PLEIndex+21, 'question']
        output_data.loc[PLEQuestions.loc[PLEIndex+21, 'index'], 'sequence'] = PLEIndex+1
        output_data.to_csv('./result/'+str(dirname)+'/'+str(dirname)+'_PLE.csv', encoding='GBK')
        PLEWin.destroy()
        messagebox.showinfo('评估结束','精神状况评估结束，请点击“3.情绪评估”继续测评！')
        PLETestBtn.config(text='已完成精神状况评估')
        PLETestBtn.config(state='disabled')
        SpeakingBtn.config(state='normal')
        JsonDict['PLE'] = 1
        log_activity(activity_log='the PLE questionnaire has been finished.')

def PLEBtnClick():
    global waittime, PLEYesBtn, QuestionLabel1, QuestionLabel2,PLEDistressBtn1,\
            PLEDistressBtn2, PLEDistressBtn3, PLEDistressBtn4, PLEDistressBtn5,\
            PLENoBtn, PLEIndex, PLEQuestions, TestProgressor, QuestionIndex, PLEFrame2
    waittime = 10
    PLEFrame1.destroy()
    PLEQuestions = pd.read_csv(scri_path+'/material/PLE.csv', encoding='GBK',) 
    PLEIndex = 0
    PLEFrame2 = tk.Frame(PLEWin, width=1280, height=720, bg='white')
    PLEFrame2.pack()
    QuestionLabel1 = tk.Label(PLEFrame2, font='宋体 18 bold', width=100,wraplength=1000, justify='left', 
                              text='1.'+PLEQuestions.loc[PLEIndex, 'question'], bg='white')
    QuestionLabel1.place(relx=0, rely=0.15)
    PLEYesBtn = tk.Button(PLEFrame2, text='是', font='宋体 20 bold', width=10, command=PLEYesBtnClick, bg='WhiteSmoke', relief='ridge')
    PLEYesBtn.place(relx=0.3, rely=0.3)
    PLENoBtn = tk.Button(PLEFrame2, text='否', font='宋体 20 bold',  width=10, command=PLENoBtnClick, bg='WhiteSmoke', relief='ridge')
    PLENoBtn.place(relx=0.5, rely=0.3)
    QuestionLabel2 = tk.Label(PLEFrame2, font='宋体 18 bold', width=100,wraplength=1000, justify='left', 
                              text='如果有，这种情况对您的困扰程度', bg='white')
    QuestionLabel2.place(relx=0, rely=0.45)
    PLEDistressBtn1 = tk.Button(PLEFrame2, text='没有', font='宋体 20 bold', state='disabled', width=10,
                                command=PLEDistressBtn1Click, bg='WhiteSmoke', relief='ridge')
    PLEDistressBtn1.place(relx=0.05, rely=0.55)
    PLEDistressBtn2 = tk.Button(PLEFrame2, text='轻微', font='宋体 20 bold', state='disabled', width=10,
                                command=PLEDistressBtn2Click, bg='WhiteSmoke', relief='ridge')
    PLEDistressBtn2.place(relx=0.25, rely=0.55)
    PLEDistressBtn3 = tk.Button(PLEFrame2, text='中等', font='宋体 20 bold', state='disabled', width=10,
                                command=PLEDistressBtn3Click, bg='WhiteSmoke', relief='ridge')
    PLEDistressBtn3.place(relx=0.45, rely=0.55)
    PLEDistressBtn4 = tk.Button(PLEFrame2, text='较严重', font='宋体 20 bold', state='disabled', width=10,
                                command=PLEDistressBtn4Click, bg='WhiteSmoke', relief='ridge')
    PLEDistressBtn4.place(relx=0.65, rely=0.55)
    PLEDistressBtn5 = tk.Button(PLEFrame2, text='严重', font='宋体 20 bold', state='disabled', width=10,
                                command=PLEDistressBtn5Click, bg='WhiteSmoke', relief='ridge')
    PLEDistressBtn5.place(relx=0.85, rely=0.55)
    log_activity(activity_log='start PLE test and show the PLE-1 question {}'.format(PLEQuestions.loc[PLEIndex, 'question']))
    TestProgressor = ttk.Progressbar(PLEFrame2, orient='horizontal', mode='determinate',
                                        length=1000, maximum=21, value=PLEIndex+1)
    TestProgressor.place(relx=0.1, rely=0.8)
    tip = tk.Label(PLEFrame2, text='版权所有和解释权  @山东师范大学心理学院', font='宋体 10 ', bg='white')
    tip.place(x=500, y=690)
    PLEWin.mainloop()

def timer_handler_PLE():
        global waittime, PLEBtn
        if waittime > 0:
            PLEWin.protocol('WM_DELETE_WINDOW', False)
            PLEFrame1.after(1000, timer_handler_PLE)
            waittime-=1
            PLEBtn['text'] = '已清楚要求，开始参与评估('+str(waittime)+'秒)'
        else:
            log_activity(activity_log='config the state of PLEBtn from "disabled" to "normal" which allow to start PLE')
            # SpeakingWin1.protocol('WM_DELETE_WINDOW', True)
            PLEBtn['text'] = '已清楚要求，开始参与评估'
            PLEBtn.config(state='normal')

def PLEInstruction():
    global PLEWin, PLEFrame1, PLEBtn, waittime
    PLEWin = tk.Toplevel(MainWin)
    PLEWin.resizable(False,False)
    PLEFrame1 = tk.Frame(PLEWin, width=1280, height=720, bg='white')
    PLEFrame1.pack()
    PLEtile = tk.Label(PLEFrame1, text='2.精神状况评估', font='黑体 25 bold', bg='white')
    PLEtile.place(relx=0.45, rely=0.1)
    f = open(scri_path+"/material/PLETestInstruction.txt", "r", encoding='utf-8')
    PLEInstruc =  f.read()
    f.close()
    SpeakingInstruc1Text = tk.Label(PLEFrame1, text=PLEInstruc, font='宋体 18 bold', 
                                    justify='left', wraplength=900, width=90, bg='white')
    SpeakingInstruc1Text.place(x=70, y=180)
    sep_hor1 = ttk.Separator(PLEFrame1, orient='horizontal')
    sep_hor2 = ttk.Separator(PLEFrame1, orient='horizontal')
    sep_ver1 = ttk.Separator(PLEFrame1, orient='vertical')
    sep_ver2 = ttk.Separator(PLEFrame1, orient='vertical')
    sep_hor1.place(x=150, y=130, width=1000)
    sep_hor2.place(x=150, y=630, width=1000)
    sep_ver1.place(x=150, y=130, height=500)
    sep_ver2.place(x=1150, y=130, height=500) 
    log_activity(activity_log='show the instruction of PLE')
    PLEBtn = tk.Button(PLEFrame1, text='已清楚要求，开始参与评估(10秒)', width=35, font='宋体 15 bold', bg='WhiteSmoke', 
                        relief='ridge', command=PLEBtnClick, state='disabled')
    PLEBtn.place(x=500, y=550)
    PLEFrame1.after(1000, timer_handler_PLE)
    waittime = 10

def MainWin3():
    global output_data, StartBtn,ExitBtn,InformBtn, MemoryBtn,RefuseBtn, SwitchBtn, \
    ConcentBtn,GuessingBtn,ExampleBtn,RefreshBtn,MainWin,scri_path, ico_path,InfoFrame1, NameLabel,\
    NameEntry,AgeLabel,YearEntry,MonthEntry,DayEntry,VerifyEntry, InstitutionEntry,\
    VerifyWin, ico_path, scri_path, GenderEntry, EthnicEntry, HeightEntry, WeightEntry,\
    HandEntry,HomeEntry, ParentEntry, SiblingEntry, EducationEntry, LocationEntry,\
    PSQIBtn,SpeakingBtn, InfoFrame2, InfoQues13Entry, InfoQues14Entry,InfoQues15_1Entry, InfoQues15_2Entry, \
    InfoQues16Entry,InfoQues17_1Entry, InfoQues17_2Entry, InfoQues18_1Entry, InfoQues18_2Entry, \
    InfoQues18_3Entry,InfoQues19Entry,InfoQues20_1Entry, InfoQues20_2Entry, InitialFrame,start_time,\
    audio_recorder,video_recorder, PLETestBtn

    # create the main frame
    # creat a infomation frame/cavans
    InitialFrame = tk.Frame(MainWin,width=1280, height=720, bg='white')
    InitialFrame.pack()
    InitialFrame_title = tk.Label(InitialFrame, text='儿童青少年情绪状态精准识别', font='黑体 25 bold', bg='white')
    InitialFrame_title.place(x=350, y=50)
    sep_hor1 = ttk.Separator(InitialFrame, orient='horizontal')
    sep_hor2 = ttk.Separator(InitialFrame, orient='horizontal')
    sep_ver1 = ttk.Separator(InitialFrame, orient='vertical')
    sep_ver2 = ttk.Separator(InitialFrame, orient='vertical') 
    sep_hor1.place(x=150, y=130, width=1000) 
    sep_hor2.place(x=150, y=630, width=1000) 
    sep_ver1.place(x=150, y=130, height=500) 
    sep_ver2.place(x=1150, y=130, height=500) 
    InformBtn = tk.Button(InitialFrame, text='评估须知', bg='DarkSeaGreen', height=1,
                        width=20, font='宋体 20 bold', command=InformShow)
    InformBtn.place(x=500, y=180, )
    PSQIBtn = tk.Button(InitialFrame, text='1.睡眠评估', bg='LightSteelBlue', width=20, height=1,
                        font='宋体 20 bold', state='disabled', command=PSQI)
    PSQIBtn.place(x=500, y=300,)
    PLETestBtn = tk.Button(InitialFrame, text='2.精神状况评估', bg='LightSteelBlue', width=20, height=1,
                        font='宋体   20 bold', state='disabled', command=PLEInstruction)
    PLETestBtn.place(x=500, y=420,)
    SpeakingBtn = tk.Button(InitialFrame, text='3.情绪评估', state='disabled',bg='LightSteelBlue', height=1,
                        width=20, font='宋体 20 bold', command=SpeakingTest)
    SpeakingBtn.place(x=500, y=540, )
    RefreshBtn = tk.Button(InitialFrame, text='Refresh', font='宋体 13 bold', command= Refresh )
    RefreshBtn.place(x=150, y=600)
    ExitBtn = tk.Button(InitialFrame, text='退出', font='宋体 13 bold', command=on_closing )
    ExitBtn.place(x=1100, y=600)
    tip = tk.Label(InitialFrame, text='版权所有和解释权  @山东师范大学心理学院', font='宋体 10 ', bg='white')
    tip.place(x=500, y=690)
    MainWin.protocol('WM_DELETE_WINDOW', on_closing)
    MainWin.mainloop()

if __name__ == '__main__':
    main()
