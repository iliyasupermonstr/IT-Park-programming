from typing import Dict
import os
from argparse import ArgumentParser
from datetime import datetime, time
from time import sleep
import playsound
import json

CLOCK_INTERVAL_SEC = 0.1
SIGNAL = 'mixkit-alarm-digital-clock-beep-989.wav'

def run_signal(repeats_count=5):
    for i in range(repeats_count):
        playsound.playsound(SIGNAL, block=True)

def save_alarm_info(name: str, time_value: datetime, repeats_count: int):
    json_obj = {
        'name':name,
        'time': time_value.strftime('%H:%M:%S'),
        'repeat': repeats_count
    }
    
    alarm_info = get_alarm_info()
    if_exists = False
    for i in range(len(alarm_info)):
        alarm_info[i]['time'] = alarm_info[i]['time'].strftime('%H:%M:%S')
        if alarm_info[i]['name'] == json_obj['name']:
            alarm_info[i] = json_obj
            if_exists = True
        elif alarm_info[i]['time'] == json_obj['time']:
            alarm_info[i] = json_obj
            if_exists = True
        else:
            pass
        
    if not if_exists:
        alarm_info.append(json_obj)
        
    with open('data_file.json', 'w') as file_ctx:
        json.dump(alarm_info, file_ctx, indent=4)                   

def get_alarm_info(file_path = 'data_file.json'):
    if os.path.exists('data_file.json'):
        with open('data_file.json') as file_ctx:
            lines = file_ctx.read()
            json_obj = json.loads(lines)
    else:
        json_obj = []
    
    for i in range(len(json_obj)):
        json_obj[i]['time'] = datetime.strptime(json_obj[i]['time'],'%H:%M:%S')
    return json_obj

def remove_alarm_info(target_alarm_name):
    alarms_info = get_alarm_info()
    removing_index = -1
    for i in range(len(alarms_info)):
        if alarms_info[i]['name'] == target_alarm_name:
            removing_index = i
    
    if removing_index != -1:
        alarms_info.pop(removing_index)
    else:
        return False
    
    json_obj = []
    for alarm in alarms_info:
        alarm['time'] = alarm['time'].strftime('%H:%M:%S')
        json_obj.append(alarm)
    
    with open('data_file.json', 'w') as file_ctx:
        json.dump(json_obj, file_ctx, indent=4)
    return True

def format_alarms(alarms_info):
    if not alarms_info:
        return 'Нет сигналов'
    message_lines = ['Сигналы будильника:']
    for info in alarms_info:
        line = f"{info['name']}: {info['time']} ({info['repeat']} раз)"
        message_lines.append(line)
    return '\n'.join(message_lines)

def get_alarm(alarms_info):
    time_value = datetime.now().time()
    for alarm in alarms_info:
        alarm_time = alarm['time']
        if (alarm_time.hour == time_value.hour and
            alarm_time.minute == time_value.minute and
            alarm_time.second == time_value.second):
            return alarm
    return None        

def main(target_time):
    while True:
        alarm = get_alarm(alarms_info)
        if alarm:
            # run_signal(repeats_count=alarm['repeat'])
            print('Пора просыпаться')
        sleep(CLOCK_INTERVAL_SEC)
    
if __name__ == '__main__':
    parser = ArgumentParser(description='Мой собственный будильник')
    parser.add_argument('--show', action='store_true')
    parser.add_argument('--add', action='store_true', help='Добавление сигнала будильника')
    parser.add_argument('--run', action='store_true', help='Запуск будильника')
    parser.add_argument('--remove', help='Удаление сигнала по имени')

    arguments = parser.parse_args()
    
    if arguments.show:
        alarms_info = get_alarm_info()
        formatting_text = format_alarms(alarms_info)
        print(formatting_text)
    
    if arguments.add:
        name = input('Введите имя сигнала: ')
        time_line = input('Время сигнала: ')
        time_value = datetime.strptime(time_line, '%H:%M:%S')
        repeats = int(input('Количество повторений: '))
        save_alarm_info(name, time_value, repeats)
    
    if arguments.run:
        alarms_info = get_alarm_info()
        main(alarms_info)
    
    if arguments.remove:
        removing_name = arguments.remove
        is_remove = remove_alarm_info(removing_name)
        if is_remove:
            print(f'Будильник {removing_name} удален')
        else:
            print(f'Будильник с именем {removing_name} не найден')
    