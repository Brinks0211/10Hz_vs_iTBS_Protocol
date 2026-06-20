from psychopy import visual, event, core, data, gui, logging
# from RecordVideo import VideoRecorder
# from RecordAudio import AudioRecorder
import pandas as pd
import sys
import random
import os
import datetime

def PicNback(dirname, HosID):
    global ScreenFrame, win, Fixation, ImageList, Image11,Image12,Image13,Image21,\
            Image22,Image23,Image31,Image32,Image33, GlobalClock, \
            Filename
    # Start recording
    # VideoRecord = VideoRecorder()
    # AudioRecord = AudioRecorder()
    # VideoRecord.start_recording()
    # AudioRecord.start_recording()
    # stimulus variety list
    dirname = dirname
    HosID = HosID
    Today = datetime.datetime.now()
    Year = Today.year
    Month = Today.month
    Day = Today.day
    Hour = Today.hour
    Min = Today.minute
    Date = "_".join([str(Year)+str('{:0>2d}'.format(Month))+str('{:0>2d}'.format(Day))+\
                     str('{:0>2d}'.format(Hour))+str('{:0>2d}'.format(Min))])
    Filename = "_".join([dirname, Date])
    FilenameCsv = './result/{}/{}_PicNback'.format(dirname, dirname)
    FilenameLog = './result/{}/{}_PicNback.log'.format(dirname, dirname)
    ExpInfo = {'ExpName':'PicNback', 'DirName':dirname, 'date':Date, 'HosID':HosID}
    ExpHandler = data.ExperimentHandler(name='PicNback', version='1.0', extraInfo=ExpInfo, 
                                        runtimeInfo=None, originPath=None, savePickle=True, 
                                        saveWideText=True, dataFileName=FilenameCsv)
    GlobalClock = core.Clock()
    logging.LogFile(FilenameLog, level=logging.INFO, filemode='w')
    logging.info('start')
    win = visual.Window([1280,720], fullscr=False, units='pix')
    Fixation = visual.TextStim(win=win, text='+', height=40)
    Image11 = visual.ImageStim(win=win, image='./material/PicNback/11.png', size=(400,400))
    Image12 = visual.ImageStim(win=win, image='./material/PicNback/12.png', size=(400,400))
    Image13 = visual.ImageStim(win=win, image='./material/PicNback/13.png', size=(400,400))
    Image21 = visual.ImageStim(win=win, image='./material/PicNback/21.png', size=(400,400))
    Image22 = visual.ImageStim(win=win, image='./material/PicNback/22.png', size=(400,400))
    Image23 = visual.ImageStim(win=win, image='./material/PicNback/23.png', size=(400,400))
    Image31 = visual.ImageStim(win=win, image='./material/PicNback/31.png', size=(400,400))
    Image32 = visual.ImageStim(win=win, image='./material/PicNback/32.png', size=(400,400))
    Image33 = visual.ImageStim(win=win, image='./material/PicNback/33.png', size=(400,400))
    Instruction = visual.ImageStim(win=win, size=(1280,720))
    PractText = visual.TextStim(win=win, font='SimSun', color='white', pos=(0,0), height=45)
    PracClock = core.Clock()
    logging.info('Start OneBack')
    event.clearEvents()

# oneback practice
    while not event.getKeys(keyList=['space']):
        Instruction.image = './material/PicNback/InstrucOneBackPrac.png'
        Instruction.draw()
        win.flip()
    conditions = [{'Image':Image12, 'Resp':'right'},
                  {'Image':Image13, 'Resp':'right'},
                  {'Image':Image13, 'Resp':'left'},
                  {'Image':Image22, 'Resp':'right'},
                  {'Image':Image22, 'Resp':'left'}]
    OneBackPractice = data.TrialHandler(trialList=conditions, nReps=1, method='sequential')
    # blank screen for 1s
    win.flip(),core.wait(1)
    # Fixation for 1s
    Fixation.draw(),win.flip(), core.wait(1)
    # PreImage1 show for 1s
    Image11.draw(), win.flip(), core.wait(1)
    win.flip(),core.wait(1)
    for thisTrial in OneBackPractice:
        event.clearEvents(), core.wait(0.001)
        # blank screen for 1s
        win.flip(),core.wait(1)
        thisTrial['Image'].draw(), win.flip(),core.wait(1)
        Keys = []
        PracClock.reset()
        while PracClock.getTime() < 3:
            NewKey = event.getKeys(keyList=['left', 'right'])
            if NewKey: 
                Keys.extend(NewKey)
                break
            if PracClock.getTime() >1:
                win.flip(), core.wait(0.001)
        if Keys == []:
            PractText.text = '已超时，要快速作答哦'
            PractText.draw(), win.flip(), core.wait(1)
        elif Keys[0] == thisTrial['Resp']:
            PractText.text = '回答正确'
            PractText.draw(), win.flip(), core.wait(1)
        else:
            PractText.text = '回答错误'
            PractText.draw(), win.flip(), core.wait(1)

# oneback
    while not event.getKeys(keyList=['space']):
        Instruction.image = './material/PicNback/InstrucOneBack.png'
        Instruction.draw()
        win.flip()
    conditions = data.importConditions('./material/PicNback/Nback.xlsx')
    # conditions = data.importConditions('./material/PicNback/NbackDebug.xlsx')
    OneBackTrials = data.TrialHandler(trialList=conditions, nReps=1, method='sequential')
    ExpHandler.addLoop(OneBackTrials)
    respClock = core.Clock()
    # blank screen for 1s
    win.flip(),core.wait(1)
    # start to show fixation for 1s
    temp = GlobalClock.getTime()
    OneBackTrials.addData('FixationStart', temp)
    Fixation.draw(),win.flip(), core.wait(1)
    # blank screen for 1s
    win.flip(), core.wait(1)
    # PreImage1 show for 1s
    Image11.draw(), win.flip(), core.wait(1)
    for thisTrial in OneBackTrials:
        event.clearEvents()
        # blank screen for 1s
        win.flip(),core.wait(1)
        temp = GlobalClock.getTime()
        OneBackTrials.addData('OneBackImageStart', temp)
        # show stim for 1s (stop showing condition in while )
        eval(thisTrial['ImageOneBack']).draw(), win.flip()  
        Keys = []
        respClock.reset()
        while respClock.getTime() < 3:
            NewKey = event.getKeys(timeStamped=respClock, keyList=['left', 'right'])
            if NewKey: 
                Keys.extend(NewKey)
                break
            if respClock.getTime() >1:
                win.flip(), core.wait(0.001)
        if Keys:
            resp, rt = Keys[0]
            temp = GlobalClock.getTime()
            OneBackTrials.addData('OneBackRespTime', temp)
            if resp == thisTrial['RespOneBack'] : OneBackTrials.addData('OneBackCorr',1)
            else: OneBackTrials.addData('OneBackCorr',0)
            OneBackTrials.addData('OneBackResp', resp)
            OneBackTrials.addData('OneBackRt', rt)
            ExpHandler.nextEntry()
        else:
            PractText.setText('已超时，要快速作答哦'), PractText.draw(), win.flip(), core.wait(1), win.flip()
            OneBackTrials.addData('OneBackRespTime', None)
            OneBackTrials.addData('OneBackCorr', 0)
            OneBackTrials.addData('OneBackResp', None)
            OneBackTrials.addData('OneBackRt', None)
            ExpHandler.nextEntry()


# twoback practice
    while not event.getKeys(keyList=['space']):
        Instruction.image = './material/PicNback/InstrucTwoBackPrac.png'
        Instruction.draw()
        win.flip()
    conditions = [{'Image':Image13, 'Resp':'left'},
                  {'Image':Image33, 'Resp':'right'},
                  {'Image':Image21, 'Resp':'right'},
                  {'Image':Image33, 'Resp':'left'},
                  {'Image':Image11, 'Resp':'right'}]
    TwoBackPractice = data.TrialHandler(trialList=conditions, nReps=1, method='sequential')
    # blank screen for 1s
    win.flip(),core.wait(1)
    # Fixation for 1s
    Fixation.draw(),win.flip(), core.wait(1)
    # PreImage1 show for 1s
    Image13.draw(), win.flip(), core.wait(1)
    win.flip(),core.wait(1)
    # PreImage2 show for 1s
    Image23.draw(), win.flip(), core.wait(1)
    win.flip(),core.wait(1)
    for thisTrial in TwoBackPractice:
        event.clearEvents(), core.wait(0.001)
        # blank screen for 1s
        win.flip(),core.wait(1)
        thisTrial['Image'].draw(), win.flip(),core.wait(1)
        Keys = []
        PracClock.reset()
        while PracClock.getTime() < 3:
            NewKey = event.getKeys(keyList=['left', 'right'])
            if NewKey: 
                Keys.extend(NewKey)
                break
            if PracClock.getTime() >1:
                win.flip(), core.wait(0.001)
        if Keys == []:
            PractText.text = '已超时，要快速作答哦'
            PractText.draw(), win.flip(), core.wait(1)
        elif Keys[0] == thisTrial['Resp']:
            PractText.text = '回答正确'
            PractText.draw(), win.flip(), core.wait(1)
        else:
            PractText.text = '回答错误'
            PractText.draw(), win.flip(), core.wait(1)

# two back
    while not event.getKeys(keyList=['space']):
        Instruction.image = './material/PicNback/InstrucTwoBack.png'
        Instruction.draw()
        win.flip()
    conditions = data.importConditions('./material/PicNback/Nback.xlsx')
    TwoBackTrials = data.TrialHandler(trialList=conditions, nReps=1, method='sequential')
    ExpHandler.addLoop(TwoBackTrials)
    respClock = core.Clock()
    # blank screen for 1s
    win.flip(), core.wait(1)
    # Fixation for 1s
    temp = GlobalClock.getTime()
    TwoBackTrials.addData('Fixation', temp)
    Fixation.draw(),win.flip(), core.wait(1)
    # blank screen for 1s
    win.flip(), core.wait(1)
    # PreImage1 for 1s
    Image12.draw(), win.flip(), core.wait(1)
    # blank screen for 1s
    win.flip(), core.wait(1)
    # PreImage2 for 1s
    Image11.draw(), win.flip(), core.wait(1)
    for thisTrial in TwoBackTrials:
        event.clearEvents()
        # blank screen for 1s
        win.flip(),core.wait(1)
        temp = GlobalClock.getTime()
        TwoBackTrials.addData('TwoBackImageStart', temp)
        # show stim for 1s (stop showing condition in while )
        eval(thisTrial['ImageTwoBack']).draw(), win.flip()  
        Keys = []
        respClock.reset()
        while respClock.getTime() < 3:
            NewKey = event.getKeys(timeStamped=respClock, keyList=['left', 'right'])
            if NewKey: 
                Keys.extend(NewKey)
                break
            if respClock.getTime() >1:
                win.flip(), core.wait(0.001)
        if Keys:
            resp, rt = Keys[0]
            temp = GlobalClock.getTime()
            TwoBackTrials.addData('TwoBackRespTime', temp)
            if resp == thisTrial['RespTwoBack'] : TwoBackTrials.addData('TwoBackCorr',1)
            else: TwoBackTrials.addData('TwoBackCorr',0,)
            TwoBackTrials.addData('TwoBackResp', resp)
            TwoBackTrials.addData('TwoBackRt', rt)
            ExpHandler.nextEntry()
        else:
            PractText.setText('已超时，要快速作答哦'), PractText.draw(), win.flip(), core.wait(1), win.flip()
            TwoBackTrials.addData('TwoBackRespTime', None)
            TwoBackTrials.addData('TwoBackCorr', 0)
            TwoBackTrials.addData('TwoBackResp', None)
            TwoBackTrials.addData('TwoBackRt', None)
            ExpHandler.nextEntry()

# ThreeBack practice
    while not event.getKeys(keyList=['space']):
        Instruction.image = './material/PicNback/InstrucThreeBackPrac.png'
        Instruction.draw()
        win.flip()
    conditions = [{'Image':Image31, 'Resp':'right'},
                  {'Image':Image23, 'Resp':'left'},
                  {'Image':Image22, 'Resp':'left'},
                  {'Image':Image33, 'Resp':'right'},
                  {'Image':Image23, 'Resp':'left'}]
    ThreeBackPractice = data.TrialHandler(trialList=conditions, nReps=1, method='sequential')
    # blank screen for 1s
    win.flip(),core.wait(1)
    # Fixation for 1s
    Fixation.draw(),win.flip(), core.wait(1)
    # PreImage1 show for 1s
    Image13.draw(), win.flip(), core.wait(1)
    win.flip(),core.wait(1)
    # PreImage2 show for 1s
    Image23.draw(), win.flip(), core.wait(1)
    win.flip(),core.wait(1)
    # PreImage3 show for 1s
    Image22.draw(), win.flip(), core.wait(1)
    win.flip(),core.wait(1)
    for thisTrial in ThreeBackPractice:
        event.clearEvents(), core.wait(0.001)
        # blank screen for 1s
        win.flip(),core.wait(1)
        thisTrial['Image'].draw(), win.flip(),core.wait(1)
        Keys = []
        PracClock.reset()
        while PracClock.getTime() < 3:
            NewKey = event.getKeys(keyList=['left', 'right'])
            if NewKey: 
                Keys.extend(NewKey)
                break
            if PracClock.getTime() >1:
                win.flip(), core.wait(0.001)
        if Keys == []:
            PractText.text = '已超时，要快速作答哦'
            PractText.draw(), win.flip(), core.wait(1)
        elif Keys[0] == thisTrial['Resp']:
            PractText.text = '回答正确'
            PractText.draw(), win.flip(), core.wait(1)
        else:
            PractText.text = '回答错误'
            PractText.draw(), win.flip(), core.wait(1)

# three back
    while not event.getKeys(keyList=['space']):
        Instruction.image = './material/PicNback/InstrucThreeBack.png'
        Instruction.draw()
        win.flip()
    conditions = data.importConditions('./material/PicNback/Nback.xlsx')
    # conditions = data.importConditions('./material/PicNback/NbackDebug.xlsx')
    ThreeBackTrials = data.TrialHandler(trialList=conditions, nReps=1, method='sequential')
    ExpHandler.addLoop(ThreeBackTrials)
    respClock = core.Clock()
    # blank screen for 1s
    win.flip(), core.wait(1)
    temp = GlobalClock.getTime()
    ThreeBackTrials.addData('Fixation', temp)
    # Fixation for 1s
    Fixation.draw(), win.flip, core.wait(1)
    # blank screen for 1s
    win.flip(), core.wait(1)
    # PreImage1 for 1s
    Image13.draw(), win.flip(), core.wait(1)
    # blank screen for 1s
    win.flip(), core.wait(1)
    # PreImage2 for 1s
    Image22.draw(), win.flip(), core.wait(1)
    # blank screen for 1s
    win.flip(), core.wait(1)
    # PreImage3 for 1s
    Image31.draw(), win.flip(), core.wait(1)
    for thisTrial in ThreeBackTrials:
        event.clearEvents()
        # blank screen for 1s
        win.flip(),core.wait(1)
        temp = GlobalClock.getTime()
        ThreeBackTrials.addData('ThreeBackImageStart', temp)
        # show stim for 1s (stop showing condition in while )
        eval(thisTrial['ImageThreeBack']).draw(), win.flip()  
        Keys = []
        respClock.reset()
        while respClock.getTime() < 3:
            NewKey = event.getKeys(timeStamped=respClock, keyList=['left', 'right'])
            if NewKey: 
                Keys.extend(NewKey)
                break
            if respClock.getTime() >1:
                win.flip(), core.wait(0.001)
        if Keys:
            resp, rt = Keys[0]
            temp = GlobalClock.getTime()
            ThreeBackTrials.addData('ThreeBackRespTime', temp)
            if resp == thisTrial['RespThreeBack'] : ThreeBackTrials.addData('ThreeBackCorr',1)
            else: ThreeBackTrials.addData('ThreeBackCorr',0,)
            ThreeBackTrials.addData('ThreeBackResp', resp)
            ThreeBackTrials.addData('ThreeBackRt', rt)
            ExpHandler.nextEntry()
        else:
            PractText.setText('已超时，要快速作答哦'), PractText.draw(), win.flip(), core.wait(1), win.flip()
            ThreeBackTrials.addData('ThreeBackRespTime', None)
            ThreeBackTrials.addData('ThreeBackCorr', 0)
            ThreeBackTrials.addData('ThreeBackResp', None)
            ThreeBackTrials.addData('ThreeBackRt', None)
            ExpHandler.nextEntry() 

    # End recording
    ScriPath = os.getcwd()
    # VideoRecord.stop_recording(ScriPath+"/result/{}/{}".format(dirname,dirname+'_Nback.avi'))
    # AudioRecord.stop_recording(ScriPath+"/result/{}/{}".format(dirname,dirname+'_Nback.wav'))

if __name__ == '__main__':
    Para = sys.argv[1:]
    PicNback(Para[0], Para[1])