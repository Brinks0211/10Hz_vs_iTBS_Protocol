from fpdf import FPDF
import os
import re
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import table

def RTcalculate(df, index):
    q1 = df[index].quantile(q=0.25)
    q3 = df[index].quantile(q=0.75)
    df = df.loc[(q1-1.5*(q3-q1) < df[index]) & (df[index] < q3 + 1.5*(q3-q1))]
    mean = round(np.mean(df[index]), 4)
    std = round(np.std(df[index]), 4)
    return mean, std

def Nback(File):
    global NbackText
    data = pd.read_csv(File)
    OneBackData = data[data['OneBackCorr'].notnull()]
    TwoBackData = data[data['TwoBackCorr'].notnull()]
    ThreeBackData = data[data['ThreeBackCorr'].notnull()]
    OneBackCorr = round(sum(OneBackData['OneBackCorr']) / len(OneBackData), 4)
    OneBackRt, OneBackStd = RTcalculate(OneBackData, 'OneBackRt')
    TwoBackCorr = round(sum(TwoBackData['TwoBackCorr']) / len(TwoBackData), 4)
    TwoBackRt, TwoBackStd = RTcalculate(TwoBackData, 'TwoBackRt')
    ThreeBackCorr = round(sum(ThreeBackData['ThreeBackCorr']) / len(ThreeBackData), 4)
    ThreeBackRt, ThreeBackStd = RTcalculate(ThreeBackData, 'ThreeBackRt')
    NbackFrame = pd.DataFrame(index=['OneBack', 'TwoBack', 'ThreeBack'], columns=['反应时', '标准差', '正确率'])
    NbackFrame.loc['OneBack', '反应时'] = OneBackRt
    NbackFrame.loc['OneBack', '标准差'] = OneBackStd
    NbackFrame.loc['OneBack', '正确率'] = OneBackCorr
    NbackFrame.loc['TwoBack', '反应时'] = TwoBackRt
    NbackFrame.loc['TwoBack', '标准差'] = TwoBackStd
    NbackFrame.loc['TwoBack', '正确率'] = TwoBackCorr
    NbackFrame.loc['ThreeBack', '反应时'] = ThreeBackRt
    NbackFrame.loc['ThreeBack', '标准差'] = ThreeBackStd
    NbackFrame.loc['ThreeBack', '正确率'] = ThreeBackCorr
    if TwoBackCorr >= 0.60:
        NbackText = '工作记忆能力良好，可通过阅读、背单词等训练保持专注力和记忆能力。\
此外，良好睡眠质量、多做有氧运动也有助于拥有更好的记忆能力。'
    elif TwoBackCorr >=0.3:
        NbackText = '工作记忆能力正常，可通过记忆训练，如读书、背单词、拆解任务等方式继续提高自己的记忆能力。此外\
良好睡眠质量、多做有氧运动也有助于拥有更好的记忆能力。'
    else:
        NbackText = '工作记忆能力正常，但仍有可提升空间，请确保已理解所测记忆任务规则。可通过记忆训练，如读书、背单词、拆解\
任务等方式提高自己的记忆能力。此外良好睡眠质量、多做有氧运动也有助于拥有更好的记忆能力。'
    plt.clf()
    plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
    fig, ax = plt.subplots(figsize=(8,2), tight_layout=True, dpi=200)  # dpi表示清晰度
    ax.xaxis.set_visible(False)  # hide the x axis
    ax.yaxis.set_visible(False)  # hide the y axis
    ax.set_frame_on(False)
    tb = table(ax, NbackFrame, loc='center', 
          cellLoc='center', colWidths=[0.2]*len(NbackFrame.columns))  # 将df换成需要保存的dataframe即可
    tb.auto_set_font_size(False)
    tb.set_fontsize(12)
    tb.scale(1.2,1.2)
    plt.savefig('PicNbackTable.png')
    # 解决中文显示问题
    plt.style.use('ggplot')
    plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
    # 平均反应时
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.bar(['OneBack', 'TwoBack', 'ThreeBack'], NbackFrame['反应时'], align='center', color='lightseagreen', width=0.3)
    ax1.errorbar(x=['OneBack', 'TwoBack', 'ThreeBack'], y=NbackFrame['反应时'], yerr=NbackFrame['标准差'], ecolor='grey', capsize=4, color='black', fmt='o')
    ax1.xaxis.set_ticks_position("bottom")
    ax1.yaxis.set_ticks_position("left")
    plt.xlabel('Nback')
    plt.ylabel('时间(秒)')
    plt.title('图1：平均反应时间（秒）')
    plt.savefig('PicNbackRT.png', dpi=100, bbox_inches='tight')
    # 平均准确率
    fig1 = plt.figure()
    ax2 = fig1.add_subplot(1, 1, 1)
    ax2.bar(['OneBack', 'TwoBack', 'ThreeBack'], NbackFrame['正确率']*100, 
            align='center', color='goldenrod', width=0.3)
    ax2.xaxis.set_ticks_position("bottom")
    ax2.yaxis.set_ticks_position("left")
    ax2.set_ylim(0,100)
    plt.xlabel('Nback')
    plt.ylabel('准确率')
    plt.title('图2：平均准确率')
    plt.savefig('PicNbackCorr.png', dpi=100, bbox_inches='tight')

def Wisconsin(File):
    global WisconsinText
    data = pd.read_csv(File)
    DataDrop = data[data['RespCorr'].notnull()]
    TotalRight = len(data[data['RespCorr']==1])
    TotalWrong = len(data[data['RespCorr']==0])
    TotalScore = len(data[data['CatagoryScore'].notnull()])
    TotalLastResp = len(data[data['RespPreTask'] == 1])
    DataColor = data[data['Category'] == 'color']
    ColorScore = len(DataColor[DataColor['CatagoryScore'].notnull()])
    ColorLastResp = len(DataColor[DataColor['RespPreTask'] == 1])
    ColorRight = len(DataColor[DataColor['RespCorr']==1])
    ColorWrong = len(DataColor[DataColor['RespCorr']==0])
    DataShape = data[data['Category'] == 'shape']
    ShapeScore = len(DataShape[DataShape['CatagoryScore'].notnull()])
    ShapeLastResp = len(DataShape[DataShape['RespPreTask'] == 1])
    ShapeRight = len(DataShape[DataShape['RespCorr']==1])
    ShapeWrong = len(DataShape[DataShape['RespCorr']==0])
    DataNum = data[data['Category'] == 'number']
    NumScore = len(DataNum[DataNum['CatagoryScore'].notnull()])
    NumLastResp = len(DataNum[DataNum['RespPreTask'] == 1])
    NumRight = len(DataNum[DataNum['RespCorr']==1])
    NumWrong = len(DataNum[DataNum['RespCorr']==0])
    WisconsinFrame = pd.DataFrame(index=['颜色规则', '图形规则', '数字规则', '总计'], 
        columns=['正确匹配该规则/总轮数','正确率','规则改变致错/总错误数'])
    WisconsinFrame.loc['颜色规则', '正确匹配该规则/总轮数'] = str(ColorScore)+'/2'
    WisconsinFrame.loc['图形规则', '正确匹配该规则/总轮数'] = str(ShapeScore)+'/3'
    WisconsinFrame.loc['数字规则', '正确匹配该规则/总轮数'] = str(NumScore)+'/3'
    WisconsinFrame.loc['总计', '正确匹配该规则/总轮数'] = str(TotalScore)+'/8'
    WisconsinFrame.loc['颜色规则', '规则改变致错/总错误数'] = str(ColorLastResp)+'/'+str(ColorWrong)
    WisconsinFrame.loc['图形规则', '规则改变致错/总错误数'] = str(ShapeLastResp)+'/'+str(ShapeWrong)
    WisconsinFrame.loc['数字规则', '规则改变致错/总错误数'] = str(NumLastResp)+'/'+str(NumWrong)
    WisconsinFrame.loc['总计', '规则改变致错/总错误数'] = str(TotalLastResp)+'/'+str(TotalWrong)
    WisconsinFrame.loc['颜色规则', '正确率'] = str(round(ColorRight/(ColorRight+ColorWrong)*100,4))+'%'
    WisconsinFrame.loc['图形规则', '正确率'] = str(round(ShapeRight/(ShapeRight+ShapeWrong)*100,2))+'%'
    WisconsinFrame.loc['数字规则', '正确率'] = str(round(NumRight/(NumRight+NumWrong)*100,2))+'%'
    WisconsinFrame.loc['总计', '正确率'] = str(round(TotalRight/(TotalRight+TotalWrong)*100,2))+'%'
    if TotalScore>=6:
        WisconsinText = '在Wisconsin任务中表现出高水平反应，认知灵活、执行功能出色。\
他们在面对任务中的不确定性和变化时能够迅速适应并做出正确的决策。具有快速的问题解决能力，\
以及有效的切换和调整策略的能力。'
    elif TotalScore>2 :
        WisconsinText = '在Wisconsin任务中认知灵活性表现良好，\
但可能需要更多的练习和经验来提高他们的执行功能。可能会表现出在某些情况下过度坚持错误策略或难以切换策略的倾向。\
建议通过像数独、填字游戏、逻辑谜题等游戏，帮助你锻炼大脑，提高思维灵活性和反应能力。'
    else:
        WisconsinText = '在Wisconsin任务中认知切换和灵活性方面表现一般。\
可能会表现出在同一策略上坚持过长时间，无法适应任务的变化或者很难从错误中学习。\
建议通过像数独、填字游戏、逻辑谜题等游戏，帮助你锻炼大脑，提高思维灵活性和反应能力；\
也可以设定一些挑战性的目标，超越自己的舒适区，比如：学习一门困难的技能、解决复杂的问题或参加挑战性的活动。'  
    plt.clf()
    plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
    fig, ax = plt.subplots(figsize=(8,2), tight_layout=True, dpi=200)  # dpi表示清晰度
    ax.xaxis.set_visible(False)  # hide the x axis
    ax.yaxis.set_visible(False)  # hide the y axis
    ax.set_frame_on(False)
    tb = table(ax, WisconsinFrame, loc='center', 
          cellLoc='center', colWidths=[0.2]*len(WisconsinFrame.columns))  # 将df换成需要保存的dataframe即可
    tb.auto_set_font_size(False)
    tb.set_fontsize(12)
    tb.scale(1.2,1.2)
    plt.savefig('WisconsinTable.png')
    plt.style.use('ggplot')
    # 解决中文显示问题
    plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
    # 平均反应时
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.bar(['颜色规则', '图形规则', '数字规则'], [ColorScore, ShapeScore, NumScore],
    align='center', color='lightseagreen', width=0.3)
    ax1.xaxis.set_ticks_position("bottom")
    ax1.yaxis.set_ticks_position("left")
    plt.xlabel('Wisconsin')
    plt.ylabel('正确匹配轮数')
    plt.title('图1：各匹配规则完成轮数')
    plt.savefig('WisconsinScore.png', dpi=100, bbox_inches='tight')
    # 平均准确率
    fig1 = plt.figure()
    ax2 = fig1.add_subplot(1, 1, 1)
    ax2.bar(['颜色规则', '图形规则', '数字规则'],  [round(ColorRight/(ColorRight+ColorWrong)*100,2),
        round(ShapeRight/(ShapeRight+ShapeWrong)*100,2), round(NumRight/(NumRight+NumWrong)*100,2)]
        , align='center', color='goldenrod', width=0.3)
    ax2.xaxis.set_ticks_position("bottom")
    ax2.yaxis.set_ticks_position("left")
    plt.xlabel('Wisconsin')
    plt.ylabel('准确率（%）')
    plt.title('图2：各匹配规则达成准确率')
    plt.savefig('WisconsinCorr.png', dpi=100, bbox_inches='tight')

def BART(File):
    global BARTText
    data = pd.read_csv(File)
    BoomScore = data[data['Boom']==1]
    LastData = data[data['RespKey']=='return']
    TotalScore = data.iloc[-1, :]['TotalScore']
    TotalBoom = len(data[data['Boom']==1])
    OrangeData = data[data['Condition']=='orange']
    GreenData = data[data['Condition']=='green']
    BlueData = data[data['Condition']=='blue']
    OrangeLastData = OrangeData[OrangeData['RespKey']=='return']
    GreenLastData = GreenData[GreenData['RespKey']=='return']
    BlueLastData = BlueData[BlueData['RespKey']=='return']
    OrangeScore = round(np.sum(OrangeLastData['LastScore']),2)
    GreenScore = round(np.sum(GreenLastData['LastScore']),2)
    BlueScore = round(np.sum(BlueLastData['LastScore']),2)
    OrangeLastScore = round(np.mean(OrangeLastData['LastScore']),2)
    GreenLastScore = round(np.mean(GreenLastData['LastScore']),2)
    BlueLastScore = round(np.mean(BlueLastData['LastScore']),2)
    OrangeBoom = len(OrangeData[OrangeData['Boom']==1])
    GreenBoom = len(GreenData[GreenData['Boom']==1])
    BlueBoom = len(BlueData[BlueData['Boom']==1])
    BARTFrame = pd.DataFrame(index=['橙色气球', '绿色气球', '蓝色气球', '总计'], 
        columns=['爆炸数','平均每个气球得分', '总得分'])
    BARTFrame.loc['橙色气球', '爆炸数'] = OrangeBoom
    BARTFrame.loc['绿色气球', '爆炸数'] = GreenBoom
    BARTFrame.loc['蓝色气球', '爆炸数'] = BlueBoom
    BARTFrame.loc['总计', '爆炸数'] = TotalBoom
    BARTFrame.loc['橙色气球', '平均每个气球得分'] = OrangeLastScore
    BARTFrame.loc['绿色气球', '平均每个气球得分'] = GreenLastScore
    BARTFrame.loc['蓝色气球', '平均每个气球得分'] = BlueLastScore
    BARTFrame.loc['总计', '平均每个气球得分'] = round(TotalScore/(60-TotalBoom), 2)
    BARTFrame.loc['橙色气球', '总得分'] = OrangeScore
    BARTFrame.loc['绿色气球', '总得分'] = GreenScore
    BARTFrame.loc['蓝色气球', '总得分'] = BlueScore
    BARTFrame.loc['总计', '总得分'] = TotalScore
    plt.clf()
    plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
    fig, ax = plt.subplots(figsize=(8,2), tight_layout=True, dpi=200)  # dpi表示清晰度
    ax.xaxis.set_visible(False)  # hide the x axis
    ax.yaxis.set_visible(False)  # hide the y axis
    ax.set_frame_on(False)
    tb = table(ax, BARTFrame, loc='center', 
          cellLoc='center', colWidths=[0.2]*len(BARTFrame.columns))  # 将df换成需要保存的dataframe即可
    tb.auto_set_font_size(False)
    tb.set_fontsize(12)
    tb.scale(1.2,1.2)
    plt.savefig('BARTTable.png')
    # plt.clf()
    # plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
    # plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
    # fig = plt.figure(figsize=(6, 2), dpi=200)  # dpi表示清晰度
    # ax = fig.add_subplot(111, frame_on=False)
    # ax.xaxis.set_visible(False)  # hide the x axis
    # ax.yaxis.set_visible(False)  # hide the y axis
    # table(ax, BARTFrame, loc='center')  # 将df换成需要保存的dataframe即可
    # plt.savefig('BARTTable.png')
    plt.style.use('ggplot')
    # 解决中文显示问题
    plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.bar(['橙色气球', '绿色气球', '蓝色气球'], [OrangeBoom, GreenBoom, BlueBoom], align='center', color='lightseagreen', width=0.3)
    ax1.xaxis.set_ticks_position("bottom")
    ax1.yaxis.set_ticks_position("left")
    plt.xlabel('BART')
    plt.ylabel('爆炸数')
    plt.title('图1：气球爆炸数')
    plt.savefig('BARTBoom.png', dpi=100, bbox_inches='tight')
    # 平均准确率
    fig1 = plt.figure()
    ax2 = fig1.add_subplot(1, 1, 1)
    ax2.bar(['橙色气球', '绿色气球', '蓝色气球'],  [OrangeScore, GreenScore, BlueScore]
        , align='center', color='goldenrod', width=0.3)
    ax2.xaxis.set_ticks_position("bottom")
    ax2.yaxis.set_ticks_position("left")
    plt.xlabel('BART')
    plt.ylabel('得分')
    plt.title('图2：不同颜色气球得分')
    plt.savefig('BARTScore.png', dpi=100, bbox_inches='tight')
    if TotalScore >= 25:
        BARTText = '在充分理解前提下，能够冷静地接受适度的风险，而不是盲目地追求高收益。能够从\
从自己的经验中进行学习，逐步调整策略，展现优秀的风险控制和决策能力。\
建议继续鼓励其在其他类似任务中培养和应用这些技能，以进一步提高决策的准确性和效率。'
    if TotalBoom >= 14:
        BARTText = '倾向于保守地管理风险往往在较低的充气次数后选择停止，以避免可能的损失，\
但这也导致了较低的总体收益。建议挑战自己,每周设定一个挑战自己舒适区的目标，比如公开演讲、参加一个陌生的社交活动或尝试\
一个新运动。记录每次冒险的经历、感受和收获，从中找到乐趣和成就感。'
    else: 
        BARTText = '参与者在任务中表现出明显的回避风险的倾向，往往在充气气球的次数较低时选择停止，无法获取潜在的更高收益。\
建议在日后尝试分析和评估风险，了解自己的什么是可接受风险，什么是不必要冒险；接受失败，坦然地从失败中学习，每次失败都是一次\
学习的机会；勇敢走出自己舒适区，阅读不同领域书籍，学习新技能，结交新朋友，拓展自己视野。'

# 提前设置好pdf的页脚和logo
class PDF(FPDF):
    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "I", 8)
        # Printing page number:
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")
        # Rendering logo:
        self.image("./material/SDMHC.png", x=10, y=4, w=40.8, h=12.5)
        # self.image("./material/SDNU.png", x=11, y=18, w=40.8, h=12.5)
        self.set_y(0)
        # 添加字体
        # self.add_font('songti', fname=scri_path+'/'+'songti.ttc',style='I')
        self.set_font("songti",)
        self.cell(0, 15, "本评估报告仅供认知方面参考，不作为诊断证明", align='R')
        self.set_y(15)
        # 设置pdf字体
        self.set_font('songti', size=20) 
        # 创建cell框，长200 高10 居中对齐 打印完后光标在下一行（new_y = 'NEXT'），左侧开始（new_x = 'LMARGIN'）
        self.cell(w=200, h=14, text='认知评估报告', align='C', new_y = 'NEXT', new_x = 'LMARGIN' )
        self.ln(2)
        self.set_font('songti', size=10)
        self.cell(w=200, h=10, text='姓名: '+str(Name)+'          住院号：'+str(HosID)+'          性别：'+str(Gender)+'          测试日期：'+str(Date),
                 align='C', new_y = 'NEXT', new_x = 'LMARGIN')

def OutputPDF():
    pdf = PDF()
    pdf.add_page()
    # 添加字体
    pdf.add_font('songti','', fname='./material/song.ttf')
    pdf.add_font('songti','B', fname='./material/song.ttf')
    pdf.ln(30)
    pdf.set_font('songti', 'B', size=10)
    pdf.cell(text='评估一：记忆评估', w=190, h=8, new_y = 'NEXT', new_x = 'LMARGIN')
    pdf.image(name='PicNbackTable.png', x=5, y=60, h=20, w=70)
    pdf.image(name='PicNbackRT.png', x=75, y=50, h=40, w=50)
    pdf.image(name='PicNbackCorr.png', x=140, y=50, h=40, w=50)
    pdf.ln(40)
    pdf.set_font('songti','')
    pdf.multi_cell(w=190, h=8, text=NbackText)
    pdf.ln(3)
    pdf.cell(text='评估二：脑灵活性评估', w=190, h=8, new_y = 'NEXT', new_x = 'LMARGIN')
    y = pdf.get_y()
    pdf.image(name='WisconsinTable.png', x=5, y=y+10, h=20, w=70)
    pdf.image(name='WisconsinScore.png', x=75, y=y, h=40, w=50)
    pdf.image(name='WisconsinCorr.png', x=140, y=y, h=40, w=50)
    pdf.ln(40)
    pdf.set_font('songti','')
    pdf.multi_cell(w=190, h=8, text=WisconsinText)
    pdf.ln(3)
    pdf.cell(text='评估三：冒险性评估', w=190, h=8, new_y = 'NEXT', new_x = 'LMARGIN')
    y = pdf.get_y()
    pdf.image(name='BARTTable.png', x=5, y=y+10, h=20, w=70)
    pdf.image(name='BARTScore.png', x=75, y=y, h=40, w=50)
    pdf.image(name='BARTBoom.png', x=140, y=y, h=40, w=50)
    pdf.ln(40)
    pdf.set_font('songti','')
    pdf.multi_cell(w=190, h=8, text=BARTText)
    try:os.mkdir('./结果报告')
    except: pass
    pdf.output('./结果报告/'+PathList[-1]+'.pdf')

def RecogAnalysis():
    global Name, HosID, Gender, Date, PathList, Dir
    Dir = input("请输入认知结果文件夹路径：")
    Name = input("请输入患者姓名：")
    # Dir = DirPara
    # Name = NamePara
    PathList = Dir.split('\\')
    JsonFile = os.path.join(Dir, PathList[-1]+'.json')
    NbackFile = os.path.join(Dir, PathList[-1]+'_PicNback.csv')
    WisconsinFile = os.path.join(Dir, PathList[-1]+'_Wisconsin.csv')
    BARTFile = os.path.join(Dir, PathList[-1]+'_BART.csv')
    with open(JsonFile, 'r', ) as JsonFile:
        InfoList = json.load(JsonFile)
    HosID = InfoList['HosID']
    Gender = InfoList['Gender']
    Date = InfoList['TimeRecog'][0:4]+'年'+InfoList['TimeRecog'][4:6]+'月'\
    +InfoList['TimeRecog'][6:8]+'日'
    try:Nback(File=NbackFile)
    except:pass
    try:Wisconsin(File=WisconsinFile)
    except:pass
    try:BART(File=BARTFile)
    except:pass
    OutputPDF()
    os.remove('WisconsinTable.png')
    os.remove('WisconsinCorr.png')
    os.remove('WisconsinScore.png')
    os.remove('PicNbackCorr.png')
    os.remove('PicNbackTable.png')
    os.remove('PicNbackRT.png')
    os.remove('BARTBoom.png')
    os.remove('BARTScore.png')
    os.remove('BARTTable.png')
    print('报告已打印')

if __name__ == '__main__':
    RecogAnalysis()
