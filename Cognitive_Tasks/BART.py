from psychopy import visual, event, core, data, gui, logging
# from RecordVideo import VideoRecorder
# from RecordAudio import AudioRecorder
import pandas as pd
import random
import os
import sys
import datetime

def BART(dirname, HosID):
    global win, Fixation, ImageList, Image11,Image12,Image13,Image21,\
            Image22,Image23,Image31,Image32,Image33, GlobalClock, \
            Filename
    # Start recording
    # VideoRecord = VideoRecorder()
    # AudioRecord = AudioRecorder()
    # VideoRecord.start_recording()
    # AudioRecord.start_recording()
    # stimulus variety list
    dirname = dirname
    Today = datetime.datetime.now()
    Year = Today.year
    Month = Today.month
    Day = Today.day
    Hour = Today.hour
    Min = Today.minute
    Date = "_".join([str(Year)+str('{:0>2d}'.format(Month))+str('{:0>2d}'.format(Day))+\
                     str('{:0>2d}'.format(Hour))+str('{:0>2d}'.format(Min))])
    Filename = "_".join([dirname, Date])
    FilenameCsv = './result/{}/{}_BART'.format(dirname, dirname)
    FilenameLog = './result/{}/{}_BART.log'.format(dirname, dirname)
    ExpInfo = {'ExpName':'BART', 'DirName':dirname, 'date':Date, }
    ExpHandler = data.ExperimentHandler(name='BART', version='1.0', extraInfo=ExpInfo, 
                                        runtimeInfo=None, originPath=None, savePickle=True, 
                                        saveWideText=True, dataFileName=FilenameCsv)
    GlobalClock = core.Clock()
    logging.LogFile(FilenameLog, level=logging.INFO, filemode='w')
    logging.info('start')
    win = visual.Window([1280,720], fullscr=False, units='pix')
    print(win.getActualFrameRate())
    Fixation = visual.TextStim(win=win, text='+', height=40)
    OriSize = (30,40)
    OriPos = (0,-20)
    BalloonImg = visual.ImageStim(win=win,size=OriSize, pos=OriPos)
    # BlueBalloon = visual.ImageStim(win=win, image='./material/BART/blue.png',size=OriSize, pos=OriPos)
    # GreenBalloon = visual.ImageStim(win=win, image='./material/BART/green.png',size=OriSize, pos=OriPos)
    Boom = visual.ImageStim(win=win, image='./material/BART/boom.png',size=(300,286), pos=(0,0))
    EnterImg = visual.ImageStim(win=win, image='./material/BART/enter.png',size=(333,125), pos=(-400,-120))
    SpaceImg = visual.ImageStim(win=win, image='./material/BART/space.png',size=(333,125), pos=(-0,-120))
    TotalImg = visual.ImageStim(win=win, image='./material/BART/total.png',size=(331,125), pos=(400,-20))
    LastImg = visual.ImageStim(win=win, image='./material/BART/last.png',size=(331,125), pos=(400,-170))
    Instruc = visual.ImageStim(win=win, image='./material/BART/Instruc.png',size=(1280,720))

    TotalScore = 0
    LastScore = 0
    TotalText = visual.TextStim(win=win, text='{:.2f}分'.format(TotalScore), pos = (500, -20), font='SimHei', color='black')
    LastText = visual.TextStim(win=win, text='{:.2f}分'.format(LastScore), pos = (500, -170), font='SimHei', color='black')
    logging.info("Start BART", )
    while not event.getKeys(keyList=['space']):
        Instruc.draw()
        win.flip()
    event.clearEvents()
    respClock = core.Clock()
    conditions = data.importConditions('./material/BART/BART.xlsx')
    trials = data.TrialHandler(trialList = conditions, nReps = 1, method='sequential')
    ExpHandler.addLoop(trials)
    for thisTrial in trials:
        LastScore = 0
        EnterClick = 1
        SizeX, SizeY = OriSize
        PosX, PosY = OriPos
        BalloonImg.image = './material/BART/{}.png'.format(thisTrial['Condition'])
        BalloonImg.size = (SizeX, SizeY)
        BalloonImg.pos = (PosX, PosY)
        OneZeroList = [0] * (thisTrial['Max']-1) + [1] 
        event.clearEvents()
        EnterImg.draw()
        SpaceImg.draw()
        TotalImg.draw()
        LastImg.draw()
        BalloonImg.draw()
        random.shuffle(OneZeroList)
        OneIndex = OneZeroList.index(1)
        trials.addData('BoomIndex', OneIndex)
        LastText.draw()
        TotalText.draw()
        win.flip()
        while EnterClick:
            event.clearEvents()
            respClock.reset()
            keys = event.waitKeys(keyList=['space','return'])
            temp = GlobalClock.getTime()
            trials.addData('GlobalTime', temp)
            temp = respClock.getTime()
            trials.addData('ReactTime', temp)
            trials.addData('RespKey', keys[0])
            if keys[0]=='space':
                if OneZeroList[0] == 0:
                    SizeX += 3
                    SizeY += 3
                    PosY += 1.5
                    LastScore += 0.05
                    BalloonImg.size = [SizeX, SizeY]
                    BalloonImg.pos = [PosX, PosY]
                    EnterImg.draw()
                    SpaceImg.draw()
                    TotalImg.draw()
                    LastImg.draw()
                    BalloonImg.draw()
                    LastText.draw()
                    TotalText.text = '{:.2f}分'.format(TotalScore)
                    TotalText.draw()                    
                    OneZeroList.remove(0)
                    random.shuffle(OneZeroList)
                    OneIndex = OneZeroList.index(1)
                    trials.addData('LastScore', LastScore)
                    trials.addData('TotalScore', TotalScore)
                    trials.addData('BoomIndex', OneIndex)
                    win.flip()
                elif OneZeroList[0] == 1:
                    LastScore = 0
                    LastText.text = '{:.2f}分'.format(LastScore)
                    trials.addData('LastScore', LastScore)
                    trials.addData('TotalScore', TotalScore)
                    Boom.draw(), win.flip(), core.wait(1)                        
                    trials.addData('Boom', 1)
                    EnterClick = 0
            elif keys[0] == 'return':
                TotalScore += LastScore
                LastText.text = '{:.2f}分'.format(LastScore)
                LastText.draw()
                TotalText.text = '{:.2f}分'.format(TotalScore)
                TotalText.draw() 
                trials.addData('LastScore', LastScore)
                trials.addData('TotalScore', TotalScore)
                EnterClick = 0
            ExpHandler.nextEntry()

    # End recording
    ScriPath = os.getcwd()
    # VideoRecord.stop_recording(ScriPath+"/result/{}/{}".format(dirname,dirname+'_BART.avi'))
    # AudioRecord.stop_recording(ScriPath+"/result/{}/{}".format(dirname,dirname+'_BART.wav'))

if __name__ == '__main__':
    Para = sys.argv[1:]
    BART(Para[0], Para[1])