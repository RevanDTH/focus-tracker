import models
import os
import json

def validate_parameters(parameters):
    if parameters["start"] == True and parameters["end"] == False and parameters["task"] != None:
        return True
    elif parameters["end"] == True and parameters["start"] == False:
        return True
    else:
        return False
    
def create_focusTime(task):
    newTask = models.focusTime(task=task)
    return newTask

def check_saveLocation():
    if not os.path.exists("./save/savefile.json"):
        os.makedirs("./save")
        with open("savefile.json", "w") as saveFile:
            savefile_str = '{}'
            saveFile.write(savefile_str)