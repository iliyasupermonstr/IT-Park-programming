from datetime import datetime,time
from time import sleep
import playsound
from typing import Dict
import os
from argparse import ArgumentParser
import json 
SIGNAL = "/Users/iliyabezrukov/Downloads/12-milky-way.mp3"
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
    'time', type=str, help='Alarm time in format hh:mm:ss'
)

parser.add_argument("repeat",type = int,default = 5,help = "ALarm signal repeats count")
arguments = parser.parse_args()
time_str = arguments.time
time_value = datetime.strptime(time_str,"%H:%M:%S")

repeats_count = arguments.repeat

main(target_time = time_value,repeats_count = repeats_count)