#!/usr/bin/env python
"""
@file    simpleTHuman.py
@author  Simon Box
@date    19/02/2013

Programme for launching the SimpleT model and setting the lights by human interface 

"""

import sumoConnect, readJunctionData, humanControl

connector = sumoConnect.sumoConnect("../SimpleT/simpleT.sumocfg",True)

connector.launchSumoAndConnect()

jd = readJunctionData.readJunctionData("../SimpleT/simpleT.jcn.xml")
junctionsList = jd.getJunctionData()

controllerList = []

for junction in junctionsList:
    controllerList.append(humanControl.humanControl(junction))


step = 0
timeStep = 10

while step == 0 or connector.traci.simulation.getMinExpectedNumber() > 0:
    connector.runSimulationForOneStep()
    for controller in controllerList:
        controller.process()
