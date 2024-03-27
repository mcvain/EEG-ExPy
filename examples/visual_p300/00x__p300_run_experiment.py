"""
P300 run experiment
===============================

This example demonstrates the initiation of an EEG stream with eeg-expy, and how to run 
an experiment. 

"""

###################################################################################################  
# Setup
# ---------------------  
#  
# Imports
import os
import sys
sys.path
sys.path.append(r'C:\Users\mcvai\EEG-ExPy')
from eegnb import generate_save_fn
from eegnb.devices.eeg import EEG
from eegnb.experiments import VisualP300, VisualN170, VisualSSVEP, visual_baselinetask

# Define some variables
# board_name = "muse2"
board_name="generic"
experiment = "visual_p300"
subject_id = 0
session_nb = 0
record_duration = 120

###################################################################################################
# Initiate EEG device
# ---------------------
#
# Start EEG device
# eeg_device = EEG(device=board_name)
eeg_device = EEG(device=board_name)

# Create save file name
save_fn = generate_save_fn(board_name, experiment, subject_id, session_nb)
print(save_fn)

###################################################################################################  
# Run experiment
# ---------------------  
#
# Create Experiment Object
p300 = VisualP300(duration=record_duration, eeg=eeg_device, save_fn=save_fn)
# p300 = VisualP300(duration=record_duration, save_fn=save_fn)
p300.run()
