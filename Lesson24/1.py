from typing import Dict
import os
from argparse import ArgumentParser
from datetime import datetime, time
from time import sleep
import playsound
import json

SIGNAL = "/Users/iliyabezrukov/Downloads/12-milky-way.mp3"
CLOCK_INTERVAL_SEC =0.1
TIME_FORMAT = "%H:%M:%S"

def save_alarm_info(name,time_value,repeats_count):
    json_obj ={
        "name":name,
        "time":time_value.strftime(TIME_FORMAT),
        "repeat": repeats_count
    }
    alarm_info = get_alarm_info()
    for i in range(len(alarm_info)):
        alarm_info[i]["time"] = alarm_info[i]["time"].strftime(TIME_FORMAT)
    alarm_info.append(json_obj)

    with open("data_file.json,'w") as file_ctx:
        json.dump(alarm_info,file_ctx,indent=4)
def get_alarm_info(file_path="data_file.json"):
    if os.path.exists("data_file.json"):
        with open("data_file.json") as file_ctx:
            lines = file_ctx.read()
            json_obj = json.loads(lines)
    else:
        json_obj = []
    for i in range(len(json_obj)):
        json_obj[i]["time"] = datetime.strptime(json_obj[i]["time"],TIME_FORMAT)
    return json_obj
def format_alarms(alarms_info):
    if not alarms_info:
        return "Сигналы будильника отсутствуют"
    message_lines  = ["Сигналы будильника"]
    for info in alarms_info:
        line = f"{info['name']}:{info['time']} ({info['repeat']} раз)"
        message_lines.append(line)
    return "\n".join(message_lines)
def is_wake_up(target_time: time) -> bool:
    while True:
        time_value = datetime.now().time()
        if(target_time.hour == time_value.hour 
        and target_time.minute == time_value.minute
        and target_time.second == time_value.second):
            break

def run_signal(repeats_count=5):
    for i in range(repeats_count):
        playsound.playsound(SIGNAL,block=True)
        
def main(target_time,repeats_count):
    is_wake_up(target_time=target_time)
    run_signal(repeats_count=repeats_count)
    print("Wake_up!")

parser = ArgumentParser(
    description='My custom alalrm'
)

parser.add_argument(
    "--show",action ="store_true"
)

# parser.add_argument("repeat",type = int,default = 5,help = "ALarm signal repeats count")
arguments = parser.parse_args()
if arguments.show:
    alarms_info = get_alarm_info()
    formatting_text = format_alarms(alarms_info)
    print(formatting_text)
# time_str = arguments.time
# time_value = datetime.strptime(time_str,"%H:%M:%S")

# repeats_count = arguments.repeat

# main(target_time = time_value,repeats_count = repeats_count)