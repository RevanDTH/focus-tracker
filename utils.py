def validate_parameters(parameters):
    if parameters["start"] == True and parameters["end"] == False and parameters["task"] != None:
        return True
    elif parameters["end"] == True and parameters["start"] == False:
        return True
    else:
        return False