# Challenge: Write a Python function to play a sound and print a message at a set time.
# Input: alarm time, sound file, message

from datetime import datetime
from datetime import timedelta
import winsound                             # only works for windows OS

def alarm(time, file, text):
    if (time < datetime.now()):             # if alarmTime has past for today, add 1 day so alarm rings tomorrow
        time += timedelta(days=1)
        print("Alarm set for tomorrow at " + str(time.time()))
    else:
        print("Alarm set for today at " + str(time.time()))
    
    while(True):
        if (time < datetime.now()):         # once current time is past alarmTime, alarm will ring
            print(text)
            winsound.PlaySound(file, winsound.SND_FILENAME)

alarmTime = datetime.strptime(str(datetime.now().date()) + " " + input(), "%Y-%m-%d %H:%M")     # must use 24-hour system
soundFile = input()
message = input()
# alarmTime = datetime.strptime(str(datetime.now().date()) + " 17:38", "%Y-%m-%d %H:%M")
# soundFile = "7 sound.wav"
# message = "Wake Up!"

alarm(alarmTime, soundFile, message)


# Provided Solution - made note for future reference

# import sched
# import time
# import winsound as ws

# def set_alarm(alarm_time, wav_file, message):
#     s = sched.scheduler(time.time, time.sleep)
#     s.enterabs(alarm_time, 1, print, argument=(message,))
#     s.enterabs(alarm_time, 1, ws.PlaySound, argument=(wav_file, ws.SND_FILENAME))
#     print('Alarm set for', time.asctime(time.localtime(alarm_time)))
#     s.run()
