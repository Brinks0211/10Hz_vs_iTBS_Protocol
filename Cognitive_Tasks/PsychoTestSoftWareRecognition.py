'''
青少年问卷评估测试
author: Zhang Yihao
Time: 2024/0326
'''

# import the third pypi
import tkinter as tk
import subprocess
import datetime
import sys
import numpy as np
import pandas as pd
import os
import time
import json
from PIL import Image, ImageTk
from tkinter import messagebox
from pypinyin import pinyin
from moviepy.editor import VideoFileClip
from BART import BART
from psychopy import visual, event, core, data, gui, logging
from PicNback import PicNback
from Wisconsin import Wisconsin
from tkinter import messagebox
from tkinter import ttk
from pypinyin import pinyin


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
            #messagebox.showinfo('使用提示','该软件仅限2024年12月31日可用，继续使用请联系开发者！')
            VerifyWin.destroy()
            MainWin0()
        else: 
            messagebox.showinfo('过期提示','该软件仅限2050年12月31日可用，继续使用请联系开发者！')
            VerifyWin.destroy()
            audio_recorder.stop_recording('temp.wav')
            video_recorder.stop_recording('temp.avi')
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

# exit confirm
def on_closing():
    global dirname, audio_recorder,scri_path,video_recorder
    if messagebox.askokcancel("Quit", "您确定想要退出吗？"):
        log_activity(activity_log='Exit the recognition test')
        save_to_json('./json/'+'/'+str(dirname)+'.json', JsonDict)
        save_to_json('./result/{}/{}.json'.format(str(dirname), str(dirname)), JsonDict)
        sys.exit()

# exit confirm
def ExitInformWin():
    global  InformFrame, waittime
    log_activity(activity_log='exit the paradigm because of refusing the inform consent')
    InformWin.destroy()
    # InformBtn.config('disable')
    # waittime = 1
    waittime = 10

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
    if messagebox.showinfo('提示', '您已同意参加评估，请点击‘1.记忆评估’。') :
        TestSwitch = 1
        InformWin.destroy()
        PicNbackBtn.config(state='normal') 
        InformBtn.config(state='disabled')
        InformBtn.config(text='已签订知情同意书')
        PicNbackBtn.config(state='normal')
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
                        '2、本评估共计3个部分，约20分钟时间（记忆评估：5分钟；脑灵活性评估：5分钟；冒险性评估：7分钟）。',
                        '3、本评估3个部分，请按顺序完成每个部分。',
                        '4、每个部分开始前，我们都提供了书面或者视频指导，请您认真观看。',
                        '5、本评估需要您带上耳机或者在安静的环境内完成。',
                        '6、在评估过程中，请您正对电脑屏幕，端正坐姿，保持与电脑屏幕摄像头并行。']
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

def Verify():
    global output_data, StartBtn,ExitBtn,InformBtn, MemoryBtn,RefuseBtn, SwitchBtn, \
    ConcentBtn,GuessingBtn,ExampleBtn,RefreshBtn,MainWin,scri_path, ico_path,InfoFrame1, NameLabel,\
    NameEntry,AgeLabel,YearEntry,MonthEntry,DayEntry,VerifyEntry, InstitutionEntry,\
    VerifyWin, ico_path, scri_path,InitialFrame,start_time,RecordTimeStr,\
    audio_recorder,video_recorder, HosIDEntry, cap, fps, delay_between_frames, video_panel,\
    VideoFrame, IsRunning, audio_source, VideoPanel

    start_time = datetime.datetime.now()
    scri_path = os.getcwd()
    ico_path = scri_path+'/material/logo.ico'
    # creat a Dataframe
    # start record video & audio
    # audio_recorder = RecordAudio.AudioRecorder()
    # video_recorder = RecordVideo.VideoRecorder()
    # audio_recorder.start_recording()  
    # video_recorder.start_recording()
    RecordTime = datetime.datetime.now() - start_time
    RecordTimeStr = f"{RecordTime.total_seconds():.2f} seconds"
    # verifywin
    VerifyWin = tk.Tk()
    # set geometry and location
    VerifyWin.iconbitmap(ico_path)
    VerifyWin.wm_iconbitmap(ico_path)
    VerifyWin.title('儿童青少年认知能力识别')
    VerifyWin.config(bg='white')
    VerifyWin.geometry('1280x720')
    VerifyWin.resizable(False, False)
    # set seperator
    VerifyWin_title = tk.Label(VerifyWin, text='儿童青少年认知能力识别', font='黑体 25 bold', bg='white')
    VerifyWin_title.place(x=470, y=50)
    sep_hor1 = ttk.Separator(VerifyWin, orient='horizontal')
    sep_hor2 = ttk.Separator(VerifyWin, orient='horizontal')
    sep_ver1 = ttk.Separator(VerifyWin, orient='vertical')
    sep_ver2 = ttk.Separator(VerifyWin, orient='vertical')
    sep_hor1.place(x=150, y=130, width=1000)
    sep_hor2.place(x=150, y=630, width=1000)
    sep_ver1.place(x=150, y=130, height=500)
    sep_ver2.place(x=1150, y=130, height=500)
    welcome = tk.Label(VerifyWin, text='欢迎使用儿童青少年认知能力识别软件', font='宋体 20 ', bg='white')
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

# save parameters
def Para():
    global dirname, scri_path, name, name_pinyin, gender, birthtime, time, age, ParaList,JsonDict,\
    HosID
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
    JsonDict = {'Name': name_pinyin, 'NameReport':name,'TimeRecog': time, 'Birth':birthtime,'Gender':gender, 'Age':age,
                'HosID':HosID, 'PicNback':0, 'Wisconsin':0, 'BART':0, }
    save_to_json('./json/'+'/'+str(dirname)+'.json', JsonDict)
    save_to_json('./result/{}/{}.json'.format(str(dirname), str(dirname)), JsonDict)

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
    institution = LocationEntry.get()
    output_data.loc['institution', 'answer'] = institution
    HosID = HosIDEntry.get()
    output_data.loc['HosID', 'answer'] = HosID
    SuperViseList = ['name', 'name_pinyin', 'year', 'month', 
                     'day', 'gender','institution', 'HosID']
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
        MainWin1()

def MainWin0():
    global output_data, StartBtn,ExitBtn,InformBtn, MemoryBtn,RefuseBtn, SwitchBtn, \
    ConcentBtn,GuessingBtn,ExampleBtn,RefreshBtn,MainWin,scri_path, ico_path,InfoFrame1, InitialFrame,start_time,\
    NameEntry, YearEntry, MonthEntry, DayEntry, GenderEntry, LocationEntry, HosIDEntry,\
    audio_recorder,video_recorder, HosIDEntry, cap, fps, delay_between_frames, video_panel,\
    VideoFrame
    # set geometry and location
    MainWin = tk.Tk()
    MainWin.config(background='white')
    MainWin.title('儿童青少年认知能力评估')
    MainWin.geometry('1280x720')
    MainWin.resizable(False, False)
    # creat a infomation frame/cavans
    output_data = pd.DataFrame(columns=['answer', 'question','sequence','read'],
                               index = ['name', 'name_pinyin', 'year', 'month', 
                     'day', 'age', 'gender','institution', 'HosID'])
    InfoFrame1 = tk.Frame(MainWin,width=1280, height=720, bg='white')
    InfoFrame1.pack()
    InfoFrame1_title = tk.Label(InfoFrame1, text='儿童青少年认知能力评估',
                            font='黑体 23 bold', bg='white')
    InfoFrame1_title.place(x=450, y=50)
    sep_hor1 = ttk.Separator(InfoFrame1, orient='horizontal')
    sep_hor2 = ttk.Separator(InfoFrame1, orient='horizontal')
    sep_ver1 = ttk.Separator(InfoFrame1, orient='vertical')
    sep_ver2 = ttk.Separator(InfoFrame1, orient='vertical')
    sep_hor1.place(x=150, y=130, width=1000)
    sep_hor2.place(x=150, y=630, width=1000)
    sep_ver1.place(x=150, y=130, height=500)
    sep_ver2.place(x=1150, y=130, height=500)
    Title = tk.Label(InfoFrame1, text='信息登记', font='黑体 20 bold', bg='white')
    Title.place(x=590, y=140)
    Title_supplement = tk.Label(InfoFrame1, text='(必填项)', font='黑体 15 bold', bg='white')
    Title_supplement.place(x=600, y=175)
    # the first line info
    NameLabel = tk.Label(InfoFrame1, text='1. 姓名/昵称：', font='宋体 18 bold', bg='white')
    NameLabel.place(x=350, y=220)
    NameEntry = tk.Entry(InfoFrame1, width=15, justify='center', bg='white', font='宋体 18 bold', highlightthickness=1)
    NameEntry.place(x=550, y=220)
    AgeLabel = tk.Label(InfoFrame1, text='2. 生日：', font='宋体 18 bold', bg='white')
    AgeLabel.place(x=350, y=290)
    var = tk.StringVar()
    YearEntry = ttk.Combobox(InfoFrame1, textvariable=var, value=([str(i) for i in range(1980,2051,1)]),
                            width=5, state = 'readonly',  font='宋体 18 bold')
    YearEntry.place(x=470, y=290)
    YearLabel = tk.Label(InfoFrame1, text='年', font='宋体 18 bold', bg='white')
    YearLabel.place(x=570, y=290)
    var = tk.StringVar()
    MonthEntry = ttk.Combobox(InfoFrame1, textvariable=var, value=([str('{:0>2d}'.format(i)) for i in range(1,13,1)]), 
                            width=2, state = 'readonly', font='宋体 18 bold')
    MonthEntry.place(x=610, y=290)
    MonthLabel = tk.Label(InfoFrame1, text='月', font='宋体 18 bold', bg='white')
    MonthLabel.place(x=670, y=290)
    var = tk.StringVar()
    DayEntry = ttk.Combobox(InfoFrame1, textvariable=var, value=([str('{:0>2d}'.format(i)) for i in range(1,32,1)]), 
                            width=2, state = 'readonly', font='宋体 18 bold')
    DayEntry.place(x=710, y=290)
    DayLabel = tk.Label(InfoFrame1, text='日', font='宋体 18 bold', bg='white')
    DayLabel.place(x=770, y=290)
    GenderLabel = tk.Label(InfoFrame1, text='3. 性别：', font='宋体 18 bold', width=10, anchor='w', bg='white')
    GenderLabel.place(x=350, y=360)
    var = tk.StringVar()
    GenderEntry = ttk.Combobox(InfoFrame1, textvariable=var, value=(['男', '女']), \
                            width=10, state = 'readonly', font='宋体 18 bold',)
    GenderEntry.place(x=480, y=360)
    LocationLabel = tk.Label(InfoFrame1, text='4. 评估机构地点：', font='宋体 18 bold', bg='white')
    LocationLabel.place(x=350, y=430)
    var = tk.StringVar()
    LocationEntry = ttk.Combobox(InfoFrame1, textvariable=var, value=(['山东省精神卫生中心']), width=30, 
                                state = 'readonly', font='宋体 18 bold')
    LocationEntry.place(x=600, y=430)
    HosIDLabel = tk.Label(InfoFrame1, text='5. 住院号/门诊号：', font='宋体 18 bold', bg='white')
    HosIDLabel.place(x=350, y=500)
    HosIDEntry = tk.Entry(InfoFrame1, width=30,  justify='center', font='宋体 18 bold', highlightthickness=1)
    HosIDEntry.place(x=600, y=500)
    StartBtn = tk.Button(InfoFrame1, text='确定', font='宋体 18 bold',  command=Start, bg='WhiteSmoke', relief='ridge',)
    StartBtn.place(x=620, y=570)
    ExitBtn = tk.Button(InfoFrame1, text='退出', font='宋体 18 bold', command=on_closing, bg='WhiteSmoke', relief='ridge')
    ExitBtn.place(x=1080, y=590)
    tip = tk.Label(InfoFrame1, text='版权所有和解释权  @山东师范大学心理学院', font='宋体 10 ', bg='white')
    tip.place(x=500, y=690)
    MainWin.protocol('WM_DELETE_WINDOW', on_closing)
    MainWin.mainloop()

def StartPicNback():
    save_to_json('./json/'+'/'+str(dirname)+'.json', JsonDict)
    save_to_json('./result/{}/{}.json'.format(str(dirname), str(dirname)), JsonDict)
    log_activity(activity_log='Start PicNback')
    PicNbackBtn.config(state='disabled')
    subprocess.run(['python','PicNback.py']+[dirname, HosID])
    WCBtn.config(state='normal')
    JsonDict['PicNback'] = 1
    log_activity(activity_log='PicNback is over')
    messagebox.showinfo('评估结束','记忆评估结束，请点击“2.脑灵活性评估”继续测评！')


def StartWC():
    save_to_json('./json/'+'/'+str(dirname)+'.json', JsonDict)
    save_to_json('./result/{}/{}.json'.format(str(dirname), str(dirname)), JsonDict)
    log_activity(activity_log='Start Wisconsin')
    WCBtn.config(state='disabled')
    subprocess.run(['python','Wisconsin.py']+[dirname, HosID])
    BARTBtn.config(state='normal')
    JsonDict['Wisconsin'] = 1
    log_activity(activity_log='Wisconsin is over')
    messagebox.showinfo('评估结束','脑灵活性评估结束，请点击“3.冒险性评估”继续测评！')

def StartBART():
    save_to_json('./json/'+'/'+str(dirname)+'.json', JsonDict)
    save_to_json('./result/{}/{}.json'.format(str(dirname), str(dirname)), JsonDict)
    log_activity(activity_log='Start BART')
    BARTBtn.config(state='disabled')
    subprocess.run(['python','BART.py']+[dirname, HosID])
    JsonDict['BART'] = 1
    log_activity(activity_log='BART is over')
    messagebox.showinfo('评估结束','您已完成冒险性评估！\n请点击确认或退出后联系医生。')

def Refresh():
    PicNbackBtn.config(state='normal')
    WCBtn.config(state='normal')
    BARTBtn.config(state='normal')
    InitialFrame.update()

def MainWin1():
    global output_data, StartBtn,ExitBtn,InformBtn, MemoryBtn,RefuseBtn, SwitchBtn, \
    ConcentBtn,GuessingBtn,ExampleBtn,RefreshBtn,MainWin,scri_path, ico_path,InfoFrame1, NameLabel,\
    NameEntry,AgeLabel,YearEntry,MonthEntry,DayEntry,VerifyEntry, InstitutionEntry,\
    VerifyWin, ico_path, scri_path,InitialFrame,start_time,PicNbackBtn, WCBtn, BARTBtn,\
    audio_recorder,video_recorder, HosIDEntry, cap, fps, delay_between_frames, video_panel,\
    VideoFrame, IsRunning, audio_source, VideoPanel
    # create the main frame
    # creat a infomation frame/cavans
    InitialFrame = tk.Frame(MainWin,width=1280, height=720, bg='white')
    InitialFrame.pack()
    InitialFrame_title = tk.Label(InitialFrame, text='儿童青少年认知能力评估', font='黑体 25 bold', bg='white')
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
    PicNbackBtn = tk.Button(InitialFrame, text='1.记忆评估', bg='LightSteelBlue', width=20, height=1,
                        font='宋体 20 bold', state='disabled', command=StartPicNback)
    PicNbackBtn.place(x=500, y=300,)
    WCBtn = tk.Button(InitialFrame, text='2.脑灵活性评估', bg='LightSteelBlue', width=20, height=1,
                        font='宋体   20 bold', state='disabled', command=StartWC)
    WCBtn.place(x=500, y=420,)
    BARTBtn = tk.Button(InitialFrame, text='3.冒险性评估', state='disabled',bg='LightSteelBlue', height=1,
                        width=20, font='宋体 20 bold', command=StartBART)
    BARTBtn.place(x=500, y=540, )
    RefreshBtn = tk.Button(InitialFrame, text='Refresh', font='宋体 13 bold', command=Refresh)
    RefreshBtn.place(x=150, y=600)
    ExitBtn = tk.Button(InitialFrame, text='退出', font='宋体 13 bold', command=on_closing )
    ExitBtn.place(x=1100, y=600)
    tip = tk.Label(InitialFrame, text='版权所有和解释权  @山东师范大学心理学院', font='宋体 10 ', bg='white')
    tip.place(x=500, y=690)
    MainWin.protocol('WM_DELETE_WINDOW', on_closing)
    MainWin.mainloop()

if __name__ == '__main__':
    Verify()
