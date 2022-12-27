################################################
#### Written By: SATYAKI DE                 ####
#### Written On:  15-May-2020               ####
#### Modified On: 26-Dec-2022               ####
####                                        ####
#### Objective: This script is a config     ####
#### file, contains all the keys for        ####
#### best bowling prediction from a sports  ####
#### streaming.                             ####
####                                        ####
################################################

import os
import platform as pl

class clsConfigClient(object):
    Curr_Path = os.path.dirname(os.path.realpath(__file__))

    os_det = pl.system()
    if os_det == "Windows":
        sep = '\\'
    else:
        sep = '/'

    conf = {
        'APP_ID': 1,
        'ARCH_DIR': Curr_Path + sep + 'arch' + sep,
        'PROFILE_PATH': Curr_Path + sep + 'profile' + sep,
        'LOG_PATH': Curr_Path + sep + 'log' + sep,
        'REPORT_PATH': Curr_Path + sep + 'output' + sep,
        'REPORT_DIR': 'output',
        'SRC_PATH': Curr_Path + sep + 'data' + sep,
        'CODE_PATH': Curr_Path + sep + 'Code' + sep,
        'APP_DESC_1': 'Predicting the direction of football!',
        'DEBUG_IND': 'N',
        'INIT_PATH': Curr_Path,
        'FILE_NAME': 'FirstPart.py',
        'TITLE': "Predicting the direction of football!",
        'PATH' : Curr_Path,
        'OPENAI_API_KEY': "sk-gfjrjIIYRED%KKLkw8373hdtYdevGKdjd734BH",
        'MODEL_NAME': "code-davinci-002",
        "KEY_Q":"What the above class is doing?"
    }
