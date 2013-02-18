"""
@file    simpleTwithTrafcod.py
@author  Simon Box and(?) Peter Knoppers
@date    12/02/2013

Control script for launching the simpleT SUMO model and then launching Trafcod and coordinating control.

"""
import sumoConnect, readJunctionData, traci

##STEP 1 - Launch SUMO ##############################################################

connector = sumoConnect.sumoConnect("../SimpleTtrafcodVersion/simpleT.sumocfg",True)
connector.launchSumoAndConnect()
######################################################################################

##STEP 2 - Launch Trafcod ############################################################

##//TODO: Insert Trafcod launch command here##########################################

######################################################################################


##STEP 3 - Coordinate junction control################################################
junctionID = "1"##The ID for the juction when communicating with SUMO
detectorIDs = ["0","1","2","3","4","5","6","7","8","9"]##The IDs for the loops when communicating with SUMO
step = 0

while step == 0 or connector.traci.simulation.getMinExpectedNumber() > 0:
    
    ##STEP 3.1 - Advance SUMO one step################################################
    connector.runSimulationForOneStep()## Will advance the simulation by 0.1 seconds
    ##################################################################################
    
    ##STEP 3.2 - Collect Loop occupancy data #########################################
    
    ##Option 1 Use Python script #####################################################
    loopOccupancyValues = [] ## 0 = "not occupied during timestep"; 1 = "occupied during timestep"
    
    for detector in detectorIDs:
        occupied = traci.inductionloop.getLastStepVehicleNumber(detector)
        loopOccupancyValues.append(occupied)
        
    ##//TODO: Insert code to pass loopOccupancyValues to Trafcod######################
    ##################################################################################
    
    ##Option 2 Let Trafcod query SUMO directly over tcp/ip############################
    tcpPort = connector.Port
    
    for detector in detectorIDs:
        pass##//TODO: Insert code triggering Trafcod to directly query detector data using
            ##tcpPort and detector following the protocol described here: http://sumo.sourceforge.net/doc/current/docs/userdoc/TraCI/Induction_Loop_Value_Retrieval.html
    
    ##################################################################################
    ##################################################################################
    
    ##STEP 3.3 - Return Signal control command to SUMO ###############################
    
    ##Option 1 Use Python script #####################################################
    controlString = "rrrrrrrrrr";
    ##//TODO: Insert code to receive the correct controlSting from Trafcod
    traci.trafficlights.setRedYellowGreenState(junctionID, controlString)## Set the traffic lights in SUMO
    ##################################################################################
    
    ##Option 2 Let Trafcod set the lights in SUMO directly over tcp/ip################
    tcpPort = connector.Port
    
    ##//TODO: Insert code triggering Trafcod to directly set traffic light state using
    ##a "control string" and the junction ID.
    ##################################################################################
    ##################################################################################
    
######################################################################################

##STEP 4 - Exit SUMO #################################################################
connector.disconnect()
######################################################################################

##STEP 5 - Exit Trafcod ##############################################################
##//TODO: insert code to exit trafcod
######################################################################################