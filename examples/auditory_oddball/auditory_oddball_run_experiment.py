"""
SSVEP run experiment
===============================

This example demonstrates the initiation of an EEG stream with eeg-expy, and how to run 
an experiment. 

"""

###################################################################################################  
# Setup
# ---------------------  
#  
# Imports
import sys
sys.path
sys.path.append(r'C:\Users\mcvai\EEG-ExPy')
import os
from eegnb import generate_save_fn
from eegnb.devices.eeg import EEG
from eegnb.experiments import AuditoryOddball



# Define some variables
# board_name = "muse2"
board_name = "generic"
experiment = "auditory_oddball"
subject_id = 0
session_nb = 0
record_duration = 120

###################################################################################################
# Initiate EEG device
# ---------------------
#
# Start EEG device
eeg_device = EEG(device=board_name)

# Create save file name
save_fn = generate_save_fn(board_name, experiment, subject_id, session_nb)
print(save_fn)

###################################################################################################  
# Run experiment
# ---------------------  
#  
AOP = AuditoryOddball(duration=record_duration, eeg=eeg_device, save_fn=save_fn)
# ssvep = VisualSSVEP(duration=record_duration, save_fn=save_fn)
AOP.run()
