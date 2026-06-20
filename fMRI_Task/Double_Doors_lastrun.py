#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on 十二月 10, 2024, at 15:01
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'Double_Doors'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    '性别[男1女2]': '',
    '年龄': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\Tianxiulingjianguoyun\\24级发教田秀玲\\开门大吉\\Double_Doors_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[2560, 1440], fullscr=True, screen=1, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "introduce1" ---
intro_image1 = visual.ImageStim(
    win=win,
    name='intro_image1', units='height', 
    image='images/introduce1.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.5, 0.556),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
intro_key_resp1 = keyboard.Keyboard()

# --- Initialize components for Routine "introduce2" ---
intro_image2 = visual.ImageStim(
    win=win,
    name='intro_image2', units='height', 
    image='images/introduce2.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.5, 0.556),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
intro_key_resp2 = keyboard.Keyboard()

# --- Initialize components for Routine "introduce3" ---
intro_image3 = visual.ImageStim(
    win=win,
    name='intro_image3', units='height', 
    image='images/introduce3.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.5, 0.556),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
intro_key_resp3 = keyboard.Keyboard()

# --- Initialize components for Routine "introduce4" ---
intro_image4 = visual.ImageStim(
    win=win,
    name='intro_image4', units='height', 
    image='images/introduce4.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.5, 0.556),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
intro_key_resp4 = keyboard.Keyboard()

# --- Initialize components for Routine "Trigger" ---
trigger = visual.TextStim(win=win, name='trigger',
    text='"等待医师开始扫描"',
    font='Open Sans',
    units='height', pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
trigger_resp = keyboard.Keyboard()

# --- Initialize components for Routine "NULL" ---
NULLtext = visual.TextStim(win=win, name='NULLtext',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Fixation" ---
fixation = visual.ShapeStim(
    win=win, name='fixation', vertices='cross',units='height', 
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "select" ---
two_doors = visual.ImageStim(
    win=win,
    name='two_doors', units='height', 
    image='images/two_door.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.5, 0.653),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
selet_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "waiting1" ---
# Run 'Begin Experiment' code from waiting_code1
#LOOP1
waiting_image1 = ''
waiting_image_1 = visual.ImageStim(
    win=win,
    name='waiting_image_1', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.5, 0.653),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "feedback1" ---
# Run 'Begin Experiment' code from fadebact_code1
#LOOP1
feedback_image1 = ''
Money_text1 = 100
feedback_image_1 = visual.ImageStim(
    win=win,
    name='feedback_image_1', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.5, 0.653),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Money_text_1 = visual.TextStim(win=win, name='Money_text_1',
    text='',
    font='Open Sans',
    pos=(0.13, -0.095), height=0.05, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "resting" ---
rest_image = visual.ImageStim(
    win=win,
    name='rest_image', units='height', 
    image='images/resting.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.5, 0.332),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "Fixation" ---
fixation = visual.ShapeStim(
    win=win, name='fixation', vertices='cross',units='height', 
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "select" ---
two_doors = visual.ImageStim(
    win=win,
    name='two_doors', units='height', 
    image='images/two_door.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.5, 0.653),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
selet_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "waiting2" ---
# Run 'Begin Experiment' code from waiting_code2
#LOOP2
waiting_image2 = ''

waiting_image_2 = visual.ImageStim(
    win=win,
    name='waiting_image_2', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.5, 0.653),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "feedback2" ---
# Run 'Begin Experiment' code from feedback_code2
#LOOP2
feedback_image2 = ''

feedback_image_2 = visual.ImageStim(
    win=win,
    name='feedback_image_2', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.5, 0.653),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Money_text_2 = visual.TextStim(win=win, name='Money_text_2',
    text='',
    font='Open Sans',
    pos=(0.13, -0.095), height=0.05, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "ending" ---
end_image = visual.ImageStim(
    win=win,
    name='end_image', units='height', 
    image='images/ending.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.5, 0.542),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "introduce1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
intro_key_resp1.keys = []
intro_key_resp1.rt = []
_intro_key_resp1_allKeys = []
# keep track of which components have finished
introduce1Components = [intro_image1, intro_key_resp1]
for thisComponent in introduce1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "introduce1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro_image1* updates
    if intro_image1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_image1.frameNStart = frameN  # exact frame index
        intro_image1.tStart = t  # local t and not account for scr refresh
        intro_image1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_image1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'intro_image1.started')
        intro_image1.setAutoDraw(True)
    
    # *intro_key_resp1* updates
    if intro_key_resp1.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_key_resp1.frameNStart = frameN  # exact frame index
        intro_key_resp1.tStart = t  # local t and not account for scr refresh
        intro_key_resp1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_key_resp1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('intro_key_resp1.started', t)
        intro_key_resp1.status = STARTED
        # keyboard checking is just starting
        intro_key_resp1.clock.reset()  # now t=0
        intro_key_resp1.clearEvents(eventType='keyboard')
    if intro_key_resp1.status == STARTED:
        theseKeys = intro_key_resp1.getKeys(keyList=['1','2','3','4'], waitRelease=False)
        _intro_key_resp1_allKeys.extend(theseKeys)
        if len(_intro_key_resp1_allKeys):
            intro_key_resp1.keys = _intro_key_resp1_allKeys[-1].name  # just the last key pressed
            intro_key_resp1.rt = _intro_key_resp1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introduce1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "introduce1" ---
for thisComponent in introduce1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if intro_key_resp1.keys in ['', [], None]:  # No response was made
    intro_key_resp1.keys = None
thisExp.addData('intro_key_resp1.keys',intro_key_resp1.keys)
if intro_key_resp1.keys != None:  # we had a response
    thisExp.addData('intro_key_resp1.rt', intro_key_resp1.rt)
thisExp.nextEntry()
# the Routine "introduce1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "introduce2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
intro_key_resp2.keys = []
intro_key_resp2.rt = []
_intro_key_resp2_allKeys = []
# keep track of which components have finished
introduce2Components = [intro_image2, intro_key_resp2]
for thisComponent in introduce2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "introduce2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro_image2* updates
    if intro_image2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_image2.frameNStart = frameN  # exact frame index
        intro_image2.tStart = t  # local t and not account for scr refresh
        intro_image2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_image2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'intro_image2.started')
        intro_image2.setAutoDraw(True)
    
    # *intro_key_resp2* updates
    waitOnFlip = False
    if intro_key_resp2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_key_resp2.frameNStart = frameN  # exact frame index
        intro_key_resp2.tStart = t  # local t and not account for scr refresh
        intro_key_resp2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_key_resp2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'intro_key_resp2.started')
        intro_key_resp2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(intro_key_resp2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(intro_key_resp2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if intro_key_resp2.status == STARTED and not waitOnFlip:
        theseKeys = intro_key_resp2.getKeys(keyList=['1','2','3','4'], waitRelease=False)
        _intro_key_resp2_allKeys.extend(theseKeys)
        if len(_intro_key_resp2_allKeys):
            intro_key_resp2.keys = _intro_key_resp2_allKeys[-1].name  # just the last key pressed
            intro_key_resp2.rt = _intro_key_resp2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introduce2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "introduce2" ---
for thisComponent in introduce2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if intro_key_resp2.keys in ['', [], None]:  # No response was made
    intro_key_resp2.keys = None
thisExp.addData('intro_key_resp2.keys',intro_key_resp2.keys)
if intro_key_resp2.keys != None:  # we had a response
    thisExp.addData('intro_key_resp2.rt', intro_key_resp2.rt)
thisExp.nextEntry()
# the Routine "introduce2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "introduce3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
intro_key_resp3.keys = []
intro_key_resp3.rt = []
_intro_key_resp3_allKeys = []
# keep track of which components have finished
introduce3Components = [intro_image3, intro_key_resp3]
for thisComponent in introduce3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "introduce3" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro_image3* updates
    if intro_image3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_image3.frameNStart = frameN  # exact frame index
        intro_image3.tStart = t  # local t and not account for scr refresh
        intro_image3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_image3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'intro_image3.started')
        intro_image3.setAutoDraw(True)
    
    # *intro_key_resp3* updates
    waitOnFlip = False
    if intro_key_resp3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_key_resp3.frameNStart = frameN  # exact frame index
        intro_key_resp3.tStart = t  # local t and not account for scr refresh
        intro_key_resp3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_key_resp3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'intro_key_resp3.started')
        intro_key_resp3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(intro_key_resp3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(intro_key_resp3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if intro_key_resp3.status == STARTED and not waitOnFlip:
        theseKeys = intro_key_resp3.getKeys(keyList=['1','2','3','4'], waitRelease=False)
        _intro_key_resp3_allKeys.extend(theseKeys)
        if len(_intro_key_resp3_allKeys):
            intro_key_resp3.keys = _intro_key_resp3_allKeys[-1].name  # just the last key pressed
            intro_key_resp3.rt = _intro_key_resp3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introduce3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "introduce3" ---
for thisComponent in introduce3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if intro_key_resp3.keys in ['', [], None]:  # No response was made
    intro_key_resp3.keys = None
thisExp.addData('intro_key_resp3.keys',intro_key_resp3.keys)
if intro_key_resp3.keys != None:  # we had a response
    thisExp.addData('intro_key_resp3.rt', intro_key_resp3.rt)
thisExp.nextEntry()
# the Routine "introduce3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "introduce4" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
intro_key_resp4.keys = []
intro_key_resp4.rt = []
_intro_key_resp4_allKeys = []
# keep track of which components have finished
introduce4Components = [intro_image4, intro_key_resp4]
for thisComponent in introduce4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "introduce4" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro_image4* updates
    if intro_image4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_image4.frameNStart = frameN  # exact frame index
        intro_image4.tStart = t  # local t and not account for scr refresh
        intro_image4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_image4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'intro_image4.started')
        intro_image4.setAutoDraw(True)
    
    # *intro_key_resp4* updates
    waitOnFlip = False
    if intro_key_resp4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_key_resp4.frameNStart = frameN  # exact frame index
        intro_key_resp4.tStart = t  # local t and not account for scr refresh
        intro_key_resp4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_key_resp4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'intro_key_resp4.started')
        intro_key_resp4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(intro_key_resp4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(intro_key_resp4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if intro_key_resp4.status == STARTED and not waitOnFlip:
        theseKeys = intro_key_resp4.getKeys(keyList=['1','2','3','4'], waitRelease=False)
        _intro_key_resp4_allKeys.extend(theseKeys)
        if len(_intro_key_resp4_allKeys):
            intro_key_resp4.keys = _intro_key_resp4_allKeys[-1].name  # just the last key pressed
            intro_key_resp4.rt = _intro_key_resp4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introduce4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "introduce4" ---
for thisComponent in introduce4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if intro_key_resp4.keys in ['', [], None]:  # No response was made
    intro_key_resp4.keys = None
thisExp.addData('intro_key_resp4.keys',intro_key_resp4.keys)
if intro_key_resp4.keys != None:  # we had a response
    thisExp.addData('intro_key_resp4.rt', intro_key_resp4.rt)
thisExp.nextEntry()
# the Routine "introduce4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Trigger" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
trigger_resp.keys = []
trigger_resp.rt = []
_trigger_resp_allKeys = []
# keep track of which components have finished
TriggerComponents = [trigger, trigger_resp]
for thisComponent in TriggerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Trigger" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *trigger* updates
    if trigger.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trigger.frameNStart = frameN  # exact frame index
        trigger.tStart = t  # local t and not account for scr refresh
        trigger.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trigger, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'trigger.started')
        trigger.setAutoDraw(True)
    
    # *trigger_resp* updates
    waitOnFlip = False
    if trigger_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trigger_resp.frameNStart = frameN  # exact frame index
        trigger_resp.tStart = t  # local t and not account for scr refresh
        trigger_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trigger_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'trigger_resp.started')
        trigger_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(trigger_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(trigger_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if trigger_resp.status == STARTED and not waitOnFlip:
        theseKeys = trigger_resp.getKeys(keyList=['s'], waitRelease=False)
        _trigger_resp_allKeys.extend(theseKeys)
        if len(_trigger_resp_allKeys):
            trigger_resp.keys = _trigger_resp_allKeys[-1].name  # just the last key pressed
            trigger_resp.rt = _trigger_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TriggerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Trigger" ---
for thisComponent in TriggerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if trigger_resp.keys in ['', [], None]:  # No response was made
    trigger_resp.keys = None
thisExp.addData('trigger_resp.keys',trigger_resp.keys)
if trigger_resp.keys != None:  # we had a response
    thisExp.addData('trigger_resp.rt', trigger_resp.rt)
thisExp.nextEntry()
# the Routine "Trigger" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "NULL" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
NULLComponents = [NULLtext]
for thisComponent in NULLComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "NULL" ---
while continueRoutine and routineTimer.getTime() < 4.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *NULLtext* updates
    if NULLtext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        NULLtext.frameNStart = frameN  # exact frame index
        NULLtext.tStart = t  # local t and not account for scr refresh
        NULLtext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(NULLtext, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'NULLtext.started')
        NULLtext.setAutoDraw(True)
    if NULLtext.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > NULLtext.tStartRefresh + 4.0-frameTolerance:
            # keep track of stop time/frame for later
            NULLtext.tStop = t  # not accounting for scr refresh
            NULLtext.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NULLtext.stopped')
            NULLtext.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in NULLComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "NULL" ---
for thisComponent in NULLComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-4.000000)

# set up handler to look after randomisation of conditions etc
LOOP_1 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('documents/loop1.xlsx'),
    seed=None, name='LOOP_1')
thisExp.addLoop(LOOP_1)  # add the loop to the experiment
thisLOOP_1 = LOOP_1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLOOP_1.rgb)
if thisLOOP_1 != None:
    for paramName in thisLOOP_1:
        exec('{} = thisLOOP_1[paramName]'.format(paramName))

for thisLOOP_1 in LOOP_1:
    currentLoop = LOOP_1
    # abbreviate parameter names if possible (e.g. rgb = thisLOOP_1.rgb)
    if thisLOOP_1 != None:
        for paramName in thisLOOP_1:
            exec('{} = thisLOOP_1[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Fixation" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    FixationComponents = [fixation]
    for thisComponent in FixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Fixation" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation.started')
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation.stopped')
                fixation.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Fixation" ---
    for thisComponent in FixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "select" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    selet_key_resp.keys = []
    selet_key_resp.rt = []
    _selet_key_resp_allKeys = []
    # keep track of which components have finished
    selectComponents = [two_doors, selet_key_resp]
    for thisComponent in selectComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "select" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *two_doors* updates
        if two_doors.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            two_doors.frameNStart = frameN  # exact frame index
            two_doors.tStart = t  # local t and not account for scr refresh
            two_doors.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(two_doors, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'two_doors.started')
            two_doors.setAutoDraw(True)
        if two_doors.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > two_doors.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                two_doors.tStop = t  # not accounting for scr refresh
                two_doors.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'two_doors.stopped')
                two_doors.setAutoDraw(False)
        
        # *selet_key_resp* updates
        waitOnFlip = False
        if selet_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            selet_key_resp.frameNStart = frameN  # exact frame index
            selet_key_resp.tStart = t  # local t and not account for scr refresh
            selet_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(selet_key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'selet_key_resp.started')
            selet_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(selet_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(selet_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if selet_key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > selet_key_resp.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                selet_key_resp.tStop = t  # not accounting for scr refresh
                selet_key_resp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'selet_key_resp.stopped')
                selet_key_resp.status = FINISHED
        if selet_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = selet_key_resp.getKeys(keyList=['1','2','3','4'], waitRelease=False)
            _selet_key_resp_allKeys.extend(theseKeys)
            if len(_selet_key_resp_allKeys):
                selet_key_resp.keys = _selet_key_resp_allKeys[-1].name  # just the last key pressed
                selet_key_resp.rt = _selet_key_resp_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in selectComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "select" ---
    for thisComponent in selectComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if selet_key_resp.keys in ['', [], None]:  # No response was made
        selet_key_resp.keys = None
    LOOP_1.addData('selet_key_resp.keys',selet_key_resp.keys)
    if selet_key_resp.keys != None:  # we had a response
        LOOP_1.addData('selet_key_resp.rt', selet_key_resp.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    
    # --- Prepare to start Routine "waiting1" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from waiting_code1
    if selet_key_resp.keys != None:
        if selet_key_resp.keys == '1'or selet_key_resp.keys == '2':
            waiting_image1 = waiting_path_L
        elif selet_key_resp.keys == '3'or selet_key_resp.keys == '4':
            waiting_image1 = waiting_path_R
    else:
        waiting_image1 = waiting_path_non
    waiting_image_1.setImage(waiting_image1)
    # keep track of which components have finished
    waiting1Components = [waiting_image_1]
    for thisComponent in waiting1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "waiting1" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *waiting_image_1* updates
        if waiting_image_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            waiting_image_1.frameNStart = frameN  # exact frame index
            waiting_image_1.tStart = t  # local t and not account for scr refresh
            waiting_image_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(waiting_image_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'waiting_image_1.started')
            waiting_image_1.setAutoDraw(True)
        if waiting_image_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > waiting_image_1.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                waiting_image_1.tStop = t  # not accounting for scr refresh
                waiting_image_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'waiting_image_1.stopped')
                waiting_image_1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in waiting1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "waiting1" ---
    for thisComponent in waiting1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    
    # --- Prepare to start Routine "feedback1" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from fadebact_code1
    
    if selet_key_resp.keys != None:
        if selet_key_resp.keys == '1'or selet_key_resp.keys == '2':
            Money_text1 += MONEY
            feedback_image1 = feedback_path_L
        elif selet_key_resp.keys == '3'or selet_key_resp.keys == '4':
            Money_text1 += MONEY
            feedback_image1 = feedback_path_R
    else:
        Money_text1 += 0
        feedback_image1 = feedback_path_non
    feedback_image_1.setImage(feedback_image1)
    Money_text_1.setText(Money_text1)
    # keep track of which components have finished
    feedback1Components = [feedback_image_1, Money_text_1]
    for thisComponent in feedback1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "feedback1" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_image_1* updates
        if feedback_image_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_image_1.frameNStart = frameN  # exact frame index
            feedback_image_1.tStart = t  # local t and not account for scr refresh
            feedback_image_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_image_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback_image_1.started')
            feedback_image_1.setAutoDraw(True)
        if feedback_image_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_image_1.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                feedback_image_1.tStop = t  # not accounting for scr refresh
                feedback_image_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_image_1.stopped')
                feedback_image_1.setAutoDraw(False)
        
        # *Money_text_1* updates
        if Money_text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Money_text_1.frameNStart = frameN  # exact frame index
            Money_text_1.tStart = t  # local t and not account for scr refresh
            Money_text_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Money_text_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Money_text_1.started')
            Money_text_1.setAutoDraw(True)
        if Money_text_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Money_text_1.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                Money_text_1.tStop = t  # not accounting for scr refresh
                Money_text_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Money_text_1.stopped')
                Money_text_1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedback1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback1" ---
    for thisComponent in feedback1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from fadebact_code1
    Money_text2 = Money_text1
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'LOOP_1'


# --- Prepare to start Routine "resting" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
restingComponents = [rest_image]
for thisComponent in restingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "resting" ---
while continueRoutine and routineTimer.getTime() < 6.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rest_image* updates
    if rest_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rest_image.frameNStart = frameN  # exact frame index
        rest_image.tStart = t  # local t and not account for scr refresh
        rest_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rest_image, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'rest_image.started')
        rest_image.setAutoDraw(True)
    if rest_image.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rest_image.tStartRefresh + 6.0-frameTolerance:
            # keep track of stop time/frame for later
            rest_image.tStop = t  # not accounting for scr refresh
            rest_image.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'rest_image.stopped')
            rest_image.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "resting" ---
for thisComponent in restingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-6.000000)

# set up handler to look after randomisation of conditions etc
LOOP_2 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('documents/loop2.xlsx'),
    seed=None, name='LOOP_2')
thisExp.addLoop(LOOP_2)  # add the loop to the experiment
thisLOOP_2 = LOOP_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLOOP_2.rgb)
if thisLOOP_2 != None:
    for paramName in thisLOOP_2:
        exec('{} = thisLOOP_2[paramName]'.format(paramName))

for thisLOOP_2 in LOOP_2:
    currentLoop = LOOP_2
    # abbreviate parameter names if possible (e.g. rgb = thisLOOP_2.rgb)
    if thisLOOP_2 != None:
        for paramName in thisLOOP_2:
            exec('{} = thisLOOP_2[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Fixation" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    FixationComponents = [fixation]
    for thisComponent in FixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Fixation" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation.started')
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation.stopped')
                fixation.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Fixation" ---
    for thisComponent in FixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "select" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    selet_key_resp.keys = []
    selet_key_resp.rt = []
    _selet_key_resp_allKeys = []
    # keep track of which components have finished
    selectComponents = [two_doors, selet_key_resp]
    for thisComponent in selectComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "select" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *two_doors* updates
        if two_doors.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            two_doors.frameNStart = frameN  # exact frame index
            two_doors.tStart = t  # local t and not account for scr refresh
            two_doors.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(two_doors, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'two_doors.started')
            two_doors.setAutoDraw(True)
        if two_doors.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > two_doors.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                two_doors.tStop = t  # not accounting for scr refresh
                two_doors.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'two_doors.stopped')
                two_doors.setAutoDraw(False)
        
        # *selet_key_resp* updates
        waitOnFlip = False
        if selet_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            selet_key_resp.frameNStart = frameN  # exact frame index
            selet_key_resp.tStart = t  # local t and not account for scr refresh
            selet_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(selet_key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'selet_key_resp.started')
            selet_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(selet_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(selet_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if selet_key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > selet_key_resp.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                selet_key_resp.tStop = t  # not accounting for scr refresh
                selet_key_resp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'selet_key_resp.stopped')
                selet_key_resp.status = FINISHED
        if selet_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = selet_key_resp.getKeys(keyList=['1','2','3','4'], waitRelease=False)
            _selet_key_resp_allKeys.extend(theseKeys)
            if len(_selet_key_resp_allKeys):
                selet_key_resp.keys = _selet_key_resp_allKeys[-1].name  # just the last key pressed
                selet_key_resp.rt = _selet_key_resp_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in selectComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "select" ---
    for thisComponent in selectComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if selet_key_resp.keys in ['', [], None]:  # No response was made
        selet_key_resp.keys = None
    LOOP_2.addData('selet_key_resp.keys',selet_key_resp.keys)
    if selet_key_resp.keys != None:  # we had a response
        LOOP_2.addData('selet_key_resp.rt', selet_key_resp.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    
    # --- Prepare to start Routine "waiting2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from waiting_code2
    if selet_key_resp.keys != None:
        if selet_key_resp.keys == '1'or selet_key_resp.keys == '2':
            waiting_image2 = waiting_path_L
        elif selet_key_resp.keys == '3'or selet_key_resp.keys == '4':
            waiting_image2 = waiting_path_R
    else:
        waiting_image2 = waiting_path_non
    waiting_image_2.setImage(waiting_image2)
    # keep track of which components have finished
    waiting2Components = [waiting_image_2]
    for thisComponent in waiting2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "waiting2" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *waiting_image_2* updates
        if waiting_image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            waiting_image_2.frameNStart = frameN  # exact frame index
            waiting_image_2.tStart = t  # local t and not account for scr refresh
            waiting_image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(waiting_image_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'waiting_image_2.started')
            waiting_image_2.setAutoDraw(True)
        if waiting_image_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > waiting_image_2.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                waiting_image_2.tStop = t  # not accounting for scr refresh
                waiting_image_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'waiting_image_2.stopped')
                waiting_image_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in waiting2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "waiting2" ---
    for thisComponent in waiting2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    
    # --- Prepare to start Routine "feedback2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from feedback_code2
    if selet_key_resp.keys == None:
        Money_text_2.setVisible = False
    else:
        Money_text_2.setVisible = True
    
    if selet_key_resp.keys != None:
        if selet_key_resp.keys == '1'or selet_key_resp.keys == '2':
            Money_text2 += MONEY
            feedback_image2 = feedback_path_L
        elif selet_key_resp.keys == '3'or selet_key_resp.keys == '4':
            Money_text2 += MONEY
            feedback_image2 = feedback_path_R
    else:
        Money_text2 += 0
        feedback_image2 = feedback_path_non
    feedback_image_2.setImage(feedback_image2)
    Money_text_2.setText(Money_text2)
    # keep track of which components have finished
    feedback2Components = [feedback_image_2, Money_text_2]
    for thisComponent in feedback2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "feedback2" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_image_2* updates
        if feedback_image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_image_2.frameNStart = frameN  # exact frame index
            feedback_image_2.tStart = t  # local t and not account for scr refresh
            feedback_image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_image_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback_image_2.started')
            feedback_image_2.setAutoDraw(True)
        if feedback_image_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_image_2.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                feedback_image_2.tStop = t  # not accounting for scr refresh
                feedback_image_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_image_2.stopped')
                feedback_image_2.setAutoDraw(False)
        
        # *Money_text_2* updates
        if Money_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Money_text_2.frameNStart = frameN  # exact frame index
            Money_text_2.tStart = t  # local t and not account for scr refresh
            Money_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Money_text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Money_text_2.started')
            Money_text_2.setAutoDraw(True)
        if Money_text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Money_text_2.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                Money_text_2.tStop = t  # not accounting for scr refresh
                Money_text_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Money_text_2.stopped')
                Money_text_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedback2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback2" ---
    for thisComponent in feedback2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'LOOP_2'


# --- Prepare to start Routine "ending" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
endingComponents = [end_image]
for thisComponent in endingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "ending" ---
while continueRoutine and routineTimer.getTime() < 6.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_image* updates
    if end_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_image.frameNStart = frameN  # exact frame index
        end_image.tStart = t  # local t and not account for scr refresh
        end_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_image, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'end_image.started')
        end_image.setAutoDraw(True)
    if end_image.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_image.tStartRefresh + 6.0-frameTolerance:
            # keep track of stop time/frame for later
            end_image.tStop = t  # not accounting for scr refresh
            end_image.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'end_image.stopped')
            end_image.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "ending" ---
for thisComponent in endingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-6.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
