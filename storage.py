from utils import *
from json import *

def create_SaveItem(focusTime):
    new_item = {
        "id": focusTime.id,
        "start_time": focusTime.start_time,
        "end_time": None,
        "duration_minutes": None,
        "task": focusTime.task
    }
    new_data = dumps(new_item, default=str)
    check_saveLocation()
    save_path = "./save/savefile.json"

    try:
        with open(save_path, "r+", encoding="utf-8") as f:
            content = f.read().strip()
            if content:
                try:
                    data_list = loads(content)
                    if not isinstance(data_list, list):
                        data_list = [data_list]
                except Exception:
                    data_list = []
            else:
                data_list = []
            
            if not data_list[-1]["end_time"]:
                print("You can't create a new focus time before ending the last one!")
                exit(1)
            else:
                data_list.append(new_item)
                f.seek(0)
                f.truncate()
                f.write(dumps(data_list, indent=2, default=str))
    except FileNotFoundError:
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(dumps([new_item], indent=2, default=str))

    return new_item
