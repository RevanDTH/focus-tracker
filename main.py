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
else:
    print("Ups! Something went wrong, please check your parameters according to the documentation.")