from fpdf import FPDF
import pandas as pd
import re
import os
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['simsun']#显示中文字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

def PSQIpic(df):
    # 数据
    labels = ['主观睡眠质量', '睡眠潜伏期', '睡眠持续性', '习惯性睡眠效率', '睡眠紊乱', '使用睡眠药物', '白天功能紊乱']
    values = []
    for i in labels:
        values.append(df.loc[0,i])
    # 计算角度
    theta = np.linspace(0, 2*np.pi, len(values), endpoint=False)
    # 将第一个点重复一次，以闭合雷达图
    values += values[:1]
    theta = np.append(theta, theta[:1])
    # 创建雷达图
    fig, ax = plt.subplots(subplot_kw=dict(polar=True))
    ax.fill(theta, values, color='b', alpha=0.25)
    # 设置标签
    ax.set_xticks(theta[:-1])
    ax.set_xticklabels(labels)
    # 添加标签到每个数据点
    for i in range(len(labels)):
        angle_rad = theta[i]
        ax.text(angle_rad, values[i], f"{values[i]}", ha='center', va='center')
    # 显示雷达图
    plt.savefig(path+'_PSQI.png', dpi = 80)

def CDIpic(df):
    # 数据
    labels = ['低自尊', '负性情绪', '快感缺乏', '效能低下', '人际问题']
    values = []
    for i in labels:
        values.append(df.loc[0,i])
    # 计算角度
    theta = np.linspace(0, 2*np.pi, len(values), endpoint=False)
    # 将第一个点重复一次，以闭合雷达图
    values += values[:1]
    theta = np.append(theta, theta[:1])
    # 创建雷达图
    fig, ax = plt.subplots(subplot_kw=dict(polar=True))
    ax.fill(theta, values, color='b', alpha=0.25)
    # 设置标签
    ax.set_xticks(theta[:-1])
    ax.set_xticklabels(labels)
    # 添加标签到每个数据点
    for i in range(len(labels)):
        angle_rad = theta[i]
        angle_deg = np.degrees(angle_rad)
        ax.text(angle_rad, values[i], f"{values[i]}", ha='center', va='center')
    # 保存雷达图为图片文件（例如，PNG）
    plt.savefig(path+'_CDI.png', dpi = 80)

def MASCpic(df):
    # 数据
    labels = ['躯体症状', '伤害逃避', '社会焦虑', '分离焦虑']
    values = []
    for i in labels:
        values.append(df.loc[0,i])
    # 计算角度
    theta = np.linspace(0, 2*np.pi, len(values), endpoint=False)
    # 将第一个点重复一次，以闭合雷达图
    values += values[:1]
    theta = np.append(theta, theta[:1])
    # 创建雷达图
    fig, ax = plt.subplots(subplot_kw=dict(polar=True))
    ax.fill(theta, values, color='b', alpha=0.25)
    # 设置标签
    ax.set_xticks(theta[:-1])
    ax.set_xticklabels(labels)
    # 添加标签到每个数据点
    for i in range(len(labels)):
        angle_rad = theta[i]
        angle_deg = np.degrees(angle_rad)
        ax.text(angle_rad, values[i], f"{values[i]}", ha='center', va='center')
    # 保存雷达图为图片文件（例如，PNG）
    plt.savefig(path+'_MASC.png', dpi = 80)

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
        self.cell(0, 15, "本评估报告仅供情绪睡眠方面参考，不作为诊断证明", align='R')
        self.set_y(15)
        # 设置pdf字体
        self.set_font('songti', size=20) 
        # 创建cell框，长200 高10 居中对齐 打印完后光标在下一行（new_y = 'NEXT'），左侧开始（new_x = 'LMARGIN'）
        self.cell(w=200, h=14, text='情绪睡眠评估报告', align='C', new_y = 'NEXT', new_x = 'LMARGIN' )
        self.ln(2)
        self.set_font('songti', size=10)
        self.cell(w=200, h=10, text='姓名: '+str(name)+'          住院号：'+str(HosID)+'          性别：'+str(gender)+'          测试日期：'+str(date),
                 align='C', new_y = 'NEXT', new_x = 'LMARGIN')

def ReportPDF(dirname):
    global path, name, date, gender, birth, scri_path, HosID
    scri_path = os.getcwd()
    para = dirname.split('_')
    birth = para[1]
    if para[2] == "1": gender='男'
    elif para[2] == '2': gender='女'
    date = para[3]
    path  = '/'.join(['./result',dirname,dirname])
    df = pd.read_csv(path+'_QuesResult.csv', encoding="GBK")
    name = df.loc[0,'name']
    HosID = str(df.loc[0, 'HosID'])
    PSQIpic(df)
    CDIpic(df)
    MASCpic(df)
    # Instantiation of inherited class
    pdf = PDF()
    # 添加新页
    pdf.add_page()
    # 添加字体
    pdf.add_font('songti','', fname='./material/song.ttf')
    pdf.add_font('songti','B', fname='./material/song.ttf')
    pdf.ln(30)
    pdf.set_font('songti')
    pdf.cell(w=200, h=12, text='  皮茨堡睡眠量表'+ '                   儿童抑郁量表                儿童青少年多维度焦虑量表', 
             align='C', new_y = 'NEXT', new_x = 'LMARGIN')
    pdf.image(name=path+'_PSQI.png', x=5, y=50, h=50, w=70)
    pdf.image(name=path+'_CDI.png', x=70, y=50, h=50, w=70)
    pdf.image(name=path+'_MASC.png', x=140, y=50, h=50, w=70)
    pdf.ln(50)
    pdf.cell(w=200, h=12, text=' PSQI-'+str(df.loc[0,'PSQI总分'])+'                      CDI-'+ \
             str(df.loc[0,'CDI总分'])+'                        MASC-'+str(df.loc[0,'MASC总分'])+'  ', 
             align='C', new_y = 'NEXT', new_x = 'LMARGIN')
    PSQI = df.loc[0,'PSQI总分']
    CDI = df.loc[0,'CDI总分']
    MASC = df.loc[0,'MASC总分']
    pdf.set_font('songti', 'B')
    pdf.cell(text='皮茨堡睡眠量表评分：'+str(PSQI), w=190, h=8, new_y = 'NEXT', new_x = 'LMARGIN')
    if PSQI <= 4:
        text = '这意味着你的\
睡眠质量非常高，基本没有任何问题。你能够很快入睡，睡眠时间\
充足且没有中途醒来的情况。如果你的评分在这个范围内，恭喜你，\
你拥有良好的睡眠质量。\n'
    elif PSQI <= 10:
        text = '睡眠质量尚可，但有一些\
小问题。可能你需要花费一些时间入睡，或者会在夜间醒来一两次。\
虽然睡眠质量不是完美的，但你仍然能够获得足够的休息和精力来\
应对日常生活。\
如果您想进一步改善睡眠质量，我们提供如下建议供参考：(1)建议每天在相同时间上床睡觉和起床；\
(2)保持房间的清洁、安静和凉爽,创造一个舒适的睡眠环境。\
(3)避免在床上使用电子设备，尤其是在睡觉前一小时内。\n'
    elif PSQI <=15:
        text = '睡眠质量一般。你可能会\
经常醒来，或者感觉早晨起床时没有精神。这可能是因为你在入睡\
时遇到了困难，或者在夜间经历了多次的中途醒来。这个评分范围\
意味着你的睡眠质量需要改善，可以尝试一些改变生活习惯或者采\
取其他措施来提高睡眠质量。为了改善睡眠质量，我们提供如下建议供参考：(1)建议每天在相同时间上床睡觉和起床；\
(2)保持房间的清洁、安静和凉爽,创造一个舒适的睡眠环境。\
(3)避免在床上使用电子设备，尤其是在睡觉前一小时内。\n'
    elif PSQI <=21:
        text = '睡眠质量较差。\
你可能会经常醒来，或者难以入睡，早晨起床时感到疲倦。\
这个评分范围意味着你的睡眠质量非常低，对你的健康和生活产生\
了负面影响。在这种情况下，你应该尽快采取措施来改善睡眠质量。\
为了改善睡眠质量，我们提供如下建议供参考：(1)建议每天在相同时间上床睡觉和起床；\
 (2)保持房间的清洁、安静和凉爽,创造一个舒适的睡眠环境。\
(3)避免在床上使用电子设备，尤其是在睡觉前一小时内。如果这些方法仍然无\
法改善你的睡眠质量，你可以咨询专业的医生或睡眠专家，寻求更\
进一步的帮助和建议。\n'
    pdf.set_font('songti','')
    pdf.multi_cell(w=190, h=8, text=text)
    pdf.set_font('songti', 'B')
    pdf.cell(text='儿童抑郁量表评分：'+str(CDI), w=190, h=8, new_y = 'NEXT', new_x = 'LMARGIN')
    if CDI <= 13:
        text = '情绪稳定，对生活充满兴趣。能够处理日常生活中的挑战和压力。社交活动和人际关系良好。建议继续保持健康的生\
活方式，包括良好的睡眠、均衡的饮食、适度的运动，并维护积极的社交关系。可以定期进行心理健康检查，以预防潜在的心理健康问题。\n'
    elif CDI <= 19:
        text = '情绪波动，可能出现间歇性的沮丧感。对日常活动失去兴趣，可能感到疲倦。睡眠和食欲可能有轻微改变。\
建议寻求社会支持，与朋友和家人分享感受。保持规律的生活作息，尝试一些心理健康促进的活动，如运动、艺术或冥想。\n'
    elif CDI <= 28:
        text = '情绪有持续的沮丧感倾向，影响日常生活。对活动和社交的兴趣明显减退。睡眠和食欲明显受影响，可能出现体重变化。\
建议寻求专业心理健康支持，可能包括心理治疗或药物治疗。建立支持网络，保持与医疗专业人士的沟通，共同制定治疗计划。\n'
    elif CDI <= 54:
        text = '情绪伴有深度的沮丧感，可能伴随有无助和绝望的情绪。日常功能受到显著影响，可能无法履行正常的工作和社交责任。\
可能出现身体症状，如头痛、消化问题等。建议： 立即寻求专业帮助。心理治疗、药物治疗或二者结合可能是有效的治疗方式。\
定期监测症状，与医疗专业人士合作，制定全面的治疗计划。\n'
    pdf.set_font('songti','')
    pdf.multi_cell(w=190, h=8, text=text)
    pdf.set_font('songti', 'B')
    pdf.cell(text='儿童青少年多维度焦虑量表评分：'+str(MASC), w=190, h=8, new_y = 'NEXT', new_x = 'LMARGIN')
    if MASC <= 40:
        text = '无焦虑倾向，能够应对日常生活中的压力和挑战，没有明显的焦虑情绪和行为。'
    elif MASC <= 54:
        text = '偶尔会出现焦虑情绪，比如偶尔感到担心、紧张或害怕，容易烦躁不安，难以集中注意力，头痛、\
腹痛等。但可以在短时间内自行缓解，不会对日常生活造成明显影响。建议通过深呼吸、冥想来缓解压力，积极参加体育\
锻炼；保持健康生活方式，保证充足睡眠和均衡饮食。'
    elif MASC <= 69:
        text = '有经常出现焦虑情绪的倾向，并可能会影响到正常生活。容易感到担心、紧张和害怕；睡眠质量\
下降，难以集中注意力；经常出现头痛、腹痛、手抖等症状；逃避社交活动或某些特定情境。建议寻求专业心理咨询师\
或精神科医生的帮助，在必要的情况下，考虑药物治疗。'
    elif MASC <= 117:
        text = '有持续出现严重焦虑的倾向，可能会严重影响其日常生活。几乎每天感到担心、紧张或害怕；注意力\
难以集中；经常出现手抖、头痛、腹痛等躯体症状；睡眠质量严重下降；拒绝社交活动或某些特定情境。建议立即寻求专业心理\
咨询师或精神科医生的帮助，进行心理治疗联合药物治疗，必要情况下，可住院治疗。'
    pdf.set_font('songti','')
    pdf.multi_cell(w=190, h=8, text=text)
    try:os.mkdir('./结果报告')
    except: pass
    pdf.output('./结果报告/'+dirname+".pdf")
       

# if __name__ == '__main__':
#     ReportPDF('431_19810203_1_20240302')