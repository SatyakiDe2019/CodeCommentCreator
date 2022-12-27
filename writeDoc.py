#####################################################
#### Written By: SATYAKI DE                      ####
#### Written On: 26-Dec-2022                     ####
#### Modified On 27-Dec-2022                     ####
####                                             ####
#### Objective: This is the main calling         ####
#### python script that will invoke the          ####
#### ChatGPT OpenAI class to initiate the        ####
#### prediction to interpret the python code     ####
#### & display the result.                       ####
#####################################################

import os
import openai
import json
from clsConfigClient import clsConfigClient as cf
import pandas as p

import ssl
import time
import datetime
import logging

from pathlib import Path

# Bypassing SSL Authentication
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

# Disbling Warning
def warn(*args, **kwargs):
    pass

import warnings
warnings.warn = warn

###############################################
###           Global Section                ###
###############################################
OPENAI_API_KEY=str(cf.conf['OPENAI_API_KEY'])
FILE_NAME=str(cf.conf['FILE_NAME'])
CODE_PATH=str(cf.conf['CODE_PATH'])
MODEL_NAME=str(cf.conf['MODEL_NAME'])
KEY_Q=str(cf.conf['KEY_Q'])
###############################################
###    End of Global Section                ###
###############################################
def readFile(inputFile):
    try:
        data = Path(inputFile).read_text()
        return data + '""" ' + KEY_Q
    except Exception as e:
        x = str(e)
        print(x)

        data = ''

        return data
def main():
    try:
        # Other useful variables
        debugInd = 'Y'
        var = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        var1 = datetime.datetime.now()

        print('Start Time: ', str(var))
        # End of useful variables

        # Initiating Log Class
        general_log_path = str(cf.conf['LOG_PATH'])

        # Enabling Logging Info
        logging.basicConfig(filename=general_log_path + 'predCode.log', level=logging.INFO)

        print('Started predicting & documenting code!')
        print('Read Class Name: ')
        print(str(FILE_NAME))

        FileNameWithPath = CODE_PATH + FILE_NAME

        data = readFile(FileNameWithPath)

        print('#'*120)
        print(data)
        print(type(data))
        print('#'*120)

        # ChatGPT API_KEY
        openai.api_key = OPENAI_API_KEY

        # Getting response from ChatGPT
        response = openai.Completion.create(
        model=MODEL_NAME,
        prompt=data,
        temperature=0,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\"\"\""]
        )

        print('Final Result:')
        print('*'*120)
        #print(response)
        print(response.choices[0].text)
        print('*'*120)

        var2 = datetime.datetime.now()

        c = var2 - var1
        minutes = c.total_seconds() / 60
        print('Total difference in minutes: ', str(minutes))

        print('End Time: ', str(var1))

    except Exception as e:
        x = str(e)
        print('Error: ', x)

if __name__ == "__main__":
    main()
