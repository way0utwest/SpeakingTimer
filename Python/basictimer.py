import time
import os
import threading

# total time is 60 * 2
total_time = 30
alarm_1 = 25
alarm_2 = 20

class Alarm(threading.Thread):
    def __init__(self, hours, minutes):
        super(Alarm, self).__init__()
        self.hours = int(hours)
        self.minutes = int(minutes)
        self.keep_running = True

    def run(self):
        try:
            while self.keep_running:
                now = time.localtime()
                if (now.tm_hour == self.hours and now.tm_min == self.minutes):
                    print("ALARM NOW!")
                    os.popen("voltage.mp3")
                    return
            time.sleep(60)
        except:
            return
    def just_die(self):
        self.keep_running = False


start = int(time.time())
end = start + total_time


#print("Start :" + str(start))
#print("End   :" + str(end))

next_second = start + 1
current = start
while  (current < end):
    current = int(time.time())
    if current == next_second:
        current_minutes = int((end - current) / 60)
        current_seconds = ((end - current) % 60)
        if current_minutes < 10:
            timer_string = "0" + str(current_minutes)
        else:
            timer_string = str(current_minutes)
        if current_seconds < 10:
            timer_string = timer_string + ":0" + str(current_seconds)
        else:
            timer_string = timer_string + ":" + str(current_seconds)
        if current_seconds == alarm_1:
            timer_string = timer_string + "  " + str(alarm_1) + " ALARM"
        if current_seconds == alarm_2:
            timer_string = timer_string + "  " + str(alarm_2) + " ALARM"
        print(timer_string)
        next_second += 1

