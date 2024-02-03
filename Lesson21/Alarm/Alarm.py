from datetime import datetime,time
from time import sleep
from playsound import playsound

CLOCK_INTERVAL_SEC = 0.1
SIGNAL_FILE = "/Users/iliyabezrukov/projects/It-Park Course/Lesson21/Alarm/Nubik_rubik_ya_v_majnkrafte_nubik_Pesnya.wav"

def run_signal(repeat_counts):
    for i in range(repeat_counts):
        playsound.playsound(SIGNAL_FILE)
def is_wake_up(target_time: time) -> bool:
    while True:
        time_value = datetime.now().time()
        if(target_time.hour == time_value.hour 
        and target_time.minute == time_value.minute
        and target_time.second == time_value.second):
            break

        sleep(CLOCK_INTERVAL_SEC)
need_time = time(19
                 , 55,30)
is_wake_up(target_time=need_time)
print("Wake Up!")
run_signal()
