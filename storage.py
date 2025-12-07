from utils import *
from json import *
from datetime import *

def create_SaveItem(focusTime):
    new_item = {
        "id": focusTime.id,
        "start_time": focusTime.start_time,
        "end_time": None,
        "duration_minutes": None,
        "task": focusTime.task
    }
    new_data = dumps(new_item, default=str)
    create_saveLocation()
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

def end_SaveItem():
    if check_saveLocation():
        save_path = "./save/savefile.json"
        with open(save_path, "r+", encoding="utf-8") as f:
            content = f.read().strip()
            if content:
                try:
                    data_list = loads(content)
                    if not isinstance(data_list, list):
                        data_list = [data_list]
                except Exception:
                    print("There is no focus time currently running. Please create a focus time before calling --end")
                    exit(1)
            else:
                print("Savefile couldn’t be found or is empty. Please create a task first!")
                exit(1)
                
            if not data_list[-1]["end_time"]:
                end_time = default_factory=lambda: datetime.datetime.now()
                end_time = datetime.now()
                start = data_list[-1]["start_time"]
                if isinstance(start, str):
                    try:
                        start_dt = datetime.fromisoformat(start)
                    except Exception:
                        try:
                            start_dt = datetime.strptime(start, "%Y-%m-%d %H:%M:%S.%f")
                        except Exception:
                            start_dt = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
                else:
                    start_dt = start
                duration_minutes = int((end_time - start_dt).total_seconds() / 60)
                data_list[-1]["end_time"] = end_time
                data_list[-1]["duration_minutes"] = duration_minutes
                f.seek(0)
                f.truncate()
                f.write(dumps(data_list, indent=2, default=str))
                return data_list[-1]
            else:
                print("There is no focus time currently running. Please create a task before calling --end")
                exit(1)



