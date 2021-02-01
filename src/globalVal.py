#-----------------------------------------------------------------------------
# Name:        globalVal.py
#
# Purpose:     This module is used set the Local config file as global value
#              which will be used in the other modules.
# Author:      Yuancheng Liu
#
# Created:     2019/05/17
# Copyright:   NUS – Singtel Cyber Security Research & Development Laboratory
# License:     YC @ NUS
#-----------------------------------------------------------------------------
"""Globals: globally defined constants and vars
    A few simple rules for globals:
    1. Don't stuff something into 'Globals' dict without creating an empty entry
        here first, so we can see all the names collected together with comment
        about why it's here.
    2. Comment every variable put here - globals obscure structural relationships,
        but also make inter-module communication easier
    3. It is good form to start each global name with 'g', if someone ignores #4
    4. It is bad form to say "from Globals import *" in case somebody ignores #3
"""
import os

dirpath = os.getcwd()
print("QSG-Manager : Current working directory is : %s" %dirpath)

#------<CONSTANTS>-------------------------------------------------------------
# Google map API billing key:
MAP_API_KEY = 'AIzaSyBoHBPqxFw40DFvCbXrj1IWNcvkzb6WkkI' # replace this with your own key.

# Gateway marker link
GW_MK_LK = 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'
# Gateway information box icon link
GW_IB_LK = '../static/images/gateway.jpg'
# Control hub marker lnik
HB_MK_LK = 'http://maps.google.com/mapfiles/ms/icons/red-dot.png'
# Control hub information box img link
HB_IB_LK = '../static/images/hub.jpg'

CH_GPS = (1.2988469, 103.8360123) # control hub gps location currently we use Singtel Comcenter POS.

#-------<GLOBAL VARIABLES (start with "g")>------------------------------------


CH_GPS = (1.2988469, 103.8360123) # control hub gps location currently we use Singtel Comcenter POS.

#-------<GLOBAL VARIABLES (start with "g")>------------------------------------
# VARIABLES are the built in data type.
gPeriod = 10
gMapFilter = ['show-inactive', 'show-gateway', 'show-control']
gMapSetting = [1, 1, 1] # Inactive, gateway, control hub communications respectively
gDevNode = []   
gLatestTime = 0.0

#-------<GLOBAL INSTANCES (start with "i")>-----------------------------------------------------
# INSTANCES are the object. 
iDataMgr = None
iSocketIO = None
iDevNode = []   # device node list
