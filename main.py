import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime


def sign_in():
    # Opens up the zoom app
    # change the path specific to your computer

    # If on windows use below line for opening zoom
    # subprocess.call('C:\\myprogram.exe')

    # If on mac / Linux use below line for opening zoom
    subprocess.call(r'C:\Users\stj.oocal\AppData\Roaming\Zoom\bin\Zoom.exe')

    time.sleep(0.25)
    media_btn = pyautogui.locateCenterOnScreen('create-meetingWoCam.png')

    pyautogui.moveTo(media_btn)
    pyautogui.click()
    # clicks the join button

    check_options = pyautogui.locateCenterOnScreen('MeetingOptions.png')
    pyautogui.moveTo(check_options)
    pyautogui.click()

    # Turn off the video if exist
    meeting_video = pyautogui.locateCenterOnScreen('start-with-video.png')
    pyautogui.moveTo(meeting_video)
    pyautogui.click()

   # Create room
    media_btn = pyautogui.locateCenterOnScreen('create-meetingWoCam.png')

    pyautogui.moveTo(media_btn)
    pyautogui.click()
    time.sleep(1)

# Reading the file
df = pd.read_csv('timings.csv')

while True:
    # checking of the current time exists in our csv file

    now = datetime.now().strftime("%H:%M")
    if now in str(df['timings']):
        row = df.loc[df['timings'] == now]

        sign_in()
        time.sleep(30)
        print('signed in')
    time.sleep(20)
