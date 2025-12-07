# Import Section
from models import *
from utils import *
from stats import *
from storage import *
from argparse import ArgumentParser

# main


parser = ArgumentParser()
parser.add_argument("--start",action="store_true",help="Starts a new focus session")
parser.add_argument("--end",action="store_true",help="Stop the current focus session")
parser.add_argument("--task", type=str)

args = vars(parser.parse_args())


if validate_parameters(args):
    if args["start"]:
        create_SaveItem(create_focusTime(args["task"])) 
        print(f"Focus time for the task {args["task"]} started!")       
    elif args["end"]:
        ended_focusTime = end_SaveItem()
        print(f"Ended current focus time for the task {ended_focusTime["task"]}. Your focus time lasted {ended_focusTime["duration_minutes"]} minutes.")
else:
    print("Ups! Something went wrong, please check your parameters according to the documentation.")