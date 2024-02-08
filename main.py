import time
from playsound import playsound


def alarm(seconds):
    passed_time = 0

    while passed_time < seconds:
        time.sleep(1)
        passed_time = passed_time + 1
        time_left = seconds - passed_time

        hours_left = time_left // 3600
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{hours_left}:{minutes_left}:{seconds_left}")

    print("Time's up!")
    playsound('alarm.mp3')


def init():
    seconds = input("Set alarm time in seconds: ")
    seconds = int(seconds)
    alarm(seconds)

init()
