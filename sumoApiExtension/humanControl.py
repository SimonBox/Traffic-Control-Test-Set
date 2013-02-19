#!/usr/bin/env python
"""
@file    humanControl.py
@author  Simon Box
@date    19/02/2013

class for human signal control

"""
import signalControl,readJunctionData, traci, fixedTimeControl, getch

class humanControl(fixedTimeControl.fixedTimeControl):
    
    def __init__(self,junctionData):
        super(humanControl,self).__init__(junctionData)
        self.timeSpan = 10;
        self.getchObj = getch._Getch()

    def process(self):
        if self.transitionObject.active:
            pass
        elif (self.getCurrentSUMOtime() - self.lastCalled) <  (self.timeSpan*1000):
            pass
        else:      
            demandedStageIndex = self.getUserInput() - 1
            
            if demandedStageIndex != self.lastStageIndex:
                self.transitionObject.newTransition(self.junctionData.id, self.junctionData.stages[self.lastStageIndex].controlString,self.junctionData.stages[demandedStageIndex].controlString)
                self.lastStageIndex = demandedStageIndex
                self.lastCalled = self.getCurrentSUMOtime()
            else:
                self.lastCalled = self.getCurrentSUMOtime()
        
        self.transitionObject.processTransition()
        
    def setTimeSpanSeconds(self,timeSpan):
        self.timeSpan = timeSpan
        
    def getUserInput(self):
        selectedChar = 0
        stageCount = len(self.junctionData.stages)
        print "Please enter the next stage for Junction %s (a number between 1 and %s):" % (self.junctionData.id, stageCount)
        while True:
            inputChar = self.getchObj()
            if inputChar != None:
                break
            
        if int(inputChar)>=1 and int(inputChar)<=stageCount:
            selectedChar = int(inputChar)
        else:
            print "The character you entered was not valid, please try again"
            self.getUserInput()
            
        return selectedChar
        