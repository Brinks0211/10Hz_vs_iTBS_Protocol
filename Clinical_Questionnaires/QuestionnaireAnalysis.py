import tkinter as tk
import numpy as np
import pandas as pd
from pypinyin import pinyin
from ReportPDF import ReportPDF

def Analysis(dirname):
    path  = '/'.join(['./result',dirname,dirname+'_MASC.csv'])
    data = pd.read_csv(path, encoding='GBK')
    output_file = pd.DataFrame()

    # PSQI
    dfPSQI = data[data.iloc[:,0].str.contains('PSQI', na=False)]
    dfPSQI = dfPSQI.apply(pd.to_numeric,errors='ignore')
    dfPSQI.set_index(dfPSQI.iloc[:,0], inplace=True)
    ind = 0
    # 主观睡眠质量
    output_file.loc[ind, '主观睡眠质量'] = dfPSQI.loc['PSQI-6','answer']
    # 睡眠潜伏期
    summary = 0
    if dfPSQI.loc['PSQI-6','answer'] <=15:
        summary = summary + 0
    elif dfPSQI.loc['PSQI-6','answer'] <=30:
        summary = summary + 1
    elif dfPSQI.loc['PSQI-6','answer'] <=60:
        summary = summary + 2
    elif dfPSQI.loc['PSQI-6','answer'] <=900:
        summary = summary + 3
    else: summary = 999
    summary = summary + dfPSQI.loc['PSQI-5a','answer']
    if summary == 0:
        score = 0
    elif summary <=2:
        score = 1
    elif summary <=4:
        score = 2
    elif summary <=6:
        score = 3
    else: score = 999
    output_file.loc[ind, '睡眠潜伏期'] = score
    # 睡眠持续性
    if dfPSQI.loc['PSQI-4','answer'] >= 7:
        score = 0
    elif dfPSQI.loc['PSQI-4','answer']  >=6:
        score = 1
    elif dfPSQI.loc['PSQI-4','answer']  >=5:
        score = 2
    elif dfPSQI.loc['PSQI-4','answer']  <5:
        score = 3
    elif dfPSQI.loc['PSQI-4','answer']  >24:
        score = 999
    elif dfPSQI.loc['PSQI-4','answer']  == None:
        score = 999
    else: score = 999
    output_file.loc[ind, '睡眠持续性'] = score
    # # 习惯性睡眠效率
    SleepHour = dfPSQI.loc['PSQI-1_Hour','answer']
    SleepTime = dfPSQI.loc['PSQI-1_Min','answer']
    GetupHour = dfPSQI.loc['PSQI-3_Hour','answer']
    GetupTime = dfPSQI.loc['PSQI-3_Min','answer']
    RealSleep = dfPSQI.loc['PSQI-4','answer']
    SleepTime = 23-SleepHour + round( (60-SleepTime)/60, 2 ) + \
                GetupHour + round( (GetupTime)/60, 2 )
    efficiency = round( RealSleep/SleepTime, 3)
    if efficiency >= 0.85:
        score = 0
    elif efficiency >= 0.75:
        score = 1
    elif efficiency >= 0.65:
        score = 2
    elif efficiency < 0.65:
        score = 3
    output_file.loc[ind,'习惯性睡眠效率'] = score
    # 睡眠紊乱
    temp = ['PSQI-5b', 'PSQI-5c', 'PSQI-5d', 'PSQI-5e',
            'PSQI-5f', 'PSQI-5g', 'PSQI-5h', 'PSQI-5i', 'PSQI-5j']
    summary = 0
    for j in temp:
        summary = summary+dfPSQI.loc[j,'answer']
    if summary == 0:
        score = 0
    elif summary <= 9 :
        score = 1
    elif summary <= 18:
        score = 2
    elif summary <= 27:
        score = 3
    else:
        score = 999
    output_file.loc[ind, '睡眠紊乱'] = score
    # 使用睡眠药物
    output_file.loc[ind, '使用睡眠药物'] = dfPSQI.loc['PSQI-7','answer']
    # 白天功能紊乱
    temp = ['PSQI-8', 'PSQI-9']
    summary = 0
    for j in temp:
        summary = summary+dfPSQI.loc[j,'answer']
    if summary == 0:
        score = 0
    elif summary <= 2:
        score = 1
    elif summary <= 4:
        score = 2
    elif summary <= 6:
        score = 3
    else:
        score = 999
    output_file.loc[ind, '白天功能紊乱'] = score
    # 总分
    temp = ['主观睡眠质量','睡眠潜伏期','睡眠持续性','习惯性睡眠效率','睡眠紊乱',
        '使用睡眠药物','白天功能紊乱']
    summary = 0
    for j in temp:
        summary = summary+output_file.loc[ind, j]
    output_file.loc[ind,'PSQI总分'] = summary

    # PLE
    dfPLE = data.loc[data.iloc[:,0].str.contains('PLE', na=False)]
    dfPLE = dfPLE.apply(pd.to_numeric,errors='ignore')
    ind = 0
    summary = 0
    for i in range(0,21):
        summary += dfPLE.iloc[i, 1]
    output_file.loc[ind,'PEL总分'] = summary
    summary = 0
    for i in range(0,21):
        summary += dfPLE.iloc[i, 1] * dfPLE.iloc[i+21, 1]
    output_file.loc[ind,'Distress总分'] = summary



    # CDI
    dfCDI = data.loc[data.iloc[:,0].str.contains('CDI', na=False)]
    dfCDI = dfCDI.apply(pd.to_numeric,errors='ignore')
    ind = 0
    # 先建两个列表，用于存放正反向计分
    # 正向计分：1,3,4,6,9,12,14,17,19,20,22,23,26,27
    forward = [0,2,3,5,8,11,13,16,18,19,21,22,25,26]
    # 反向计分：2,5,7,8,10,11,13,15,16,18,21,24,25
    reverse = [1,4,6,7,9,10,12,14,15,17,20,23,24]
    for i in reverse:
        dfCDI.iloc[i,1] = 2 - dfCDI.iloc[i,1]
    # 构建各个维度的列表
    # 低自尊、2 7 9 14 25
    temp = [1,6,8,13,24]
    summary = 0
    for j in temp:
        summary = summary+dfCDI.iloc[j,1]
        output_file.loc[ind,'低自尊'] = summary
    # 负性情绪、1 6 8 10 11 13
    temp = [0,5,7,9,10,12]
    summary = 0
    for j in temp:
        summary = summary+dfCDI.iloc[j,1]
        output_file.loc[ind, '负性情绪'] = summary
    # 快感缺乏、4 16 17 18 19 20 21 22
    temp = [3, 15,16,17,18,19,20,21]
    summary = 0
    for j in temp:
        summary = summary+dfCDI.iloc[j,1]
        output_file.loc[ind, '快感缺乏'] = summary
    # 效能低下、3 15 23 24
    temp = [2,14,22,23]
    summary = 0
    for j in temp:
        summary = summary+dfCDI.iloc[j,1]
        output_file.loc[ind, '效能低下'] = summary
    # 人际问题、5 12 26 27
    temp = [4,11,25,26]
    summary = 0
    for j in temp:
        summary = summary+dfCDI.iloc[j,1]
        output_file.loc[ind, '人际问题'] = summary
    # 总分
    summary = 0
    for j in range(0,27,1):
        summary = summary+dfCDI.iloc[j,1]
        output_file.loc[ind, 'CDI总分'] = summary
        
    # MASC
    dfMASC = data.loc[data.iloc[:,0].str.contains('MASC', na=False)]
    dfMASC = dfMASC.apply(pd.to_numeric,errors='ignore', )
    ind = 0
    # 躯体症状 1，6，8，12，15，18，20，24，27，31，35，38
    temp = [0,5,7,11,14,17,19,23,26,30,34,37]
    summary = 0
    for j in temp:
        summary = summary+dfMASC.iloc[j,1]
        output_file.loc[ind, '躯体症状'] = summary
    # 伤害逃避：2，5，11，13，21，25，28，32，36
    temp = [1,4,10,12,20,24,27,31,35]
    summary = 0
    for j in temp:
        summary = summary+dfMASC.iloc[j,1]
        output_file.loc[ind,  '伤害逃避'] = summary
    # 社会焦虑：3，10，14，16，22，29，33，37，39
    temp = [2,9,13,15,21,28,32,36,38]
    summary = 0
    for j in temp:
        summary = summary+dfMASC.iloc[j,1]
        output_file.loc[ind,  '社会焦虑'] = summary
    # 分离焦虑：4，7，9，17，19，23，26，30，34
    temp = [3,6,8,16,18,22,25,29,33]
    summary = 0
    for j in temp:
        summary = summary+dfMASC.iloc[j,1]
        output_file.loc[ind, '分离焦虑'] = summary
    # 总分
    summary = 0
    for j in range(0,39,1):
        summary = summary+dfMASC.iloc[j,1]
        output_file.loc[ind, 'MASC总分'] = summary
    data.set_index(data.iloc[:,0], inplace=True)
    output_file.loc[ind, 'name'] = data.loc['name', 'answer']
    output_file.loc[ind, 'HosID'] = data.loc['HosID', 'answer']
    outputpath  = '/'.join(['./result',dirname,dirname+'_QuesResult.csv'])
    output_file.to_csv(outputpath, encoding='GBK', index=False)
    ReportPDF(dirname)

# if __name__ == '__main__':
#     Analysis('zhangyihao_19800102_1_20240326')