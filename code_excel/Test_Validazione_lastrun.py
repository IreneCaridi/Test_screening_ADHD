#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.2),
    on agosto 01, 2022, at 17:39
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

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
psychopyVersion = '2022.1.2'
expName = 'Test_Shapes'  # from the Builder filename that created this script
expInfo = {'participant': '', 'age': '', 'session': '001'}
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
    originPath='C:\\Users\\irene.LAPTOP-IPO788K1\\Desktop\\Polimi\\NECST\\Progetto NL2\\Test_Validazione\\Test_Validazione_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0.0000, 0.0000, 0.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
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

# Initialize components for Routine "Incoraggiamento"
IncoraggiamentoClock = core.Clock()
IncoText = visual.TextStim(win=win, name='IncoText',
    text="GRAZIE PER SVOLGERE QUESTO TEST!\nIL TUO CONTRIBUTO E' IMPORTANTE!\n\nClicca qualsiasi parte dello schermo per proseguire.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
IncoMouse = event.Mouse(win=win)
x, y = [None, None]
IncoMouse.mouseClock = core.Clock()

# Initialize components for Routine "InitialInstruction"
InitialInstructionClock = core.Clock()
TxtInitInstr = visual.TextStim(win=win, name='TxtInitInstr',
    text="IL TEST PREVEDE DIVERSE SCHERMATE:\n\nNELLA PRIMA VIENE MOSTRATA UN'ISTRUZIONE, DA LEGGERE ATTENTAMENTE E RICORDARE;\n\nNELLA SECONDA VENGONO MOSTRATE OTTO IMMAGINI TRA CUI SELEZIONARE QUELLE CHE CORRISPONDONO ALL'ISTRUZIONE LETTA PRECEDENTEMENTE.\n\nClicca qualsiasi parte dello schermo per proseguire.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
NextInitIstr = event.Mouse(win=win)
x, y = [None, None]
NextInitIstr.mouseClock = core.Clock()

# Initialize components for Routine "InitialInstruction2"
InitialInstruction2Clock = core.Clock()
TxtInitInstr_2 = visual.TextStim(win=win, name='TxtInitInstr_2',
    text="UNA VOLTA SELEZIONATA LA PRIMA RISPOSTA QUESTA VERRA' EVIDENZIATA.\n\nLE RISPOSTE DATE NON POSSONO ESSERE MODIFICATE.\n\nIL TEMPO DI SELEZIONE E' DI 20 SECONDI PER OGNI IMMAGINE.\nSE NON VIENE DATA RISPOSTA, IL TEST PROSEGUE RIQUADRANDO IL TIMER.\n\nClicca qualsiasi parte dello schermo per proseguire.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
NextInitIstr_2 = event.Mouse(win=win)
x, y = [None, None]
NextInitIstr_2.mouseClock = core.Clock()

# Initialize components for Routine "Attention"
AttentionClock = core.Clock()
txtAtt = visual.TextStim(win=win, name='txtAtt',
    text='!!!!!ATTENZIONE!!!!!\nNON CLICCARE LA STESSA IMMAGINE DUE VOLTE!\n\nClicca qualsiasi parte dello schermo per proseguire.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
MouseAtt = event.Mouse(win=win)
x, y = [None, None]
MouseAtt.mouseClock = core.Clock()

# Initialize components for Routine "InstrProva_2"
InstrProva_2Clock = core.Clock()
IncoText_2 = visual.TextStim(win=win, name='IncoText_2',
    text='ANCHE SE LE ISTRUZIONI SEMBRANO TANTE,\nNON TI SCORAGGIARE!\n\nClicca qualsiasi parte dello schermo per proseguire.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
IncoMouse_2 = event.Mouse(win=win)
x, y = [None, None]
IncoMouse_2.mouseClock = core.Clock()

# Initialize components for Routine "InstProva"
InstProvaClock = core.Clock()
NextIstrProva = event.Mouse(win=win)
x, y = [None, None]
NextIstrProva.mouseClock = core.Clock()
TxtIstrProva = visual.TextStim(win=win, name='TxtIstrProva',
    text="SEGUE UNA SESSIONE DI PROVA PER PERMETTERTI DI PRENDERE CONFIDENZA CON IL TEST.\n\nLE SETTE ISTRUZIONI CHE LEGGERAI SARANNO LE STESSE DEL TEST VERO E PROPRIO COSI' DA AIUTARTI!\n\nClicca qualsiasi parte dello schermo per proseguire.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
Instr_Test = visual.TextStim(win=win, name='Instr_Test',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Instr_Mouse = event.Mouse(win=win)
x, y = [None, None]
Instr_Mouse.mouseClock = core.Clock()

# Initialize components for Routine "images_Answer1"
images_Answer1Clock = core.Clock()
image1 = visual.ImageStim(
    win=win,
    name='image1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
image2 = visual.ImageStim(
    win=win,
    name='image2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image3 = visual.ImageStim(
    win=win,
    name='image3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image4 = visual.ImageStim(
    win=win,
    name='image4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
image5 = visual.ImageStim(
    win=win,
    name='image5', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
image6 = visual.ImageStim(
    win=win,
    name='image6', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
image7 = visual.ImageStim(
    win=win,
    name='image7', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
image8 = visual.ImageStim(
    win=win,
    name='image8', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
answer = event.Mouse(win=win)
x, y = [None, None]
answer.mouseClock = core.Clock()
countdown1 = visual.TextStim(win=win, name='countdown1',
    text='',
    font='Open Sans',
    pos=(0.7, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);

# Initialize components for Routine "image_Answer2Prova"
image_Answer2ProvaClock = core.Clock()
image1_4 = visual.ImageStim(
    win=win,
    name='image1_4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
image2_4 = visual.ImageStim(
    win=win,
    name='image2_4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image3_4 = visual.ImageStim(
    win=win,
    name='image3_4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image4_4 = visual.ImageStim(
    win=win,
    name='image4_4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
image5_4 = visual.ImageStim(
    win=win,
    name='image5_4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
image6_4 = visual.ImageStim(
    win=win,
    name='image6_4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
image7_4 = visual.ImageStim(
    win=win,
    name='image7_4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
image8_4 = visual.ImageStim(
    win=win,
    name='image8_4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
answer_4 = event.Mouse(win=win)
x, y = [None, None]
answer_4.mouseClock = core.Clock()
imageSelected_2 = visual.ImageStim(
    win=win,
    name='imageSelected_2', 
    image='images/Opacity.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=0.5,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
countdown2_2 = visual.TextStim(win=win, name='countdown2_2',
    text='',
    font='Open Sans',
    pos=(0.7, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# Initialize components for Routine "NextInstruction"
NextInstructionClock = core.Clock()
Next_Test = visual.TextStim(win=win, name='Next_Test',
    text='PROSSIMA ISTRUZIONE TRA 3 SECONDI',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "StartTest"
StartTestClock = core.Clock()
Txt_Start = visual.TextStim(win=win, name='Txt_Start',
    text="COMPLIMENTI!\nHAI COMPLETATO LA FASE DI PROVA,\nORA INIZIA IL TEST!\n\nIL TEST E' COMPOSTO DA DODICI DOMANDE.\n\nClicca qualsiasi parte dello schermo per proseguire",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Next_Start = event.Mouse(win=win)
x, y = [None, None]
Next_Start.mouseClock = core.Clock()

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
Instr_Test = visual.TextStim(win=win, name='Instr_Test',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Instr_Mouse = event.Mouse(win=win)
x, y = [None, None]
Instr_Mouse.mouseClock = core.Clock()

# Initialize components for Routine "images_Answer1"
images_Answer1Clock = core.Clock()
image1 = visual.ImageStim(
    win=win,
    name='image1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
image2 = visual.ImageStim(
    win=win,
    name='image2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image3 = visual.ImageStim(
    win=win,
    name='image3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image4 = visual.ImageStim(
    win=win,
    name='image4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
image5 = visual.ImageStim(
    win=win,
    name='image5', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
image6 = visual.ImageStim(
    win=win,
    name='image6', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
image7 = visual.ImageStim(
    win=win,
    name='image7', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
image8 = visual.ImageStim(
    win=win,
    name='image8', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
answer = event.Mouse(win=win)
x, y = [None, None]
answer.mouseClock = core.Clock()
countdown1 = visual.TextStim(win=win, name='countdown1',
    text='',
    font='Open Sans',
    pos=(0.7, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);

# Initialize components for Routine "images_Answer2"
images_Answer2Clock = core.Clock()
image1_3 = visual.ImageStim(
    win=win,
    name='image1_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
image2_3 = visual.ImageStim(
    win=win,
    name='image2_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image3_3 = visual.ImageStim(
    win=win,
    name='image3_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image4_3 = visual.ImageStim(
    win=win,
    name='image4_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
image5_3 = visual.ImageStim(
    win=win,
    name='image5_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
image6_3 = visual.ImageStim(
    win=win,
    name='image6_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
image7_3 = visual.ImageStim(
    win=win,
    name='image7_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
image8_3 = visual.ImageStim(
    win=win,
    name='image8_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
answer_3 = event.Mouse(win=win)
x, y = [None, None]
answer_3.mouseClock = core.Clock()
imageSelected = visual.ImageStim(
    win=win,
    name='imageSelected', 
    image='images/Selected.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=0.5,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
countdown2 = visual.TextStim(win=win, name='countdown2',
    text='',
    font='Open Sans',
    pos=(0.7, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# Initialize components for Routine "NextInstruction"
NextInstructionClock = core.Clock()
Next_Test = visual.TextStim(win=win, name='Next_Test',
    text='PROSSIMA ISTRUZIONE TRA 3 SECONDI',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "FineTest"
FineTestClock = core.Clock()
Txt_Fine = visual.TextStim(win=win, name='Txt_Fine',
    text='FINE TEST\n\nGRAZIE PER AVER PARTECIPATO!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Incoraggiamento"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the IncoMouse
gotValidClick = False  # until a click is received
# keep track of which components have finished
IncoraggiamentoComponents = [IncoText, IncoMouse]
for thisComponent in IncoraggiamentoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
IncoraggiamentoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Incoraggiamento"-------
while continueRoutine:
    # get current time
    t = IncoraggiamentoClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=IncoraggiamentoClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *IncoText* updates
    if IncoText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        IncoText.frameNStart = frameN  # exact frame index
        IncoText.tStart = t  # local t and not account for scr refresh
        IncoText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IncoText, 'tStartRefresh')  # time at next scr refresh
        IncoText.setAutoDraw(True)
    # *IncoMouse* updates
    if IncoMouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        IncoMouse.frameNStart = frameN  # exact frame index
        IncoMouse.tStart = t  # local t and not account for scr refresh
        IncoMouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IncoMouse, 'tStartRefresh')  # time at next scr refresh
        IncoMouse.status = STARTED
        IncoMouse.mouseClock.reset()
        prevButtonState = IncoMouse.getPressed()  # if button is down already this ISN'T a new click
    if IncoMouse.status == STARTED:  # only update if started and not finished!
        buttons = IncoMouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False  # abort routine on response    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IncoraggiamentoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Incoraggiamento"-------
for thisComponent in IncoraggiamentoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "Incoraggiamento" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "InitialInstruction"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the NextInitIstr
gotValidClick = False  # until a click is received
# keep track of which components have finished
InitialInstructionComponents = [TxtInitInstr, NextInitIstr]
for thisComponent in InitialInstructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InitialInstructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "InitialInstruction"-------
while continueRoutine:
    # get current time
    t = InitialInstructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InitialInstructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *TxtInitInstr* updates
    if TxtInitInstr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TxtInitInstr.frameNStart = frameN  # exact frame index
        TxtInitInstr.tStart = t  # local t and not account for scr refresh
        TxtInitInstr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TxtInitInstr, 'tStartRefresh')  # time at next scr refresh
        TxtInitInstr.setAutoDraw(True)
    # *NextInitIstr* updates
    if NextInitIstr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        NextInitIstr.frameNStart = frameN  # exact frame index
        NextInitIstr.tStart = t  # local t and not account for scr refresh
        NextInitIstr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(NextInitIstr, 'tStartRefresh')  # time at next scr refresh
        NextInitIstr.status = STARTED
        NextInitIstr.mouseClock.reset()
        prevButtonState = NextInitIstr.getPressed()  # if button is down already this ISN'T a new click
    if NextInitIstr.status == STARTED:  # only update if started and not finished!
        buttons = NextInitIstr.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False  # abort routine on response    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InitialInstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InitialInstruction"-------
for thisComponent in InitialInstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "InitialInstruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "InitialInstruction2"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the NextInitIstr_2
gotValidClick = False  # until a click is received
# keep track of which components have finished
InitialInstruction2Components = [TxtInitInstr_2, NextInitIstr_2]
for thisComponent in InitialInstruction2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InitialInstruction2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "InitialInstruction2"-------
while continueRoutine:
    # get current time
    t = InitialInstruction2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InitialInstruction2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *TxtInitInstr_2* updates
    if TxtInitInstr_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TxtInitInstr_2.frameNStart = frameN  # exact frame index
        TxtInitInstr_2.tStart = t  # local t and not account for scr refresh
        TxtInitInstr_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TxtInitInstr_2, 'tStartRefresh')  # time at next scr refresh
        TxtInitInstr_2.setAutoDraw(True)
    # *NextInitIstr_2* updates
    if NextInitIstr_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        NextInitIstr_2.frameNStart = frameN  # exact frame index
        NextInitIstr_2.tStart = t  # local t and not account for scr refresh
        NextInitIstr_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(NextInitIstr_2, 'tStartRefresh')  # time at next scr refresh
        NextInitIstr_2.status = STARTED
        NextInitIstr_2.mouseClock.reset()
        prevButtonState = NextInitIstr_2.getPressed()  # if button is down already this ISN'T a new click
    if NextInitIstr_2.status == STARTED:  # only update if started and not finished!
        buttons = NextInitIstr_2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False  # abort routine on response    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InitialInstruction2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InitialInstruction2"-------
for thisComponent in InitialInstruction2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "InitialInstruction2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Attention"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the MouseAtt
gotValidClick = False  # until a click is received
# keep track of which components have finished
AttentionComponents = [txtAtt, MouseAtt]
for thisComponent in AttentionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
AttentionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Attention"-------
while continueRoutine:
    # get current time
    t = AttentionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=AttentionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *txtAtt* updates
    if txtAtt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        txtAtt.frameNStart = frameN  # exact frame index
        txtAtt.tStart = t  # local t and not account for scr refresh
        txtAtt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(txtAtt, 'tStartRefresh')  # time at next scr refresh
        txtAtt.setAutoDraw(True)
    # *MouseAtt* updates
    if MouseAtt.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        MouseAtt.frameNStart = frameN  # exact frame index
        MouseAtt.tStart = t  # local t and not account for scr refresh
        MouseAtt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MouseAtt, 'tStartRefresh')  # time at next scr refresh
        MouseAtt.status = STARTED
        MouseAtt.mouseClock.reset()
        prevButtonState = MouseAtt.getPressed()  # if button is down already this ISN'T a new click
    if MouseAtt.status == STARTED:  # only update if started and not finished!
        buttons = MouseAtt.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False  # abort routine on response    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in AttentionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Attention"-------
for thisComponent in AttentionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "Attention" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "InstrProva_2"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the IncoMouse_2
gotValidClick = False  # until a click is received
# keep track of which components have finished
InstrProva_2Components = [IncoText_2, IncoMouse_2]
for thisComponent in InstrProva_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstrProva_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "InstrProva_2"-------
while continueRoutine:
    # get current time
    t = InstrProva_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstrProva_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *IncoText_2* updates
    if IncoText_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        IncoText_2.frameNStart = frameN  # exact frame index
        IncoText_2.tStart = t  # local t and not account for scr refresh
        IncoText_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IncoText_2, 'tStartRefresh')  # time at next scr refresh
        IncoText_2.setAutoDraw(True)
    # *IncoMouse_2* updates
    if IncoMouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        IncoMouse_2.frameNStart = frameN  # exact frame index
        IncoMouse_2.tStart = t  # local t and not account for scr refresh
        IncoMouse_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IncoMouse_2, 'tStartRefresh')  # time at next scr refresh
        IncoMouse_2.status = STARTED
        IncoMouse_2.mouseClock.reset()
        prevButtonState = IncoMouse_2.getPressed()  # if button is down already this ISN'T a new click
    if IncoMouse_2.status == STARTED:  # only update if started and not finished!
        buttons = IncoMouse_2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False  # abort routine on response    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstrProva_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InstrProva_2"-------
for thisComponent in InstrProva_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "InstrProva_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "InstProva"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the NextIstrProva
gotValidClick = False  # until a click is received
# keep track of which components have finished
InstProvaComponents = [NextIstrProva, TxtIstrProva]
for thisComponent in InstProvaComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstProvaClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "InstProva"-------
while continueRoutine:
    # get current time
    t = InstProvaClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstProvaClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *NextIstrProva* updates
    if NextIstrProva.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        NextIstrProva.frameNStart = frameN  # exact frame index
        NextIstrProva.tStart = t  # local t and not account for scr refresh
        NextIstrProva.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(NextIstrProva, 'tStartRefresh')  # time at next scr refresh
        NextIstrProva.status = STARTED
        NextIstrProva.mouseClock.reset()
        prevButtonState = NextIstrProva.getPressed()  # if button is down already this ISN'T a new click
    if NextIstrProva.status == STARTED:  # only update if started and not finished!
        buttons = NextIstrProva.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False  # abort routine on response    
    # *TxtIstrProva* updates
    if TxtIstrProva.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TxtIstrProva.frameNStart = frameN  # exact frame index
        TxtIstrProva.tStart = t  # local t and not account for scr refresh
        TxtIstrProva.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TxtIstrProva, 'tStartRefresh')  # time at next scr refresh
        TxtIstrProva.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstProvaComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InstProva"-------
for thisComponent in InstProvaComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "InstProva" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condProva.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instructions"-------
    continueRoutine = True
    # update component parameters for each repeat
    Instr_Test.setText('SELEZIONA DUE IMMAGINI CON ' + str(title) + '\n\n Clicca lo schermo per vedere le immagini.')
    # setup some python lists for storing info about the Instr_Mouse
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    instructionsComponents = [Instr_Test, Instr_Mouse]
    for thisComponent in instructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instructions"-------
    while continueRoutine:
        # get current time
        t = instructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Instr_Test* updates
        if Instr_Test.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instr_Test.frameNStart = frameN  # exact frame index
            Instr_Test.tStart = t  # local t and not account for scr refresh
            Instr_Test.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instr_Test, 'tStartRefresh')  # time at next scr refresh
            Instr_Test.setAutoDraw(True)
        # *Instr_Mouse* updates
        if Instr_Mouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instr_Mouse.frameNStart = frameN  # exact frame index
            Instr_Mouse.tStart = t  # local t and not account for scr refresh
            Instr_Mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instr_Mouse, 'tStartRefresh')  # time at next scr refresh
            Instr_Mouse.status = STARTED
            Instr_Mouse.mouseClock.reset()
            prevButtonState = Instr_Mouse.getPressed()  # if button is down already this ISN'T a new click
        if Instr_Mouse.status == STARTED:  # only update if started and not finished!
            buttons = Instr_Mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    continueRoutine = False  # abort routine on response        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructions"-------
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_2 (TrialHandler)
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "images_Answer1"-------
    continueRoutine = True
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    image1.setPos((posix_SideLeft, posiy_Up))
    image1.setSize((size_x, size_y))
    image1.setImage(image_1)
    image2.setPos((posix_CenterLeft, posiy_Up))
    image2.setSize((size_x, size_y))
    image2.setImage(image_2)
    image3.setPos((posix_CenterRight, posiy_Up))
    image3.setSize((size_x, size_y))
    image3.setImage(image_3)
    image4.setPos((posix_SideRight , posiy_Up))
    image4.setSize((size_x, size_y))
    image4.setImage(image_4)
    image5.setPos((posix_SideLeft, posiy_Down))
    image5.setSize((size_x, size_y))
    image5.setImage(image_5)
    image6.setPos((posix_CenterLeft, posiy_Down))
    image6.setSize((size_x, size_y))
    image6.setImage(image_6)
    image7.setPos((posix_CenterRight, posiy_Down))
    image7.setSize((size_x, size_y))
    image7.setImage(image_7)
    image8.setPos((posix_SideRight, posiy_Down))
    image8.setSize((size_x, size_y))
    image8.setImage(image_8)
    # setup some python lists for storing info about the answer
    answer.x = []
    answer.y = []
    answer.leftButton = []
    answer.midButton = []
    answer.rightButton = []
    answer.time = []
    answer.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    images_Answer1Components = [image1, image2, image3, image4, image5, image6, image7, image8, answer, countdown1]
    for thisComponent in images_Answer1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    images_Answer1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "images_Answer1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = images_Answer1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=images_Answer1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image1* updates
        if image1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image1.frameNStart = frameN  # exact frame index
            image1.tStart = t  # local t and not account for scr refresh
            image1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image1, 'tStartRefresh')  # time at next scr refresh
            image1.setAutoDraw(True)
        if image1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image1.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image1.tStop = t  # not accounting for scr refresh
                image1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image1, 'tStopRefresh')  # time at next scr refresh
                image1.setAutoDraw(False)
        
        # *image2* updates
        if image2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image2.frameNStart = frameN  # exact frame index
            image2.tStart = t  # local t and not account for scr refresh
            image2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image2, 'tStartRefresh')  # time at next scr refresh
            image2.setAutoDraw(True)
        if image2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image2.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image2.tStop = t  # not accounting for scr refresh
                image2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image2, 'tStopRefresh')  # time at next scr refresh
                image2.setAutoDraw(False)
        
        # *image3* updates
        if image3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image3.frameNStart = frameN  # exact frame index
            image3.tStart = t  # local t and not account for scr refresh
            image3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image3, 'tStartRefresh')  # time at next scr refresh
            image3.setAutoDraw(True)
        if image3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image3.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image3.tStop = t  # not accounting for scr refresh
                image3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image3, 'tStopRefresh')  # time at next scr refresh
                image3.setAutoDraw(False)
        
        # *image4* updates
        if image4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image4.frameNStart = frameN  # exact frame index
            image4.tStart = t  # local t and not account for scr refresh
            image4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image4, 'tStartRefresh')  # time at next scr refresh
            image4.setAutoDraw(True)
        if image4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image4.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image4.tStop = t  # not accounting for scr refresh
                image4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image4, 'tStopRefresh')  # time at next scr refresh
                image4.setAutoDraw(False)
        
        # *image5* updates
        if image5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image5.frameNStart = frameN  # exact frame index
            image5.tStart = t  # local t and not account for scr refresh
            image5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image5, 'tStartRefresh')  # time at next scr refresh
            image5.setAutoDraw(True)
        if image5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image5.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image5.tStop = t  # not accounting for scr refresh
                image5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image5, 'tStopRefresh')  # time at next scr refresh
                image5.setAutoDraw(False)
        
        # *image6* updates
        if image6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image6.frameNStart = frameN  # exact frame index
            image6.tStart = t  # local t and not account for scr refresh
            image6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image6, 'tStartRefresh')  # time at next scr refresh
            image6.setAutoDraw(True)
        if image6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image6.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image6.tStop = t  # not accounting for scr refresh
                image6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image6, 'tStopRefresh')  # time at next scr refresh
                image6.setAutoDraw(False)
        
        # *image7* updates
        if image7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image7.frameNStart = frameN  # exact frame index
            image7.tStart = t  # local t and not account for scr refresh
            image7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image7, 'tStartRefresh')  # time at next scr refresh
            image7.setAutoDraw(True)
        if image7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image7.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image7.tStop = t  # not accounting for scr refresh
                image7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image7, 'tStopRefresh')  # time at next scr refresh
                image7.setAutoDraw(False)
        
        # *image8* updates
        if image8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image8.frameNStart = frameN  # exact frame index
            image8.tStart = t  # local t and not account for scr refresh
            image8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image8, 'tStartRefresh')  # time at next scr refresh
            image8.setAutoDraw(True)
        if image8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image8.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image8.tStop = t  # not accounting for scr refresh
                image8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image8, 'tStopRefresh')  # time at next scr refresh
                image8.setAutoDraw(False)
        # *answer* updates
        if answer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            answer.frameNStart = frameN  # exact frame index
            answer.tStart = t  # local t and not account for scr refresh
            answer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(answer, 'tStartRefresh')  # time at next scr refresh
            answer.status = STARTED
            answer.mouseClock.reset()
            prevButtonState = answer.getPressed()  # if button is down already this ISN'T a new click
        if answer.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > answer.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                answer.tStop = t  # not accounting for scr refresh
                answer.frameNStop = frameN  # exact frame index
                win.timeOnFlip(answer, 'tStopRefresh')  # time at next scr refresh
                answer.status = FINISHED
        if answer.status == STARTED:  # only update if started and not finished!
            x, y = answer.getPos()
            answer.x.append(x)
            answer.y.append(y)
            buttons = answer.getPressed()
            answer.leftButton.append(buttons[0])
            answer.midButton.append(buttons[1])
            answer.rightButton.append(buttons[2])
            answer.time.append(answer.mouseClock.getTime())
            buttons = answer.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([image1, image2, image3, image4, image5, image6, image7, image8])
                        clickableList = [image1, image2, image3, image4, image5, image6, image7, image8]
                    except:
                        clickableList = [[image1, image2, image3, image4, image5, image6, image7, image8]]
                    for obj in clickableList:
                        if obj.contains(answer):
                            gotValidClick = True
                            answer.clicked_name.append(obj.name)
                    if gotValidClick:
                        continueRoutine = False  # abort routine on response
        
        # *countdown1* updates
        if countdown1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            countdown1.frameNStart = frameN  # exact frame index
            countdown1.tStart = t  # local t and not account for scr refresh
            countdown1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(countdown1, 'tStartRefresh')  # time at next scr refresh
            countdown1.setAutoDraw(True)
        if countdown1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > countdown1.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                countdown1.tStop = t  # not accounting for scr refresh
                countdown1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(countdown1, 'tStopRefresh')  # time at next scr refresh
                countdown1.setAutoDraw(False)
        if countdown1.status == STARTED:  # only update if drawing
            countdown1.setText(round(20.0 - t, 1), log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in images_Answer1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "images_Answer1"-------
    for thisComponent in images_Answer1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('answer.x', answer.x)
    trials_2.addData('answer.y', answer.y)
    trials_2.addData('answer.leftButton', answer.leftButton)
    trials_2.addData('answer.midButton', answer.midButton)
    trials_2.addData('answer.rightButton', answer.rightButton)
    trials_2.addData('answer.time', answer.time)
    trials_2.addData('answer.clicked_name', answer.clicked_name)
    trials_2.addData('answer.started', answer.tStartRefresh)
    trials_2.addData('answer.stopped', answer.tStopRefresh)
    
    # ------Prepare to start Routine "image_Answer2Prova"-------
    continueRoutine = True
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    image1_4.setPos((posix_SideLeft, posiy_Up))
    image1_4.setSize((size_x, size_y))
    image1_4.setImage(image_1)
    image2_4.setPos((posix_CenterLeft, posiy_Up))
    image2_4.setSize((size_x, size_y))
    image2_4.setImage(image_2)
    image3_4.setPos((posix_CenterRight, posiy_Up))
    image3_4.setSize((size_x, size_y))
    image3_4.setImage(image_3)
    image4_4.setPos((posix_SideRight , posiy_Up))
    image4_4.setSize((size_x, size_y))
    image4_4.setImage(image_4)
    image5_4.setPos((posix_SideLeft, posiy_Down))
    image5_4.setSize((size_x, size_y))
    image5_4.setImage(image_5)
    image6_4.setPos((posix_CenterLeft, posiy_Down))
    image6_4.setSize((size_x, size_y))
    image6_4.setImage(image_6)
    image7_4.setPos((posix_CenterRight, posiy_Down))
    image7_4.setSize((size_x, size_y))
    image7_4.setImage(image_7)
    image8_4.setPos((posix_SideRight, posiy_Down))
    image8_4.setSize((size_x, size_y))
    image8_4.setImage(image_8)
    # setup some python lists for storing info about the answer_4
    answer_4.x = []
    answer_4.y = []
    answer_4.leftButton = []
    answer_4.midButton = []
    answer_4.rightButton = []
    answer_4.time = []
    answer_4.clicked_name = []
    gotValidClick = False  # until a click is received
    imageSelected_2.setSize((size_x, size_y))
    if answer.clicked_name:
        if answer.clicked_name[-1] == "image1":
            posriqx=posix_SideLeft 
            posreqy=posiy_Up
        elif answer.clicked_name[-1]== "image2":
            posriqx=posix_CenterLeft 
            posreqy=posiy_Up
        elif answer.clicked_name[-1] == "image3":
            posriqx=posix_CenterRight 
            posreqy=posiy_Up
        elif answer.clicked_name[-1] == "image4":
            posriqx=posix_SideRight
            posreqy=posiy_Up    
        elif answer.clicked_name[-1] == "image5":
            posriqx=posix_SideLeft 
            posreqy=posiy_Down
        elif answer.clicked_name[-1]== "image6":
            posriqx=posix_CenterLeft 
            posreqy=posiy_Down
        elif answer.clicked_name[-1] == "image7":
            posriqx=posix_CenterRight 
            posreqy=posiy_Down
        elif answer.clicked_name[-1] == "image8":
            posriqx=posix_SideRight 
            posreqy=posiy_Down
    else:
        posriqx=0.7
        posreqy=0
        
    imageSelected_2.setPos((posriqx, posreqy))
    # keep track of which components have finished
    image_Answer2ProvaComponents = [image1_4, image2_4, image3_4, image4_4, image5_4, image6_4, image7_4, image8_4, answer_4, imageSelected_2, countdown2_2]
    for thisComponent in image_Answer2ProvaComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    image_Answer2ProvaClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "image_Answer2Prova"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = image_Answer2ProvaClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=image_Answer2ProvaClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image1_4* updates
        if image1_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image1_4.frameNStart = frameN  # exact frame index
            image1_4.tStart = t  # local t and not account for scr refresh
            image1_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image1_4, 'tStartRefresh')  # time at next scr refresh
            image1_4.setAutoDraw(True)
        if image1_4.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 20-frameTolerance:
                # keep track of stop time/frame for later
                image1_4.tStop = t  # not accounting for scr refresh
                image1_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image1_4, 'tStopRefresh')  # time at next scr refresh
                image1_4.setAutoDraw(False)
        
        # *image2_4* updates
        if image2_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image2_4.frameNStart = frameN  # exact frame index
            image2_4.tStart = t  # local t and not account for scr refresh
            image2_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image2_4, 'tStartRefresh')  # time at next scr refresh
            image2_4.setAutoDraw(True)
        if image2_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image2_4.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image2_4.tStop = t  # not accounting for scr refresh
                image2_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image2_4, 'tStopRefresh')  # time at next scr refresh
                image2_4.setAutoDraw(False)
        
        # *image3_4* updates
        if image3_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image3_4.frameNStart = frameN  # exact frame index
            image3_4.tStart = t  # local t and not account for scr refresh
            image3_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image3_4, 'tStartRefresh')  # time at next scr refresh
            image3_4.setAutoDraw(True)
        if image3_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image3_4.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image3_4.tStop = t  # not accounting for scr refresh
                image3_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image3_4, 'tStopRefresh')  # time at next scr refresh
                image3_4.setAutoDraw(False)
        
        # *image4_4* updates
        if image4_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image4_4.frameNStart = frameN  # exact frame index
            image4_4.tStart = t  # local t and not account for scr refresh
            image4_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image4_4, 'tStartRefresh')  # time at next scr refresh
            image4_4.setAutoDraw(True)
        if image4_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image4_4.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image4_4.tStop = t  # not accounting for scr refresh
                image4_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image4_4, 'tStopRefresh')  # time at next scr refresh
                image4_4.setAutoDraw(False)
        
        # *image5_4* updates
        if image5_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image5_4.frameNStart = frameN  # exact frame index
            image5_4.tStart = t  # local t and not account for scr refresh
            image5_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image5_4, 'tStartRefresh')  # time at next scr refresh
            image5_4.setAutoDraw(True)
        if image5_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image5_4.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image5_4.tStop = t  # not accounting for scr refresh
                image5_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image5_4, 'tStopRefresh')  # time at next scr refresh
                image5_4.setAutoDraw(False)
        
        # *image6_4* updates
        if image6_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image6_4.frameNStart = frameN  # exact frame index
            image6_4.tStart = t  # local t and not account for scr refresh
            image6_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image6_4, 'tStartRefresh')  # time at next scr refresh
            image6_4.setAutoDraw(True)
        if image6_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image6_4.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image6_4.tStop = t  # not accounting for scr refresh
                image6_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image6_4, 'tStopRefresh')  # time at next scr refresh
                image6_4.setAutoDraw(False)
        
        # *image7_4* updates
        if image7_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image7_4.frameNStart = frameN  # exact frame index
            image7_4.tStart = t  # local t and not account for scr refresh
            image7_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image7_4, 'tStartRefresh')  # time at next scr refresh
            image7_4.setAutoDraw(True)
        if image7_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image7_4.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image7_4.tStop = t  # not accounting for scr refresh
                image7_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image7_4, 'tStopRefresh')  # time at next scr refresh
                image7_4.setAutoDraw(False)
        
        # *image8_4* updates
        if image8_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image8_4.frameNStart = frameN  # exact frame index
            image8_4.tStart = t  # local t and not account for scr refresh
            image8_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image8_4, 'tStartRefresh')  # time at next scr refresh
            image8_4.setAutoDraw(True)
        if image8_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image8_4.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image8_4.tStop = t  # not accounting for scr refresh
                image8_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image8_4, 'tStopRefresh')  # time at next scr refresh
                image8_4.setAutoDraw(False)
        # *answer_4* updates
        if answer_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            answer_4.frameNStart = frameN  # exact frame index
            answer_4.tStart = t  # local t and not account for scr refresh
            answer_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(answer_4, 'tStartRefresh')  # time at next scr refresh
            answer_4.status = STARTED
            answer_4.mouseClock.reset()
            prevButtonState = answer_4.getPressed()  # if button is down already this ISN'T a new click
        if answer_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > answer_4.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                answer_4.tStop = t  # not accounting for scr refresh
                answer_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(answer_4, 'tStopRefresh')  # time at next scr refresh
                answer_4.status = FINISHED
        if answer_4.status == STARTED:  # only update if started and not finished!
            x, y = answer_4.getPos()
            answer_4.x.append(x)
            answer_4.y.append(y)
            buttons = answer_4.getPressed()
            answer_4.leftButton.append(buttons[0])
            answer_4.midButton.append(buttons[1])
            answer_4.rightButton.append(buttons[2])
            answer_4.time.append(answer_4.mouseClock.getTime())
            buttons = answer_4.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([image1, image2, image3, image4, image5, image6, image7, image8])
                        clickableList = [image1, image2, image3, image4, image5, image6, image7, image8]
                    except:
                        clickableList = [[image1, image2, image3, image4, image5, image6, image7, image8]]
                    for obj in clickableList:
                        if obj.contains(answer_4):
                            gotValidClick = True
                            answer_4.clicked_name.append(obj.name)
                    if gotValidClick:
                        continueRoutine = False  # abort routine on response
        
        # *imageSelected_2* updates
        if imageSelected_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageSelected_2.frameNStart = frameN  # exact frame index
            imageSelected_2.tStart = t  # local t and not account for scr refresh
            imageSelected_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageSelected_2, 'tStartRefresh')  # time at next scr refresh
            imageSelected_2.setAutoDraw(True)
        if imageSelected_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageSelected_2.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                imageSelected_2.tStop = t  # not accounting for scr refresh
                imageSelected_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageSelected_2, 'tStopRefresh')  # time at next scr refresh
                imageSelected_2.setAutoDraw(False)
        
        # *countdown2_2* updates
        if countdown2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            countdown2_2.frameNStart = frameN  # exact frame index
            countdown2_2.tStart = t  # local t and not account for scr refresh
            countdown2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(countdown2_2, 'tStartRefresh')  # time at next scr refresh
            countdown2_2.setAutoDraw(True)
        if countdown2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > countdown2_2.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                countdown2_2.tStop = t  # not accounting for scr refresh
                countdown2_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(countdown2_2, 'tStopRefresh')  # time at next scr refresh
                countdown2_2.setAutoDraw(False)
        if countdown2_2.status == STARTED:  # only update if drawing
            countdown2_2.setText(round(20.0 - t, 1), log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in image_Answer2ProvaComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "image_Answer2Prova"-------
    for thisComponent in image_Answer2ProvaComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('answer_4.x', answer_4.x)
    trials_2.addData('answer_4.y', answer_4.y)
    trials_2.addData('answer_4.leftButton', answer_4.leftButton)
    trials_2.addData('answer_4.midButton', answer_4.midButton)
    trials_2.addData('answer_4.rightButton', answer_4.rightButton)
    trials_2.addData('answer_4.time', answer_4.time)
    trials_2.addData('answer_4.clicked_name', answer_4.clicked_name)
    trials_2.addData('answer_4.started', answer_4.tStartRefresh)
    trials_2.addData('answer_4.stopped', answer_4.tStopRefresh)
    if (answer.clicked_name and answer_4.clicked_name):
        if((answer.clicked_name[-1]==correct_Answer1 or answer.clicked_name[-1]==correct_Answer2) and (answer_4.clicked_name[-1]==correct_Answer1 or answer_4.clicked_name[-1]==correct_Answer2)):
            trials_2.addData('score', 1)
        else:
            trials_2.addData('score', 0)
    else:
            trials_2.addData('score', -1)
    
    
    # ------Prepare to start Routine "NextInstruction"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    NextInstructionComponents = [Next_Test]
    for thisComponent in NextInstructionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    NextInstructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "NextInstruction"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = NextInstructionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=NextInstructionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Next_Test* updates
        if Next_Test.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Next_Test.frameNStart = frameN  # exact frame index
            Next_Test.tStart = t  # local t and not account for scr refresh
            Next_Test.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Next_Test, 'tStartRefresh')  # time at next scr refresh
            Next_Test.setAutoDraw(True)
        if Next_Test.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Next_Test.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                Next_Test.tStop = t  # not accounting for scr refresh
                Next_Test.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Next_Test, 'tStopRefresh')  # time at next scr refresh
                Next_Test.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in NextInstructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "NextInstruction"-------
    for thisComponent in NextInstructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_2'


# ------Prepare to start Routine "StartTest"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the Next_Start
gotValidClick = False  # until a click is received
# keep track of which components have finished
StartTestComponents = [Txt_Start, Next_Start]
for thisComponent in StartTestComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
StartTestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "StartTest"-------
while continueRoutine:
    # get current time
    t = StartTestClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=StartTestClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Txt_Start* updates
    if Txt_Start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Txt_Start.frameNStart = frameN  # exact frame index
        Txt_Start.tStart = t  # local t and not account for scr refresh
        Txt_Start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Txt_Start, 'tStartRefresh')  # time at next scr refresh
        Txt_Start.setAutoDraw(True)
    # *Next_Start* updates
    if Next_Start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Next_Start.frameNStart = frameN  # exact frame index
        Next_Start.tStart = t  # local t and not account for scr refresh
        Next_Start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Next_Start, 'tStartRefresh')  # time at next scr refresh
        Next_Start.status = STARTED
        Next_Start.mouseClock.reset()
        prevButtonState = Next_Start.getPressed()  # if button is down already this ISN'T a new click
    if Next_Start.status == STARTED:  # only update if started and not finished!
        buttons = Next_Start.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False  # abort routine on response    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartTestComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "StartTest"-------
for thisComponent in StartTestComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "StartTest" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('cond.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instructions"-------
    continueRoutine = True
    # update component parameters for each repeat
    Instr_Test.setText('SELEZIONA DUE IMMAGINI CON ' + str(title) + '\n\n Clicca lo schermo per vedere le immagini.')
    # setup some python lists for storing info about the Instr_Mouse
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    instructionsComponents = [Instr_Test, Instr_Mouse]
    for thisComponent in instructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instructions"-------
    while continueRoutine:
        # get current time
        t = instructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Instr_Test* updates
        if Instr_Test.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instr_Test.frameNStart = frameN  # exact frame index
            Instr_Test.tStart = t  # local t and not account for scr refresh
            Instr_Test.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instr_Test, 'tStartRefresh')  # time at next scr refresh
            Instr_Test.setAutoDraw(True)
        # *Instr_Mouse* updates
        if Instr_Mouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instr_Mouse.frameNStart = frameN  # exact frame index
            Instr_Mouse.tStart = t  # local t and not account for scr refresh
            Instr_Mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instr_Mouse, 'tStartRefresh')  # time at next scr refresh
            Instr_Mouse.status = STARTED
            Instr_Mouse.mouseClock.reset()
            prevButtonState = Instr_Mouse.getPressed()  # if button is down already this ISN'T a new click
        if Instr_Mouse.status == STARTED:  # only update if started and not finished!
            buttons = Instr_Mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    continueRoutine = False  # abort routine on response        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructions"-------
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "images_Answer1"-------
    continueRoutine = True
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    image1.setPos((posix_SideLeft, posiy_Up))
    image1.setSize((size_x, size_y))
    image1.setImage(image_1)
    image2.setPos((posix_CenterLeft, posiy_Up))
    image2.setSize((size_x, size_y))
    image2.setImage(image_2)
    image3.setPos((posix_CenterRight, posiy_Up))
    image3.setSize((size_x, size_y))
    image3.setImage(image_3)
    image4.setPos((posix_SideRight , posiy_Up))
    image4.setSize((size_x, size_y))
    image4.setImage(image_4)
    image5.setPos((posix_SideLeft, posiy_Down))
    image5.setSize((size_x, size_y))
    image5.setImage(image_5)
    image6.setPos((posix_CenterLeft, posiy_Down))
    image6.setSize((size_x, size_y))
    image6.setImage(image_6)
    image7.setPos((posix_CenterRight, posiy_Down))
    image7.setSize((size_x, size_y))
    image7.setImage(image_7)
    image8.setPos((posix_SideRight, posiy_Down))
    image8.setSize((size_x, size_y))
    image8.setImage(image_8)
    # setup some python lists for storing info about the answer
    answer.x = []
    answer.y = []
    answer.leftButton = []
    answer.midButton = []
    answer.rightButton = []
    answer.time = []
    answer.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    images_Answer1Components = [image1, image2, image3, image4, image5, image6, image7, image8, answer, countdown1]
    for thisComponent in images_Answer1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    images_Answer1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "images_Answer1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = images_Answer1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=images_Answer1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image1* updates
        if image1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image1.frameNStart = frameN  # exact frame index
            image1.tStart = t  # local t and not account for scr refresh
            image1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image1, 'tStartRefresh')  # time at next scr refresh
            image1.setAutoDraw(True)
        if image1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image1.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image1.tStop = t  # not accounting for scr refresh
                image1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image1, 'tStopRefresh')  # time at next scr refresh
                image1.setAutoDraw(False)
        
        # *image2* updates
        if image2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image2.frameNStart = frameN  # exact frame index
            image2.tStart = t  # local t and not account for scr refresh
            image2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image2, 'tStartRefresh')  # time at next scr refresh
            image2.setAutoDraw(True)
        if image2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image2.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image2.tStop = t  # not accounting for scr refresh
                image2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image2, 'tStopRefresh')  # time at next scr refresh
                image2.setAutoDraw(False)
        
        # *image3* updates
        if image3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image3.frameNStart = frameN  # exact frame index
            image3.tStart = t  # local t and not account for scr refresh
            image3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image3, 'tStartRefresh')  # time at next scr refresh
            image3.setAutoDraw(True)
        if image3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image3.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image3.tStop = t  # not accounting for scr refresh
                image3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image3, 'tStopRefresh')  # time at next scr refresh
                image3.setAutoDraw(False)
        
        # *image4* updates
        if image4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image4.frameNStart = frameN  # exact frame index
            image4.tStart = t  # local t and not account for scr refresh
            image4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image4, 'tStartRefresh')  # time at next scr refresh
            image4.setAutoDraw(True)
        if image4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image4.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image4.tStop = t  # not accounting for scr refresh
                image4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image4, 'tStopRefresh')  # time at next scr refresh
                image4.setAutoDraw(False)
        
        # *image5* updates
        if image5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image5.frameNStart = frameN  # exact frame index
            image5.tStart = t  # local t and not account for scr refresh
            image5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image5, 'tStartRefresh')  # time at next scr refresh
            image5.setAutoDraw(True)
        if image5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image5.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image5.tStop = t  # not accounting for scr refresh
                image5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image5, 'tStopRefresh')  # time at next scr refresh
                image5.setAutoDraw(False)
        
        # *image6* updates
        if image6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image6.frameNStart = frameN  # exact frame index
            image6.tStart = t  # local t and not account for scr refresh
            image6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image6, 'tStartRefresh')  # time at next scr refresh
            image6.setAutoDraw(True)
        if image6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image6.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image6.tStop = t  # not accounting for scr refresh
                image6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image6, 'tStopRefresh')  # time at next scr refresh
                image6.setAutoDraw(False)
        
        # *image7* updates
        if image7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image7.frameNStart = frameN  # exact frame index
            image7.tStart = t  # local t and not account for scr refresh
            image7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image7, 'tStartRefresh')  # time at next scr refresh
            image7.setAutoDraw(True)
        if image7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image7.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image7.tStop = t  # not accounting for scr refresh
                image7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image7, 'tStopRefresh')  # time at next scr refresh
                image7.setAutoDraw(False)
        
        # *image8* updates
        if image8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image8.frameNStart = frameN  # exact frame index
            image8.tStart = t  # local t and not account for scr refresh
            image8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image8, 'tStartRefresh')  # time at next scr refresh
            image8.setAutoDraw(True)
        if image8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image8.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image8.tStop = t  # not accounting for scr refresh
                image8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image8, 'tStopRefresh')  # time at next scr refresh
                image8.setAutoDraw(False)
        # *answer* updates
        if answer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            answer.frameNStart = frameN  # exact frame index
            answer.tStart = t  # local t and not account for scr refresh
            answer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(answer, 'tStartRefresh')  # time at next scr refresh
            answer.status = STARTED
            answer.mouseClock.reset()
            prevButtonState = answer.getPressed()  # if button is down already this ISN'T a new click
        if answer.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > answer.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                answer.tStop = t  # not accounting for scr refresh
                answer.frameNStop = frameN  # exact frame index
                win.timeOnFlip(answer, 'tStopRefresh')  # time at next scr refresh
                answer.status = FINISHED
        if answer.status == STARTED:  # only update if started and not finished!
            x, y = answer.getPos()
            answer.x.append(x)
            answer.y.append(y)
            buttons = answer.getPressed()
            answer.leftButton.append(buttons[0])
            answer.midButton.append(buttons[1])
            answer.rightButton.append(buttons[2])
            answer.time.append(answer.mouseClock.getTime())
            buttons = answer.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([image1, image2, image3, image4, image5, image6, image7, image8])
                        clickableList = [image1, image2, image3, image4, image5, image6, image7, image8]
                    except:
                        clickableList = [[image1, image2, image3, image4, image5, image6, image7, image8]]
                    for obj in clickableList:
                        if obj.contains(answer):
                            gotValidClick = True
                            answer.clicked_name.append(obj.name)
                    if gotValidClick:
                        continueRoutine = False  # abort routine on response
        
        # *countdown1* updates
        if countdown1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            countdown1.frameNStart = frameN  # exact frame index
            countdown1.tStart = t  # local t and not account for scr refresh
            countdown1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(countdown1, 'tStartRefresh')  # time at next scr refresh
            countdown1.setAutoDraw(True)
        if countdown1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > countdown1.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                countdown1.tStop = t  # not accounting for scr refresh
                countdown1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(countdown1, 'tStopRefresh')  # time at next scr refresh
                countdown1.setAutoDraw(False)
        if countdown1.status == STARTED:  # only update if drawing
            countdown1.setText(round(20.0 - t, 1), log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in images_Answer1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "images_Answer1"-------
    for thisComponent in images_Answer1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('answer.x', answer.x)
    trials.addData('answer.y', answer.y)
    trials.addData('answer.leftButton', answer.leftButton)
    trials.addData('answer.midButton', answer.midButton)
    trials.addData('answer.rightButton', answer.rightButton)
    trials.addData('answer.time', answer.time)
    trials.addData('answer.clicked_name', answer.clicked_name)
    trials.addData('answer.started', answer.tStartRefresh)
    trials.addData('answer.stopped', answer.tStopRefresh)
    
    # ------Prepare to start Routine "images_Answer2"-------
    continueRoutine = True
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    image1_3.setPos((posix_SideLeft, posiy_Up))
    image1_3.setSize((size_x, size_y))
    image1_3.setImage(image_1)
    image2_3.setPos((posix_CenterLeft, posiy_Up))
    image2_3.setSize((size_x, size_y))
    image2_3.setImage(image_2)
    image3_3.setPos((posix_CenterRight, posiy_Up))
    image3_3.setSize((size_x, size_y))
    image3_3.setImage(image_3)
    image4_3.setPos((posix_SideRight , posiy_Up))
    image4_3.setSize((size_x, size_y))
    image4_3.setImage(image_4)
    image5_3.setPos((posix_SideLeft, posiy_Down))
    image5_3.setSize((size_x, size_y))
    image5_3.setImage(image_5)
    image6_3.setPos((posix_CenterLeft, posiy_Down))
    image6_3.setSize((size_x, size_y))
    image6_3.setImage(image_6)
    image7_3.setPos((posix_CenterRight, posiy_Down))
    image7_3.setSize((size_x, size_y))
    image7_3.setImage(image_7)
    image8_3.setPos((posix_SideRight, posiy_Down))
    image8_3.setSize((size_x, size_y))
    image8_3.setImage(image_8)
    # setup some python lists for storing info about the answer_3
    answer_3.x = []
    answer_3.y = []
    answer_3.leftButton = []
    answer_3.midButton = []
    answer_3.rightButton = []
    answer_3.time = []
    answer_3.clicked_name = []
    gotValidClick = False  # until a click is received
    imageSelected.setSize((size_x, size_y))
    if answer.clicked_name:
        if answer.clicked_name[-1] == "image1":
            posriqx=posix_SideLeft 
            posreqy=posiy_Up
        elif answer.clicked_name[-1]== "image2":
            posriqx=posix_CenterLeft 
            posreqy=posiy_Up
        elif answer.clicked_name[-1] == "image3":
            posriqx=posix_CenterRight 
            posreqy=posiy_Up
        elif answer.clicked_name[-1] == "image4":
            posriqx=posix_SideRight
            posreqy=posiy_Up    
        elif answer.clicked_name[-1] == "image5":
            posriqx=posix_SideLeft 
            posreqy=posiy_Down
        elif answer.clicked_name[-1]== "image6":
            posriqx=posix_CenterLeft 
            posreqy=posiy_Down
        elif answer.clicked_name[-1] == "image7":
            posriqx=posix_CenterRight 
            posreqy=posiy_Down
        elif answer.clicked_name[-1] == "image8":
            posriqx=posix_SideRight
            posreqy=posiy_Down
    else:
        posriqx=0.7
        posreqy=0
        
    imageSelected.setPos((posriqx, posreqy))
    # keep track of which components have finished
    images_Answer2Components = [image1_3, image2_3, image3_3, image4_3, image5_3, image6_3, image7_3, image8_3, answer_3, imageSelected, countdown2]
    for thisComponent in images_Answer2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    images_Answer2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "images_Answer2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = images_Answer2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=images_Answer2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image1_3* updates
        if image1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image1_3.frameNStart = frameN  # exact frame index
            image1_3.tStart = t  # local t and not account for scr refresh
            image1_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image1_3, 'tStartRefresh')  # time at next scr refresh
            image1_3.setAutoDraw(True)
        if image1_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image1_3.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image1_3.tStop = t  # not accounting for scr refresh
                image1_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image1_3, 'tStopRefresh')  # time at next scr refresh
                image1_3.setAutoDraw(False)
        
        # *image2_3* updates
        if image2_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image2_3.frameNStart = frameN  # exact frame index
            image2_3.tStart = t  # local t and not account for scr refresh
            image2_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image2_3, 'tStartRefresh')  # time at next scr refresh
            image2_3.setAutoDraw(True)
        if image2_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image2_3.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image2_3.tStop = t  # not accounting for scr refresh
                image2_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image2_3, 'tStopRefresh')  # time at next scr refresh
                image2_3.setAutoDraw(False)
        
        # *image3_3* updates
        if image3_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image3_3.frameNStart = frameN  # exact frame index
            image3_3.tStart = t  # local t and not account for scr refresh
            image3_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image3_3, 'tStartRefresh')  # time at next scr refresh
            image3_3.setAutoDraw(True)
        if image3_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image3_3.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image3_3.tStop = t  # not accounting for scr refresh
                image3_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image3_3, 'tStopRefresh')  # time at next scr refresh
                image3_3.setAutoDraw(False)
        
        # *image4_3* updates
        if image4_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image4_3.frameNStart = frameN  # exact frame index
            image4_3.tStart = t  # local t and not account for scr refresh
            image4_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image4_3, 'tStartRefresh')  # time at next scr refresh
            image4_3.setAutoDraw(True)
        if image4_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image4_3.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image4_3.tStop = t  # not accounting for scr refresh
                image4_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image4_3, 'tStopRefresh')  # time at next scr refresh
                image4_3.setAutoDraw(False)
        
        # *image5_3* updates
        if image5_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image5_3.frameNStart = frameN  # exact frame index
            image5_3.tStart = t  # local t and not account for scr refresh
            image5_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image5_3, 'tStartRefresh')  # time at next scr refresh
            image5_3.setAutoDraw(True)
        if image5_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image5_3.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image5_3.tStop = t  # not accounting for scr refresh
                image5_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image5_3, 'tStopRefresh')  # time at next scr refresh
                image5_3.setAutoDraw(False)
        
        # *image6_3* updates
        if image6_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image6_3.frameNStart = frameN  # exact frame index
            image6_3.tStart = t  # local t and not account for scr refresh
            image6_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image6_3, 'tStartRefresh')  # time at next scr refresh
            image6_3.setAutoDraw(True)
        if image6_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image6_3.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image6_3.tStop = t  # not accounting for scr refresh
                image6_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image6_3, 'tStopRefresh')  # time at next scr refresh
                image6_3.setAutoDraw(False)
        
        # *image7_3* updates
        if image7_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image7_3.frameNStart = frameN  # exact frame index
            image7_3.tStart = t  # local t and not account for scr refresh
            image7_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image7_3, 'tStartRefresh')  # time at next scr refresh
            image7_3.setAutoDraw(True)
        if image7_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image7_3.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image7_3.tStop = t  # not accounting for scr refresh
                image7_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image7_3, 'tStopRefresh')  # time at next scr refresh
                image7_3.setAutoDraw(False)
        
        # *image8_3* updates
        if image8_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image8_3.frameNStart = frameN  # exact frame index
            image8_3.tStart = t  # local t and not account for scr refresh
            image8_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image8_3, 'tStartRefresh')  # time at next scr refresh
            image8_3.setAutoDraw(True)
        if image8_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image8_3.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                image8_3.tStop = t  # not accounting for scr refresh
                image8_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image8_3, 'tStopRefresh')  # time at next scr refresh
                image8_3.setAutoDraw(False)
        # *answer_3* updates
        if answer_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            answer_3.frameNStart = frameN  # exact frame index
            answer_3.tStart = t  # local t and not account for scr refresh
            answer_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(answer_3, 'tStartRefresh')  # time at next scr refresh
            answer_3.status = STARTED
            answer_3.mouseClock.reset()
            prevButtonState = answer_3.getPressed()  # if button is down already this ISN'T a new click
        if answer_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > answer_3.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                answer_3.tStop = t  # not accounting for scr refresh
                answer_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(answer_3, 'tStopRefresh')  # time at next scr refresh
                answer_3.status = FINISHED
        if answer_3.status == STARTED:  # only update if started and not finished!
            x, y = answer_3.getPos()
            answer_3.x.append(x)
            answer_3.y.append(y)
            buttons = answer_3.getPressed()
            answer_3.leftButton.append(buttons[0])
            answer_3.midButton.append(buttons[1])
            answer_3.rightButton.append(buttons[2])
            answer_3.time.append(answer_3.mouseClock.getTime())
            buttons = answer_3.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([image1, image2, image3, image4, image5, image6, image7, image8])
                        clickableList = [image1, image2, image3, image4, image5, image6, image7, image8]
                    except:
                        clickableList = [[image1, image2, image3, image4, image5, image6, image7, image8]]
                    for obj in clickableList:
                        if obj.contains(answer_3):
                            gotValidClick = True
                            answer_3.clicked_name.append(obj.name)
                    if gotValidClick:
                        continueRoutine = False  # abort routine on response
        
        # *imageSelected* updates
        if imageSelected.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageSelected.frameNStart = frameN  # exact frame index
            imageSelected.tStart = t  # local t and not account for scr refresh
            imageSelected.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageSelected, 'tStartRefresh')  # time at next scr refresh
            imageSelected.setAutoDraw(True)
        if imageSelected.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageSelected.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                imageSelected.tStop = t  # not accounting for scr refresh
                imageSelected.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageSelected, 'tStopRefresh')  # time at next scr refresh
                imageSelected.setAutoDraw(False)
        
        # *countdown2* updates
        if countdown2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            countdown2.frameNStart = frameN  # exact frame index
            countdown2.tStart = t  # local t and not account for scr refresh
            countdown2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(countdown2, 'tStartRefresh')  # time at next scr refresh
            countdown2.setAutoDraw(True)
        if countdown2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > countdown2.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                countdown2.tStop = t  # not accounting for scr refresh
                countdown2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(countdown2, 'tStopRefresh')  # time at next scr refresh
                countdown2.setAutoDraw(False)
        if countdown2.status == STARTED:  # only update if drawing
            countdown2.setText(round(20.0 - t, 1), log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in images_Answer2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "images_Answer2"-------
    for thisComponent in images_Answer2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('answer_3.x', answer_3.x)
    trials.addData('answer_3.y', answer_3.y)
    trials.addData('answer_3.leftButton', answer_3.leftButton)
    trials.addData('answer_3.midButton', answer_3.midButton)
    trials.addData('answer_3.rightButton', answer_3.rightButton)
    trials.addData('answer_3.time', answer_3.time)
    trials.addData('answer_3.clicked_name', answer_3.clicked_name)
    trials.addData('answer_3.started', answer_3.tStartRefresh)
    trials.addData('answer_3.stopped', answer_3.tStopRefresh)
    if (answer.clicked_name and answer_3.clicked_name):
        if((answer.clicked_name[-1]==correct_Answer1 or answer.clicked_name[-1]==correct_Answer2) and (answer_3.clicked_name[-1]==correct_Answer1 or answer_3.clicked_name[-1]==correct_Answer2)):
            trials.addData('score', 1)
        else:
            trials.addData('score', 0)
    else:
        trials.addData('score', -1)
    
    # ------Prepare to start Routine "NextInstruction"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    NextInstructionComponents = [Next_Test]
    for thisComponent in NextInstructionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    NextInstructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "NextInstruction"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = NextInstructionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=NextInstructionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Next_Test* updates
        if Next_Test.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Next_Test.frameNStart = frameN  # exact frame index
            Next_Test.tStart = t  # local t and not account for scr refresh
            Next_Test.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Next_Test, 'tStartRefresh')  # time at next scr refresh
            Next_Test.setAutoDraw(True)
        if Next_Test.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Next_Test.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                Next_Test.tStop = t  # not accounting for scr refresh
                Next_Test.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Next_Test, 'tStopRefresh')  # time at next scr refresh
                Next_Test.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in NextInstructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "NextInstruction"-------
    for thisComponent in NextInstructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# ------Prepare to start Routine "FineTest"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
FineTestComponents = [Txt_Fine]
for thisComponent in FineTestComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
FineTestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "FineTest"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = FineTestClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=FineTestClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Txt_Fine* updates
    if Txt_Fine.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Txt_Fine.frameNStart = frameN  # exact frame index
        Txt_Fine.tStart = t  # local t and not account for scr refresh
        Txt_Fine.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Txt_Fine, 'tStartRefresh')  # time at next scr refresh
        Txt_Fine.setAutoDraw(True)
    if Txt_Fine.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Txt_Fine.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Txt_Fine.tStop = t  # not accounting for scr refresh
            Txt_Fine.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Txt_Fine, 'tStopRefresh')  # time at next scr refresh
            Txt_Fine.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FineTestComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "FineTest"-------
for thisComponent in FineTestComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

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
