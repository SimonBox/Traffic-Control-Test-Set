#!/usr/bin/env python
"""
@file    fixedTimeControl.py
@author  Simon Box
@date    31/01/2013

class for fixed time signal control

"""
import signalControl,readJunctionData, traci

class fixedTimeControl(signalControl.signalControl):
    def __init__(self,junctionData):
        super(fixedTimeControl,self).__init__()
        self.junctionData = junctionData
        self.firstCalled = self.getCurrentSUMOtime()
        self.lastCalled = self.getCurrentSUMOtime()
        self.lastStageIndex = 0
        traci.trafficlights.setRedYellowGreenState(self.junctionData.id, self.junctionData.stages[self.lastStageIndex].controlString)
        
    def process(self):
        if self.transitionObject.active:
            pass
        elif (self.getCurrentSUMOtime() - self.firstCalled) < (self.junctionData.offset*1000):
            pass
        elif (self.getCurrentSUMOtime() - self.lastCalled) < (self.junctionData.stages[self.lastStageIndex].period*1000):
            pass
        else:      
            if len(self.junctionData.stages) != (self.lastStageIndex)+1:
                self.transitionObject.newTransition(self.junctionData.id, self.junctionData.stages[self.lastStageIndex].controlString,self.junctionData.stages[self.lastStageIndex + 1].controlString)
                self.lastStageIndex +=1
                self.lastCalled = self.getCurrentSUMOtime()
            else:
                self.transitionObject.newTransition(self.junctionData.id, self.junctionData.stages[self.lastStageIndex].controlString,self.junctionData.stages[0].controlString)
                self.lastStageIndex =0
                self.lastCalled = self.getCurrentSUMOtime()
                
        
        super(fixedTimeControl, self).process()
            
        
            
            
            
            
        