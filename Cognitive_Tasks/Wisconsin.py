from psychopy import visual, event, core, data, gui, logging
# from RecordVideo import VideoRecorder
# from RecordAudio import AudioRecorder
import pandas as pd
import numpy as np
import random
import os
import sys
import datetime


def Wisconsin(dirname, HosID):
    global win, Fixation, GlobalClock, \
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
    FilenameCsv = './result/{}/{}_Wisconsin'.format(dirname, dirname)
    FilenameLog = './result/{}/{}_Wisconsin.log'.format(dirname, dirname)
    ExpInfo = {'ExpName':'Wisconsin', 'DirName':dirname, 'date':Date, }
    ExpHandler = data.ExperimentHandler(name='Wisconsin', version='1.0', extraInfo=ExpInfo, 
                                        runtimeInfo=None, originPath=None, savePickle=True, 
                                        saveWideText=True, dataFileName=FilenameCsv)
    GlobalClock = core.Clock()
    TrialClock = core.Clock()
    logging.LogFile(FilenameLog, level=logging.INFO, filemode='w')
    logging.info('Start Wisconsin')
    win = visual.Window([1280,720], fullscr=False, units='pix')
    Fixation = visual.TextStim(win=win, text='+', height=40)
    ImageCR1 = visual.ImageStim(win=win, image='./material/Wisconsin/CR1.png',size=(126,154), pos=(-230,200))
    ImageTG2 = visual.ImageStim(win=win, image='./material/Wisconsin/TG2.png',size=(126,154), pos=(0,200))
    ImagePB3 = visual.ImageStim(win=win, image='./material/Wisconsin/PB3.png',size=(126,154), pos=(230,200))
    ImageSY4 = visual.ImageStim(win=win, image='./material/Wisconsin/SY4.png',size=(126,154), pos=(460,200))
    Instruc1 = visual.ImageStim(win=win, image='./material/Wisconsin/Instruc1.png',size=(1280,720))
    Instruc2 = visual.ImageStim(win=win, image='./material/Wisconsin/Instruc2.png',size=(1280,720))
    ImageResp = visual.ImageStim(win=win, size=(126,154), pos=(-500,-100))
    ImageCorr = visual.ImageStim(win=win, size=(70, 70))
    Selection1 = visual.TextStim(win=win, text='1', height=30, pos=(-230,100))
    Selection2 = visual.TextStim(win=win, text='2', height=30, pos=(0,100))
    Selection3 = visual.TextStim(win=win, text='3', height=30, pos=(230,100))
    Selection4 = visual.TextStim(win=win, text='4', height=30, pos=(460,100))
    Pos0 = (-500,-100)
    Pos1 = (-230, -100)
    Pos2 = (0, -100)
    Pos3 = (230, -100)
    Pos4 = (460, -100)
    PosList = [Pos0, Pos1, Pos2, Pos3]
    CorrPos1 = (-230, -230)
    CorrPos2 = (0, -230)
    CorrPos3 = (230, -230)
    CorrPos4 = (460, -230)
    logging.info("Start Wisconsin", )
    event.clearEvents()
    MaterialDir = './material/Wisconsin'
    respClock = core.Clock()
    combo = 0
    BreakSwitch = 0
    for i in range(100):
        SpaceUnPress = 1
        UpPress = 0
        if BreakSwitch: break
        while SpaceUnPress:
            Instruc1.draw()
            win.flip()
            if event.getKeys(['space']):
                SpaceUnPress = 0
                UpPress = 1
        while UpPress:
            Instruc2.draw()
            win.flip()
            if event.getKeys(['up']):
                UpPress = 0
            if event.getKeys(['space']):
                BreakSwitch = 1
                UpPress = 0

    conditions = data.importConditions('./material/Wisconsin/Wisconsin.xlsx')
    trials = data.TrialHandler(trialList=conditions, nReps=1, method='sequential')
    ExpHandler.addLoop(trials)
    for thisTrial in trials:
        ImageResp.setPos(Pos0)
        ImageCorr.setSize((70,70))
        respClock.reset()
        event.clearEvents()
        temp = GlobalClock.getTime()
        trials.addData('ImageStimTime', temp)
        KeyPress = 0 
        if combo == 5 and thisTrial['Sequence'] < 10: 
            trials.addData('KeyRespTime', '')
            trials.addData('KeyResp', '')
            trials.addData('RespRt', '')
            trials.addData('RespCorr', '')
            trials.addData('RespPreTask', '')
            ExpHandler.nextEntry()
            continue
        elif combo == 5 and thisTrial['Sequence'] == 10: 
            combo = 0
            trials.addData('CatagoryScore',1)
            ExpHandler.nextEntry()
            continue
        TrialClock.reset()
        while TrialClock.getTime() <= 5:
            ImageCR1.draw()
            ImageTG2.draw()
            ImagePB3.draw()
            ImageSY4.draw()
            Selection1.draw()
            Selection2.draw()
            Selection3.draw()
            Selection4.draw()
            ImageResp.setImage('/'.join([MaterialDir,thisTrial['Card']+'.png']))
            ImageResp.draw()
            win.flip()
            for key in event.getKeys():
                if key in ['1','2','3','4','num_1','num_2','num_3','num_4',]:
                    temp = GlobalClock.getTime()
                    trials.addData('KeyRespTime', temp)
                    temp = respClock.getTime()
                    trials.addData('KeyResp', key)
                    trials.addData('RespRt', temp)
                    KeyPress = 1
                    break
            if KeyPress == 1: break
        if KeyPress == 1:
            if key == 'num_1': key = 1
            elif key == 'num_2': key = 2
            elif key == 'num_3': key = 3
            elif key == 'num_4': key = 4            
            if int(key) == int(thisTrial['CorrResp']):
                trials.addData('RespCorr', 1), trials.addData('RespPreTask',0)
                ImageCorr.image = './material/Wisconsin/correct.png'
                combo += 1
                ExpHandler.nextEntry()
                if combo == 5 and thisTrial['Sequence'] == 10:
                    trials.addData('CatagoryScore',1)
                    ExpHandler.nextEntry()
                    combo = 0
            elif int(key) == int(thisTrial['PreResp']):
                trials.addData('RespCorr', 0), trials.addData('RespPreTask',1)
                ImageCorr.image = './material/Wisconsin/error.png'
                combo = 0
                ExpHandler.nextEntry()
            else: 
                trials.addData('RespCorr', 0), trials.addData('RespPreTask',0)  
                ImageCorr.image = './material/Wisconsin/error.png'
                combo = 0  
                ExpHandler.nextEntry()
        else :
            key = 999
            combo = 0
            trials.addData('KeyRespTime', None)
            trials.addData('KeyResp', None)
            trials.addData('RespRt', None)
            trials.addData('RespCorr', 0)
            trials.addData('RespPreTask', 0)
            ExpHandler.nextEntry()
            ImageCorr.image = './material/Wisconsin/tooslow.png'
            ImageCorr.setSize((550,80))
        TrialClock.reset()
        while TrialClock.getTime() <= 1:
            ImageCR1.draw()
            ImageTG2.draw()
            ImagePB3.draw()
            ImageSY4.draw()
            Selection1.draw()
            Selection2.draw()
            Selection3.draw()
            Selection4.draw()
            if int(key) == 1:ImageResp.setPos(Pos1), ImageCorr.setPos(CorrPos1), ImageResp.draw()
            elif int(key) == 2:ImageResp.setPos(Pos2), ImageCorr.setPos(CorrPos2), ImageResp.draw()
            elif int(key) == 3:ImageResp.setPos(Pos3), ImageCorr.setPos(CorrPos3), ImageResp.draw()
            elif int(key) == 4:ImageResp.setPos(Pos4), ImageCorr.setPos(CorrPos4), ImageResp.draw()
            else: ImageCorr.setPos((0,-100))
            ImageCorr.draw()
            win.flip()

    # End recording
    ScriPath = os.getcwd()
    # VideoRecord.stop_recording(ScriPath+"/result/{}/{}".format(dirname,dirname+'_Wisconsin.avi'))
    # AudioRecord.stop_recording(ScriPath+"/result/{}/{}".format(dirname,dirname+'_Wisconsin.wav'))

if __name__ == '__main__':
    Para = sys.argv[1:]
    Wisconsin(Para[0], Para[1])